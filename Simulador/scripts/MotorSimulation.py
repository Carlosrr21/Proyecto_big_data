import datetime
import time
import random
import requests

class MotorSimulation:

    temperatura=0; 
    velocidad =0;
    sonido = 0;
    iotagenturl="";
    iotagentkey="";
    
    def __init__(self,iotagenturl,iotagentkey):
        self.iotagenturl = iotagenturl
        self.iotagentkey = iotagentkey
        

    
    def payload(self,devicename,date):
        #v|80|t|50|s|85|d|%Y-%m-%dT%H:%M:%SZ
        
        ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.temperatura = random.uniform(45, 80)
        self.velocidad = random.uniform(9500,31000)
        self.sonido = random.uniform(40, 60)
        payloadStr = "n|"+devicename+"|v|"+str("{0:.2f}".format(self.velocidad))+"|t|"+str("{0:.2f}".format(self.temperatura))+"|s|"+str("{0:.2f}".format(self.sonido))
        payloadStr= payloadStr+"|d|"+str(ahora) 
        return payloadStr

    def sendData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Motor"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            payload1 = self.payload(devicename,datetime.datetime.now())
            r1 = requests.post(url= endpoint1,headers=header, data=payload1)
            print("datos sensor {} {} ".format(devicename,payload1))
            time.sleep(0.5)
            i+=1
            
    def sendHistoricalData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Motor"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            idays = 30
           
            while idays >=1:
                date=datetime.datetime.now() + datetime.timedelta(days=idays*-1)
                payload1 = self.payload(devicename,date)
                r1 = requests.post(url= endpoint1,headers=header, data=payload1)
                print("datos sensor {} {} ".format(devicename,payload1))
                idays-=1
                time.sleep(0.5)
            i+=1

