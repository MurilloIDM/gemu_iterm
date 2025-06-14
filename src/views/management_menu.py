from rich.console import Console
from rich.prompt import Prompt

console = Console()


def render_management_menu():
    console.print("1️⃣    [cyan]Cadastrar movimentação[/cyan]")
    console.print("2️⃣    [green]Deletar movimentação[/green]")
    console.print("3️⃣    [yellow]Voltar[/yellow]")

    option = Prompt.ask("\nDigite a opção desejada", choices=["1", "2", "3"])
    return option
