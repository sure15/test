import hashlib
db={}
def md5(data1,data2):
    data2=data2+data1+'the-Salt'
    m=hashlib.md5(data2.encode(encoding='utf8'))
    password1=m.hexdigest()
    return(password1)
def login():
    data1=input('请输入用户名：  ')
    data2=input('请输入密码：  ')
    password1=md5(data1,data2)
    if data1 in db:
        if password1==db[data1]:
            print('登陆成功')
        else:
            print('密码错误')
    else:
        print('不存在该用户')
def register():
    data1=input('请输入您的用户名： ')
    data2=input('请输入您的密码： ')
    password1=md5(data1,data2)
    db[data1]=password1
