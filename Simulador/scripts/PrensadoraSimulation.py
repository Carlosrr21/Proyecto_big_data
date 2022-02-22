# -*- coding: utf-8 -*-
import datetime
import time
import random
from pip._vendor import requests

class PrensadoraSimulation:

    fuerza=0; 
    temperatura =0;
    humedad = 0;
    iotagenturl="";
    iotagentkey="";
    
    def __init__(self,iotagenturl,iotagentkey):
        self.iotagenturl = iotagenturl
        self.iotagentkey = iotagentkey
        

    
    def payload(self,devicename,date):
        #p|80|b|50|t|85
        ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.fuerza = random.uniform(2, 10)
        self.temperatura = random.uniform(15, 75)
        self.humedad = random.uniform(5, 25)
        payloadStr = "f|"+str("{0:.2f}".format(self.fuerza))+"|t|"+str("{0:.2f}".format(self.temperatura))+"|h|"+str("{0:.2f}".format(self.humedad))
        payloadStr= "n|"+devicename+"|"+payloadStr+"|d|"+str(ahora) 
        return payloadStr

    def sendData(self):

        

        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Prensadora"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            payload1 = self.payload(devicename,datetime.datetime.now())
            r1 = requests.post(url= endpoint1,headers=header, data=payload1)
            print("datos sensor {} {} ".format(devicename,payload1))
            i+=1
            time.sleep(1)

    def sendHistoricalData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Prensadora0"+str(i)
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
       




