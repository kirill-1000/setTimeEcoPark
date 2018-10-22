Скрипт написан для установки времени в автоматических и ручных барьерах AUTOGARD 

https://www.autogard.cz/en/

http://www.apsecopark.ru/

Суть проблемы: Если используется система без центрального сервера то из-за отсутсвия синхронизации 
аппаратное время плат устройств не совпадает с мировым. 

Скрипт посылает время компьютера с которгого запускается на устройство.
Пакет посылается по udp.

python3 setTimeEcoPark.py -ip xxx.xxx.xxx.xxx -port xxxx 

Проверен на АПС EcoPark EPE, АПС EcoPark EPA, АПС EcoPark EPS

Requirements

    python >=3.5
