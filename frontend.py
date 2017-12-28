"""
A program that stores book information, title, year , author and ISBN. Users can
search an entry,
add an entry,
delete an entry,
update an entry,
also see the entire list
close
"""

from tkinter import *
from backend import Database

database =Database("Books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index=lbox.curselection()
        selected_tuple = lbox.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[3])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[2])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass

def view_command():
    lbox.delete(0,END)
    for row in database.view():
        lbox.insert(END,row)

def search_command():
    lbox.delete(0,END)
    for row in database.search(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        lbox.insert(END,row)

def add_command():
    database.insert(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    lbox.delete(0,END)
    lbox.insert(END,(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())


window=Tk()

window.wm_title("Book Catalogue")

L1=Label(window, text="Title")
L1.grid(row=0,column=0)

L2=Label(window, text="Year")
L2.grid(row=1, column=0)

L3=Label(window, text="Author")
L3.grid(row=0, column=2)

L4=Label(window, text="ISBN")
L4.grid(row=1, column=2)

Title_text= StringVar()
e1=Entry(window,textvariable=Title_text)
e1.grid(row=0,column=1)

Year_text= StringVar()
e2=Entry(window,textvariable=Year_text)
e2.grid(row=1,column=1)

Author_text= StringVar()
e3=Entry(window,textvariable=Author_text)
e3.grid(row=0,column=3)

ISBN_text= StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)


lbox=Listbox(window,height= 6, width= 35)
lbox.grid(row=3,column=0, rowspan=7, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=7)

lbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=lbox.yview)

lbox.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text= "View all", width=12, command=view_command)
b1.grid(row=3,column=3)

b2=Button(window, text= "Search Entry", width=12, command=search_command)
b2.grid(row=4,column=3)

b3=Button(window, text= "Add Entry", width=12, command=add_command)
b3.grid(row=5,column=3)

b4=Button(window, text= "Update selected", width=12, command=update_command)
b4.grid(row=6,column=3)

b5=Button(window, text= "Delete selected", width=12, command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window, text= "Close", width=12, command= window.destroy)
b6.grid(row=8,column=3)

window.mainloop()
