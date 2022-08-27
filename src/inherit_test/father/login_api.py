import abc


class LoginAPI(abc.ABC):
    @abc.abstractmethod
    def login(self):
        pass