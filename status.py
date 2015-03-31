#网站状态监测器
import urllib,urllib.request

f=open('url.txt','r')
data=f.read().split('\n')
f.close()
zongshu=len(data)
b=0
data1=[]
for each in data:
    try:
        a=urllib.request.urlopen(each).read()
        b=b+1
        print(len(a),'Yes!这是第%d条记录。'%(b))
    except:
        b=b+1
        c=each,'这个网址无法访问！这是第%d条记录。'%(b)
        print(c)
        data1.append(c)
print('总共%d条记录，执行完毕！'%(b))
fs=open('result.txt','w')
fs.write(str(data1))
fs.close()
    
