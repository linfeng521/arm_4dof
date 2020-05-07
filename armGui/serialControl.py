import serial
from mapFunction import actually,grip
try:
    ser = serial.Serial('com3', 9600, timeout=1)
except Exception as e:
    print(e)

def send_data(value):
    try:
        object = value.split(',')
        # 除去手抓位置
        idea_degree_list = object[:-1]
        # print(idea_degree_list)
        actually_degree_list = []
        for index,idea_degree in enumerate(idea_degree_list):
            actually_degree = actually(index,int(idea_degree))
            actually_degree_list.append(actually_degree)
            # print(actually_degree)
        actually_degree_list_str = str(actually_degree_list)[1:-1]
        actually_command = actually_degree_list_str + ',' + str(grip(object[-1]))
        # print('---hello----')
        # print(actually_command)
        ser.write(actually_command.encode('utf-8'))
        response= ser.readall().decode('utf-8')
        # print(response) #0:90;1:0;2:90;3:90;
        # 用于占位id索引
        response_list = [0,0,0,0,0,0]
        for i in response.split(';')[:-1]:
            id,degree = i.split(':')
            response_list[int(id)] = degree
        # print(li) ['90', '0', '90', '90', 0, 0]
        print('理想位置:',object,'实际位置:',response_list)
        return response_list,object

    except Exception as e:
        print(e)
