import tkinter as gui
import Driver


def button_callback():
    Driver.main_loop(e1.get(), e2.get())


main_window = gui.Tk()
main_window.title('Insta-pie-bot')

gui.Label(main_window, text='Username:').grid(row=0)
gui.Label(main_window, text='Password:').grid(row=1)
e1 = gui.Entry(main_window)
e2 = gui.Entry(main_window, show="*")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button = gui.Button(main_window, text='Submit',
                    width=25, command=button_callback, fg='Blue')
button.grid(row=2, column=1)

main_window.mainloop()
