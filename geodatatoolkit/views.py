from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from collections import namedtuple
import serial
import asyncio
import time
from datetime import datetime
import psycopg2
from django_globals import globals

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def index(request):
    return render(request,"index.html",{})

def sensorDataCloud(request):
    return render(request,"sensors.html",{})

def sensorDataLocal(request):
    return render(request,"sensors_local.html",{})

def ApiSensor1(request):
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM disto")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    disto_status_file="disto_status.txt"
    disto_status_read=open(disto_status_file,"r")
    status=int(disto_status_read.read())
    disto_status_read.close()
    if status==0:
        return JsonResponse({"error":True,"data":False},safe=True)
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="SELECT * FROM disto_realtime"
    cursor_local.execute(sql)
    all_data=dictfetchall(cursor_local)
    cursor_local.close()
    conn_local.close()
    return JsonResponse(all_data,safe=False)


def ApiSensor2(request):
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM gpsnn")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    gpsnn_status_file="gpsnn_status.txt"
    gpsnn_status_read=open(gpsnn_status_file,"r")
    status=int(gpsnn_status_read.read())
    gpsnn_status_read.close()
    if status==0:
        return JsonResponse({"error":True,"data":False},safe=True)    
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="SELECT * FROM gpsnn_realtime"
    cursor_local.execute(sql)
    all_data=dictfetchall(cursor_local)    
    cursor_local.close()
    conn_local.close()
    return JsonResponse(all_data,safe=False)  

def ApiSensor3(request):
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM sensordata")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sylvac_status_file="sylvac_status.txt"
    sylvac_status_read=open(sylvac_status_file,"r")
    status=int(sylvac_status_read.read())
    sylvac_status_read.close()
    if status==0:
        return JsonResponse({"error":True,"data":False},safe=True)
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="SELECT * FROM sensordata_realtime"
    cursor_local.execute(sql)
    all_data=dictfetchall(cursor_local)
    cursor_local.close()
    conn_local.close()
    return JsonResponse(all_data,safe=False)

def ApiSensor4(request):
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM disto")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    dxl_status_file="dxl_status.txt"
    dxl_status_read=open(dxl_status_file,"r")
    status=int(dxl_status_read.read())
    dxl_status_read.close()
    if status==0:
        return JsonResponse({"error":True,"data":False},safe=True)
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="SELECT * FROM dxl_realtime"
    cursor_local.execute(sql)
    all_data=dictfetchall(cursor_local)
    cursor_local.close()
    conn_local.close()
    return JsonResponse(all_data,safe=False)

#### LOCAL DATA
def ApiLocalSensor1(request):
    all_data=None
    conn_remote=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM disto")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM disto"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)


def ApiLocalSensor2(request):
    all_data=None
    conn_remote=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM gpsnn")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM gpsnn"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)  

def ApiLocalSensor3(request):
    all_data=None
    conn_remote=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM sensordata")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM sensordata"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()    
    return JsonResponse(all_data,safe=False)

def ApiLocalSensor4(request):
    print('HERE')
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM dxl")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    conn_remote=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_remote=conn_remote.cursor()
    sql="SELECT * FROM dxl"
    cursor_remote.execute(sql)
    print(all_data)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)

### CLOUD DATA

def ApiRemoteSensor1(request):
    all_data=None
    conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM disto")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM disto"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)


def ApiRemoteSensor2(request):
    all_data=None
    conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM gpsnn")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM gpsnn"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)  

def ApiRemoteSensor3(request):
    all_data=None
    conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_remote=conn_remote.cursor()
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM sensordata")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    #return render(request,"sensors.html",{})
    sql="SELECT * FROM sensordata"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()    
    return JsonResponse(all_data,safe=False)

def ApiRemoteSensor4(request):
    all_data=None
    #with connection.cursor() as cursor:
    #    cursor.execute("SELECT * FROM dxl")
    #    all_data=dictfetchall(cursor)
    #print(all_data)
    conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_remote=conn_remote.cursor()
    sql="SELECT * FROM dxl"
    cursor_remote.execute(sql)
    all_data=dictfetchall(cursor_remote)
    cursor_remote.close()
    conn_remote.close()
    return JsonResponse(all_data,safe=False)



def getByteSize(bytesize):
    if bytesize==5:
        return serial.FIVEBITS
    elif bytesize==6:
        return serial.SIXBITS
    elif bytesize==7:
        return serial.SEVENBITS
    elif bytesize==8:
        return serial.EIGHTBITS

