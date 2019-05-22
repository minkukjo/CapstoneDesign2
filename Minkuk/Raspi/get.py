#-*- coding:utf-8 -*-

import sys
import requests
import threading
import time
import RPi.GPIO as GPIO

reload(sys)

sys.setdefaultencoding('utf-8')

#######define
LED = 11
SRV = 12

#######command
TURNONLIGHT="ºÒÄÑÁà".decode('cp949').encode('utf-8')
TURNOFFLIGHT="ºÒ²¨Áà".decode('cp949').encode('utf-8')
BLIND_ON="Ã¢¿­¾î".decode('cp949').encode('utf-8')
BLIND_OFF="Ã¢´Ý¾Æ".decode('cp949').encode('utf-8')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(SRV,GPIO.OUT)

freq=100.0
deg_min = 0.0
deg_max = 180.0
dc_min = 5.0
dc_max = 22.0


url ='http://104.199.172.147'

def convert_dc(deg):
	return ((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

p = GPIO.PWM(SRV,freq)

p.start(0)

def getrun():
	response = requests.get(url)
	if response.text != "Empty":
		print(response.text)
		str = response.text.replace(" ","")
		print(str)		
		if str == TURNONLIGHT:
			GPIO.output(LED,GPIO.HIGH)
		elif str == TURNOFFLIGHT:
			GPIO.output(LED,GPIO.LOW)
		elif str == BLIND_ON:
			for deg in range(170,-1,-10):
				dc = convert_dc(float(deg))
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
		elif str == BLIND_OFF:
			for deg in range(0, 171,10):
				dc = convert_dc(float(deg))
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
	threading.Timer(5,getrun).start()


try:
	while 1:
		getrun()
except KeyboardInterrupt:
	pass

p.stop()

GPIO.cleanup()

