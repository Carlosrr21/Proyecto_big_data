# -*- coding: utf-8 -*-
import datetime
import time
import random
from pip._vendor import requests

class ProductsSimulation:
    def sendData(iotagenturl,iotagentkey):

        
        devicename1 ="Prensadora1"  
        devicename2 ="Prensadora2"
        devicename3 ="Prensadora3"



        url = iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911
        endpoint1 = url+devicename1+"&k="+iotagentkey
        endpoint2 = url+devicename2+"&k="+iotagentkey
        endpoint3 = url+devicename3+"&k="+iotagentkey
        header = {"ContentType":"text/plain"} 


        ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        fuerza = random.uniform(2, 10)
        temperatura = random.uniform(15, 35)
        payload1 = "p|"+str("{0:.2f}".format(fuerza))
        r1 = requests.post(url= endpoint1,headers=header, data=payload1)
        print("datos sensor {} {} ".format(devicename1,payload1))
        time.sleep(1)
            
        fuerza_2 = random.uniform(2, 10)
        temperatura_2 = random.uniform(15, 35)
        payload2 = "p|"+str("{0:.2f}".format(fuerza_2))
        r2 = requests.post(url= endpoint2,headers=header, data=payload2)
        print("datos sensor {} {}".format(devicename2,payload2))
        time.sleep(1)

        fuerza_3 = random.uniform(2, 10)
        temperatura_3 = random.uniform(15, 35)
        payload3 = "p|"+str("{0:.2f}".format(fuerza_3))
        r3 = requests.post(url= endpoint3,headers=header, data=payload3)
        print("datos sensor {} {}".format(devicename3,payload3))
        time.sleep(1)




