#data type error
from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title("Addition")
root.title("600x400")
input_box = Entry(root)
input_box.pack()
def addition():
    number = 5
    get_input = input_box.get()
    
    try: 
        print(number + get_input)
        
    except(TypeError):
        messagebox.showinfo("Error", "Cannot Add Two Different Data Types : Integer And String")
    
button = Button(root, text = "Addition", command = addition)
button.pack()
root.mainloop()
        