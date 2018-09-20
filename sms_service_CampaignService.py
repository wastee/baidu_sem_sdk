# coding=utf-8
from .ApiSDKJsonClient import ApiSDKJsonClient


class sms_service_CampaignService(ApiSDKJsonClient):
    def __init__(self, token=None):
        ApiSDKJsonClient.__init__(self, 'sms', 'service', 'CampaignService',
                                  token)

    def getCampaign(self, getCampaignRequest=None):
        return self.execute('getCampaign', getCampaignRequest)

    def updateCampaign(self, updateCampaignRequest=None):
        return self.execute('updateCampaign', updateCampaignRequest)

    def deleteCampaign(self, deleteCampaignRequest=None):
        return self.execute('deleteCampaign', deleteCampaignRequest)

    def addCampaign(self, addCampaignRequest=None):
        return self.execute('addCampaign', addCampaignRequest)
