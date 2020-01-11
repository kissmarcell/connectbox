from connectbox import Requester, LoginRequest


def login(self, key):
    req = self.set(15, {
        "Username": "admin",
        "Password": key
    })
    return LoginRequest(req.status_code, req.text, self.request.text.startswith("successful"))


def logout(self):
    req = self.set(16)
    return req


def changeLang(self, lang):
    req = self.set(4, {
        "lang": lang
    })
    return req


Requester.login = login
Requester.logout = logout
Requester.changeLang = changeLang