import os
import pytest
import subprocess

if __name__ == '__main__':
    # 定义报告目录
    report_dir = './report'
    html_report_dir = './report/html'

    # 如果报告目录不存在，则创建
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    if not os.path.exists(html_report_dir):
        os.makedirs(html_report_dir)

    # 执行 pytest 测试用例并生成 Allure 结果
    pytest.main(['-s', '-q', './api_test/test_01_login.py', '--alluredir={}'.format(report_dir)])

    # 生成 Allure HTML 报告
    subprocess.call(['allure', 'generate', report_dir, '-o', html_report_dir, '--clean'])

    # 打开 Allure 报告（可选）
    subprocess.call(['allure', 'open', html_report_dir])