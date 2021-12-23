""" service cls"""


class Service:
    """service cls"""

    def __init__(self, env: str):
        """get require env:str"""

        self.APP_ENV = env

    def get_env(self):
        """return APP_ENV"""

        return self.APP_ENV

    def __repr__(self):
        """repr instanse"""

        return f"env = {self.APP_ENV}"
