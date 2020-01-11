import requests
from collections import OrderedDict


class Request():
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


class LoginRequest(Request):
    def __init__(self, status_code, text, success):
        super().__init__(status_code, text)
        self.success = success


class Requester():

    def __init__(self, ip):
        self.ip = "http://" + ip
        self.setter = "/xml/setter.xml"
        self.getter = "/xml/getter.xml"
        self.token = ""

    def __setToken(self):
        self.token = self.request.cookies.get('sessionToken')

    def get(self, fun, args={}):
        data = OrderedDict([
            ("token", self.token),
            ("fun", fun)
        ])
        if args:
            for key, value in args.items():
                data[key] = value
        self.request = requests.post(self.ip + self.getter, data=data, allow_redirects=False)
        self.__setToken()
        return Request(self.request.status_code, self.request.text)

    def set(self, fun, args={}):
        data = OrderedDict([
            ("token", self.token),
            ("fun", fun)
        ])
        if args:
            for key, value in args.items():
                data[key] = value
        self.request = requests.post(self.ip + self.setter, data=data, allow_redirects=False)
        self.__setToken()
        return Request(self.request.status_code, self.request.text)