from typing import Self

import stem

import config

stem.util.log.get_logger().propagate = False


class TorController:

    def __init__(self) -> None:
        self.controller = stem.control.Controller.from_port(
            address=config.TOR_HOST,
            port=config.TOR_CONTROL_PORT)
        self.controller.authenticate(password=config.TOR_PASSWORD)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.controller.close()

    def reload(self) -> None:
        self.controller.signal(stem.Signal.NEWNYM)
