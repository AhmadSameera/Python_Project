from tkinter import *
from MainAmica import *
def fun():
    try:
        while True:
            main1()
    except:
        pass

    finally:
        print('facing some issues. Wait...')
root = Tk()
# set window size
root.geometry("800x600")
root.resizable(False, False)

#set window color
root['bg']='light blue'
# root['bg']= PhotoImage(file="v1.gif")

turn_off = Button(root, text="STOP",height=3, width=14,fg = "blue", command=root.quit)
turn_off.place(x=650,y=450)

turn_on = Button(root, text="SPEAK",height=3, width=14,fg = "blue", command=fun)
turn_on.place(x=550,y=450)

lable1 = Label(root, bg="Blue", fg="pink", text="AMICA",pady=10, width=20, height=1).grid(row=0)

# txt = Text(root,bg="white", fg="pink", width=50)
# txt.grid(row=1, column=0, columnspan=2)
#
# scrollbar = Scrollbar(txt)
# scrollbar.place(relheight=1, relx=0.974)
#
# e = Entry(root, fg="pink", width=55)
# e.grid(row=2, column=0)

root.mainloop()