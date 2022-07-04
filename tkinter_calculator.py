from tkinter import *

root = Tk()
root.title('')

e = Entry(root, width = 30, borderwidth = 5)
e.grid(row=0,column=0, columnspan=4)

def num_click(x):
	e.insert(len(e.get()),int(x))

num_lst=[]
operation_lst=[]

def dot_click():
    e.insert(len(e.get()), '.')

def operation_click(x):
	num_lst.append(float(e.get()))
	operation_lst.append(x)
	e.delete(0, END)
	
    
def delfunc():
    e.delete(0,END)
    num_lst=[]
    operation_lst=[]

def addfunc(x,y):
    return float(x+y)

def subfunc(x,y):
    return float(x-y)

def multiply(x,y):
    return float(x*y)

def divide(x,y):
    return float(x/y)
    
def equalfunc(lst1, lst2):
    if len(lst1)<1:
        pass
    else:
        result= 0
        for s in lst2:
            if s == '+':
                lst1.append(float(e.get()))
                result = addfunc(lst1[0], lst1[1])
                lst1.pop(0)
                lst1.pop(0)
                lst2.pop(0)
                e.delete(0,END)
                e.insert(0,result)
            elif s == '-':
                lst1.append(float(e.get()))
                result = subfunc(lst1[0], lst1[1])
                lst1.pop(0)
                lst1.pop(0)
                lst2.pop(0)
                e.delete(0,END)
                e.insert(0,result)
            elif s== '*':
                lst1.append(float(e.get()))
                result = multiply(lst1[0], lst1[1])
                lst1.pop(0)
                lst1.pop(0)
                lst2.pop(0)
                e.delete(0,END)
                e.insert(0,result)
            else:
                lst1.append(float(e.get()))
                result = divide(lst1[0], lst1[1])
                lst1.pop(0)
                lst1.pop(0)
                lst2.pop(0)
                e.delete(0,END)
                e.insert(0,result)

button_1 = Button(root, text = 1, padx = 15, pady=20, bg='white', borderwidth=2, command = lambda: num_click(button_1.cget('text')))
button_2 = Button(root, text = 2, padx = 15, pady=20, bg='white', command = lambda: num_click(button_2.cget('text')))
button_3 = Button(root, text = 3, padx = 15, pady=20, bg='white', command = lambda: num_click(button_3.cget('text')))


button_4 = Button(root, text = 4, padx = 15, pady=20, bg='white', command = lambda: num_click(button_4.cget('text')))
button_5 = Button(root, text = 5, padx = 15, pady=20, bg='white', command = lambda: num_click(button_5.cget('text')))
button_6 = Button(root, text = 6, padx = 15, pady=20, bg='white', command = lambda: num_click(button_6.cget('text')))


button_7 = Button(root, text = 7, padx = 15, pady=20, bg='white', command = lambda: num_click(button_7.cget('text')))
button_8 = Button(root, text = 8, padx = 15, pady=20, bg='white', command = lambda: num_click(button_8.cget('text')))
button_9 = Button(root, text = 9, padx = 15, pady=20, bg='white', command = lambda: num_click(button_9.cget('text')))


button_0 = Button(root, text = 0, padx = 15, pady=20, bg='white', command = lambda: num_click(button_0.cget('text')))

button_dot = Button(root, text = '.', padx=16, pady=20, command = dot_click)
button_add = Button(root, text = '+', padx=14, pady = 20, command = lambda: operation_click(button_add.cget('text')))
button_sub = Button(root, text = '-', padx = 15, pady = 20, command = lambda: operation_click(button_sub.cget('text')))
button_multiply = Button(root, text='*', padx = 15, pady = 20, command = lambda: operation_click(button_multiply.cget('text')))
button_divide = Button(root, text = '/', padx = 15, pady=20, command = lambda: operation_click(button_divide.cget('text')))
button_equal = Button(root, text='=', padx = 14, pady=20, command = lambda: equalfunc(num_lst, operation_lst))
button_del = Button(root, text = 'del', padx = 10, pady=20, command = delfunc, width=23)                        
                    
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_dot.grid(row=4, column=0)
button_del.grid(row=5, column=0, rowspan=4, columnspan=4)

root.mainloop()