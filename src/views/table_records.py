import locale

from rich.console import Console
from rich.table import Table
from rich.align import Align

table = Table(show_lines=True)
console = Console()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def render_table_records(month, data=[]):
    table.title = f"Registros de entradas/saídas do mês de {month}"

    table.add_column("ID", vertical="middle", justify="center")
    table.add_column("Descrição", vertical="middle")
    table.add_column("Banco", vertical="middle")
    table.add_column("Tipo", vertical="middle")
    table.add_column("Período", vertical="middle")
    table.add_column("Data", vertical="middle")
    table.add_column("Valor", style="green", justify="right")
    table.add_column("Concluído?", style="#F2E205", justify="center")

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
                record["date"],
                locale.currency(record["value"], grouping=True),
                "SIM" if record["completed"] else "NÃO"
            )

        console.print("\n")
        console.print(Align(table, align="center"))