def getParity(parity):
    if parity==0:
        return serial.PARITY_NONE
    elif parity==1:
        return serial.PARITY_ODD
    elif parity==2:
        return serial.PARITY_EVEN
    elif parity==3:
        return serial.PARITY_MARK
    elif parity==4:
        return serial.PARITY_SPACE


def runDXL(request,sensor,com_port,baudrate,bytesize,parity,isInternet):
    conn_remote= None
    cursor_remote=None
    dxl_status_file="dxl_status.txt"
    dxl_status=open(dxl_status_file,"w")
    dxl_status.write('1')
    dxl_status.close()
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local2=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local3=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    if isInternet:
        conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_local=conn_local.cursor()
    cursor_local2=conn_local2.cursor()
    cursor_local3=conn_local3.cursor()
    if isInternet:
        cursor_remote=conn_remote.cursor()
    try:
        if sensor=='DXL':
            a = 0
            i = 0
            n=3
            nn=1

            ser = serial.Serial(port=com_port,
                            baudrate=int(baudrate),
                            bytesize=getByteSize(int(bytesize)),
                            parity=getParity(int(parity)),
                            timeout=200)
            sql="DELETE FROM dxl_realtime"
            cursor_local2.execute(sql)
            conn_local2.commit()
            cursor_local2.close()
            conn_local2.close()

            status=1                
            while status==1:

                a=0
                d=str(datetime.today())
                z = d.split(" ")
                da = z[0]
                date = da.split("-")
                jahr = date[0]
                monat = date[1]
                tag = date[2]
                datum=jahr+monat+tag
                ti = z[1]
                time_ = ti.split(":")
                hh = time_[0]
                mm = time_[1]
                ss = time_[2]
                ss = int (float(ss))
                if ss<10:
                    ss = '0'+ str(ss)
                    zeit =hh+mm+ss
                else:
                    zeit = hh + mm + str(ss)
                name = 'D:/Neuer Ordner (2)/data/PPython' + 'dxl' + datum + zeit + '.txt'
                #filename = name
                print(name)
                datei = open(name, "w")
                dxl_status_file="dxl_status.txt"
                dxl_status=open(dxl_status_file,"w")
                dxl_status.write('1')
                dxl_status.close()
                status=1
                print("SETTING TO 1")
                while status==1:
                    #ser.write(b"%R1Q,2107:0\r\n")
                    #ser.write(b"%R1Q,2003:0\r\n")
                    print("HERE")
                    if ser.isOpen() != True:
                        dxl_status_file="dxl_status.txt"
                        dxl_status=open(dxl_status_file,"w")
                        dxl_status.write('0')
                        dxl_status.close()
                        status=0
                        ser.close()
                        print('STOPPING DXL serial is not open')
                        return JsonResponse({"data":False},safe=True) 
                    ser.write(b"g\r\n")
                    print("READING SENSOR VALUE")
                    line = ser.readline(24)   # lese eine Zeile aus dem seriellen Port 24
                    zeile = str(line)
                    valuex=zeile[4:8]
                    valuey=zeile[9:14]
                    print (zeile)
                    print(valuex)
                    print(valuey)
                    t = time.time ()
                    datei.write('%10.2f'%t+' '+valuex+''+valuey+'\n')#write to a file 9,20
                    print('%1.3f'%t)
                    #time.sleep(1)
                    a += 1
                    sql2 = "INSERT INTO dxl(x,y) VALUES (%s,%s)" %(valuex,valuey)
                    sql3 = "INSERT INTO dxl_realtime(x,y) VALUES (%s,%s)" %(valuex,valuey)
                    cursor_local.execute(sql2)
                    cursor_local3.execute(sql3)
                    if isInternet:        
                        cursor_remote.execute(sql2)
                    conn_local.commit()
                    conn_local3.commit()
                    if isInternet:
                        conn_remote.commit()
                    print("record inserted in dxl table.")
                    dxl_status_read=open(dxl_status_file,"r")
                    status=int(dxl_status_read.read())
                    dxl_status_read.close()
                
                    if status==0:
                        cursor_local.close()
                        cursor_local3.close()
                        if isInternet:
                            cursor_remote.close()
                        conn_local.close()
                        conn_local3.close()
                        if isInternet:
                            conn_remote.close()
                        datei.close()
                        ser.close()
                        return JsonResponse({"data":"dxl task completed"},safe=False) 
                
                datei.close()
    except Exception as e:
        print(e)
        dxl_status_file="dxl_status.txt"
        dxl_status=open(dxl_status_file,"w")
        dxl_status.write('0')
        dxl_status.close()
        status=0
        #ser.close()
        print('STOPPING DXL serial is not open')
        print(str(e))
        return JsonResponse({"data":False},safe=True) 

    cursor_local.close()
    cursor_local3.close()
    if isInternet:
        cursor_remote.close()
    conn_local.close()
    conn_local3.close()
    if isInternet:
        conn_remote.close()
    ser.close()
    return JsonResponse({"data": "dxl task complete"},safe=False)

    



