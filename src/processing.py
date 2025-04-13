from typing import Dict, List, Union


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует операции в списке по ключу 'state'"""
    list_of_operation = []
    for item in operations:
        if item["state"] == state:
            list_of_operation.append(item)
    return list_of_operation


def sort_by_date(operations: List[Dict], flow: bool = True) -> Union[List, str]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""
    sort_by_date_list = sorted(operations, key=lambda operation: operation["date"], reverse=flow)
    return sort_by_date_list
