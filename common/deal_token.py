import os
import yaml
import json
from common.get_log import setup_logging

logger = setup_logging()

def extract_access_token(res):
    if not res:
        logger.error("Response is empty or None")
        return None

    # 尝试从字典中提取 access_token
    if isinstance(res, dict):
        return res.get('access_token')
    # 尝试从 JSON 字符串中提取 access_token
    if isinstance(res, str):
        try:
            res_dict = json.loads(res)
            return res_dict.get('access_token')
        except json.JSONDecodeError:
            logger.error(f"Failed to parse response as JSON. Content: {repr(res)}", exc_info=True)
            # 尝试从字符串中直接提取 access_token
            if 'access_token' in res:
                try:
                    return res.split('access_token')[1].split('"')[1]
                except IndexError:
                    logger.error("Failed to extract access_token from string response", exc_info=True)

    logger.error(f"Unsupported response type: {type(res)}")
    return None



def write_token(res):
    access_token = extract_access_token(res)
    if access_token is None:
        logger.error("Failed to extract access_token from response")
        return

    curPath = os.path.abspath(os.path.dirname(__file__))
    yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "configs/access_token.yml")

    tokenValue = {
        'access_token': access_token
    }
    with open(yamlPath, 'w', encoding='utf-8') as f:
        yaml.dump(tokenValue, f)
    logger.info('\n token已保存至配置文件中')