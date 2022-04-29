import smtplib
import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
# import subject as subject
import logging

from bs4 import BeautifulSoup as bs
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.utils import COMMASPACE, formatdate

files_to_send = 'dict_ip.text'
msg = MIMEMultipart('alternative')
# msg['Subject'] = subject
# html = open('mail.html').read()
# text = bs(html, 'html.parser').text
# text_part = MIMEText(text, 'plain')
# html_part = MIMEText(html, 'html')

# msg.attach(text_part)
# msg.attach(html_part)
with open('dict_ip.txt', 'rb') as f:
    data = f.read()
    attach_part = MIMEBase('application', 'octet_stream')
    attach_part.set_payload(data)
encoders.encode_base64(attach_part)
attach_part.add_header('Content-Disposition', f'atachment; filename={files_to_send}')

# Открытие файла с ip и вывод содержимого
# with open('dict_ip.txt', 'r') as f_ip:
#     ip_text = f_ip.read()
#     print(ip_text)
#
# # Создание списка с помощью .split()
# items_ip = ip_text[0:-1].split(',')
# # Вывод списка
# print(items_ip)
#
# items_ip_list = list[items_ip]
# print(items_ip_list)

smtpObj = smtplib.SMTP('172.17.74.49', 25)
# #
# # # smtpObj.starttls()
# # print(smtpObj)
# #
# # # Отправка строки приветствия SMTP-серверу методом .ehlo()
smtpObj.ehlo()
# # # при успешном завершении операции с SMTP выводится:
# # # (250, b'zabbix.em.local\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nENHANCEDSTATUSCODES\n8BITMIME\nDSN')
# # print(smtpObj.ehlo())
# # # f = open('dict_ip.txt', 'w')
# # # f.write(str(list_ip))
# # # f.close()
#
# smtpObj.sendmail('hdwpost@em.mos.ru', 'KurochkinAV@em.mos.ru', str(msg))
# # # # 'Subject: Andryukha, hello!!!! How are you ?? What are you doing???'
# smtpObj.quit()


logging.basicConfig(filename='sample.log', level=logging.INFO)

logging.debug('This is a debug message')
logging.info('Informational message')
logging.error('An error has happened!')