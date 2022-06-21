# Geometry Error
from tkinter import*
root = Tk()
root.title("Geometry Error")

try :
    root.geometry("600")
    
except : 
    print("Bad Geometry Error, Only One Dimension Passed In Geometry Instead Of Two")
    
root.mainloop()
