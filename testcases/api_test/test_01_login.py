# @Time :2024/11/4 10:54
import os

import pytest
import allure
import json
from testcases.conftest import api_data
from common.get_log import setup_logging
from operation.fastweb import login_user

logger = setup_logging()


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))



@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():

    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username,password)
        step_1(username)
        # 查看实际访问网页的预期结果
        assert result.success == except_result, result.error
        assert result.response.json().get("code") == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("msg") == except_msg, result.error
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_login.py'])







