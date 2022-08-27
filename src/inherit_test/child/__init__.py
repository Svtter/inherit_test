
from inherit_test.center import settings


def new_get_login_method():
    return 'inherit_test.child.login'


# duck type
settings.get_login_method = new_get_login_method


print('child method loaded.')
