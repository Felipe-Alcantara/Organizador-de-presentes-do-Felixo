"""Menu de entrada do Organizador de Presentes do Felixo.

Porta de entrada única do projeto (padrão Felixo System Design):

    python start_app.py

Abre um menu interativo onde você instala as dependências do menu,
configura o servidor local, inicia o site e consulta o status.
O site em si é estático (index.html) — o servidor local existe apenas
para servi-lo com uma URL http://, como no GitHub Pages.
"""

from __future__ import annotations

import json
import socket
import subprocess
import sys
import threading
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_FILE = ROOT / ".start_app.json"
DEFAULT_CONFIG = {"port": 8000, "open_browser": True}
TUI_DEPS = ("questionary", "rich")


# ----------------------------------------------------------------------------
# Bootstrap das dependências do menu (questionary + rich)
# ----------------------------------------------------------------------------
def bootstrap_tui():
    """Garante as bibliotecas do menu; oferece instalação se faltarem."""
    missing = []
    for dep in TUI_DEPS:
        try:
            __import__(dep)
        except ImportError:
            missing.append(dep)
    if not missing:
        return True

    print("Este menu usa as bibliotecas: " + ", ".join(missing) + " (ainda não instaladas).")
    answer = input("Instalar agora com pip? [s/N] ").strip().lower()
    if answer != "s":
        print("Sem problema — instale depois com:")
        print(f"  {sys.executable} -m pip install " + " ".join(missing))
        return False
    result = subprocess.run([sys.executable, "-m", "pip", "install", *missing])
    if result.returncode != 0:
        print("A instalação falhou. Verifique sua conexão e tente de novo.")
        return False
    return True


if not bootstrap_tui():
    sys.exit(1)

import questionary
from questionary import Choice
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


# ----------------------------------------------------------------------------
# Configuração (.start_app.json — fora do versionamento)
# ----------------------------------------------------------------------------
def load_config() -> dict:
    """Lê a configuração local; volta ao padrão se o arquivo faltar ou estiver corrompido."""
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        return {**DEFAULT_CONFIG, **data}
    except (OSError, ValueError):
        return dict(DEFAULT_CONFIG)


def save_config(config: dict) -> None:
    CONFIG_FILE.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


# ----------------------------------------------------------------------------
# Servidor local (serve o index.html como um site estático)
# ----------------------------------------------------------------------------
class _QuietHandler(SimpleHTTPRequestHandler):
    """Serve arquivos sem imprimir uma linha de log por requisição."""

    def log_message(self, *args, **kwargs):  # noqa: D102 - silencia o log padrão
        pass


class LocalServer:
    """Servidor HTTP em thread para servir a pasta do projeto."""

    def __init__(self):
        self._httpd: ThreadingHTTPServer | None = None
        self._thread: threading.Thread | None = None
        self.port: int | None = None

    @property
    def running(self) -> bool:
        return self._httpd is not None

    def start(self, port: int) -> None:
        handler = partial(_QuietHandler, directory=str(ROOT))
        self._httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
        self._thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        self._thread.start()
        self.port = port

    def stop(self) -> None:
        if self._httpd:
            self._httpd.shutdown()
            self._httpd.server_close()
            self._httpd = None
            self._thread = None
            self.port = None


def port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("127.0.0.1", port)) == 0


# ----------------------------------------------------------------------------
# Ações do menu
# ----------------------------------------------------------------------------
def action_start(server: LocalServer, config: dict) -> None:
    if server.running:
        console.print(f"[yellow]O site já está no ar em[/] http://127.0.0.1:{server.port}/")
        return
    port = config["port"]
    if port_in_use(port):
        console.print(
            f"[red]A porta {port} já está em uso por outro programa.[/]\n"
            "Escolha outra porta em [bold]Configurar[/] e tente de novo."
        )
        return
    try:
        server.start(port)
    except OSError as err:
        console.print(f"[red]Não foi possível iniciar o servidor:[/] {err}")
        return
    url = f"http://127.0.0.1:{port}/"
    console.print(Panel(f"Site no ar: [bold link={url}]{url}[/]", style="green", expand=False))
    if config["open_browser"]:
        webbrowser.open(url)
        console.print("[dim]Navegador aberto (desative em Configurar, se preferir).[/]")


