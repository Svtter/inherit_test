
from inherit_test.center import settings


def new_get_login_method():
    return 'inherit_test.child.login'


# duck type
# Q: 这种修改是否是一种必然呢？能否不修改，也能得到相同的效果？
settings.get_login_method = new_get_login_method


print('child method loaded.')
