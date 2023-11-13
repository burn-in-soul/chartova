## Конфигурация
Нужен Redis/RabbitMQ для работы очереди

В файле `config.py`:

```python
HOURS = {  # Коэффициент голосов по часам
    0: Decimal('0.05'),
    1: Decimal('0.03'),
    2: Decimal('0.02'),
    3: Decimal('0.01'),
    4: Decimal('0.01'),
    5: Decimal('0.01'),
    6: Decimal('0.01'),
    7: Decimal('0.03'),
    8: Decimal('0.04'),
    9: Decimal('0.03'),
    10: Decimal('0.03'),
    11: Decimal('0.03'),
    12: Decimal('0.03'),
    13: Decimal('0.03'),
    14: Decimal('0.03'),
    15: Decimal('0.04'),
    16: Decimal('0.05'),
    17: Decimal('0.05'),
    18: Decimal('0.06'),
    19: Decimal('0.07'),
    20: Decimal('0.09'),
    21: Decimal('0.09'),
    22: Decimal('0.08'),
    23: Decimal('0.08'),
}
RANDOM_INTERVAL = 2 # граница дополнительного интервала [-RANDOM_INTERVAL, RANDOM_INTERVAL]
CELERY_BROKER = '' # брокер для заданий (redis/rabbitmq)
TOR_HOST = ''
TOR_PORT = 9095
TOR_CONTROL_PORT = 9051
TOR_PROXY = f'socks5://{TOR_HOST}:{TOR_PORT}'
TOR_PASSWORD = '' # пароль для контроля TOR
```

## Запуск celery

```shell
vim /etc/systemd/system/chartova-celery.service
```

```shell
[Unit]
Description=Celery Service
After=network.target

[Service]
Type=simple
User=$USER
Group=$GROUP
WorkingDirectory=$DIR
ExecStart=$POETRY_ENV_DIR/bin/celery -A celery_app worker -l info
Restart=always

[Install]
WantedBy=multi-user.target
```

```shell
sudo systemctl daemon-reload
sudo systemctl start chartova-celery
sudo systemctl enable chartova-celery
```


## Запуск голосования

Запуск скрипта каждый час:
```shell
$POETRY_ENV_DIR/bin/python main.py track_id vote_count
```
`vote_count` - количество голосов в день.
Запустит в селери задания в соответствии с общим кол-вом голосов в день и коэффициентом часа. 
