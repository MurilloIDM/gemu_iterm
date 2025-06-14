import re

from rich.console import Console
from rich.prompt import Prompt

from utils.clean_view import clean_view

console = Console()


def render_filter_menu():
    while True:
        clean_view()
        period = Prompt.ask("Informe o período de consulta (Padrão = MM/YYYY)")

        if re.match(r"^(0[1-9]|1[0-2])\/\d{4}$", period):
            return period
