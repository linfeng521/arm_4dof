# arm_4dof
四自由度机械臂

### GUI
使用tkinter：
  程序入口在new_grid.py
  
### arduino uno

接受usb输入的数据格式：90,90,90,90,90,90

### 添加trajectory.py轨迹规划
  - matlabS/trajectory
  - matlabS/util 常见的数组round工具包

### 使用python的serial库进行usb通信

### 添加相机标定以及视觉分析模块
 - objectS/first: 基于形状,角点检测,质心位置获取
 - objectS/mogDemo: 背景分割器

 Todo:
    添加树莓派与arduino蓝牙模块串口通讯,取代之前usb连接,将DC12V口专用于供电