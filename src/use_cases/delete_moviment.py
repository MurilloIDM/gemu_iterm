from rich.console import Console

from utils.clean_view import clean_view

console = Console()


def delete_moviment(db_connection, id_moviment, user):
    clean_view()

    with console.status("[bold green]Deletando movimentação..."):
        db_cursor = db_connection.cursor()

        db_cursor.execute("DELETE FROM moviments WHERE id=%s AND username=%s;", (id_moviment, user))

        db_connection.commit()
        db_cursor.close()
