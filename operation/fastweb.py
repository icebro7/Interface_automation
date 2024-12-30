# @Time :2024/11/29 17:24

from core.result_base import ResultBase
from api.fast_api import fast
from common.get_log import setup_logging


logger = setup_logging()


def login_user(username, password):
    result = ResultBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    res = fast.login(json=payload, headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
        result.token = res.json()["data"]["access_token"]

    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def get_user_info(token):
    result = ResultBase()
    header = {
        'accept': 'application/json',
        'token': token
    }
    res = fast.get_user_info(headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def create_user(token,email,username,password,is_active,is_superuser,role_ids,dept_id):
    result = ResultBase()
    header = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'token': token
    }
    payload = {
        "email": email,
        "username": username,
        "password": password,
        "is_active": is_active,
        "is_superuser": is_superuser,
        "role_ids": role_ids,
        "dept_id": dept_id
    }
    res = fast.create_user(json=payload, headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True

    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


# 登录用户
# print(login_user("admin", "123456").response.json().get("code"))
# 正确返回
# {"code":200,"msg":"OK","data":{"access_token":"exxx","username":"admin"}}

# 错误返回
# {"code":400,"msg":"密码错误!","data":null}


# 创建用户
# token = login_user("admin","123456").token
# print(token)
# create_user(token)

# 查看用户
# token = login_user("admin", "123456").token
# print(get_user_info(token).response.json())