def stopDXL(request):
    dxl_status_file="dxl_status.txt"
    dxl_status=open(dxl_status_file,"w")
    dxl_status.write('0')
    dxl_status.close()
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="DELETE FROM dxl_realtime"
    cursor_local.execute(sql)
    conn_local.commit()
    cursor_local.close()
    conn_local.close()    
    print("STOPPING DXL")
    return JsonResponse({"data": True},safe=False)    


def runSYLVAC(request,sensor,com_port,baudrate,bytesize,parity,isInternet):
    port=com_port
    request.COOKIES["sylvac"]=True
    globals.request.COOKIES["sylvac"]=True
    conn_remote= None
    cursor_remote=None
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local2=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local3=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    if isInternet:
        conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_local=conn_local.cursor()
    cursor_local2=conn_local2.cursor()
    cursor_local3=conn_local3.cursor()
    if isInternet:
        cursor_remote=conn_remote.cursor()
    try:
        if sensor=='SYLVAC':
            ser = serial.Serial(port=com_port,
                            baudrate=int(baudrate),
                            bytesize=getByteSize(int(bytesize)),
                            parity=getParity(int(parity)),
                            timeout=200)
            print ("Serial port is open")
            if ser.isOpen() == True:
                filename = ''
                # bestimmen der Laenge einer Datei und die Anzahl der Dateien
                # Diese geben die Laenge der Messung vor
                a = 0
                n = 3
                nn = 1
                #conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
                #cursor_local=conn_local.cursor()
                sql="DELETE FROM sensordata_realtime"
                cursor_local2.execute(sql)
                conn_local2.commit()
                cursor_local2.close()
                conn_local2.close()
                #conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
                #cursor_local=conn_local.cursor()
                #cursor_local2=conn_local.cursor()   
                status=1         
                while status==1:
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
                    sylvac_status_file="sylvac_status.txt"
                    print(name)
                    datei = open(name, "w")
                    sylvac_status=open(sylvac_status_file,"w")
                    sylvac_status.write('1')
                    sylvac_status.close()
                    print(n)
                    print(a)
                    #infinite loop
                    sylvac_status_read=open(sylvac_status_file,"r")
                    status=int(sylvac_status_read.read())
                    sylvac_status_read.close()
                    while status==1:
                        print('COOKIES')
                        #print(request.COOKIES['sylvac'])
                        #print(globals.request.COOKIES['sylvac'])
                        if ser.isOpen()!=True:
                            sylvac_status_file="sylvac_status.txt"
                            sylvac_status=open(sylvac_status_file,"w")
                            sylvac_status.write('0')
                            sylvac_status.close()
                            status=0
                            print('STOPPING DXL serial is not open')
                            return JsonResponse({"data":False},safe=True) 
                        #ser.write(b"%R1Q,2107:0\r\n")
                        #ser.write(b"%R1Q,2003:0\r\n")
                        ser.write(b"?\r")
                        line = ser.read(9)  # lese eine Zeile aus dem seriellen Port
                        print(line)
                        print(line.decode("utf-8"))
                        print('----')
                        zeile = str(line)

                        t = time.time()
                        print('%10.4f' % t)
                        #datei.write('%10.4f' %(str(datetime.now())) + ' ' + zeile[2:10] + '\n')  # schreiben in eine Datei
                        datei.write('%s' %(str(datetime.now())) + ' ' + zeile[2:10] + '\n')  # schreiben in eine Datei
                        time.sleep(2)
                        a += 1
                        print(zeile[2:10])
                        sql2 = "INSERT INTO sensordata (value) VALUES (%s)" %(zeile[2:10])
                        sql3 = "INSERT INTO sensordata_realtime (value) VALUES (%s)" %(zeile[2:10])
                        cursor_local.execute(sql2)
                        cursor_local3.execute(sql3)
                        if isInternet:        
                            cursor_remote.execute(sql2)
                        conn_local.commit()
                        conn_local3.commit()
                        if isInternet:
                            conn_remote.commit()
                        print("record inserted in sensordata table.")
                        sylvac_status_read=open(sylvac_status_file,"r")
                        status=int(sylvac_status_read.read())
                        sylvac_status_read.close()
                        if status==0:
                            cursor_local.close()
                            cursor_local2.close()
                            cursor_local3.close()
                            if isInternet:
                                cursor_remote.close()
                            conn_local.close()
                            conn_local2.close()
                            conn_local3.close()
                            if isInternet:
                                conn_remote.close()
                            datei.close()
                            return JsonResponse({"data":"sylvac task completed"},safe=False)  
                    print("SYLVAC COMPLETED TASK")
                datei.close()
            else:
                sylvac_status_file="sylvac_status.txt"
                sylvac_status=open(sylvac_status_file,"w")
                sylvac_status.write('0')
                sylvac_status.close()
                status=0
                print('STOPPING SYLVAC serial is not open')
                return JsonResponse({"error":True,"data":False},safe=True)
    except:
            sylvac_status_file="sylvac_status.txt"
            sylvac_status=open(sylvac_status_file,"w")
            sylvac_status.write('0')
            sylvac_status.close()
            status=0
            print('STOPPING SYLVAC serial is not open')
            return JsonResponse({"error":True,"data":False},safe=True)
                
    cursor_local.close()
    cursor_local2.close()
    cursor_local3.close()
    if isInternet:
        cursor_remote.close()
    conn_local.close()
    conn_local2.close()
    conn_local3.close()
    if isInternet:
        conn_remote.close()
    return JsonResponse({"data": "sylvac task complete"},safe=False)


