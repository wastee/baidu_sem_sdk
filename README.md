# Baidu SEM SDK
This is a Python3 SDK for Baidu SEM.
Original SDK is write by Python2. And it is out of date.
I changed it to make it run perfect in Python3, but no Python2.
I also delete some outdated API, and add a few new API.

I saved a few dictionary to json files in utils foler which i used to use.
Hope you like it.

Baidu SEM API doc: https://cloud.baidu.com/doc/SEM/guanliAPI.html

# Baidu SEM SDK说明
这是一个Python3 版本的Baidu SEM SDK
原始的版本是用Python2编写的，同时也已经过期。
我把它改成了可以完美运行在Python3的版本，但没有适配Python2。
同时我删除了一些老旧的API，添加了一些新的API。

我保存了一些常用的字典在utils文件夹的json里。
希望你们喜欢。

Baidu SEM API 文档: https://cloud.baidu.com/doc/SEM/guanliAPI.html


--------------------------

代码示例：
    from sms_service_AccountService import *
    service = sms_service_AccountService()
    account_info_body = {
        'accountFields': [
            'balance',  # 账户余额
            'budgetType',  # 预算类型
            'budget',  # 账户预算
            'cost',  # 账户累积消费
            'regDomain',  # 账户注册域名
            'regionTarget',  # 推广地域列表
            'userStat',  # 账户状态
        ]
    }
    print(getAccountInfo(account_info_body)
