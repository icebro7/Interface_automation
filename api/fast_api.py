# @Time :2024/12/2 9:10
# fastapi网站api操作

import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 修改为对应的配置文件路径
data_file_path = os.path.join(BASE_PATH, "data", "yaml", "api_config_fast.yml")
api_root_url = data.load_yaml(data_file_path)["host"]


class FastWeb(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(FastWeb, self).__init__(api_root_url)

    def login(self, **kwargs):
        # 修改为对应的yaml文件路径
        url = data.load_yaml(data_file_path)["login"]["url"]
        return self.post(url, **kwargs)

    def get_user_info(self, **kwargs):
        url = data.load_yaml(data_file_path)["get_user_info"]["url"]

        return self.get(url, **kwargs)

    def create_user(self, **kwargs):
        url = data.load_yaml(data_file_path)["create_user"]["url"]
        return self.post(url, **kwargs)


fast = FastWeb(api_root_url)
