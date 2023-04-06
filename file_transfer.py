import tkinter as tk
from tkinter import *
import tkinter.filedialog


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #Creates button to seleft files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() pad and and pad y are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #Creates bytton to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
             #Creates function to select source directory
        def sourceDir(self):
            selectSourceDir = tkinter.filedialog.askdirectory()
            #The .delete(0, END) will clear the content that is inserted in the entry widget
            # this allows the path to be inserted into the entry widget properly
            self.source_dir.delete(0, END)
            #The .insert method will insert the user selection to the source_dir entry
            self.source_dir.insert(0, selectSourceDir)
            #Creates button to select files from the source directory
            self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

        #Creates function to select destination directory
        def destDir(self):
            selectDestDir = tkinter.filedialog.askdirectory()
            #The .insert method will insert the user selection to the destination_dir entry widget
            #allows for the entry to be inserted into the widget properly
            self.destination_dir.delete(0, END)
            #The .insert method will insert the user selection to the destination_dir entry
            self.destination_dir.insert(0, selectDestDir)
            #Creates a button to select destination of files
            self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        

   
    
        









if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
