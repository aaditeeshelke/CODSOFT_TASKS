
from tkinter import*
from tkinter import ttk


class do:
    

    def __init__(self,root):
        
        self.root = root
        self.root.title('TO DO LIST')
        self.root.geometry('500x510+400+100')
        self.label = Label(root, text='TO-DO-LIST', font=('Comic Sans MS', 25), width=15, bd=10, bg='purple', fg='yellow')
        self.label.pack(side='top', fill=BOTH)
       
        self.label1 = Label(root, text='ADD WISHLIST', font=('Comic Sans MS', 15), width=15, bd=10, bg='violet', fg='black')
        self.label1.place(x=300,y=90)

        self.label2 = Label(root, text='WISHLIST', font=('Comic Sans MS', 15), width=15, bd=10, bg='violet', fg='black')
        self.label2.place(x=40,y=90)

        self.main_text = Listbox(self.root,height=10,bd =5,width=18,bg='gray',font=('ariel',20 ,'bold'))
        self.main_text.place(x=0,y=150)

        self.text = Text(self.root,bd=5,height=2,width=20,bg='gray',font=('ariel',10 ,'bold'))
        self.text.place(x=320,y=175)

        self.button = Button(root,text='UPDATE',font=('ariel',20 ,'bold'),width='10',bd=5,bg='sky blue',fg='black',command=self.add)
        self.button.place(x=300,y=300)

        self.button1 = Button(root, text='DELETE', font=('ariel', 20, 'bold'), width='10', bd=5, bg='red', fg='black', command=self.delete)
        self.button1.place(x=300, y=400)

       
        

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)
           
    def delete(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            self.main_text.delete(selected_index)
            with open('data.txt', 'r') as file:
                lines = file.readlines()
            with open('data.txt', 'w') as file:
                for index, line in enumerate(lines):
                    if index not in selected_index:
                        file.write(line)
   
    def read_data(self):
        with open('data.txt', 'r') as file:
            for line in file:
                self.main_text.insert(END, line.strip())
        


def main():
    root=Tk()
    ui=do(root)
    root.mainloop()

if __name__ == "__main__":
    main()