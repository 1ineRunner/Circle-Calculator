from tkinter import *
import tkinter.font as tkfont
from tkinter import colorchooser


# Setup Class
class Run(Tk):
    def __init__(self):
        super(Run, self).__init__()
        self.title("Circle Calculator")

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
            Variables.labels[19]['font'] = font_size + 2
            Variables.fontStyle.configure(size=font_size + 2)
            print("Current font size: ", font_size)
            Variables.font_size_error.forget()

    @staticmethod
    def decrease_label_font():
        font_size = Variables.fontStyle['size']
        if font_size < 20:
            Variables.font_size_error.pack(side="top")
        else:
            Variables.labels[19]['font'] = font_size - 2
            Variables.fontStyle.configure(size=font_size - 2)
            print("Current font size: ", font_size)
            Variables.font_size_error.forget()

    # Function for formulae used to calculate the answer
    @staticmethod
    def find():
        try:
            # Vars for number input and unit input
            units_input = Variables.var2.get()
            number_input = Variables.var.get()

            # If the input number is greater than 999 or less than -999 display an error
            if number_input > 999 or number_input < -999:
                Variables.input_range_error.pack()
            else:
                # Calculations to generate the results & round generated results to fourth decimal place
                area_in_full = (3.14 * (Variables.var.get() ** 2))
                rounded_area = str(round(area_in_full, 4))
                Variables.area_result.config(text="" + rounded_area)
                Variables.area_result.place(x=480, y=400)

                diameter_in_full = (2 * Variables.var.get())
                rounded_diameter = str(round(diameter_in_full, 4))
                Variables.diameter_result.config(text="" + rounded_diameter)
                Variables.diameter_result.place(x=480, y=600)

                circumference_in_full = (2 * 3.14 * Variables.var.get())
                rounded_circumference = str(round(circumference_in_full, 4))
                Variables.circumference_result.config(text="" + rounded_circumference)
                Variables.circumference_result.place(x=480, y=500)

                # Input units are valid if they are alphabetical only, less than three characters or empty
                if units_input.isalpha() and len(units_input) < 3 or units_input == "":
                    Variables.area_units.forget()
                    Variables.diameter_units.forget()
                    Variables.circumference_units.forget()

                    Variables.area_units.config(text="" + units_input)
                    Variables.area_units.place(x=740, y=400)

                    Variables.diameter_units.config(text="" + units_input)
                    Variables.diameter_units.place(x=740, y=600)

                    Variables.circumference_units.config(text="" + units_input)
                    Variables.circumference_units.place(x=740, y=500)

                    # So forget any previous error:
                    Variables.unit_error.forget()

                else:
                    # It's an invalid string to use as units:
                    Variables.unit_error.pack()

                # So forget any previous error:
                Variables.input_range_error.forget()

        # Handle invalid input:
        except TclError:
            Variables.input_range_error.pack()

    # Function Help dialogue
    @staticmethod
    def help():
        win = Toplevel(Variables.calculator)
        Run.set_resolution(window=win, div=2, div2=2)

        entry_title = Label(win, text="Help Dialogue", font=Variables.fontStyle)
        instruction_1 = Label(win, text="1. Use the \"Zoom\" + and - icons to increase and"
                                        " decrease the size of the font on the page")
        instruction_2 = Label(win, text="2. Use the \"Colour\" button to select a colour for the"
                                        " text using the built-in colour picker")
        instruction_3 = Label(win, text="3. Type a number to calculate with into the first entry"
                                        " bar under the \"-Input a radius-\" title")
        instruction_4 = Label(win, text="4. Optionally, you can type at most two letters in the"
                                        " second entry bar to act as units")
        instruction_5 = Label(win, text="5. When you are ready to calculate the result, click"
                                        " the button \"Calculate & Find Out\"")

        # Append labels for colour and font setting in help dialogue
        Variables.labels.append(entry_title)
        Variables.labels.append(instruction_1)
        Variables.labels.append(instruction_2)
        Variables.labels.append(instruction_3)
        Variables.labels.append(instruction_4)
        Variables.labels.append(instruction_5)

        # Placement of labels in help dialogue
        entry_title.pack()
        instruction_1.pack()
        instruction_2.pack()
        instruction_3.pack()
        instruction_4.pack()
        instruction_5.pack()


