from inherit_test.center import settings
from .login_api import LoginAPI
import importlib.util
import importlib


class LoginManager:
    def __init__(self) -> None:
        login_module = importlib.import_module(settings.get_login_method())
        self.login_imp: LoginAPI = login_module.LoginImp()

    def login(self):
        self.login_imp.login()

