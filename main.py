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

main_lable = Label(text="WalkHeart stock management system")
main_lable.pack()
root.mainloop()
