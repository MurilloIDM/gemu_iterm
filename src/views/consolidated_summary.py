import locale

from rich.console import Console
from rich.align import Align
from rich.layout import Layout
from rich.table import Table
from rich.columns import Columns

from use_cases.get_summary import get_summary

from utils.clean_view import clean_view

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

console = Console()
layout = Layout(name="root")


def render_consolidated_summary(data=[]):
    clean_view()

    columns = []
    summary = get_summary(data)
    banks = sorted([bank for bank in summary])

    for bank in banks:
        table = Table()
        table.title = f"Resumo {bank}"

        table.add_column("Entrada", style="green", justify="center")
        table.add_column("Saída", style="green", justify="center")
        table.add_column("Resultante", style="green", justify="center")

        table.add_row(
            locale.currency(summary[bank]['input'], grouping=True),
            locale.currency(summary[bank]['output'], grouping=True),
            locale.currency(summary[bank]['resulting'], grouping=True)
        )

        columns.append(Align(table, align="center", vertical="top"))

    console.print(Align(Columns(columns), align="center"))
