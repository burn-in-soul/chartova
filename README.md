## Конфигурация
Нужен Redis/RabbitMQ для работы очереди

В файле `config.py`:

```python
HOURS = {} # Коэффициент голосов по часам
RANDOM_INTERVAL = 2 # граница дополнительного интервала [-RANDOM_INTERVAL, RANDOM_INTERVAL]
CELERY_BROKER = '' # брокер для заданий (redis/rabbitmq)
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
