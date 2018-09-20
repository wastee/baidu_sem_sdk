# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_DynamicCreativeService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service',
                                  'DynamicCreativeService', token)

    def getDynCreative(self, getDynCreativeRequest=None):
        return self.execute('getDynCreative', getDynCreativeRequest)

    def getExclusionTypeByCampaignId(self,
                                     getExclusionTypeByCampaignIdRequest=None):

        return self.execute('getExclusionTypeByCampaignId',
                            getExclusionTypeByCampaignIdRequest)

    def addDynCreative(self, addDynCreativeRequest=None):
        return self.execute('addDynCreative', addDynCreativeRequest)

    def deleteDynCreative(self, deleteDynCreativeRequest=None):
        return self.execute('deleteDynCreative', deleteDynCreativeRequest)

    def updateDynCreative(self, updateDynCreativeRequest=None):
        return self.execute('updateDynCreative', updateDynCreativeRequest)

    def addExclusionType(self, addExclusionTypeRequest=None):
        return self.execute('addExclusionType', addExclusionTypeRequest)

    def delExclusionType(self, delExclusionTypeRequest=None):
        return self.execute('delExclusionType', delExclusionTypeRequest)
