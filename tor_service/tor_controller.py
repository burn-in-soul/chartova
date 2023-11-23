from typing import Self

import stem

import config

stem.util.log.get_logger().propagate = False


class TorController:

    def __init__(self) -> None:
        self._controller = stem.control.Controller.from_port(
            address=config.TOR_HOST,
            port=config.TOR_CONTROL_PORT)
        self._controller.authenticate(password=config.TOR_PASSWORD)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._reload()
        self._controller.close()

    def _reload(self) -> None:
        self._controller.signal(stem.Signal.NEWNYM)
