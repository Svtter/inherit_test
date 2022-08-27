

class Settings:
    def get_login_method(self):
        LOGIN_METHOD = 'inherit_test.father.login'
        return LOGIN_METHOD


settings = Settings()

plugins = [
    'inherit_test.father',
    'inherit_test.child'
]
