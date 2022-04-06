from tkinter import *
root = Tk()
root.title('Simple Calculator 2000')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2 
w = w - 200 # смещение от середины
h = h - 250
root.geometry('288x495+{}+{}'.format(w, h))
root.resizable(False, False)
def click_hendler(event=None):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(event))
def clear_event():
    ent.delete(0, END)
def eq(x):
    x = x.get()
    x = calc(x)
    ent.delete(0, END)
    ent.insert(0, x)
def back(x):
    x = x.get()
    x = x[0: -1]
    ent.delete(0, END)
    ent.insert(0, x)
def calc(x):
    x = razd(x)
    z = -1
    y = float(x[0][0])
    for i in x[1]:
        z +=1
        w = x[1][z]
        if w == '+':
            y += float(x[0][z+1])
        elif w == '-':
            y -= float(x[0][z+1])
        elif w == '*':
            y *= float(x[0][z+1])
        elif w == '/':
            y /= float(x[0][z+1])
    y = str(y)
    return y
def razd(x):
    chislo = ''
    chisla = []
    ban = ['+','-','/','*']
    znaki = []
    for i in x:
        if i in ban and chislo != '': 
            chisla.append(chislo)
            znaki.append(i)
            chislo = ''
        else:
            chislo += i
    else:
        chisla.append(chislo)
    return [chisla, znaki]
ent = Entry(root, width=40, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# lab = Label(root, width=40, borderwidth=5)
# lab.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
but_1= Button(root, text='1', padx=40, pady=20, command= lambda: click_hendler('1'))
but_2= Button(root, text='2', padx=40, pady=20, command= lambda: click_hendler('2'))
but_3= Button(root, text='3', padx=40, pady=20, command= lambda: click_hendler('3'))
but_4= Button(root, text='4', padx=40, pady=20, command= lambda: click_hendler('4'))
but_5= Button(root, text='5', padx=40, pady=20, command= lambda: click_hendler('5'))
but_6= Button(root, text='6', padx=40, pady=20, command= lambda: click_hendler('6'))
but_7= Button(root, text='7', padx=40, pady=20, command= lambda: click_hendler('7'))
but_8= Button(root, text='8', padx=40, pady=20, command= lambda: click_hendler('8'))
but_9= Button(root, text='9', padx=40, pady=20, command= lambda: click_hendler('9'))
but_0= Button(root, text='0', padx=40, pady=20, command= lambda: click_hendler('0'))
but_add = Button(root, text='+', padx=40, pady=20, command= lambda: click_hendler('+'))
but_m = Button(root, text='-', padx=40, pady=20, command= lambda: click_hendler('-'))
but_s = Button(root, text='*', padx=40, pady=20, command= lambda: click_hendler('*'))
but_r = Button(root, text='/', padx=40, pady=20, command= lambda: click_hendler('/'))
but_b = Button(root, text='Backspase', padx=40, pady=20, command= lambda: back(ent))
but_ = Button(root, text='.', padx=40, pady=20, command= lambda: click_hendler('.'))
but_e  = Button(root, text='=', padx=40, pady=20,command=lambda: eq(ent))
but_clear = Button(root, text='Clear', padx=40, pady=20, command= clear_event)
but_1.grid(row=1, column=0)
but_2.grid(row=1, column=1)
but_3.grid(row=1, column=2, sticky='we')
but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2, sticky='we')
but_7.grid(row=3, column=0)
but_8.grid(row=3, column=1)
but_9.grid(row=3, column=2, sticky='we')
but_0.grid(row=4, column=0)
but_m.grid(row=4, column=1)
but_r.grid(row=4, column=2, sticky='we')
but_add.grid(row=5, column=0)
but_s.grid(row=5, column=1)
but_e.grid(row=5, column=2, sticky='we')
but_.grid(row=6, column=0, sticky='we')
but_b.grid(row=6, column=1, columnspan=2, sticky='we')
but_clear.grid(row=7, column=0,columnspan=3, sticky='we')
root.mainloop()
