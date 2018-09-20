# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_KeywordService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'KeywordService',
                                  token)

    def updateWord(self, updateWordRequest=None):
        return self.execute('updateWord', updateWordRequest)

    def addWord(self, addWordRequest=None):
        return self.execute('addWord', addWordRequest)

    def deleteWord(self, deleteWordRequest=None):
        return self.execute('deleteWord', deleteWordRequest)

    def getWord(self, getWordRequest=None):
        return self.execute('getWord', getWordRequest)
