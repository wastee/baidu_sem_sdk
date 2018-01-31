import os
import sys
import json
import configparser
import traceback as tb
import requests

from AuthHeader import *
from DataPack import *


class ApiSDKJsonClient():
    # client params
    __productline = None
    __version = None
    __service = None
    __url = None
    __username = None
    __password = None
    __token = None
    __target = None
    __accessToken = None
    __action = None

    # conf params
    urlconf = None
    usernameconf = None
    passwordconf = None
    tokenconf = None
    targetconf = None
    actionconf = None

    def __init__(self, productline, version, service):
        try:
            self.initConfig()
            self.__productline = productline
            self.__version = version
            self.__service = service
            self.__url = self.urlconf
            self.__username = ApiSDKJsonClient.usernameconf
            self.__password = ApiSDKJsonClient.passwordconf
            self.__token = ApiSDKJsonClient.tokenconf
            self.__target = ApiSDKJsonClient.targetconf
            self.__action = ApiSDKJsonClient.actionconf
        except Exception as e:
            print(e)
            tb.print_exc()

    def initConfig(self):
        if (ApiSDKJsonClient.actionconf == None):
            cf = configparser.ConfigParser()
            cf.read(os.path.abspath(os.path.dirname(__file__)) + "./api.properties", encoding='utf-8')
            ApiSDKJsonClient.urlconf = cf.get("api", "serverUrl")
            ApiSDKJsonClient.usernameconf = cf.get("api", "username")
            ApiSDKJsonClient.passwordconf = cf.get("api", "password")
            ApiSDKJsonClient.tokenconf = cf.get("api", "token")
            ApiSDKJsonClient.targetconf = cf.get("api", "target")
            ApiSDKJsonClient.actionconf = cf.get("api", "action")

    def execute(self, method, body):
        try:
            url = self.__url + '/json/' + self.__productline + '/' + self.__version + '/' + self.__service + '/' + method
            header = AuthHeader(username=self.__username, password=self.__password, token=self.__token,
                                target=self.__target, accessToken=self.__accessToken)
            if (body is None):
                body = {}
            pre_jsondata = DataPack(header, body)
            jsonStr = json.dumps(pre_jsondata, default=convert_to_builtin_type, skipkeys=True)
            print(jsonStr)
            headers = {'content-type': 'application/json;charset=utf-8'}
            r = requests.post(url, data=jsonStr, headers=headers)
            return r.json()
        except Exception as e:
            print(e)
            tb.print_exc()

    def setUrl(self, url):
        self.__url = url

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setToken(self, token):
        self.__token = token

    def setTarget(self, target):
        self.__target = target

    def setAccessToken(self, accessToken):
        self.__accessToken = accessToken


# 转换函数
def convert_to_builtin_type(obj):
    # 把MyObj对象转换成dict类型的对象
    d = {}
    d.update(obj.__dict__)
    return d


if __name__ == '__main__':
    result = ApiSDKJsonClient(productline='sms', version='service', service='LiveReportService').execute(method='getAccountLiveData', body={'dataType': 1,'device': 0,})
    print(result)