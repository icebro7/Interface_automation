# @Time :2024/11/4 11:10
import requests
import urllib3
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from common.get_log import setup_logging



class RunMethod(object):
    def __init__(self):
        # 创建一个会话
        self.session = requests.Session()
        # 定义重试策略
        retries = Retry(
            total=5,  # 总重试次数
            backoff_factor=0.1,  # 重试之间的延迟时间
            status_forcelist=[500, 502, 503, 504],  # 需要重试的HTTP状态码
            # method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]  # 需要重试的HTTP方法
        )
        # 将重试策略挂载到会话
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.logger = setup_logging()

    def get_main(self,url,headers,data=None):
        # 忽略不安全的请求警告信息
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        response = requests.get(url=url,headers=headers,data=data,verify=False)
        return response

    def post_main(self,url,headers,data):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        response = requests.post(url=url,headers=headers,data=data,verify=False)
        return response

    def run_main(self,method,url,headers,data=None):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if method.lower() == "post":
            res = self.post_main(url, headers, data)
        elif method.lower() == "get":
            res = self.get_main(url, headers, data)
        else:
            error = self.logger.error('\n 不支持该方法')

        # 检查响应的内容类型是否为JSON
        if 'application/json' in res.headers.get('Content-Type', ''):
            return res.json()
        else:
            return res.text




