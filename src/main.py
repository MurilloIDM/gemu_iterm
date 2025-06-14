from rich.console import Console

from views.main_menu import render_main_menu
from views.filter_menu import render_filter_menu
from views.form_create import render_form_create
from views.form_access import render_form_access
from views.form_delete import render_form_delete
from views.table_records import render_table_records
from views.management_menu import render_management_menu
from views.consolidated_summary import render_consolidated_summary

from use_cases.get_moviments import get_moviments
from use_cases.delete_moviment import delete_moviment
from use_cases.register_moviment import register_moviment

from config.database import get_connection

from utils.clean_view import clean_view

console = Console()

db_connection = get_connection()

try:
    clean_view()
    username = render_form_access()

    while True:
        clean_view()
        main_option = render_main_menu()

        if main_option == '1':
            period = render_filter_menu()
            data = get_moviments(db_connection, period, username)

            render_consolidated_summary(data)
            render_table_records(period, data)
        elif main_option == '2':
            clean_view()
            management_option = render_management_menu()

            if management_option == '1':
                moviment = render_form_create()
                register_moviment(db_connection, moviment, username)

                input("Cadastro realizado com sucesso! Para seguir, aperte qualquer tecla...")
                continue
            elif management_option == '2':
                id_moviment = render_form_delete()
                delete_moviment(db_connection, id_moviment, username)

                input("Deleção realizada com sucesso! Para seguir, aperte qualquer tecla...")
                continue
            else:
                continue
        else:
            console.print("\n[#8C1C03]Programa finalizado. Foi um prazer te auxiliar![/#8C1C03]")
            break

        console.print("\n")
        input("Para exibir o menu novamente, aperte qualquer tecla...")
finally:
    console.print("\n[DATABASE] - Conexão encerrada.")
    db_connection.close()
