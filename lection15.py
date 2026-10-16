import tkinter

def lection15():
    """
    tkinter (part 1)
    """

    def on_button_click():
        l.config(text = "Clicked!")

    window = tkinter.Tk()
    window.wm_title("Main")
    window.geometry("800x600")

    l = tkinter.Label(None, text="Hello")
    l.pack()

    b = tkinter.Button(window, text="ClickMe", command=on_button_click)
    b.pack()

    window.mainloop()

