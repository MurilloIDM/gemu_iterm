from rich.console import Console
from rich.prompt import Prompt

console = Console()


def render_form_access():
    username = Prompt.ask("Informe seu primeiro nome")
    return username.lower()
