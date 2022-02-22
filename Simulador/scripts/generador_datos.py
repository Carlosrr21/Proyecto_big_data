from subprocess import call
from time import sleep
from ProductsSimulation import ProductsSimulation 
from PrensadoraSimulation import PrensadoraSimulation 
from MotorSimulation import MotorSimulation
import os

IOT_AGENT_URL = os.getenv('IOT_AGENT_URL', 'http://localhost:7896/iot/d')
IOT_AGENT_KEY = os.getenv('IOT_AGENT_KEY', '4jggokgpepnvsb2uv4s40d5911')

prensadora = PrensadoraSimulation(IOT_AGENT_URL,IOT_AGENT_KEY)
motor= MotorSimulation(IOT_AGENT_URL,IOT_AGENT_KEY)


i=0
while 1==1:

  prensadora.sendData()
  motor.sendData()
  
  i+=1
 
