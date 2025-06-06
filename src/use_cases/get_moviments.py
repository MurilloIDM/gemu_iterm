import re

MOCK_DATA = [
    {
        "id": 1,
        "description": "Saque",
        "bank": "ITAÚ",
        "type": "SAÍDA",
        "period": "MENSAL",
        "date": "10/06/2025",
        "value": 22.5,
        "completed": False
    },
    {
        "id": 2,
        "description": "Transferência Nubank",
        "bank": "ITAÚ",
        "type": "ENTRADA",
        "period": "MENSAL",
        "date": "10/06/2025",
        "value": 100,
        "completed": False
    },
    {
        "id": 3,
        "description": "Serviços - IDEM Tecnologia",
        "bank": "NUBANK",
        "type": "ENTRADA",
        "period": "MENSAL",
        "date": "10/06/2025",
        "value": 1000,
        "completed": False
    },
    {
        "id": 4,
        "description": "Fatura cartão",
        "bank": "NUBANK",
        "type": "SAÍDA",
        "period": "MENSAL",
        "date": "10/06/2025",
        "value": 234.23,
        "completed": False
    },
    {
        "id": 4,
        "description": "Viagem João Pessoa",
        "bank": "NUBANK",
        "type": "SAÍDA",
        "period": "MENSAL",
        "date": "15/06/2025",
        "value": 123.88,
        "completed": False
    },
]


def get_moviments(period):
    # TODO: Implementar loader para consulta
    # TODO: Agrupar e ordenar por mês, tipo (consulta banco)
    moviments = list(filter(lambda moviment: re.search(period, str(moviment["date"])), MOCK_DATA))

    moviments.sort(key=lambda moviment: (moviment['bank'], moviment['type']))

    return moviments
