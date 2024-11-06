import requests
import time
from datetime import datetime, timezone, timedelta

def fetch_time():
    """Отправляет запрос к Yandex API и выводит результат"""
    url = "https://yandex.com/time/sync.json?geo=213"
    start_time = time.time()
    response = requests.get(url)
    response_raw = response.json()
    print("Raw response: ", response_raw)

    """Человекопонятный формат"""
    timestamp = response_raw['time']/1000
    formatted_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    time_zone = response_raw.get("tzinfo", {}).get("name", "Unknown")
    print("Time in human-readable format: ", formatted_time)
    print("Time zone: ", time_zone)

    """Вычисление дельты времени"""
    end_time = time.time()
    request_duration = end_time - start_time
    server_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    local_time = datetime.fromtimestamp(start_time, tz=timezone.utc)
    delta = server_time - local_time + timedelta(seconds=request_duration)
    print("Delta time: ", delta)
    return delta.total_seconds()

def calculate_average_delta():
    """Выполняет 5 запросов и выводит среднюю дельту времени"""
    deltas = [fetch_time() for _ in range(5)]
    average_delta = sum(deltas) / len(deltas)
    print("Average delta time over 5 requests: ", average_delta)