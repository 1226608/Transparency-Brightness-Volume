import tkinter as tk
import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
# 创建一个窗口并指定窗口的大小

class VolumeControlApp:
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
        self.volume = self.interface.QueryInterface(IAudioEndpointVolume)
        self.window = tk.Tk()
        self.window.configure(bg="#E8E8E8")
        self.window.title("标题")
        self.window.attributes('-alpha',1)
        屏幕宽度=self.window.winfo_screenwidth()
        屏幕高度=self.window.winfo_screenheight()
        窗口宽度=600;窗口高度=600
        x = (屏幕宽度 // 2) - (窗口宽度 // 2)
        y = (屏幕高度 // 2) - (窗口高度 // 2)
        self.window.geometry('{}x{}+{}+{}'.format(窗口宽度, 窗口高度, x, y))
        self.window.attributes("-toolwindow", 1)
        # 创建一个按钮并指定位置
        self.button = tk.Button(self.window,bg="#E8E8E8",fg="#1E1E1E",text="日",anchor="center",font=("黑体", 15), activebackground="red")
        self.button.place(x=25, y=25,width=50, height=50,anchor="center")

        # 创建一个按钮并指定位置
        self.button1 = tk.Button(self.window,bg="#E8E8E8",fg="#1E1E1E",text="未置顶",anchor="center",font=("黑体", 10), activebackground="red")
        self.button1.place(x=75, y=25,width=50, height=50,anchor="center")
        # 创建一个滑块
                                                                                        #最大值 最小值      横还是竖          长度       宽度   是否显示当前值    刻度数量    最小移动距离       滑块的宽度     是否去除边框 
        self.scale1 = tk.Scale(self.window,font=("黑体",12),troughcolor='#E8E8E8',label="透",from_=100,to=0,orient="vertical",length=400,width=16,showvalue=0,tickinterval=9,resolution=10,sliderlength=50,highlightthickness=0)
        self.scale2 = tk.Scale(self.window,font=("黑体",12),troughcolor='#E8E8E8',label="亮",from_=100,to=0,orient="vertical",length=400,width=16,showvalue=0,tickinterval=9,resolution=10,sliderlength=50,highlightthickness=0)
        self.scale3 = tk.Scale(self.window,font=("黑体",12),troughcolor='#E8E8E8',label="音",from_=100,to=0,orient="vertical",length=400,width=16,showvalue=0,tickinterval=9,resolution=10,sliderlength=50,highlightthickness=0)
        self.scale3.set(int(self.volume.GetMasterVolumeLevelScalar() * 100))
        self.scale3.pack(padx=20, pady=10, fill=tk.X)

        self.mute_var = tk.BooleanVar()
        self.mute_checkbutton = tk.Checkbutton(self.window,font=("黑体",12),text="未静音",variable=self.mute_var,width=100, height=100,)
        self.mute_checkbutton.pack(fill=tk.X)
        
        self.mute_checkbutton.place(x=140,y=480,width=80,height=40)
        self.mute_checkbutton.config(fg='#1E1E1E',bg="#E8E8E8",activebackground="#E8E8E8")
        self.scale1.set(100)#初始值
        初始亮度 = sbc.get_brightness()
        self.scale2.set(初始亮度)#初始值
        self.scale1.place(x=0, y=70)
        self.scale2.place(x=70, y=70)
        self.scale3.place(x=140, y=70)
        self.scale3.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='blue')
        self.scale2.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='red')
        self.scale1.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='orange')

        # 定义滑块事件函数
        def 滑块事件1(opacity):
            # 将滑块组件的值除以100以得到透明度的小数表示
            opacity_fraction = float(opacity) / 100.0
            # 将透明度分数传递给attributes()方法以更新窗口的透明度
            self.window.attributes('-alpha', opacity_fraction)
        # 将滑块事件函数绑定到滑块组件的回调函数中
        self.scale1.config(command=滑块事件1)

        # 定义滑块屏幕亮度事件函数
        def 滑块事件2(opacity):
            sbc.set_brightness(opacity)
        self.scale2.config(command=滑块事件2)

        def 滑块事件3(opacity):
            scaled_value = int(opacity)
            self.volume.SetMasterVolumeLevelScalar(scaled_value / 100, None)
            update_mute_state()
        self.scale3.config(command=滑块事件3)

        def 勾选框被点击():
            self.volume.SetMute(self.mute_var.get(), None)
            if self.mute_var.get() == True:
                self.mute_checkbutton.configure(text="已静音")
            else:
                self.mute_checkbutton.configure(text="未静音")
        self.mute_checkbutton.config(command=勾选框被点击)
        # 定义按钮事件函数
        def 按钮事件():
            if self.window.cget("bg") == "#E8E8E8":
                self.window.configure(bg="#1E1E1E")
                self.button1.configure(bg="#1E1E1E", fg="#E8E8E8")
                self.button.configure(bg="#1E1E1E", fg="#E8E8E8", text="月")
                self.scale3.config(fg='#E8E8E8',troughcolor='#1E1E1E',bg='#1E1E1E',activebackground='blue')
                self.scale2.config(fg='#E8E8E8',troughcolor='#1E1E1E',bg='#1E1E1E',activebackground='red')
                self.scale1.config(fg='#E8E8E8',troughcolor='#1E1E1E',bg='#1E1E1E',activebackground='orange')
                self.mute_checkbutton.config(fg='#E8E8E8',bg="#1E1E1E",activebackground="#1E1E1E")
            else:
                self.window.configure(bg="#E8E8E8")
                self.button.configure(bg="#E8E8E8", fg="#1E1E1E", text="日")
                self.button1.configure(bg="#E8E8E8", fg="#1E1E1E")
                self.scale3.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='blue')
                self.scale2.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='red')
                self.scale1.config(fg='#1E1E1E',troughcolor='#E8E8E8',bg='#E8E8E8',activebackground='orange')
                self.mute_checkbutton.config(fg='#1E1E1E',bg="#E8E8E8",activebackground="#E8E8E8")
        # 将按钮事件函数绑定到按钮组件的回调函数中
        self.button.config(command=按钮事件)
        def 按钮事件1():
            if self.window.attributes('-topmost') ==True:
                self.button1.configure(text="未置顶")
                self.window.attributes('-topmost', False)
            else:
                self.window.attributes('-topmost', True)
                self.button1.configure(text="已置顶")
        # 将按钮事件函数绑定到按钮组件的回调函数中
        self.button1.config(command=按钮事件1)

        def update_mute_state():
            if self.volume.GetMasterVolumeLevelScalar() == 0:
                self.mute_var.set(True)
                self.volume.SetMute(True, None)
                self.mute_checkbutton.configure(text="已静音")
            else:
                self.mute_var.set(False)
                self.volume.SetMute(False, None)
                self.mute_checkbutton.configure(text="未静音")
        # 运行窗口的主循环
        self.window.mainloop()
app = VolumeControlApp()