def stopSYLVAC(request):
    sylvac_status_file="sylvac_status.txt"
    sylvac_status=open(sylvac_status_file,"w")
    sylvac_status.write('0')
    sylvac_status.close()
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="DELETE FROM sensordata_realtime"
    cursor_local.execute(sql)
    conn_local.commit()
    cursor_local.close()
    conn_local.close()
    print("STOPPING SYLVAC")
    return JsonResponse({"data": True},safe=False)


def runDISTO(requet,sensor,com_port,baudrate,bytesize,parity,isInternet):
    port=com_port
    conn_remote=None
    cursor_remote=None
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local2=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local3=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    if isInternet:
        conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_local=conn_local.cursor()
    cursor_local2=conn_local2.cursor()
    cursor_local3=conn_local3.cursor()
    if isInternet:
        cursor_remote=conn_remote.cursor()
    ser = serial.Serial(port=com_port,
                        baudrate=int(baudrate),
                        bytesize=getByteSize(int(bytesize)),
                        parity=getParity(int(parity)),
                        timeout=200)
    try:                    
        if sensor=="DISTO":
            if ser.isOpen() == True:

                filename = ''
                a = 0
                i = 0

                n = 5
                nn = 1
                sql="DELETE FROM disto_realtime"
                cursor_local2.execute(sql)
                conn_local2.commit()
                cursor_local2.close()
                conn_local2.close()
                status=1
                while status==1:
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
                    #print(n)
                    #print(a)
                    disto_status_file="disto_status.txt"
                    disto_status=open(disto_status_file,"w")
                    disto_status.write('1')
                    disto_status.close()
                    status=1    
                    while status==1:
                        if ser.isOpen()!=True:
                            disto_status_file="disto_status.txt"
                            disto_status=open(disto_status_file,"w")
                            disto_status.write('0')
                            disto_status.close()
                            status=0
                            #print('STOPPING DXL serial is not open')
                            return JsonResponse({"data":False},safe=True) 
                        ser.write(b"g\r\n")
                        line = ser.readline(40)  # lese eine Zeile aus dem seriellen Port
                        zeile = str(line)
                        t = time.time()
                        print('%10.3f' % t)
                        datei.write('%10.3f' % t + ' ' + zeile[9:15] + '\n')  # schreiben in eine Datei
                        time.sleep(2)
                        a += 1
                        #sql = "INSERT INTO disto (date, value) VALUES (%s, %s)"
                        print("-------DISTO VALUE------")
                        print(zeile[9:17])
                        sql2 ="INSERT INTO disto(value) VALUES(%s)" %(zeile[9:17])
                        sql3="INSERT INTO disto_realtime(value) VALUES(%s)" %(zeile[9:17])
                        #val = ('%10.3f'% t, zeile[9:17])
                        #cur.execute(sql, val)
                        #conn.commit()
                        cursor_local.execute(sql2)
                        cursor_local3.execute(sql3)
                        if isInternet:        
                            cursor_remote.execute(sql2)
                        conn_local.commit()
                        conn_local3.commit()
                        if isInternet:
                            conn_remote.commit()

                        print("record inserted in disto table.")
                        disto_status_read=open(disto_status_file,"r")
                        status=int(disto_status_read.read())
                        disto_status_read.close()
                        if status==0:
                            cursor_local.close()
                            cursor_local3.close()
                            if isInternet:
                                cursor_remote.close()
                            conn_local.close()
                            conn_local3.close()
                            if isInternet:
                                conn_remote.close()
                            datei.close()
                            return JsonResponse({"data":"disto task completed"},safe=False)  
                    print('STOPPING DISTO')
                    datei.close()
            else:
                disto_status_file="disto_status.txt"
                disto_status=open(disto_status_file,"w")
                disto_status.write('0')
                disto_status.close()
                status=0
                #print('STOPPING DXL serial is not open')
                return JsonResponse({"data":False},safe=True) 
            cursor_local.close()
            cursor_local3.close()
            if isInternet:
                cursor_remote.close()
            conn_local.close()
            conn_local3.close()
            if isInternet:
                conn_remote.close()
            return JsonResponse({"data":"disto task completed"},safe=False)
    except:
        disto_status_file="disto_status.txt"
        disto_status=open(disto_status_file,"w")
        disto_status.write('0')
        disto_status.close()
        status=0
        #print('STOPPING DXL serial is not open')
        return JsonResponse({"data":False},safe=True) 


