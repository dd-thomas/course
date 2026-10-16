import tkinter
import tkinter.ttk

def lection16():
    """
    tkinter (part 2)
    """

    class Gui(tkinter.Tk):
        def __init__(self, title : str, geometry : str):
            super().__init__()
            self.title(title)
            self.geometry(geometry)

            self.__male__ = tkinter.IntVar()
            self.__female__ = tkinter.IntVar()

        def on_male_checked(self):
            self.multiline_text.insert(tkinter.END, "Male checked\n" if self.__male__.get() == 1 else "")
            self.update()

        def on_female_checked(self):
            self.multiline_text.insert(tkinter.END, "Female checked\n" if self.__female__.get() == 1 else "")
            self.update()

        def on_options_combobox_selected(self, event):
            self.name_label.config(text=self.options_combobox.get())
            self.update()

        def on_button_reset_clicked(self):
            self.__male__.set(0)
            self.__female__.set(0)

        def on_button_confirm_edit_clicked(self):
            value = self.name_entry.get()
            self.name_entry.delete(0, tkinter.END)
            self.multiline_text.insert(tkinter.END, f"{value}\n")
            self.update()

        def Init(self):
            self.name_label = tkinter.Label(text="Enter your name:")
            self.name_label.pack()

            self.name_entry = tkinter.Entry()
            self.name_entry.pack()

            self.multiline_text = tkinter.Text()
            self.multiline_text.pack()

            self.button_reset_checkers = tkinter.Button(text="Reset", command=self.on_button_reset_clicked)
            self.button_reset_checkers.pack()

            self.button_confirm_edit = tkinter.Button(text="Confirm edit", command=self.on_button_confirm_edit_clicked)
            self.button_confirm_edit.pack()

            self.check_male = tkinter.Checkbutton(text="male", variable=self.__male__, command=self.on_male_checked)
            self.check_male.pack()

            self.check_female = tkinter.Checkbutton(text="female", variable=self.__female__, command=self.on_female_checked)
            self.check_female.pack()

            self.options_combobox = tkinter.ttk.Combobox(values=["Slow", "Medium", "Fast"])
            self.options_combobox.pack()
            self.options_combobox.set("Slow")
            self.options_combobox.bind("<<ComboboxSelected>>", self.on_options_combobox_selected)

            self.mainloop()

    gui = Gui("Lection 16", "1024x768")
    gui.Init()

