import re

from rich.console import Console
from rich.prompt import Prompt

console = Console()


def render_form_create():
    description = Prompt.ask("Informe a descrição")

    bank = Prompt.ask("Informe o banco").upper()

    period = Prompt.ask("Informe o período", choices=["MENSAL", "SEMESTRAL", "ANUAL", "PARCELA"])

    if (period == "PARCELA"):
        parcel = Prompt.ask("Informe a parcela (ex: 8 de 10)")
        period = f"{period} ({parcel})"

    typeMoviment = Prompt.ask("Informe o tipo", choices=["ENTRADA", "SAÍDA"])

    date = ""
    while True:
        date = Prompt.ask("Informe a data seguindo o padrão (ex: 01/12/2003)")

        if re.match(r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}\b", date):
            break

    value = ""
    while True:
        value = Prompt.ask("Informe o valor seguindo o padrão (ex: 1000.25)")

        if re.match(r"^\d+([.,]\d{1,2})?$", value):
            break

    return {
        "description": description,
        "bank": bank,
        "period": period,
        "type": typeMoviment,
        "date": date,
        "value": float(value)
    }
