import tkinter as tk
from tkinter import messagebox
import sympy as sp


class UserData:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}"


class InputForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Input Form")
        self.master.geometry("800x600")

        # Create labels and entry fields
        tk.Label(master, text="Enter X Vert:").pack()
        tk.Label(master, text="Enter X Horz:").pack()
        self.entry_XVert = tk.Entry(master)
        self.entry_XHorz = tk.Entry(master)

        self.entry_XVert.pack()
        self.entry_XHorz.pack()

        tk.Label(master, text="Enter Y Vert:").pack()
        tk.Label(master, text="Enter Y Horz:").pack()
        self.entry_YVert = tk.Entry(master)
        self.entry_YHorz = tk.Entry(master)

        self.entry_YVert.pack()
        self.entry_YHorz.pack()

        tk.Label(master, text="Enter Z Vert:").pack()
        tk.Label(master, text="Enter Z Horz:").pack()
        self.entry_ZVert = tk.Entry(master)
        self.entry_ZHorz = tk.Entry(master)

        self.entry_ZVert.pack()
        self.entry_ZHorz.pack()

        self.result_label = tk.Label(master, text="", justify=tk.LEFT)
        self.result_label.pack(pady=10)

        # Create a submit button
        submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        submit_button.pack()

    def submit_form(self):
        # Get the values from the input fields
        entry_XVert = int(self.entry_XVert.get())
        entry_XHorz = int(self.entry_XVert.get())
        entry_YVert = int(self.entry_YVert.get())
        entry_YHorz = int(self.entry_YHorz.get())
        entry_ZVert = int(self.entry_ZVert.get())
        entry_ZHorz = int(self.entry_ZHorz.get())

        total_X = (entry_XVert * 10) + entry_XHorz
        total_Y = (entry_YVert * 10) + entry_YHorz
        total_Z = (entry_ZVert * 10) + entry_ZHorz

        firstEqu = (2 * total_X) + 11
        secondEqu = (2 * total_Z + total_Y) - 5
        thirdEqu = abs((total_Y + total_Z) - total_X)

        displayResult = f"X: {firstEqu}\nY: {secondEqu}\nZ: {thirdEqu}"
        self.result_label.config(text=displayResult)

        """
        # Display the information in a message box
        messagebox.showinfo("First Equation", firstEqu)
        messagebox.showinfo("Second Equation", secondEqu)
        messagebox.showinfo("Third Equation", thirdEqu)
        """

        # Clear the fields after submission
        self.entry_XVert.delete(0, tk.END)
        self.entry_XHorz.delete(0, tk.END)
        self.entry_YVert.delete(0, tk.END)
        self.entry_YHorz.delete(0, tk.END)
        self.entry_ZVert.delete(0, tk.END)
        self.entry_ZHorz.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InputForm(root)
    root.mainloop()