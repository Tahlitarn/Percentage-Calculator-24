from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb
from ttkbootstrap.icons import Icon
from PIL import ImageTk, Image

root = ttkb.Window(themename="morph")
root.title("Converter")
#root.iconbitmap('./img_logo.ico')
root.geometry("200x180")


frm = ttkb.Frame(root, bootstyle="cyborg")
frm.pack(pady=2)

label_Title = ttkb.Label(frm, text="PERCENTAGE CALCULATOR", justify="center", font=("elephan", 10, "bold"))
label_Title.grid(row=0, column=0)

txt_num = ttkb.Entry(frm, font=("tahoma", 15, "bold"), justify= "center", width=10)
txt_num.grid(row=1, column=0, pady=5)

c_option = StringVar()
rdb_option= ttkb.Radiobutton(frm, bootstyle="primary",variable=c_option, text="20%", value="20%")
rdb_option.grid(row=2, column=0, pady=5)


rdb_option1= ttkb.Radiobutton(frm, bootstyle="info",variable=c_option, text="40%", value="40%")
rdb_option1.grid(row=3, column=0)

lbl_output = ttkb.Label(frm,text="", font=("tahoma", 15, "bold"))
lbl_output.grid(row=4,column=0)

def convt():
    if(c_option.get() == "20%"):
        x = (20/100) * int(txt_num.get())
        lbl_output.config(text=x)
    else:
        x = (40/100) * int(txt_num.get())
        lbl_output.config(text=x)
btn_convert = ttkb.Button(frm, bootstyle="primary outline", text="CONVERT", command=convt)
btn_convert.grid(row=5, column=0)
root.mainloop()
