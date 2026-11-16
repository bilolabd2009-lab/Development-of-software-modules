"""Загрузка заказов смены и расчёт выручки по официантам."""

from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Читает заказы смены из CSV-файла.

    Args:
        path: Путь к CSV-файлу с колонками waiter и kopeks.

    Returns:
        Список заказов в том порядке, в каком они записаны в файле.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку каждого официанта и сортирует по убыванию.

    Args:
        orders: Заказы смены.
        top: Сколько официантов оставить в ответе; 0 — всех.

    Raises:
        ValueError: Если список заказов пуст.

    Returns:
        Словарь «официант → выручка в копейках», от большей суммы к меньшей.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Сортирует заказы по убыванию суммы, меняя сам список.

    Args:
        orders: Заказы, которые нужно упорядочить.
    """
    orders.sort(key=lambda order: -order.kopeks)
