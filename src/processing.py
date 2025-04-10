from typing import Any, Dict, List


def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует операции в списке по ключу 'state'"""
    list_of_operation = []
    for item in operations:
        if item["state"] == state:
            list_of_operation.append(item)
    return list_of_operation


def sort_by_date(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""
    return sorted(operations, key=lambda item: item["date"], reverse=True)
