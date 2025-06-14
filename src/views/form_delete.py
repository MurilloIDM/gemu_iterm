from rich.console import Console
from rich.prompt import Prompt

console = Console()


def render_form_delete():
    id = Prompt.ask("Informe o ID da movimentação")
    return int(id)
