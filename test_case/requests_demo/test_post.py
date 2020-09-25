import requests

def test_post_json():
    data = {
  "pwd": "y123456",
  "userName": "yy123"
}
    r = requests.post("http://qa.yansl.com:8084/login",json=data) #json关键字发送json类型数据
    print(r.text)


def test_post_formdata(pub_data):
    #post请求键值对数据
    data = {
    "userName": "yy123"
}
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h) #data关键字发送json类型数据
    print(r.text)


def test_post_upload_file(pub_data):
    # post请求上传文件
    data = {
        "file": open("aa.xls","rb")
    }
    h = {"token": pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=h)  # files关键字发送文件类型数据
    print(r.text)
