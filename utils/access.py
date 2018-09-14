# set_token
def set_token(username, password, token):
    result = """[api]
    serverUrl=https://api.baidu.com
    username={}
    password={}
    token={}
    target={}
    action=API-SDK""".format(username, password, token, username)
    return result