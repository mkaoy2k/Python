import tkinter as tk
from tkinter import ttk


def main():
    """
    The main entry point of the application.

    Initializes an instance of the Application class and starts the main event 
    loop.
    """
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    def __init__(self):
        """
        Initializes an instance of the Application class.

        Sets the window title and configures the grid layout.
        Creates two instances of the InputForm class and adds them to the grid.
        """
        super().__init__()
        self.title("Simple App")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(self, parent):
        """
        Initializes an instance of the InputForm class.

        Configures the grid layout, creates an entry field, and adds buttons for 
        adding and clearing the list. 
        
        The entry field is bound to the add_to_list method, which is also used 
        as the command for the "Add" button. 
        
        The "Clear" button is bound to the clear_list method.

        Parameters:
            parent: The parent widget of the InputForm instance.

        Returns:
            None
        """
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", self.add_to_list)

        self.entry_btn = tk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        self.entry_btn2 = tk.Button(self, text="Clear", command=self.clear_list)
        self.entry_btn2.grid(row=0, column=2)

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")

    def add_to_list(self, _event=None):
        """
        Adds the text from the entry field to the list box.

        Parameters:
            _event (object): The event object passed when the function is called from an event binding. Defaults to None.

        Returns:
            None
        """
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.text_list.delete(0, tk.END)


if __name__ == "__main__":
    main()