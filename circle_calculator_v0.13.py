import tkinter.font as tkfont
from tkinter import *
from tkinter import colorchooser


# Setup Class
class Run(Tk):
    def __init__(self):
        super(Run, self).__init__()

        self.title("Circle Calculator")

    # Sets the resolution of the window according to the monitor
    @staticmethod
    def set_resolution():
        width = frame.winfo_screenwidth()
        height = frame.winfo_screenheight()
        result = str(width) + "x" + str(height)
        frame.geometry(result)

    # Changes colour of text on screen
    @staticmethod
    def change_colour():
        colour_in_full = str(colorchooser.askcolor(title="pick a colour"))
        remove_unicode = str(colour_in_full.replace("\')", ""))
        colour = str(remove_unicode.split('#')[1].lstrip().split(' ')[0])
        print(f"Current text colour: #{colour}")
        # frame['bg'] = '#' + colour
        # diagram['bg'] = '#' + colour

        for label in labels:
            label['fg'] = '#' + colour

    @staticmethod
    # Increase and decrease label font size
    def increase_label_font():
        font_size = fontStyle['size']
        if font_size > 40:
            font_size_error.pack(side="top")
        else:
            labels[13]['font'] = font_size + 2
            fontStyle.configure(size=font_size + 2)
            print("Current font size: ", font_size)
            font_size_error.forget()

    @staticmethod
    def decrease_label_font():
        font_size = fontStyle['size']
        if font_size < 20:
            font_size_error.pack(side="top")
        else:
            labels[13]['font'] = font_size - 2
            fontStyle.configure(size=font_size - 2)
            print("Current font size: ", font_size)
            font_size_error.forget()

    @staticmethod
    # Function for formulae used to calculate the answer
    def find():
        try:
            number_input = var.get()
            if number_input > 999 or number_input < -999:
                input_range_error.pack()
            else:
                area_result.config(text="" + str(3.14 * (var.get() ** 2)))
                area_result.place(x=450, y=400)
                circumference_result.config(text="" + str(2 * 3.14 * var.get()))
                circumference_result.place(x=450, y=500)
                diameter_result.config(text="" + str(2 * var.get()))
                diameter_result.place(x=450, y=600)
                input_range_error.forget()
        except TclError:
            input_range_error.pack()


# Setup of window instance, variables, fonts, and lists
frame = Run()
var = DoubleVar()
clicked = StringVar()
clicked.set("Units")
circle = PhotoImage(file="resources/circle.png")
fontStyle = tkfont.Font(family="Times_New_Roman", size=30)
labels = []
units_options = [
    "mm",
    "cm",
    "m",
    "km",
    "inch",
    "feet"
]

# class Labels(Tk):
# def __init__(self):
#   super(Labels, self).__init__()

# @staticmethod
# def draw_labels():
# Draw Circle diagram image
diagram = Label(frame, image=circle, bg="light gray")
diagram.place(x=870, y=250)

# Draw Entry box title
entry_title = Label(frame, text="-Input a value-", font=fontStyle)
entry_title.place(x=300, y=100)
labels.append(entry_title)

# Draw Entry box (Radius)
entry_box = Entry(frame, textvariable=var, font=fontStyle)
entry_box.place(x=200, y=200)

# Draw Units options dropdown menu
drop = OptionMenu(frame, clicked, *units_options)
drop.pack()

# Draw Entry box subtitle (Radius=), (r=)
entry_subtitle_r = Label(frame, text="r =", font=fontStyle, bg="light gray")
entry_subtitle_r.place(x=100, y=200)
labels.append(entry_subtitle_r)

# Draw Area, Circumference & Diameter (=)
entry_subtitle_area = Label(frame, text="Area =", font=fontStyle, bg="light gray")
entry_subtitle_area.place(x=100, y=400)
labels.append(entry_subtitle_area)
entry_subtitle_circumference = Label(frame, text="Circumference =", font=fontStyle, bg="light gray")
entry_subtitle_circumference.place(x=100, y=500)
labels.append(entry_subtitle_circumference)
entry_subtitle_diameter = Label(frame, text="Diameter =", font=fontStyle, bg="light gray")
entry_subtitle_diameter.place(x=100, y=600)
labels.append(entry_subtitle_diameter)

# Draw Area, Circumference & Diameter's results
area_result = Label(frame, font=fontStyle, bg="light gray")
labels.append(area_result)
circumference_result = Label(frame, font=fontStyle, bg="light gray")
labels.append(circumference_result)
diameter_result = Label(frame, font=fontStyle, bg="light gray")
labels.append(diameter_result)

# Draw colour picker button
colour_button = Button(frame, text="colour", width=20, command=Run.change_colour)
colour_button.place(x=0, y=79)

# Draw Fine Out Button (Submit)
find_button = Button(frame, text="Find Out", font=fontStyle, bg="light gray", command=Run.find)
find_button.place(x=400, y=300)
labels.append(find_button)

# Draw Increase and Decrease font size buttons
increase_font = Button(frame, text="+", width=20,
                       command=Run.increase_label_font)
decrease_font = Button(frame, text="-", width=20,
                       command=Run.decrease_label_font)

increase_font.place(x=1, y=1)
decrease_font.place(x=1, y=40)

# Draw Units
entry_units = Label(frame, textvariable=clicked, font=fontStyle, bg="light gray")
entry_units.place(x=700, y=200)
labels.append(entry_units)
area_units = Label(frame, textvariable=clicked, font=fontStyle, bg="light gray")
area_units.place(x=760, y=400)
labels.append(area_units)
circumference_units = Label(frame, textvariable=clicked, font=fontStyle, bg="light gray")
circumference_units.place(x=760, y=500)
labels.append(circumference_units)
diameter_units = Label(frame, textvariable=clicked, font=fontStyle, bg="light gray")
diameter_units.place(x=760, y=600)
labels.append(diameter_units)
placeholder = Label(frame, text="", font=fontStyle, width=0, height=0)
placeholder.pack_forget()
labels.append(placeholder)

# Set error label
font_size_error = Label(frame, text="Font size limit reached", font="Times_New_Roman 10 bold", fg="red")
input_range_error = Label(frame, text="Please enter a number between -999 and 999",
                          font="Times_New_Roman 10 bold", fg="red")

if __name__ == '__main__':
    # Labels.draw_labels()
    frame.set_resolution()
    frame.mainloop()
