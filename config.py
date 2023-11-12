from decimal import Decimal

HOURS = {
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

RANDOM_INTERVAL = 2

CELERY_BROKER = 'redis://localhost:6379/'

TOR_PROXY = 'socks5://127.0.0.1:9050'
