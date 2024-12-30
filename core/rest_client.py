# @Time :2024/11/29 15:23
import os
import requests
import json as complexjson
from common.get_log import setup_logging


class RestClient():
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()
        self.logger = setup_logging()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        files = kwargs.get("files")
        cookies = kwargs.get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        elif method == "POST":
            return self.session.post(url, data, json, **kwargs)
        elif method == "PUT":
            if json:
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        elif method == "DELETE":
            return self.session.delete(url, **kwargs)
        elif method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        self.logger.info("接口请求地址 ==>> {}".format(url))
        self.logger.info("接口请求方式 ==>> {}".format(method))
        self.logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        self.logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        self.logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        self.logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))


