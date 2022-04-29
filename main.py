import ipaddress
from typing import TextIO
import pyfiglet
import sys
import socket
from datetime import datetime
import smtplib


# Создание Баннера PORT SCANNER
ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
# Вывод баннера
print(ascii_banner)

# Открытие файла с ip и вывод содержимого
with open('ip.txt', 'r') as f_ip:
    ip_text = f_ip.read()
    print(ip_text)

# Создание списка с помощью .split()
items_ip = ip_text[0:-1].split(',')
# Вывод списка
print(items_ip)

# Открытие файла с портами и вывод содержимого
with open('port.txt', 'r') as f_port:
    port_text = f_port.read()
    print(port_text)
items_port = port_text[0:9].split(',')
print(items_port)

# Создание пустого словаря для заполнения ip адресами и доступными им портами
open_ip_dict = {}

# С помощью цикла перебераем содержимое списка, элементами которого являются ip адреса
#  осущевляется проверка на "закрыт" или "открыт" порт 443
for element_ip in items_ip:
    for element_port in items_port:
        ip = ipaddress.ip_address(element_ip)
        target = socket.gethostbyname(element_ip)
        print('-' * 50)
        print('Scanning Target: ' + target)
        print('Scanning started at: ' + str(datetime.now()))
        print('-' * 50)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, int(element_port)))
        if result == 0:
            print('Ip адрес: ', element_ip,   '------->>>  '   'порт:', element_port, 'открыт !!!')
            open_ip_dict[element_ip] = element_port
        else:
            print('Ip адрес: ', element_ip,   '------->>>  '   'порт:', element_port, 'закрыт !!!')
print('-' * 50)

# Вывод словаря c ip  и доступными им портами
print('Ip адрес и доступный ему порт: ', '\n', open_ip_dict)

f = open('dict_ip.txt', 'w')
f.write(str(open_ip_dict))
f.close()

# Отправка результата работы скрипта на почту

smtpObj = smtplib.SMTP('172.17.74.49', 25)
# smtpObj.starttls()
print(smtpObj)

# Отправка строки приветствия SMTP-серверу методом .ehlo()
smtpObj.ehlo()
# при успешном завершении операции с SMTP выводится:
# (250, b'zabbix.em.local\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nENHANCEDSTATUSCODES\n8BITMIME\nDSN')
print(smtpObj.ehlo())

# Начало TLS-шифрования методом .starttls
# smtpObj.starttls()
# print(smtpObj.starttls())
# Будем думать что для порта 25 TLS-шифрование настроено

# Выполнение процедуры входа на SMTP-сервер
# smtpObj.login('KurochkinAV@em.mos.ru', 'KAV_013yrgpem!')



smtpObj.sendmail('hdwpost@em.mos.ru', 'KurochkinAV@em.mos.ru', list[open_ip_dict] )
# 'Subject: Andryukha, hello!!!! How are you ?? What are you doing???'
smtpObj.quit()