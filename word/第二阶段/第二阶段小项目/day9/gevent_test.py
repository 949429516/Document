import gevent 

def foo():
    print("Running in foo")
    gevent.sleep(2)
    print("switch to foo again")

def bar():
    print("Running in bar")
    gevent.sleep(3)
    print("switch to bar again")

#将两个函数设置为协成,此时协成函数运行
f = gevent.spawn(foo)
b = gevent.spawn(bar)

#回收协成
gevent.joinall([f,b])
