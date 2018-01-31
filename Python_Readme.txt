====================当前版本信息====================
当前版本：V4 Beta1.0.0

发布日期：2014-12-18

====================================================

====================修改历史====================


================================================

************************************************中文*****************************************************
发布介绍:

此客户端库,目前支持百度商业推广API V4版功能。 
使用示例请参考*Example.py。本客户端库旨在提供调用封装以及代理类生成，并不提供客户端业务逻辑。 
使用过程中如果遇到任何问题，请联系apihelp@baidu.com并在标题注明《Baidu API Client V4使用过程问题求助》


注意事项:

1. 相关工具安装
使用json方式调用Python SDK需要安装requests插件，下载地址：http://www.python-requests.org/en/latest/user/install/#install 

2. 如何使用Python SDK

如何初始化Service？ 
使用者获取具体的service对象方法是：


       service = sms_service_AccountService()
sms_service_AccountService的三段分别代表产品线缩写、版本号、服务名 
此时会从baidu-api.properties里加载默认用户信息，包括url、username、password、token、target、accessToken等。
若想重新设置这些参数，可以执行以下方法：


       service.setUsername("xxx")
       service.setPassword("xxx")
       service.setToken("xxx")
如何调用API进行请求 ? 
使用获取的service对象调用其指定方法，如

       request = {"accountFields":["userId", "cost"]}
       res = service.getAccountInfo(request)
       printJsonResponse(res)
       print PreviewUtil.decode(res["body"]["data"])
res中保存了这次调用返回结果，可以调用printJsonResponse方法打印结果，用户也可以类似上例自定义方法获取结果。
3. 本客户端库的运行环境 ?

       python 2.7+
4. 服务器证书 ?

如果想通过程序下载报告，可以导入证书VeriSign_G5.crt到开发环境

------------------------------------------------------------------------------------------------------------------
Copyright 2014 Baidu.com Inc.
Baidu API Team
