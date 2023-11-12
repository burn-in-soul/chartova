from pystemd.systemd1 import Unit


class SystemdService:

    def restart(self, name: str) -> None:
        unit = Unit(f'{name}.service')
        unit.Unit.Restart(mode=b's')
