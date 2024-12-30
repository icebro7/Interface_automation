# Interface_automation

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure** ，主要是针对本人的一个接口项目来开展，通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。
>相关接口项目：[基于 FastAPI + Vue3 + Naive UI 的现代化前后端分离开发平台](https://github.com/icebro7/fastwebsite.git)

## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

## 项目部署

首先在根目录找到```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：
```
pip3 install -r requirements.txt
```

接着在根目录中的data目录下找到yaml文件，配置需要进行测试的接口地址、请求方法、请求参数、请求头、预期结果等数据。

然后在根目录中的api目录修改对应路径

最后窗口执行测试用例：

```
pytest -s -q ./testcases/api_test/test_01_login.py --alluredir=./testcases/report
```

生成 Allure HTML 报告：

```
# 需要提前配置allure环境
allure generate ./testcases/report -o ./testcases/report/html --clean
```

打开 Allure 报告：

```
allure open ./testcases/report/html
```


**注意**：因为我这里是针对自己的接口项目进行测试，如果想直接执行我的测试用例来查看效果，需要提前部署上面提到的[基于 FastAPI + Vue3 + Naive UI 的现代化前后端分离开发平台](https://github.com/icebro7/fastwebsite.git)



## 目录说明

```
├── api                   // 接口封装层
├── common                // 各种工具类
├── configs               // 配置文件
├── core                  // requests请求方法封装、关键字返回结果类
├── data                  // 数据存放目录
│   └── yaml              // yaml文件目录
├── log                   // 日志存放目录
├── operation             // 关键字封装层
└── testcases             // 测试用例
    └── api_test          // api测试用例
    └── report            // 测试报告
```

