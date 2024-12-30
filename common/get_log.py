import logging
import os
from datetime import datetime

def setup_logging():
    # 创建日志记录器
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 检查是否已经存在一个 FileHandler
    if not logger.hasHandlers():
        # 创建控制台处理器，并设置日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 获取根目录路径
        file_dir = os.path.abspath(os.path.dirname(__file__))
        root_path = os.path.join(file_dir, '..')

        # 检查并创建最外层的 log 文件夹
        log_base_dir = os.path.join(root_path, 'log')
        if not os.path.exists(log_base_dir):
            os.makedirs(log_base_dir)

        # 创建文件处理器，并设置日志级别
        current_month = datetime.now().strftime('%Y_%m')
        log_dir = os.path.join(log_base_dir, f'log_{current_month}')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建日志文件路径
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file_path = os.path.join(log_dir, f'app_{timestamp}.log')

        # 使用 delay=True 参数延迟文件的打开
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8', delay=True)
        file_handler.setLevel(logging.DEBUG)

        # 创建日志格式化器
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 将格式化器添加到处理器
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    # 设置日志记录
    logger = setup_logging()

    # 记录不同级别的日志
    logger.debug('这是一个调试信息')
    logger.info('这是一个信息')
    logger.warning('这是一个警告')
    logger.error('这是一个错误')
    logger.critical('这是一个严重错误')