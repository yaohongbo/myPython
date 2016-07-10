from Tkinter import *

class Calculator(Tk):
    def __init__(self):
        def callback(param):
            if param in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/']:
                temp = display.get() + param
                display.set(temp)
            elif param == '=':
                try:
                    display.set(eval(display.get()))
                except:
                    display.set("input error")
                else:
                    display.set("")
        Tk.__init__(self)
        self.title("calculator.py")
        self.geometry('300x300')
        self.resizable(width=False, height=False)
        # frame
        frame = Frame(self)
        frame.pack(side=TOP)
        # entry---justify:control how the text is justified
        entry = Entry(frame, width=30, justify=RIGHT)
        entry.grid(row=0, columnspan=5)
        display = StringVar()
        display.set('')
        entry['textvariable'] = display
        # button
        count = 0
        button_name = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '/', 'clear', '=']
        for i in range(4):
            for j in range(4):
                def cb(char=button_name[count]):
                    callback(char)

                Button(frame, borderwidth=2, width=5, height=2, text=button_name[count], command=cb). \
                    grid(row=i + 1, column=j)
                count += 1

        def callback(param):
            if param in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/']:
                    temp = display.get() + param
                    display.set(temp)
            elif param == '=':
                    try:
                        display.set(eval(display.get()))
                    except:
                        display.set("input error")
            else:
                    display.set("")


if __name__ == '__main__':
    Calculator().mainloop()
