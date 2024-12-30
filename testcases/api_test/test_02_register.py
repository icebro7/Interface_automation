# @Time :2024/12/24 11:02
import pytest
import allure
import json
from testcases.conftest import api_data
from common.get_log import setup_logging
from operation.fastweb import create_user, login_user

logger = setup_logging()


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, password, email):
    logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}".format(username, password, email))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户注册模块")
class TestUserRegister():
    @allure.story("用例--注册用户")
    @allure.description("该用例是针对注册用户接口的测试")
    @pytest.mark.parametrize(
        "email,username,password,is_active,is_superuser,role_ids,dept_id,except_result, except_code, except_msg",
        api_data["test_register_user"])
    def test_register_user(self, email, username, password, is_active, is_superuser, role_ids, dept_id, except_result,
                           except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        token = login_user("admin", "123456").token
        result = create_user(token, email, username, password, is_active, is_superuser, role_ids, dept_id)
        step_1(username, password, email)
        # assert result.success == except_result, result.error
        assert result.response.json().get("code") == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("msg") == except_msg, result.error
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_login.py'])
