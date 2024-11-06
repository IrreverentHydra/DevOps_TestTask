# DevOps_TestTask

## Описание
Проект включает два модуля:
1. `fetch_time.py` - скрипт для работы с API времени Yandex.
2. `generate_versions.py` - скрипт для генерации версий на основе конфигурационного файла.

## Установка
1. Клонируйте проект и установите зависимости:
    git clone <URL>
    cd project_name
    pip install -r requirements.txt


## Конфигурация
Шаблоны версий для `generate_versions.py` находятся в `config/config.json`.

## Использование
Для запуска:

1. Получение времени и расчета дельты:
    python main.py fetch_time

2. Генерация и фильтрация версий:
    python main.py generate_versions <product_version> config/config.json

### Пример
python main.py generate_versions "3.7.5" "config/config.json"
