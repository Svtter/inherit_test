from importlib import import_module
from inherit_test.center import plugins, settings
from inherit_test.father.main_logic import LoginManager


def load_plugins():
    for p in plugins:
        import_module(p)


if __name__ == "__main__":
    load_plugins()
    print(settings.get_login_method())
    login_manager = LoginManager()
    login_manager.login()
