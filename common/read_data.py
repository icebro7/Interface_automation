# @Time :2024/11/29 15:32
import yaml
import json
from configparser import ConfigParser
from common.get_log import setup_logging

class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        self.logger = setup_logging()

    def load_yaml(self, file_path):
        self.logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        self.logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_json(self, file_path):
        self.logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        self.logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        self.logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

data = ReadFileData()