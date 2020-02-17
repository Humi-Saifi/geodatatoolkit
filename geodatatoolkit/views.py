from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from collections import namedtuple
import serial
import time
from datetime import datetime
import psycopg2

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    return render(request,"index.html",{})

def sensorData(request):
    return render(request,"sensors.html",{})

def ApiSensor1(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM disto")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)

def ApiSensor2(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM gpsnn")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)  

def ApiSensor3(request):
    all_data=None
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sensordata")
        all_data=dictfetchall(cursor)
    print(all_data)
    #return render(request,"sensors.html",{})
    return JsonResponse(all_data,safe=False)     


def runComPort(request):
    print(request.POST)
    com_port=request.POST['com_port']
    port=com_port
    if com_port=='COM4':
        ser = serial.Serial(port='COM4',
                        baudrate=4800,
                        bytesize=serial.SEVENBITS,
                        parity=serial.PARITY_EVEN,
                        timeout=200)
        print ("Serial port is open")
        if ser.isOpen() == True:

            filename = ''
            # bestimmen der Laenge einer Datei und die Anzahl der Dateien
            # Diese geben die Laenge der Messung vor
            a = 0
            i = 0
            # m = float (input('Laenge einer Datei in Minuten:'))
            # n = int (input('Anzahl der Dateien: '))
            # p = m*60

            n = 3
            nn = 1

            while a < nn:
                a = 0
                d = str(datetime.today())
                z = d.split(" ")
                da = z[0]
                date = da.split("-")
                jahr = date[0]
                monat = date[1]
                tag = date[2]
                datum = jahr + monat + tag
                ti = z[1]
                time_ = ti.split(":")
                hh = time_[0]
                mm = time_[1]
                ss = time_[2]
                ss = int(float(ss))
                if ss < 10:
                    ss = '0' + str(ss)
                    zeit = hh + mm + ss
                else:
                    zeit = hh + mm + str(ss)
                name = 'D:/Neuer Ordner (2)/data/PPython' + 'sylvac' + datum + zeit + '.txt'
                filename = name
                print(name)
                datei = open(name, "w")

                print(n)
                print(a)

                #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',                   db='sensor')  # connection with db
                connection=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
                cursor=connection.cursor()
                #connection2=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
                #cursor2=connection2.cursor()

                conn=connection
                #cur = conn.cursor()

                if conn:
                    print(" Connect!")
                    print("=========" + port + "=========")
                    #sql_com_port = "INSERT INTO com_port(com,status,table_name) VALUES ('COM4',1,'sensordata')"
                    #cursor.execute(sql2)
                    #connection2.commit()

                else:
                    print("Not Connect!")

                while a < n:

                    # ser.write(b"%R1Q,2107:0\r\n")
                    # ser.write(b"%R1Q,2003:0\r\n")
                    ser.write(b"?\r")

                    line = ser.read(9)  # lese eine Zeile aus dem seriellen Port
                    zeile = str(line)

                    if conn:  # if the connection was successful insert the data to table

                        if port == 'COM4':
                            t = time.time()
                            print('%10.4f' % t)

                            datei.write('%10.4f' % t + ' ' + zeile[2:10] + '\n')  # schreiben in eine Datei
                            time.sleep(2)
                            a += 1

                            com_port='COM4'
                            status=1;
                            table_name='sensordata';
                            sql = "INSERT INTO sensordata (date, value) VALUES (%s, %s)"
                            sql2 = "INSERT INTO sensordata (value) VALUES (%s)" %(zeile[2:10])

                            val = ('%10.4f' % t, zeile[2:10])
                            #cur.execute(sql, val)
                            cursor.execute(sql2)        
                            connection.commit()
                            #conn.commit()

                            print("record inserted in sensordata table.")

                datei.close()

        #cur.close()
        #conn.close()
        cursor.close()
        connection.close()
        #cursor2.close()
        #connection2.close()

        return JsonResponse({"sensor_id":3},safe=False)  
    
    elif com_port=='COM3':
        ser = serial.Serial(port='COM3',
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        timeout=200)
        if ser.isOpen() == True:

            filename = ''
            # bestimmen der Laenge einer Datei und die Anzahl der Dateien
            # Diese geben die Laenge der Messung vor
            a = 0
            i = 0
            # m = float (input('Laenge einer Datei in Minuten:'))
            # n = int (input('Anzahl der Dateien: '))
            # p = m*60

            n = 5
            nn = 1

            while a < nn:
                a = 0
                d = str(datetime.today())
                z = d.split(" ")
                da = z[0]
                date = da.split("-")
                jahr = date[0]
                monat = date[1]
                tag = date[2]
                datum = jahr + monat + tag
                ti = z[1]
                time_ = ti.split(":")
                hh = time_[0]
                mm = time_[1]
                ss = time_[2]
                ss = int(float(ss))
                if ss < 10:
                    ss = '0' + str(ss)
                    zeit = hh + mm + ss
                else:
                    zeit = hh + mm + str(ss)
                name = 'D:/Neuer Ordner (2)/data/PPython' + 'disto' + datum + zeit + '.txt'
                filename = name
                print(name)
                datei = open(name, "w")

                print(n)
                print(a)

                #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',
                #                    db='sensor')  # connection with db
                #cur = conn.cursor()
                connection=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
                cursor=connection.cursor()
                conn=connection
                if conn:
                    print(" Connect!")
                    print("=========" + port + "=========")
                else:
                    print("Not Connect!")

                while a < n:

                    # ser.write(b"%R1Q,2107:0\r\n")
                    # ser.write(b"%R1Q,2003:0\r\n")
                    ser.write(b"g\r\n")

                    line = ser.readline(40)  # lese eine Zeile aus dem seriellen Port
                    zeile = str(line)

                    if conn:  # if the connection was successful insert the data to table

                        if port == 'COM3':
                            t = time.time()
                            print('%10.3f' % t)

                            datei.write('%10.3f' % t + ' ' + zeile[9:15] + '\n')  # schreiben in eine Datei
                            time.sleep(2)
                            a += 1


                            sql = "INSERT INTO disto (date, value) VALUES (%s, %s)"
                            print(zeile[9:17])
                            sql2 ="INSERT INTO disto(value) VALUES(%s)" %(zeile[9:17])
                            val = ('%10.3f'% t, zeile[9:17])
                            #cur.execute(sql, val)
                            #conn.commit()
                            cursor.execute(sql2)
                            connection.commit()

                            print("record inserted in disto table.")

                datei.close()

        #cur.close()
        #conn.close()
        cursor.close()
        connection.close()
        return JsonResponse({"sensor_id":1},safe=False)  
    
    elif com_port=='COM10':
        ser = serial.Serial(port='COM10',
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        timeout=200)
        a = 0
        i = 0
        # m = float (input('Laenge einer Datei in Minuten:'))
        # n = int (input('Anzahl der Dateien: '))
        # p = m*60

        n = 200
        nn = 1

        #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='sensor')  # connection with db
        #cur = conn.cursor()
        connection = psycopg2.connect(user="dssbcuwcqanxot",
                                    password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",
                                    host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com", port="5432",
                                    database="d4sboi6172opf9")
        cursor = connection.cursor()
        conn=connection

        if conn:
            print(" Connect!")
            print("=========" + port + "=========")
        else:
            print("Not Connect!")


        while a < nn:
            a = 0
            d = str(datetime.today())
            z = d.split(" ")
            da = z[0]
            date = da.split("-")
            jahr = date[0]
            monat = date[1]
            tag = date[2]
            datum = jahr + monat + tag
            ti = z[1]
            time_ = ti.split(":")
            hh = time_[0]
            mm = time_[1]
            ss = time_[2]
            ss = int(float(ss))
            if ss < 10:
                ss = '0' + str(ss)
                zeit = hh + mm + ss
            else:
                zeit = hh + mm + str(ss)
            name = 'D:/Neuer Ordner (2)/data/PPython' + 'gnss' + datum + zeit + '.txt'
            print(name)
            datei = open(name, "w")

            print(n)
            print(a)

            while a < n:

                # ser.write(b"%R1Q,2107:0\r\n")
                # ser.write(b"%R1Q,2003:0\r\n")
                # ser.write(b"?\r")

                line = ser.readline()  # lese eine Zeile aus dem seriellen Port
                # print (line)
                zeile = str(line)
                # print (zeile[3:8])
                if zeile[3:8] == "GNGLL":
                    t = time.time()

                    print('############')
                    print('%10.4f' % t)
                    print(zeile[9:45])

                    datei.write('%10.4f' % t + ' ' + zeile[9:45] + '\n')  # schreiben in eine Datei

                    my_string = zeile[9:45]
                    result = [x.strip() for x in my_string.split(',')]

                    if conn:
                        sql = "INSERT INTO gpsnn (date, wide, lenght, GPStime) VALUES (%s, %s, %s, %s)"
                        sql2 = "INSERT INTO gpsnn(wide,lenght,GPStime) VALUES(%s,%s,%s)" %(result[0],result[2],result[4])
                        val = ('%10.4f' % t, result[0], result[2], result[4])
                        #cur.execute(sql, val)
                        #conn.commit()
                        cursor.execute(sql2)
                        connection.commit()

                        print("record inserted in gpsnn table.")


                time.sleep(0)
                a += 1
            datei.close()
        #cur.close()
        #conn.close()
        cursor.close()
        connection.close()
        return JsonResponse({"sensor_id":2},safe=False)  

def dashboard(request):
    return render(request,"dashboard.html",{})