def action_stop(server: LocalServer) -> None:
    if not server.running:
        console.print("[yellow]O servidor não está rodando.[/]")
        return
    server.stop()
    console.print("[green]Servidor parado.[/]")


def action_setup() -> None:
    console.print("Este projeto é um site estático — a única dependência é o próprio menu.")
    console.print(f"Instalando/atualizando: [bold]{', '.join(TUI_DEPS)}[/]…")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", *TUI_DEPS])
    if result.returncode == 0:
        console.print("[green]Dependências prontas.[/]")
    else:
        console.print("[red]A instalação falhou — veja a mensagem do pip acima.[/]")


def action_configure(config: dict) -> None:
    port_answer = questionary.text(
        "Porta do servidor local:",
        default=str(config["port"]),
        validate=lambda v: v.isdigit() and 1024 <= int(v) <= 65535 or "Use um número entre 1024 e 65535",
    ).ask()
    if port_answer is None:
        return
    open_browser = questionary.confirm(
        "Abrir o navegador automaticamente ao iniciar?",
        default=config["open_browser"],
    ).ask()
    if open_browser is None:
        return
    config["port"] = int(port_answer)
    config["open_browser"] = open_browser
    save_config(config)
    console.print("[green]Configuração salva[/] [dim](.start_app.json)[/]")


def action_status(server: LocalServer, config: dict) -> None:
    table = Table(title="Status do projeto", show_header=False, title_style="bold magenta")
    table.add_column(style="bold")
    table.add_column()
    table.add_row("Python", sys.version.split()[0])
    table.add_row("index.html", "✅ presente" if (ROOT / "index.html").exists() else "❌ não encontrado")
    deps = []
    for dep in TUI_DEPS:
        try:
            __import__(dep)
            deps.append(f"✅ {dep}")
        except ImportError:
            deps.append(f"❌ {dep}")
    table.add_row("Dependências do menu", "  ".join(deps))
    table.add_row("Porta configurada", str(config["port"]))
    table.add_row("Abrir navegador", "sim" if config["open_browser"] else "não")
    if server.running:
        table.add_row("Servidor local", f"🟢 rodando em http://127.0.0.1:{server.port}/")
    elif port_in_use(config["port"]):
        table.add_row("Servidor local", f"🟡 parado aqui, mas a porta {config['port']} está ocupada por outro programa")
    else:
        table.add_row("Servidor local", "⚪ parado")
    table.add_row("Versão pública", "https://gifts.felixo.com.br (GitHub Pages)")
    console.print(table)


# ----------------------------------------------------------------------------
# Menu principal
# ----------------------------------------------------------------------------
def main() -> None:
    config = load_config()
    server = LocalServer()
    console.print(
        Panel(
            "[bold magenta]🎁 Organizador de Presentes do Felixo[/]\n"
            "[dim]Menu de entrada — instale, configure e rode o site por aqui.[/]",
            expand=False,
        )
    )
    try:
        while True:
            running = server.running
            choices = [
                Choice(
                    ("🔄 Parar servidor — derruba o site local" if running
                     else "🚀 Iniciar — sobe o site local e mostra a URL"),
                    value="stop" if running else "start",
                ),
                Choice("📦 Instalar / Setup — instala as dependências do menu", value="setup"),
                Choice("⚙️  Configurar — porta e abertura do navegador", value="configure"),
                Choice("📊 Status — dependências, servidor e configuração", value="status"),
                Choice("🚪 Sair — para o servidor (se ativo) e fecha o menu", value="quit"),
            ]
            action = questionary.select("O que você quer fazer?", choices=choices).ask()
            if action in (None, "quit"):
                break
            elif action == "start":
                action_start(server, config)
            elif action == "stop":
                action_stop(server)
            elif action == "setup":
                action_setup()
            elif action == "configure":
                action_configure(config)
            elif action == "status":
                action_status(server, config)
    finally:
        if server.running:
            server.stop()
            console.print("[dim]Servidor local parado.[/]")
    console.print("[bold magenta]Até a próxima! ✨[/]")


if __name__ == "__main__":
    main()
