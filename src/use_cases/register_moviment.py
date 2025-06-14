from rich.console import Console

from utils.clean_view import clean_view

console = Console()


def register_moviment(db_connection, data, user):
    clean_view()

    with console.status("[bold green]Cadastrando movimentação..."):
        db_cursor = db_connection.cursor()

        db_cursor.execute("""
                        INSERT INTO moviments (description, bank, period, type, pay_date, value, username)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (data["description"], data["bank"], data["period"], data["type"], data["date"], data["value"], user))

        db_connection.commit()
        db_cursor.close()
