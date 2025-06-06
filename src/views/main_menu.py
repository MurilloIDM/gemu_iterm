from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align

console = Console()


def render_main_menu():
    title_panel = Align.center("[bold #8CBCE1]GEMU ITERM[/bold #8CBCE1]", vertical="middle")
    subtitle_panel = "[white bold]O seu assistente para organizar suas finanças![/white bold]"

    console.print(Panel(title_panel, subtitle=subtitle_panel), style="#8CBCE1")

    console.print("\n")
    console.print("1️⃣    [#F2E205]Visualizar finanças de um mês[/#F2E205]")
    console.print("2️⃣    [#F2B705]Exportar finanças de um mês[/#F2B705]")
    console.print("3️⃣    [#A6774E]Gerenciar movimentação de entrada/saída[/#A6774E]")
    console.print("4️⃣    [#8C1C03]Sair[/#8C1C03]\n")

    option = Prompt.ask("Digite a opção desejada", choices=["1", "2", "3", "4"])

    return option
