# trip — расходы в поездке

Программа считает, сколько всего потрачено за поездку и какая средняя трата, и печатает отчёт.

## Запуск

Windows (PowerShell):

```text
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python trip.py
```

macOS / Linux:

```text
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python trip.py
```

## Что печатает

```text
ОТЧЁТ ПО ПОЕЗДКЕ          (зелёный жирный заголовок через Rich)
--------------------------------
записей: 10
всего потрачено: 7900 ₽
средняя трата: 790.00 ₽
```

Расчёты (`calculate_total`, `calculate_average`) лежат в `calculator.py`.
