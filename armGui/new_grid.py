from tkinter import *
import tkinter.font as tkFont
from serialControl import send_data

steady_pos = [90,60,180,0,0,0]

def getValue(event=None):
    value = s1.get(), s2.get(), s3.get(), s4.get(),s5.get()
    text1.delete(0.0, END)
    text1.insert(0.0, 'servo1(腰) will  go to ' + str(value[0]) + ' degree\n')
    text1.insert(INSERT, 'servo2(肩) will  go to ' + str(value[1]) + ' degree\n')
    text1.insert(INSERT, 'serv03(肘) will  go to ' + str(value[2]) + ' degree\n')
    text1.insert(INSERT, 'servo4(腕) will  go to ' + str(value[3]) + ' degree\n')
    text1.insert(INSERT, 'grip(手抓) will  抓取直径: ' + str(value[4]) + ' mm的工件\n')
    return str(value[0])+','+str(value[1])+','+ str(value[2])+','+ str(value[3])+','+ str(value[4])


def setDefault():
    s1.set(steady_pos[0])
    s2.set(steady_pos[1])
    s3.set(steady_pos[2])
    s4.set(steady_pos[3])
    s5.set(steady_pos[4])

def send(event=None):
    response_list, idea_degree_list = send_data(getValue()) #['90', '0', '90', '90', 0, 0]
    text2.delete(0.0, END)
    text2.insert(0.0, 'servo1(腰) had  gone to ' + idea_degree_list[0] + '('+ response_list[0]+ ') degree\n')
    text2.insert(INSERT, 'servo2(肩) had  gone to ' + idea_degree_list[1] + '('+response_list[1] + ') degree\n')
    text2.insert(INSERT, 'serv03(肘) had  gone to ' + idea_degree_list[2] + '('+response_list[2] + ') degree\n')
    text2.insert(INSERT, 'servo4(腕) had  gone to ' + idea_degree_list[3] + '('+response_list[3] + ') degree\n')
    text2.insert(INSERT, 'grip(手抓) had  抓取直径: ' + idea_degree_list[4] + '('+response_list[4] + ') mm的工件\n')
    text2.insert(INSERT,"*****ALL servo has done successfully******")

def sendlist(event=None):
    command_list = text3.get(0.0,END)
    for i in command_list.strip().split('#'):
        if i == None:
            pass
        send_data(i[1:-1])
root = Tk()
# 设置窗口大小
winWidth = 900
winHeight = 700
# 获取屏幕分辨率
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# scale value
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
# 设置主窗口标题
root.title("四自由度机械臂参数说明")
# 设置窗口初始位置在屏幕居中
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
ft = tkFont.Font(size=15, weight=tkFont.BOLD)

s1 = Scale(root, from_=0, to=180, tickinterval=20, resolution=2, length=600, bd=10, fg='#ff4400', troughcolor='red',
           orient=HORIZONTAL, font=ft,variable=value1,command=getValue,width=8,showvalue=0)
l1 = Label(text="Servo1(腰)：(degree)")
e1 = Entry(root,width=5,bd=3,bg='#57faff',textvariable=value1)

l1.grid(row=0, column=0)
s1.grid(row=0, column=1,columnspan=6)
e1.grid(row=0,column=7)

s2 = Scale(root, from_=0, to=180, tickinterval=20, resolution=2, length=600, bd=10, fg='#ff4400', troughcolor='green',
           orient=HORIZONTAL, font=ft,variable=value2,command=getValue,width=8,showvalue=0)
l2 = Label(text="Servo2(肩)：(degree)")
e2 = Entry(root,width=5,bd=3,bg='#57faff',textvariable=value2)
l2.grid(row=1, column=0)
s2.grid(row=1, column=1,columnspan=6)
e2.grid(row=1,column=7)

s3 = Scale(root, from_=0, to=180, tickinterval=20, resolution=2, length=600, bd=10, fg='#ff4400', troughcolor='blue',
           orient=HORIZONTAL, font=ft,variable=value3,command=getValue,width=8,showvalue=0)
l3 = Label(text="Servo3(肘)：(degree)")
e3 = Entry(root,width=5,bd=3,bg='#57faff',textvariable=value3)
l3.grid(row=2, column=0)
s3.grid(row=2, column=1,columnspan=6)
e3.grid(row=2,column=7)

s4 = Scale(root, from_=0, to=180, tickinterval=20, resolution=2, length=600, bd=10, fg='#ff4400', troughcolor='pink',
           orient=HORIZONTAL, font=ft,variable=value4,command=getValue,width=8,showvalue=0)
l4 = Label(text="Servo4(腕)：(degree)")
e4 = Entry(root,width=5,bd=3,bg='#57faff',textvariable=value4)
l4.grid(row=3, column=0)
s4.grid(row=3, column=1,columnspan=6)
e4.grid(row=3,column=7)

s5 = Scale(root, from_=10, to=65, tickinterval=5, resolution=1, length=600, bd=10, fg='#ff4400', troughcolor='#4EEE94',
           orient=HORIZONTAL, font=ft,variable=value5,command=getValue,width=8,showvalue=0)
s5.grid(row=4,column=1,columnspan=6)
l5 = Label(text="手抓目标直径:(mm)")
l5.grid(row=4, column=0)
e5 = Entry(root,width=5,bd=3,bg='#57faff',textvariable=value5)
e5.grid(row=4,column=7)

l5 = Label(text="发送数据")
l5.grid(row=5,column=0)
text1 = Text(root, width=40, height=6)
text1.grid(row=5, column=1, columnspan=2)

l5 = Label(text="收到数据")
l5.grid(row=5,column=3)
text2 = Text(root, width=50, height=6)
text2.grid(row=5, column=4, columnspan=2)

# 绑定回车事件
e1.bind('<Return>', send)
e2.bind('<Return>', send)
e3.bind('<Return>', send)
e4.bind('<Return>', send)

bt1 = Button(root, text='获取位置', command=getValue)
bt1.grid(row=6, column=2)
bt2 = Button(root, text='默认位置', command=setDefault)
bt2.grid(row=6, column=3)
bt3 = Button(root, text='发送位置', command=send)
bt3.grid(row=6, column=4)

# 输入指令序列text
l6 = Label(text="输入指令序列")
l6.grid(row=7,column=0)
text3 = Text(root, width=80, height=10)
text3.grid(row=7,column=1,columnspan=8)
bt4 = Button(root, text='发送指令序列', command=sendlist)
bt4.grid(row=7,column=9)
# 调用默认位置函数

setDefault()
root.mainloop()
