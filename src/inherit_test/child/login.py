from inherit_test.father.login_api import LoginAPI


class LoginImp(LoginAPI):
    def login(self):
        print('child logic ...')
        print('hello world')
        print('child logic end ...')
