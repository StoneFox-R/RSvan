import urllib.request,requests
import http.client
import json

test_data = {"username":"aaa"}
 #Context是你的表里的列
test_data = json.dumps(test_data)
 #此处将数据转换成JSON格式才能提交，不然会返回107错误
requrl = "/1/classes/_User/" 
 #替换为自己的表名
headerdata = {"X-Bmob-Application-Id":"37a47ce39b7cee8e517b274a64f499d4",
"X-Bmob-REST-API-Key":"40f5607475cffc3f67631a93460abec4",
"Content-Type": "application/json"}
class BmobCloud():
    def Login(self,username,password):
        print('start')

    def Registered(self,username,password):
        test_data={'username':str(username),'password':str(password)}
    def Login(self,username,password):
        data={'username':str(username),'password':str(password)}
        r=requests.get("https://api2.bmob.cn/1/login",params=data,headers=headerdata)
        s=r.text.split('"')
        if s[1]=='createdAt':
            print('User:'+username+'login successful')
            return True
        #print(s)
        #print(r.text.split(','))

    def Post(self,username,password):
        test_data={'username':str(username),'password':str(password)}
        test_data = json.dumps(test_data)
        conn = http.client.HTTPConnection("api.bmob.cn")
        conn.request(method="POST",url=requrl,body=test_data,headers = headerdata )
        response = conn.getresponse()
        res= response.read()
        print (res)

    def Get(self,id):
        requrl = "/1/classes/_User/%s"%(id) 
        conn = http.client.HTTPConnection("api.bmob.cn")
        conn.request(method="GET",url=requrl,headers = headerdata,body=test_data )
        response = conn.getresponse()
        res= response.read()
        print (res)
    def Put(self,id,password):
        requrl = "/1/classes/_User/%s"%(id) 
        print(requrl)
        worrd="{'password':%s}"%(password)
        print (worrd)
        print(headerdata)
        conn = http.client.HTTPConnection("api.bmob.cn")
        conn.request(method="PUT",url=requrl,headers = headerdata,body=test_data)
        response = conn.getresponse()
        res= response.read()
        print (res)
    def send(self,method,):
        print()


#BmobCloud.Login(BmobCloud,"c44455faf0",1231234569)
#BmobCloud.Put(BmobCloud,"c44455faf0",1231234569)
