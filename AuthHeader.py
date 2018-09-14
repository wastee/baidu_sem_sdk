# coding=utf-8
'''
    AuthHeader
'''


class AuthHeader():
    def __init__(self,
                 username=None,
                 password=None,
                 token=None,
                 target=None,
                 accessToken=None):
        self.username = username
        self.password = password
        self.token = token
        self.target = target
        self.accessToken = accessToken
        self.action = 'API-SDK'

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setToken(self, token):
        self.token = token

    def setTarget(self, target):
        self.target = target

    def setAccessToken(self, accessToken):
        self.accessToken = accessToken
