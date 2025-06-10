from rich.console import Console

from utils.clean_view import clean_view

console = Console()


def get_moviments(db_connection, period, user):
    clean_view()

    with console.status("[bold green]Buscando movimentações do período..."):
        db_cursor = db_connection.cursor()

        period_list = period.split("/")
        formatted_period = f"{period_list[1]}-{period_list[0]}"

        db_cursor.execute(f"""
                        SELECT * FROM moviments
                        WHERE pay_date::text LIKE '{formatted_period}%'
                        AND username = '{user}'
                        ORDER BY bank, type
        """)

        moviments = db_cursor.fetchall()

        db_cursor.close()

        return moviments