def stopDISTO(request):
    disto_status_file="disto_status.txt"
    disto_status=open(disto_status_file,"w")
    disto_status.write('0')
    disto_status.close()
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="DELETE FROM disto_realtime"
    cursor_local.execute(sql)
    conn_local.commit()
    cursor_local.close()
    conn_local.close()    
    print("STOPPING DISTO")
    return JsonResponse({"data": True},safe=False)

def runGPSNN(request,sensor,com_port,baudrate,bytesize,parity,isInternet):
    port=com_port
    conn_remote=None
    cursor_remote=None
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local2=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_local3=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    conn_remote=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    cursor_local=conn_local.cursor()
    cursor_local2=conn_local2.cursor()
    cursor_local3=conn_local3.cursor()
    cursor_remote=conn_remote.cursor()
    ser = serial.Serial(port=com_port,
                        baudrate=int(baudrate),
                        bytesize=getByteSize(int(bytesize)),
                        parity=getParity(int(parity)),
                        timeout=200)
    
    try:

        if sensor=='GPSNN':
            a = 0
            i = 0
            # m = float (input('Laenge einer Datei in Minuten:'))
            # n = int (input('Anzahl der Dateien: '))
            # p = m*60

            n = 200
            nn = 1
            sql="DELETE FROM gpsnn_realtime"
            cursor_local2.execute(sql)
            conn_local2.commit()
            cursor_local2.close()
            conn_local2.close()
            status=1
            while status==1:
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
                gpsnn_status_file="gpsnn_status.txt"
                gpsnn_status=open(gpsnn_status_file,"w")
                gpsnn_status.write('1')
                gpsnn_status.close()
                status=1
                while status==1:

                    # ser.write(b"%R1Q,2107:0\r\n")
                    # ser.write(b"%R1Q,2003:0\r\n")
                    # ser.write(b"?\r")
                    if ser.isOpen()!=True:
                        gpsnn_status_file="gpsnn_status.txt"
                        gpsnn_status=open(gpsnn_status_file,"w")
                        gpsnn_status.write('0')
                        gpsnn_status.close()
                        status=0
                        #print('STOPPING DXL serial is not open')
                        return JsonResponse({"data":False},safe=True)

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

                        
                        sql = "INSERT INTO gpsnn (date, wide, lenght, GPStime) VALUES (%s, %s, %s, %s)"
                        sql2 = "INSERT INTO gpsnn(wide,lenght,GPStime) VALUES(%s,%s,%s)" %(result[0],result[2],result[4])
                        sql3 = "INSERT INTO gpsnn_realtime(wide,lenght,GPStime) VALUES(%s,%s,%s)" %(result[0],result[2],result[4])
                        val = ('%10.4f' % t, result[0], result[2], result[4])
                        cursor_local.execute(sql2)
                        cursor_local3.execute(sql3)
                        if isInternet:        
                            cursor_remote.execute(sql2)
                        conn_local.commit()
                        conn_local3.commit()
                        if isInternet:
                            conn_remote.commit()

                        print("record inserted in disto table.")
                        gpsnn_status_read=open(gpsnn_status_file,"r")
                        status=int(gpsnn_status_read.read())
                        gpsnn_status_read.close()
                        if status==0:
                            cursor_local.close()
                            cursor_local3.close()
                            if isInternet:
                                cursor_remote.close()
                            conn_local.close()
                            conn_local3.close()
                            if isInternet:
                                conn_remote.close()
                            datei.close()
                            return JsonResponse({"data":"gpsnn task completed"},safe=False)                

                print('STOPPING GPSNN')
                datei.close()
            cursor_local.close()
            cursor_local3.close()
            if isInternet:
                cursor_remote.close()
            conn_local.close()
            conn_local3.close()
            if isInternet:
                conn_remote.close()
            return JsonResponse({"data":"gpsnn task completed"},safe=False)
    except:
        gpsnn_status_file="gpsnn_status.txt"
        gpsnn_status=open(gpsnn_status_file,"w")
        gpsnn_status.write('0')
        gpsnn_status.close()
        status=0
        #print('STOPPING DXL serial is not open')
        return JsonResponse({"data":False},safe=True)

    

