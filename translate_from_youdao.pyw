from fanyi import translate_main as trans_m
from tkinter import *

def keycontral(event):
    if event.keysym=='Return':
        main_login()
def keycontral2(event):
    if event.keysym == 'Return':
        win.destroy()

# 搭建窗口&全局变量
win = Tk()
win.title('有道翻译API')
win.geometry('400x160+1100+150')
#600x200, text_w=42, button_x=260, button_y=170

#窗体初始化
# Label(win, text='输入内容：').place(x=80, y=110)
InputText = Text(win, height=25, width=28)
InputText.pack(side='left')
# InputText.insert(INSERT,"Input content to translate.")

OutputText = Text(win, height=25, width=28)
OutputText.pack(side='right')

def main_login():
    OutputText.delete('1.0','end')
    content = InputText.get('1.0',END)
    # print(content)
    result = trans_m(content)
    OutputText.insert(END,result)


btn_login = Button(win, text='->', width=10, command=main_login)
btn_login.bind_all('<Return>',keycontral)
btn_login.place(x=160, y=130)

win.mainloop()
