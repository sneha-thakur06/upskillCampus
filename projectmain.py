from tkinter import * 
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    specialchar=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+specialchar
    # print(all)
    password_length=int(length_Box.get())


    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))
    
    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    
    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))
    




def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
password=Label(root,text='Password Generator',font=('times new roman',20, 'bold'),bg='gray20',fg='white')
password.grid(pady=10)
weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)


mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)


strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthlable=Label(root,text='Password Length',font=('times new roman',20, 'bold'),bg='gray20',fg='white')
lengthlable.grid()

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid()


generateButton=Button(root,text="Generate",font=Font,command=generator)
generateButton.grid(pady=5)

passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid(pady=5)

copyButton=Button(root,text="Copy",font=Font)
copyButton.grid(pady=5)

root.mainloop()

