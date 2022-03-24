from tkinter import *
 

def sim_p(event):
    lab['text'] += '+'
def sim_m(event):
    lab['text'] += '-'
def sim_s(event):
    lab['text'] += '*'
def sim_r(event):
    lab['text'] += '/'
def sim_e(event):
    lab['text'] = calc(lab['text'])
def sim_1(event):
    lab['text'] += '1'
def sim_2(event):
    lab['text'] += '2'
def sim_3(event):
    lab['text'] += '3'
def sim_4(event):
    lab['text'] += '4'
def sim_5(event):
    lab['text'] += '5'
def sim_6(event):
    lab['text'] += '6'
def sim_7(event):
    lab['text'] += '7'
def sim_8(event):
    lab['text'] += '8'
def sim_9(event):
    lab['text'] += '9'
def sim_0(event):
    lab['text'] += '0'
def sim(event):
    lab['text'] = ''
def sim_(event):
    lab['text'] = lab['text'][0:-1]
def sim_o(event):
    lab['text'] += '.'
 
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
    return y


root = Tk()
root.title('калькулятор')

f_top = Frame(root)
f_bot = Frame(root)
f_1= Frame(root)
f_2= Frame(root)
f_3= Frame(root)
f_4= Frame(root)
f_5= Frame(root)

but_p = Button(f_bot, text="+", width=15, height=3)
but_m= Button(f_top, text="-", width=15, height=3)
but_s= Button(f_bot, text="*", width=15, height=3)
but_r= Button(f_top, text='/', width=15, height=3)
but_e= Button(f_bot, text='=', width=15, height=3)
but_1= Button(f_1, text='1', width=15, height=3)
but_2= Button(f_1, text='2', width=15, height=3)
but_3= Button(f_1, text='3', width=15, height=3)
but_4= Button(f_2, text='4', width=15, height=3)
but_5= Button(f_2, text='5', width=15, height=3)
but_6= Button(f_2, text='6', width=15, height=3)
but_7= Button(f_3, text='7', width=15, height=3)
but_8= Button(f_3, text='8', width=15, height=3)
but_9= Button(f_3, text='9', width=15, height=3)
but_0= Button(f_top, text='0', width=15, height=3)
but = Button(text='Clear', width=48, height=3)
but_ = Button(f_4,text='Backspase', width=35, height=3)
but_o =Button(f_4,text='.', width=11, height=3)

lab = Label(f_5, width=25, height=1, bg='white', fg='black', padx=10, pady=10, font=(20))

but_p.bind('<Button-1>', sim_p)
but_m.bind('<Button-1>', sim_m)
but_s.bind('<Button-1>', sim_s)
but_r.bind('<Button-1>', sim_r)
but_e.bind('<Button-1>', sim_e)
but_1.bind('<Button-1>', sim_1)
but_2.bind('<Button-1>', sim_2)
but_3.bind('<Button-1>', sim_3)
but_4.bind('<Button-1>', sim_4)
but_5.bind('<Button-1>', sim_5)
but_6.bind('<Button-1>', sim_6)
but_7.bind('<Button-1>', sim_7)
but_8.bind('<Button-1>', sim_8)
but_9.bind('<Button-1>', sim_9)
but_0.bind('<Button-1>', sim_0)
but.bind('<Button-1>', sim)
but_.bind('<Button-1>', sim_)
but_o.bind('<Button-1>', sim_o)

f_5.pack(expand=1)
lab.pack()
# Рамки
f_1.pack()
f_2.pack()
f_3.pack()
f_top.pack()
f_bot.pack()
f_4.pack()

# Кнопки числа
but_0.pack(side=LEFT)
but_1.pack(side=LEFT)
but_2.pack(side=LEFT)
but_3.pack(side=LEFT)
but_4.pack(side=LEFT)
but_5.pack(side=LEFT)
but_6.pack(side=LEFT)
but_7.pack(side=LEFT)
but_8.pack(side=LEFT)
but_9.pack(side=LEFT)



# Кнопки действий
but_p.pack(side=LEFT)
but_m.pack(side=LEFT)
but_s.pack(side=LEFT)
but_r.pack(side=LEFT)
but_e.pack(side=LEFT)
but_.pack(side=LEFT)
but_o.pack(side=LEFT)
but.pack()


root.mainloop()
