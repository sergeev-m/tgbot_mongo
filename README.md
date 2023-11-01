# Telegram bot, mongodb

Алгоритм агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам

- Паттерн репозиторий
- Асинхронный код

### Пример входных данных:
{
"dt_from":"2022-09-01T00:00:00",
"dt_upto":"2022-12-31T23:59:00",
"group_type":"month"
}

###  Пример ответа:  
{"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]}

## Старт

```bash
git clone git@github.com:sergeev-m/tgbot_mongo.git

# Переименовать .env.example на .env

docker-compose up
```

## Используемы инструменты

- python - 3.11
- Asyncio
- aiogram
- MongoDB - 7
- docker compose - 3.9

***

### Контакты

Михаил  
[email](server-15@yandex.ru)  
[telegram](https://t.me/sergeev_mikhail)
