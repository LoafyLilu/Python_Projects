import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")


        #Label above entry and buttons
        self.lbl = Label(self.master, text="Enter your custom text, or click Default HTML Page button")
        self.lbl.grid(row=0, column=0, padx=(10,10), pady=(10,10))
        #Entry space for user input
        self.entry = Entry(self.master, text=None, width=75)
        self.entry.grid(row=1, columnspan=2, padx=(10,10), pady=(10,10))
        #button and placement for default html page button
        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, columnspan=2, padx=(10,10) , pady=(10,10))
        #button and placement for custom html button
        self.btn = Button(self.master, text="Custom HTML Page", width=20, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))
        

    def defaultHTML(self):
        htmlText = "Heya! This is the default text!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        #passes in user input as htmlText value
        string = self.entry.get()
        htmlText = string
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
