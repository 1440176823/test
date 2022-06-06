"""
@Time : 2021/7/8 21:54
@Author : liweiwei
@Email : 1440176823@qq.com
@File : test_fixture.py
@Project : pytest
@feature :
1. 练习pytest装饰器
2. 以登录函数作为被装饰的函数，来模拟以下应用场景：当测试用例需要先登录在执行时，
可以通过pytest装饰器来装饰登录函数，并把登录函数名称作为参数传给测试用例。
@实现步骤：
"""

import pytest


@pytest.fixture()
def login():
    print('\nlogin operation')


def test_case_7(login):
    print('\nenter test_case_7')
    assert True


def test_case_8():
    print('\nenter test_case_8')
    assert True


def test_case_9(login):
    print('\nenter test_case_9')
    assert True


if __name__ == '__main__':
    args = ['-s', '-q', 'test_fixture.py']
    pytest.main(args)
