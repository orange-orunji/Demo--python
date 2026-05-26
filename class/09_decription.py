"""
装饰器
"""
def outer(func):
    def inner():
        print("start")
        func()
        print("end")
    return inner
@outer
def sleep():
    print("sleepping")
sleep()