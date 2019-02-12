def t():
    name = "look"
    print("who am i ? : " ,name)
t()
def huangwei():
    name = '1.黄伟'
    print("who1",name)
    def liuyang():
        name = '刘洋'
        print("who2",name)
        def nulige():
            name= '努力哥'
            print("who3",name)
        print("who4",name)
        nulige()
    liuyang()
    print("who5",name)
huangwei()

t = lambda x:x+1
print(t(2))


## 定义好两个函数
def foo():
    print('111')


def bar():
    print('from the bar')
bar()
#调用
foo()