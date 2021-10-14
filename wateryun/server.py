#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import time, datetime
import pymysql
import struct
import ctypes
import func_timeout
from func_timeout import func_set_timeout

'''日志记录'''
import traceback



# 进制转换
def hex_to_float(h):
    i = int(h,16)
    return struct.unpack('<f',struct.pack('<I', i))[0]
def hex2float(h):
    i = int(h,16)
    cp = ctypes.pointer(ctypes.c_int(i))
    fp = ctypes.cast(cp,ctypes.POINTER(ctypes.c_float))
    return fp.contents.value

def connect_mysql():
    #连接数据库
    conn=pymysql.connect(host = 'localhost' 
    ,user = 'root' # 用户名
    ,passwd='Wb,123456' # 密码
    ,port= 3306 # 端口，默认为3306
    ,db='Database_undergroundwater' # 数据库名称
    ,charset='utf8' # 字符编码
    )

    cur = conn.cursor() # 生成游标对象
    return cur,conn

# 命令
sensorDepthReadCmd = bytes.fromhex('02 03 00 01 08 01 D2 39')  # Sensor read depth
sensorConductivityReadCmd = bytes.fromhex('01 03 00 00 00 02 C4 0B')  # Sensor instruction,read conductivity.
sensorResistivityReadCmd = bytes.fromhex('01 03 00 02 00 02 65 CB')  # Sensor instruction, read resistivity.
sensorTemperatureReadCmd = bytes.fromhex('01 03 00 04 00 02 85 CA')  # Sensor instruction, read temperature.
sensorTDSReadCmd = bytes.fromhex('01 03 00 06 00 02 24 0A')  # Sensor instruction, read TDS.
sensorSalinityReadCmd = bytes.fromhex('01 03 00 08 00 02 45 C9')  # Sensor instruction, read salinity.

commends = {"水位":sensorDepthReadCmd,"电导率":sensorConductivityReadCmd,"电阻率":sensorResistivityReadCmd,"温度":sensorTemperatureReadCmd,"TDS":sensorTDSReadCmd,"盐度":sensorSalinityReadCmd}

class ServerSocket(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(2)
        

    def accept(self):
        conn,addr = self.s.accept()
        return conn,addr
    # 接收数据
    def recv_data(self,conn):
        buffer=[conn.recv(1024)]    #一开始的部分,用于等待传输开始,避免接收不到的情况.
        if buffer[0] in (0,-1):    #返回0,-1代表出错
            return False
        conn.setblocking(0)    #非阻塞模式
        while True:    
            try:
                data = conn.recv(1024)    #接收1024字节
                buffer.append(data)    #拼接到结果中
            except BlockingIOError as e:    #如果没有数据了
                break    #退出循环
        conn.setblocking(1)    #恢复阻塞模式
        return b"".join(buffer)#.decode("utf-8")

    # 发送数据
    def send_data(self, para,conn):
        return conn.sendall(para)

    # 关闭连接
    def close_conn(self):
        return self.s.close()

@func_set_timeout(10) # 设定超时时间
def get_value(server,conn):
    rectime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return_list = []
    return_list.append(rectime)
    for index in commends.keys():
        print("采集{}".format(index))
        server.send_data(commends[index],conn)
        water_Bytes = server.recv_data(conn)
        if water_Bytes == False:
            print("接收出错")
            return -1
        water_hex = water_Bytes.hex()
        return_list.append(water_hex)
    return return_list



def main():
    link_server = ServerSocket('0.0.0.0', 2133)
    # tcp_conn,tcp_addr = link_server.accept()
    while True:
        print("<+++++++++++++++++++++++++++++++++++>")
        tcp_conn,tcp_addr = link_server.accept()
        print("连接成功")
        mysql_cur,mysql_conn = connect_mysql()
        #当前时间
        rectime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # rectime = datetime.datetime.strptime(rectime, "%Y-%m-%d %H:%M:%S")
        print("<===================================>")
        try:
            data_list = get_value(link_server,tcp_conn)
            if(data_list == -1):
                print("连接断开")
                tcp_conn.close()
                print("重连")
                tcp_conn,tcp_addr = link_server.accept()
                continue
        except func_timeout.exceptions.FunctionTimedOut as e1:
            with open('logs/server_log.log',"a") as f:
                traceback.print_exc(file = f)
            print("超时")
            tcp_conn.shutdown(2)
            tcp_conn.close()
            print("连接已断开，准备重连")
            print("重连")
            continue
        except Exception as e:
            print("未知错误")
            with open('logs/server_log.log',"a") as f:
                traceback.print_exc(file = f)
                tcp_conn.shutdown(2)
                tcp_conn.close()
                print("连接已断开，准备重连")
                print("重连")
            continue
        mysql_list = []
        mysql_list.append(data_list[0])#时间
        print("当前时间：",mysql_list[0])
        mysql_list.append(int(str(data_list[1][6:10]),16)/100)#水位
        print("水位：",mysql_list[1])
        mysql_list.append(round(hex2float(data_list[2][6:14]),3)*1000)#电导率
        print("电导率：",mysql_list[2])
        mysql_list.append(round(hex2float(data_list[3][6:14]),3))#电阻率
        print("电阻率：",mysql_list[3])
        mysql_list.append(round(hex2float(data_list[4][6:14]),1))#温度
        print("温度：",mysql_list[4])
        mysql_list.append(round(hex2float(data_list[5][6:14]),3))#TDS
        print("TDS：",mysql_list[5])
        mysql_list.append(round(hex2float(data_list[6][6:14]),3))#盐度
        print("盐度：",mysql_list[6])
        device_id=str(tcp_addr[0])
        depth,conduct,resistivity,temperature,tds,salinity,rectime = mysql_list[1],mysql_list[2],mysql_list[3],mysql_list[4],mysql_list[5],mysql_list[6],mysql_list[0]
        sql = "insert into Table_water(deviceID,depth,conduct,resistivity,temperature,tds,salinity,date_time) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (device_id,depth,conduct,resistivity,temperature,tds,salinity,rectime)
        mysql_cur.execute(sql,values)
        mysql_conn.commit()
        print("数据传入成功")
        mysql_cur.close()
        mysql_conn.close()
        tcp_conn.close()
        print("<===================================>")
        time.sleep(2)
    
    link_server.close_conn()
    


if __name__ == '__main__':
    main()