# Class for Setup of window instance, variables, fonts, and lists
class Variables:
    def __int__(self):
        super(Variables, self).__init__()

    calculator = Run()
    var = DoubleVar()
    var2 = StringVar()
    labels = []
    circle = PhotoImage(file="resources/circle.png")
    fontStyle = tkfont.Font(family="Times_New_Roman", size=30)
    bold = tkfont.Font(family="Times_New_Roman 10 bold", size=10)
    diagram = Label(calculator, image=circle)

    # Initialization of all labels
    # Draw Entry box title
    entry_title = Label(calculator, text="-Input a radius-", font=fontStyle)

    # Draw Entry boxes (Radius & Units)
    entry_box = Entry(calculator, textvariable=var, width=15, font=fontStyle)
    entry_box2 = Entry(calculator, textvariable=var2, width=5, font=fontStyle)

    # Draw Entry box subtitles (r= & u=)
    entry_subtitle_r = Label(calculator, text="r =", font=fontStyle)
    entry_subtitle_u = Label(calculator, text="u =", font=fontStyle)

    # Draw Area, Circumference & Diameter result subtitles (=)
    entry_subtitle_area = Label(calculator, text="Area =", font=fontStyle)
    entry_subtitle_diameter = Label(calculator, text="Diameter =", font=fontStyle)
    entry_subtitle_circumference = Label(calculator, text="Circumference =", font=fontStyle)

    # Draw Area, Circumference & Diameter's results
    area_result = Label(calculator, font=fontStyle)
    diameter_result = Label(calculator, font=fontStyle)
    circumference_result = Label(calculator, font=fontStyle)

    # Draw clickable buttons (font increase/decrease, colour_button, help_button, find_button)
    increase_font = Button(calculator, text="Zoom In +", width=20,
                           command=Run.increase_label_font)
    decrease_font = Button(calculator, text="Zoom Out -", width=20,
                           command=Run.decrease_label_font)
    colour_button = Button(calculator, text="Colour", width=20, command=Run.change_colour)
    help_button = Button(calculator, text="Help", width=20, command=Run.help)
    find_button = Button(calculator, text="Calculate & Find Out", font=fontStyle,
                         command=Run.find)

    # Draw input units for calculated results (var2)
    area_units = Label(calculator, font=fontStyle)
    diameter_units = Label(calculator, font=fontStyle)
    circumference_units = Label(calculator, font=fontStyle)

    # Placeholder label (This was to fix a bug with font size on other labels)
    placeholder = Label(calculator, text="", font=fontStyle, width=0, height=0)
    placeholder.pack_forget()

    # Append Labels for colour and font setting
    labels.append(entry_title)
    labels.append(entry_box)
    labels.append(entry_box2)

    labels.append(entry_subtitle_r)
    labels.append(entry_subtitle_u)
    labels.append(entry_subtitle_area)
    labels.append(entry_subtitle_diameter)
    labels.append(entry_subtitle_circumference)

    labels.append(area_result)
    labels.append(diameter_result)
    labels.append(circumference_result)

    labels.append(increase_font)
    labels.append(decrease_font)
    labels.append(colour_button)
    labels.append(help_button)
    labels.append(find_button)

    labels.append(area_units)
    labels.append(diameter_units)
    labels.append(circumference_units)
    labels.append(placeholder)

    # Set error labels
    font_size_error = Label(calculator, text="Font size limit reached", font=bold, fg="red")
    input_range_error = Label(calculator, text="Please enter a number between -999 and 999",
                              font=bold, fg="red")
    unit_error = Label(calculator, text="Please enter 1 or 2 LETTER/S for the units",
                       font=bold, fg="red")

    # Placement of labels
    diagram.place(x=870, y=250)
    entry_title.place(x=240, y=100)
    entry_box.place(x=160, y=200)
    entry_box2.place(x=640, y=200)

    entry_subtitle_r.place(x=95, y=200)
    entry_subtitle_u.place(x=560, y=200)
    entry_subtitle_area.place(x=100, y=400)
    entry_subtitle_diameter.place(x=100, y=500)
    entry_subtitle_circumference.place(x=100, y=600)

    increase_font.place(x=1, y=1)
    decrease_font.place(x=1, y=40)
    colour_button.place(x=0, y=79)
    help_button.place(x=0, y=118)
    find_button.place(x=210, y=300)


if __name__ == '__main__':
    Run.set_resolution(window=Variables.calculator, div=1, div2=1)

    Variables.calculator.mainloop()
