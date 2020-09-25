import pytest

'''
socpe表示作用域范围，从小到大
function ：每个用例被运行之前会被执行一次
class ：每个类被运行之前会被执行一次
module ：每个模块被运行之前会被执行一次
session ：项目启动时会被运行一次
'''

@pytest.fixture(scope="function") # 作用域
def aa():
    print("fixture函数被运行了")
    return 11

class Test111():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)

class Test222():
    def test_aa(self,aa):
        print(aa)
    def test_bb(self,aa):
        print(aa)
