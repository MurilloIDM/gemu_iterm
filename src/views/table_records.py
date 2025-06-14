import locale
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.align import Align

console = Console()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def render_table_records(month, data=[]):
    table = Table(show_lines=True)
    table.title = f"Registros de entradas/saídas do mês de {month}"

    table.add_column("ID", vertical="middle", justify="center")
    table.add_column("Descrição", vertical="middle")
    table.add_column("Banco", vertical="middle")
    table.add_column("Tipo", vertical="middle")
    table.add_column("Período", vertical="middle")
    table.add_column("Data", vertical="middle")
    table.add_column("Valor", style="green", justify="right")

    if len(data) == 0:
        console.print("\nOps... 🥲 Não foram encontrados registros para o mês selecionado!")
    else:
        for record in data:
            table.add_row(
                str(record["id"]),
                record["description"],
                record["bank"],
                record["type"],
                record["period"],
                record["pay_date"],
                locale.currency(record["value"], grouping=True)
            )

        console.print("\n")
        console.print(Align(table, align="center"))
