import dbus


class DbusService:

    def __init__(self) -> None:
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1',
                                     '/org/freedesktop/systemd1')
        self.manager = dbus.Interface(systemd1,
                                      'org.freedesktop.systemd1.Manager')

    def restart(self, name: str) -> None:
        self.manager.RestartUnit(name, 'fail')
