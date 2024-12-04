from tkinter import*
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog

root=Tk()
root.title('Kucherova Elizabet')
root.geometry('400x260')

nt=ttk.Notebook(root)
tab1=Frame(nt)
tab2=Frame(nt)
tab3=Frame(nt)

#tab1
def cal():
    num1=int(math.get())
    num2=int(math2.get())

    if com.get()=='+':
        res=num1+num2
    if com.get()=='-':
        res=num1-num2
    if com.get()=='*':
        res=num1*num2
    if com.get()=='/':
        if num2==0:
            messagebox.showinfo('Результат', 'На ноль делить нельзя')
        else:
            res=num1/num2
    messagebox.showinfo('Результат', f'Результат: {res}')

nt.add(tab1, text='First')

lbl=Label(tab1, text='Calculator')
lbl.grid(column=2, row=0)

math=Entry(tab1)
math.grid(column=0, row=3, padx=5, pady=5)

math2=Entry(tab1)
math2.grid(column=3, row=3, padx=5, pady=5)

com=Combobox(tab1)
com.grid(column=0, row=0)

lbl2=Label(tab1, text='Vibery deistvie')
lbl2.grid(column=2, row=5)

com['values']=('+', '-', '*', '/')
com.grid(column=2, row=6)

bt=Button(tab1, text='Raschitat', command=cal)
bt.grid(column=2, row=7)

#tab2
def cl():
    v=[]
    if sl1.get()==1:
        v.append('Первый вариант')
    if sl2.get()==1:
        v.append('Второй вариант')
    if sl3.get()==1:
        v.append('Третий вариант')
    if v:
        messagebox.showinfo('Вывод', 'Вы выбрали '+','.join(v))
    else:
        messagebox.showinfo('Вывод','Вы не выбрали вариант')

sl1=BooleanVar()
sl2=BooleanVar()
sl3=BooleanVar()

nt.add(tab2, text='Second')
lbls=Label(tab2, text='Vibor')
lbls.grid(column=2, row=0)

rad1=Checkbutton(tab2, text='1', variable=sl1)
rad2=Checkbutton(tab2, text='2', variable=sl2)
rad3=Checkbutton(tab2, text='3', variable=sl3)

rad1.grid(column=2, row=1)
rad2.grid(column=2, row=2)
rad3.grid(column=2, row=3)

btn2=Button(tab2, text='Click', command=cl )
btn2.grid(column=2, row=4)

#tab3
def open():
    filepath=filedialog.askopenfilename()
    if filepath !='':
        with open(filepath, 'r') as file:
            t=file.read()
            txt.delete('1.0', 'end')
            txt.insert('1.0', t)

nt.add(tab3, text='Third')

txt=Text(tab3, width=48, height=12)
txt.grid()

btn3=Button(tab3, text='Загрузить файл', command=open)
btn3.grid()

nt.pack(expand=1, fill='both')
root.mainloop()
