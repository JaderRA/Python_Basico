import requests
import datetime
import time
import json


cidade=input("Escreva sua cidade: ")

req=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid={key}')

tempo=json.loads(req.text)

print('Condição: ', tempo['weather'][0]['main'])
print('Temperatura Agora: ', round(float(tempo['main']['temp'])-273.15, 2), 'ºC')
print('Temperatura Máxima: ', round(float(tempo['main']['temp_max'])-273.15, 2), 'ºC')
print('Temperatura Mínima: ', round(float(tempo['main']['temp_min'])-273.15, 2), 'ºC')
print('Sensação Térmica: ', round(float(tempo['main']['feels_like'])-273.15, 2), 'ºC')
print('Umidade: ', tempo['main']['humidity'],'%')
