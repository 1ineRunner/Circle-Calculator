import tkinter.font as tkfont
from tkinter import *
from tkinter import colorchooser


# Setup Class
class Run:
    def __init__(self):
        super(Run, self).__init__()

    # Sets the resolution of the window according to the monitor
    @staticmethod
    def set_resolution(window, div, div2):
        width = int(window.winfo_screenwidth() / div)
        height = int(window.winfo_screenheight() / div2)
        result = str(width) + "x" + str(height)
        window.geometry(result.format(width / 2, height / 2))

    # Changes colour of text on screen
    @staticmethod
    def change_colour():
        colour_in_full = str(colorchooser.askcolor(title="Pick a colour"))
        remove_unicode = str(colour_in_full.replace("\')", ""))
        colour = str(remove_unicode.split('#')[1].lstrip().split(' ')[0])
        print(f"Current text colour: #{colour}")
        for label in Variables.labels:
            label['fg'] = '#' + colour


    # Increase and decrease label font size
    @staticmethod
    def increase_label_font():
        font_size = Variables.fontStyle['size']
        if font_size > 34:
            Variables.font_size_error.pack(side="top")
        else:
            Variables.labels[13]['font'] = font_size + 2
            Variables.fontStyle.configure(size=font_size + 2)
            print("Current font size: ", font_size)
            Variables.font_size_error.forget()

    @staticmethod
    def decrease_label_font():
        font_size = Variables.fontStyle['size']
        if font_size < 20:
            Variables.font_size_error.pack(side="top")
        else:
            Variables.labels[13]['font'] = font_size - 2
            Variables.fontStyle.configure(size=font_size - 2)
            print("Current font size: ", font_size)
            Variables.font_size_error.forget()

    # Function for formulae used to calculate the answer
    @staticmethod
    def find():
        try:
            number_input = Variables.var.get()
            if number_input > 999 or number_input < -999:
                Variables.input_range_error.pack()
            else:
                unrounded_area = (3.14 * (Variables.var.get() ** 2))
                rounded_area = str(round(unrounded_area, 4))
                Variables.area_result.config(text="" + rounded_area)
                Variables.area_result.place(x=450, y=400)

                unrounded_diameter = (2 * Variables.var.get())
                rounded_diameter = str(round(unrounded_diameter, 4))
                Variables.diameter_result.config(text="" + rounded_diameter)
                Variables.diameter_result.place(x=450, y=600)

                unrounded_circumference = (2 * 3.14 * Variables.var.get())
                rounded_circumference = str(round(unrounded_circumference, 4))
                Variables.circumference_result.config(text="" + rounded_circumference)
                Variables.circumference_result.place(x=450, y=500)

                Variables.input_range_error.forget()
        except TclError:
            Variables.input_range_error.pack()

    @staticmethod
    def help():
        win = Toplevel(Variables.calculator)
        Run.set_resolution(window=win, div=4, div2=2)


# Class for Main Window
class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Circle Calculator")


# Class for Setup of window instance, variables, fonts, and lists
class Variables:
    calculator = App()
    settings = Run()
    var = DoubleVar()
    clicked = StringVar()
    clicked.set("units")
    circle = PhotoImage(file="resources/circle.png")
    fontStyle = tkfont.Font(family="Times_New_Roman", size=30)
    labels = []
    units_options = [
        "units",
        "mm",
        "cm",
        "m",
        "km",
        "inch",
        "feet"
    ]

    diagram = Label(calculator, image=circle)
    diagram.place(x=870, y=250)

    # Draw Entry box title
    entry_title = Label(calculator, text="-Input a radius-", font=fontStyle)
    entry_title.place(x=240, y=100)
    labels.append(entry_title)

    # Draw Entry box (Radius)
    entry_box = Entry(calculator, textvariable=var, font=fontStyle)
    entry_box.place(x=160, y=200)

    # Draw Units options dropdown menu
    drop = OptionMenu(calculator, clicked, *units_options)
    drop.pack()

    # Draw Entry box subtitle (Radius=), (r=)
    entry_subtitle_r = Label(calculator, text="r =", font=fontStyle)
    entry_subtitle_r.place(x=95, y=200)
    labels.append(entry_subtitle_r)

    # Draw Area, Circumference & Diameter (=)
    entry_subtitle_area = Label(calculator, text="Area =", font=fontStyle)
    entry_subtitle_area.place(x=100, y=400)
    labels.append(entry_subtitle_area)

    entry_subtitle_diameter = Label(calculator, text="Diameter =", font=fontStyle)
    entry_subtitle_diameter.place(x=100, y=500)
    labels.append(entry_subtitle_diameter)

    entry_subtitle_circumference = Label(calculator, text="Circumference =", font=fontStyle)
    entry_subtitle_circumference.place(x=100, y=600)
    labels.append(entry_subtitle_circumference)

    # Draw Area, Circumference & Diameter's results
    area_result = Label(calculator, font=fontStyle)
    labels.append(area_result)
    diameter_result = Label(calculator, font=fontStyle)
    labels.append(diameter_result)
    circumference_result = Label(calculator, font=fontStyle)
    labels.append(circumference_result)

    # Draw colour picker button
    colour_button = Button(calculator, text="Colour", width=20, command=Run.change_colour)
    colour_button.place(x=0, y=79)

    # Draw Fine Out Button (Submit)
    find_button = Button(calculator, text="Calculate & Find Out", font=fontStyle, command=Run.find)
    find_button.place(x=210, y=300)
    labels.append(find_button)

    # Draw Increase and Decrease font size buttons
    increase_font = Button(calculator, text="Zoom In +", width=20,
                           command=Run.increase_label_font)
    decrease_font = Button(calculator, text="Zoom Out -", width=20,
                           command=Run.decrease_label_font)

    increase_font.place(x=1, y=1)
    decrease_font.place(x=1, y=40)

    help_button = Button(calculator, text="Help", width=20, command=Run.help)
    help_button.place(x=0, y=118)

    # Draw Units
    entry_units = Label(calculator, textvariable=clicked, font=fontStyle)
    entry_units.place(x=740, y=200)
    labels.append(entry_units)

    area_units = Label(calculator, textvariable=clicked, font=fontStyle)
    area_units.place(x=740, y=400)
    labels.append(area_units)

    diameter_units = Label(calculator, textvariable=clicked, font=fontStyle)
    diameter_units.place(x=740, y=600)
    labels.append(diameter_units)
    placeholder = Label(calculator, text="", font=fontStyle, width=0, height=0)

    circumference_units = Label(calculator, textvariable=clicked, font=fontStyle)
    circumference_units.place(x=740, y=500)
    labels.append(circumference_units)

    # Place Holder Label
    placeholder.pack_forget()
    labels.append(placeholder)

    # Set error label
    font_size_error = Label(calculator, text="Font size limit reached", font="Times_New_Roman 10 bold", fg="red")
    input_range_error = Label(calculator, text="Please enter a number between -999 and 999",
                              font="Times_New_Roman 10 bold", fg="red")


if __name__ == '__main__':
    Run.set_resolution(window=Variables.calculator, div=1, div2=1)
    Variables.calculator.mainloop()
