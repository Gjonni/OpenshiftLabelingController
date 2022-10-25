import os
from library.Logging import Logging


class ValidationEnviroment:
    def __init__(self):
        self.engineUrl = os.environ.get("ENGINE_URL")
        self.datacenter = os.environ.get("DATACENTER")
        self.username = os.environ.get("USERNAME")
        self.password = os.environ.get("PASSWORD")
        self.loglevel = os.environ.get("LOGLEVEL")

    @property
    def engineUrl(self):
        return self._engineUrl

    @engineUrl.setter
    def engineUrl(self, value):
        if not value:
            raise ValueError("ENGINE_URL is not set.")
        self._engineUrl = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("USERNAME is not set.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("PASSWORD is not set.")
        self._password = value

    @property
    def loglevel(self):
        return self._loglevel

    @loglevel.setter
    def loglevel(self, value):
        if not value:
            raise ValueError("LOGLEVEL is not set.")
        self._loglevel = value

    @property
    def datacenter(self):
        return self._datacenter

    @datacenter.setter
    def datacenter(self, value):
        if not value:
            raise ValueError("DATACENTER is not set.")
        self._datacenter = value.split(',')
