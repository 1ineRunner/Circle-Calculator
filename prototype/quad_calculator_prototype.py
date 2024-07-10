from tkinter import *
import tkinter.font as font


# Setup Class
class Setup(Tk):
    def __init__(self):
        super(Setup, self).__init__()
        self.title("Advanced Math Calculator")

    # Sets the resolution of the window according to the monitor
    @staticmethod
    def set_resolution(window, div, div2):
        width = int(window.winfo_screenwidth() / div)
        height = int(window.winfo_screenheight() / div2)
        result = str(width) + "x" + str(height)
        window.geometry(result.format(width / 2, height / 2))

    # Function for formulae used to calculate the answer
    @staticmethod
    def find():
        try:
            # Vars for number input
            number_input2 = Variables.var2.get()
            number_input = Variables.var.get()

            # If the input number is greater than 999 or less than -999 display an error
            if number_input > 999 or number_input < -999 or number_input2 > 999 or number_input < -999:
                Variables.input_range_error.pack()
            else:
                # Calculations to generate the results & round generated results to fourth decimal place
                sum_in_full = (number_input + number_input2)
                rounded_sum = str(round(sum_in_full, 4))
                Variables.sum_result.config(text="" + rounded_sum)
                Variables.sum_result.place(x=480, y=300)

                div_in_full = (number_input / number_input2)
                rounded_div = str(round(div_in_full, 4))
                Variables.div_result.config(text="" + rounded_div)
                Variables.div_result.place(x=480, y=400)

                subt_in_full = (number_input - number_input2)
                rounded_subt = str(round(subt_in_full, 4))
                Variables.subt_result.config(text="" + rounded_subt)
                Variables.subt_result.place(x=480, y=500)

                mult_in_full = (number_input * number_input2)
                rounded_mult = str(round(mult_in_full, 4))
                Variables.mult_result.config(text="" + rounded_mult)
                Variables.mult_result.place(x=480, y=600)

                # So forget any previous error:
                Variables.input_range_error.forget()
                Variables.division_error.forget()

        # Handle invalid input:
        except TclError:
            Variables.input_range_error.pack()
        except ZeroDivisionError:
            Variables.division_error.pack()


# Class for Setup of window instance, variables, fonts, and lists
class Variables:
    def __int__(self):
        super(Variables, self).__init__()

    # Placement of labels
    @staticmethod
    def placement():
        Variables.entry_title.place(x=240, y=50)
        Variables.entry_box.place(x=260, y=100)
        Variables.entry_box2.place(x=740, y=100)
        Variables.entry_box_num1.place(x=95, y=100)
        Variables.entry_box_num2.place(x=560, y=100)
        Variables.entry_subtitle_area.place(x=100, y=300)
        Variables.entry_subtitle_diameter.place(x=100, y=400)
        Variables.entry_subtitle_circumference.place(x=100, y=500)
        Variables.entry_subtitle_multiply.place(x=100, y=600)
        Variables.find_button.place(x=210, y=200)

    calculator = Setup()
    var = DoubleVar()
    var2 = DoubleVar()
    labels = []
    fontStyle = font.Font(family="Times_New_Roman", size=30)
    bold = font.Font(family="Times_New_Roman 10 bold", size=10)

    # Initialization of all labels
    # Draw Entry box title
    entry_title = Label(calculator, text="-Input some numbers-", font=fontStyle)

    # Draw Entry boxes (Radius)
    entry_box = Entry(calculator, textvariable=var, width=5, font=fontStyle)
    entry_box2 = Entry(calculator, textvariable=var2, width=5, font=fontStyle)

    # Draw Entry box subtitles (r= & u=)
    entry_box_num1 = Label(calculator, text="Num1 =", font=fontStyle)
    entry_box_num2 = Label(calculator, text="Num2 =", font=fontStyle)

    # Draw Area, Circumference & Diameter result subtitles (=)
    entry_subtitle_area = Label(calculator, text="Sum =", font=fontStyle)
    entry_subtitle_diameter = Label(calculator, text="Divide =", font=fontStyle)
    entry_subtitle_circumference = Label(calculator, text="Subtract =", font=fontStyle)
    entry_subtitle_multiply = Label(calculator, text="Multiply =", font=fontStyle)

    # Draw Area, Circumference & Diameter's results
    sum_result = Label(calculator, font=fontStyle)
    subt_result = Label(calculator, font=fontStyle)
    mult_result = Label(calculator, font=fontStyle)
    div_result = Label(calculator, font=fontStyle)

    # Draw clickable buttons (font increase/decrease, colour_button, help_button, find_button)

    find_button = Button(calculator, text="Calculate & Find Out", font=fontStyle,
                         command=Setup.find)

    # Draw input units for calculated results (var2)
    area_units = Label(calculator, font=fontStyle)
    diameter_units = Label(calculator, font=fontStyle)
    circumference_units = Label(calculator, font=fontStyle)

    # Placeholder label (This was to fix a bug with font size on other labels)
    placeholder = Label(calculator, text="", font=fontStyle, width=0, height=0)
    placeholder.pack_forget()

    # Set error labels
    font_size_error = Label(calculator, text="Font size limit reached", font=bold, fg="red")
    input_range_error = Label(calculator, text="Please enter number/s between -999 and 999",
                              font=bold, fg="red")
    division_error = Label(calculator, text="Please enter at least one number in each entry box",
                           font=bold, fg="red")


if __name__ == '__main__':
    Setup.set_resolution(window=Variables.calculator, div=1, div2=1)
    Variables.placement()
    Variables.calculator.mainloop()
