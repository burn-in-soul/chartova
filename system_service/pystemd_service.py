from pystemd.systemd1 import Unit


class SystemdService:

    def restart(self, name: bytes) -> None:
        with Unit(name) as service:
            service.Unit.Restart(b'replace')
