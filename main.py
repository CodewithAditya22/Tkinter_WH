from tkinter import *

root = Tk()
root.title("WalkHeart Stock Management")
# width x hight
# ---------------------------------- 590x400 --------------------------------- #
root.geometry("590x400")
#min and max -Start
root.minsize(590, 400)
root.maxsize(590, 400)
#min and max -End
logo_photo = PhotoImage(file="logof.png")

img_logo_lable = Label(image=logo_photo)
main_lable = Label(text="WalkHeart stock management system", )
img_logo_lable.pack()
main_lable.pack()
root.mainloop()