def stopGPSNN(request):
    gpsnn_status_file="gpsnn_status.txt"
    gpsnn_status=open(gpsnn_status_file,"w")
    gpsnn_status.write('0')
    gpsnn_status.close()
    conn_local=psycopg2.connect(user="postgres",password="postgres",host="localhost",port="5432",database="sensors")
    cursor_local=conn_local.cursor()
    sql="DELETE FROM gpsnn_realtime"
    cursor_local.execute(sql)
    conn_local.commit()
    cursor_local.close()
    conn_local.close()    
    print("STOPPING GPSNN")
    return JsonResponse({"data": True},safe=False)


def deconnect(request):
    sensor=request.POST['sensor']
    if sensor=='SYLVAC':
        print('STOP SYLVAC')
        stopSYLVAC(request)
    elif sensor=='DISTO':
        print('STOP DISTO')
        stopDISTO(request)
    elif sensor=='GPSNN':
        print('STOP GPSNN')
        stopGPSNN(request)
    elif sensor=='DXL':
        print('STOP DXL')
        stopDXL(request)

async def AsyncResponse(request,sensor):
    time.sleep(5)
    return JsonResponse({"sensor_id":sensor},safe=False)

def runComPort(request):
    print(request.POST)
    com_port=request.POST['com_port']
    sensor=request.POST['sensor']
    baudrate=request.POST['baudrate']
    parity=request.POST['parity']
    bytesize=request.POST['bytesize']
    isInternet=int(request.POST['isInternet'])
    port=com_port
    if sensor=='DXL':
        print('running DXL')
        runDXL(request,sensor,com_port,baudrate,bytesize,parity,isInternet)
    if sensor=='SYLVAC':
        print('running SYLVAC')
        runSYLVAC(request,sensor,com_port,baudrate,bytesize,parity,isInternet)
    elif sensor=='DISTO':
        print('running DISTO')
        runDISTO(request,sensor,com_port,baudrate,bytesize,parity,isInternet)
    elif sensor=='GPSNN':
        print('running GPSNN')
        runGPSNN(request,sensor,com_port,baudrate,bytesize,parity,isInternet)

    
    
    # if com_port=='COM4':
    #     ser = serial.Serial(port='COM4',
    #                     baudrate=4800,
    #                     bytesize=serial.SEVENBITS,
    #                     parity=serial.PARITY_EVEN,
    #                     timeout=200)
    #     print ("Serial port is open")
    #     if ser.isOpen() == True:

    #         filename = ''
    #         # bestimmen der Laenge einer Datei und die Anzahl der Dateien
    #         # Diese geben die Laenge der Messung vor
    #         a = 0
    #         i = 0
    #         # m = float (input('Laenge einer Datei in Minuten:'))
    #         # n = int (input('Anzahl der Dateien: '))
    #         # p = m*60

    #         n = 3
    #         nn = 1

    #         while a < nn:
    #             a = 0
    #             d = str(datetime.today())
    #             z = d.split(" ")
    #             da = z[0]
    #             date = da.split("-")
    #             jahr = date[0]
    #             monat = date[1]
    #             tag = date[2]
    #             datum = jahr + monat + tag
    #             ti = z[1]
    #             time_ = ti.split(":")
    #             hh = time_[0]
    #             mm = time_[1]
    #             ss = time_[2]
    #             ss = int(float(ss))
    #             if ss < 10:
    #                 ss = '0' + str(ss)
    #                 zeit = hh + mm + ss
    #             else:
    #                 zeit = hh + mm + str(ss)
    #             name = 'D:/Neuer Ordner (2)/data/PPython' + 'sylvac' + datum + zeit + '.txt'
    #             filename = name
    #             print(name)
    #             datei = open(name, "w")

    #             print(n)
    #             print(a)

    #             #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',                   db='sensor')  # connection with db
    #             connection=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    #             cursor=connection.cursor()
    #             #connection2=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    #             #cursor2=connection2.cursor()

    #             conn=connection
    #             #cur = conn.cursor()

    #             if conn:
    #                 print(" Connect!")
    #                 print("=========" + port + "=========")
    #                 #sql_com_port = "INSERT INTO com_port(com,status,table_name) VALUES ('COM4',1,'sensordata')"
    #                 #cursor.execute(sql2)
    #                 #connection2.commit()

    #             else:
    #                 print("Not Connect!")

    #             while a < n:

    #                 # ser.write(b"%R1Q,2107:0\r\n")
    #                 # ser.write(b"%R1Q,2003:0\r\n")
    #                 ser.write(b"?\r")

    #                 line = ser.read(9)  # lese eine Zeile aus dem seriellen Port
    #                 zeile = str(line)

    #                 if conn:  # if the connection was successful insert the data to table

    #                     if port == 'COM4':
    #                         t = time.time()
    #                         print('%10.4f' % t)

    #                         datei.write('%10.4f' % t + ' ' + zeile[2:10] + '\n')  # schreiben in eine Datei
    #                         time.sleep(2)
    #                         a += 1

    #                         com_port='COM4'
    #                         status=1;
    #                         table_name='sensordata';
    #                         sql = "INSERT INTO sensordata (date, value) VALUES (%s, %s)"
    #                         sql2 = "INSERT INTO sensordata (value) VALUES (%s)" %(zeile[2:10])

    #                         val = ('%10.4f' % t, zeile[2:10])
    #                         #cur.execute(sql, val)
    #                         cursor.execute(sql2)        
    #                         connection.commit()
    #                         #conn.commit()

    #                         print("record inserted in sensordata table.")

    #             datei.close()

    #     #cur.close()
    #     #conn.close()
    #     cursor.close()
    #     connection.close()
    #     #cursor2.close()
    #     #connection2.close()

    #     return JsonResponse({"sensor_id":3},safe=False)  
    
    # elif com_port=='COM3':
    #     ser = serial.Serial(port='COM3',
    #                     baudrate=9600,
    #                     bytesize=serial.EIGHTBITS,
    #                     parity=serial.PARITY_NONE,
    #                     timeout=200)
    #     if ser.isOpen() == True:

    #         filename = ''
    #         # bestimmen der Laenge einer Datei und die Anzahl der Dateien
    #         # Diese geben die Laenge der Messung vor
    #         a = 0
    #         i = 0
    #         # m = float (input('Laenge einer Datei in Minuten:'))
    #         # n = int (input('Anzahl der Dateien: '))
    #         # p = m*60

    #         n = 5
    #         nn = 1

    #         while a < nn:
    #             a = 0
    #             d = str(datetime.today())
    #             z = d.split(" ")
    #             da = z[0]
    #             date = da.split("-")
    #             jahr = date[0]
    #             monat = date[1]
    #             tag = date[2]
    #             datum = jahr + monat + tag
    #             ti = z[1]
    #             time_ = ti.split(":")
    #             hh = time_[0]
    #             mm = time_[1]
    #             ss = time_[2]
    #             ss = int(float(ss))
    #             if ss < 10:
    #                 ss = '0' + str(ss)
    #                 zeit = hh + mm + ss
    #             else:
    #                 zeit = hh + mm + str(ss)
    #             name = 'D:/Neuer Ordner (2)/data/PPython' + 'disto' + datum + zeit + '.txt'
    #             filename = name
    #             print(name)
    #             datei = open(name, "w")

    #             print(n)
    #             print(a)

    #             #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',
    #             #                    db='sensor')  # connection with db
    #             #cur = conn.cursor()
    #             connection=psycopg2.connect(user="dssbcuwcqanxot",password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com",port="5432",database="d4sboi6172opf9")
    #             cursor=connection.cursor()
    #             conn=connection
    #             if conn:
    #                 print(" Connect!")
    #                 print("=========" + port + "=========")
    #             else:
    #                 print("Not Connect!")

    #             while a < n:

    #                 # ser.write(b"%R1Q,2107:0\r\n")
    #                 # ser.write(b"%R1Q,2003:0\r\n")
    #                 ser.write(b"g\r\n")

    #                 line = ser.readline(40)  # lese eine Zeile aus dem seriellen Port
    #                 zeile = str(line)

    #                 if conn:  # if the connection was successful insert the data to table

    #                     if port == 'COM3':
    #                         t = time.time()
    #                         print('%10.3f' % t)

    #                         datei.write('%10.3f' % t + ' ' + zeile[9:15] + '\n')  # schreiben in eine Datei
    #                         time.sleep(2)
    #                         a += 1


    #                         sql = "INSERT INTO disto (date, value) VALUES (%s, %s)"
    #                         print(zeile[9:17])
    #                         sql2 ="INSERT INTO disto(value) VALUES(%s)" %(zeile[9:17])
    #                         val = ('%10.3f'% t, zeile[9:17])
    #                         #cur.execute(sql, val)
    #                         #conn.commit()
    #                         cursor.execute(sql2)
    #                         connection.commit()

    #                         print("record inserted in disto table.")

    #             datei.close()

    #     #cur.close()
    #     #conn.close()
    #     cursor.close()
    #     connection.close()
    #     return JsonResponse({"sensor_id":1},safe=False)  
    
    # elif com_port=='COM10':
    #     ser = serial.Serial(port='COM10',
    #                     baudrate=115200,
    #                     bytesize=serial.EIGHTBITS,
    #                     parity=serial.PARITY_NONE,
    #                     timeout=200)
    #     a = 0
    #     i = 0
    #     # m = float (input('Laenge einer Datei in Minuten:'))
    #     # n = int (input('Anzahl der Dateien: '))
    #     # p = m*60

    #     n = 200
    #     nn = 1

    #     #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='',db='sensor')  # connection with db
    #     #cur = conn.cursor()
    #     connection = psycopg2.connect(user="dssbcuwcqanxot",
    #                                 password="47e67cdfdb55aed7e79847bf4b7811c640c5835a49f80e102ea9434b7669e95e",
    #                                 host="ec2-54-246-89-234.eu-west-1.compute.amazonaws.com", port="5432",
    #                                 database="d4sboi6172opf9")
    #     cursor = connection.cursor()
    #     conn=connection

    #     if conn:
    #         print(" Connect!")
    #         print("=========" + port + "=========")
    #     else:
    #         print("Not Connect!")


    #     while a < nn:
    #         a = 0
    #         d = str(datetime.today())
    #         z = d.split(" ")
    #         da = z[0]
    #         date = da.split("-")
    #         jahr = date[0]
    #         monat = date[1]
    #         tag = date[2]
    #         datum = jahr + monat + tag
    #         ti = z[1]
    #         time_ = ti.split(":")
    #         hh = time_[0]
    #         mm = time_[1]
    #         ss = time_[2]
    #         ss = int(float(ss))
    #         if ss < 10:
    #             ss = '0' + str(ss)
    #             zeit = hh + mm + ss
    #         else:
    #             zeit = hh + mm + str(ss)
    #         name = 'D:/Neuer Ordner (2)/data/PPython' + 'gnss' + datum + zeit + '.txt'
    #         print(name)
    #         datei = open(name, "w")

    #         print(n)
    #         print(a)

    #         while a < n:

    #             # ser.write(b"%R1Q,2107:0\r\n")
    #             # ser.write(b"%R1Q,2003:0\r\n")
    #             # ser.write(b"?\r")

    #             line = ser.readline()  # lese eine Zeile aus dem seriellen Port
    #             # print (line)
    #             zeile = str(line)
    #             # print (zeile[3:8])
    #             if zeile[3:8] == "GNGLL":
    #                 t = time.time()

    #                 print('############')
    #                 print('%10.4f' % t)
    #                 print(zeile[9:45])

    #                 datei.write('%10.4f' % t + ' ' + zeile[9:45] + '\n')  # schreiben in eine Datei

    #                 my_string = zeile[9:45]
    #                 result = [x.strip() for x in my_string.split(',')]

    #                 if conn:
    #                     sql = "INSERT INTO gpsnn (date, wide, lenght, GPStime) VALUES (%s, %s, %s, %s)"
    #                     sql2 = "INSERT INTO gpsnn(wide,lenght,GPStime) VALUES(%s,%s,%s)" %(result[0],result[2],result[4])
    #                     val = ('%10.4f' % t, result[0], result[2], result[4])
    #                     #cur.execute(sql, val)
    #                     #conn.commit()
    #                     cursor.execute(sql2)
    #                     connection.commit()

    #                     print("record inserted in gpsnn table.")


    #             time.sleep(0)
    #             a += 1
    #         datei.close()
    #     #cur.close()
    #     #conn.close()
    #     cursor.close()
    #     connection.close()
    #     return JsonResponse({"sensor_id":2},safe=False)  

def dashboard(request):
    request.COOKIES['sylvac']=False
    globals.request.COOKIES['sylvac']=False
    return render(request,"dashboard.html",{})


