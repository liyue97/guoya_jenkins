import allure
import requests
#request发送http请求

@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例1")
def test_no_params():
    #使用requests.get发送一个get请求
    #r = requests.get("https://www.baidu.com/")
    #使用requests.request发送一个get请求
    #r = requests.request(method="get",url="https://www.baidu.com/")
    sess = requests.session()#使用session建立连接
    r = sess.request(method="get",url="https://www.baidu.com/")#再发送请求，无论请求多少次，连接只建立一次
    r = sess.request(method="get",url="https://www.baidu.com/")
    print(r.text) #text获取响应对象中，响应正文的数据


@allure.feature("get请求")
@allure.story("带参数")
@allure.title("用例2")
def test_get_query():
    #get请求带参数
    params = {"accountName":"yy123"} #把get参数都放入一个字典中
    r = requests.request("get","http://qa.yansl.com:8084/acc/getAccInfo",params = params)#请求时以params关键字传参
    print(r.text)

@allure.feature("get请求")
@allure.story("path参数")
@allure.title("用例3")
def test_get_path():
    #get请求参数在path中
    #使用.format进行字符串格式化
    r = requests.request("get","http://qa.yansl.com:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1,pageSize=10))
    print(r.text)

@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例4")
def test_get_file(pub_data):
    # get请求下载文件
    with allure.step("第一步、准备测试数据"):pass
    p = {"pridCode":"ower360"}
    h = {"token":pub_data["token"]}
    with allure.step("第二步、发送请求"):pass
    r = requests.request("get","http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步、请求数据"):
        allure.attach("请求行,请求头,请求正文","请求信息",allure.attachment_type.TEXT)
    #r.content获取响应正文的字节码（二进制）
    with open("aa.xls","wb") as f: # with语法 打开文件，并赋值给变量f
        f.write(r.content) # 把响应正文中的数据写入到文件中