# @Time :2024/12/6 20:53

import pytest
from pathlib import Path
import allure
from api.fast_api import fast
from common.read_data import data
from common.get_log import setup_logging
# from common.mysql_operate import db

logger = setup_logging()


BASE_PATH = Path(__file__).resolve().parent.parent

# 映射文件扩展名到加载函数
LOADERS = {
    '.yaml': data.load_yaml,
    '.yml': data.load_yaml,
    '.json': data.load_json,
    '.ini': data.load_ini,
}

# 获取数据，对各文件夹内容进行分类提取
def get_data(dir, file_name):
    data_file_path = BASE_PATH / "data" / dir / file_name
    file_extension = data_file_path.suffix.lower()

    try:
        loader = LOADERS.get(file_extension)
        if not loader:
            pytest.skip(f"Unsupported file type: {file_extension}")
        return loader(data_file_path)
    except Exception as ex:
        pytest.skip(f"Error loading file {data_file_path}: {ex}")


api_data = get_data("yaml", "api_test_data.yml")

@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")

@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))
















