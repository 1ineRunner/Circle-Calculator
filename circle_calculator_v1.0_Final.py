from tkinter import *
import tkinter.font as font
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
        try:
            full_hex = str(colorchooser.askcolor(title="Pick a colour"))
            rm_unicode = str(full_hex.replace("\')", ""))
            hue = str(rm_unicode.split('#')[1].lstrip().split(' ')[0])
            print(f"Current text colour: #{hue}")
            for label in Variables.labels:
                label['fg'] = '#' + hue

        except TclError:
            print("Did not match dialogue colour due to PID mismatch")

        except IndexError:
            print("Cannot change dialogue colour due to window source")

    # Increase and decrease label font size
    @staticmethod
    def increase_label_font():
        font_size = Variables.fontStyle['size']
        if font_size > 34:
            Variables.zoom_error.pack(side="top")
        else:
            Variables.labels[19]['font'] = font_size + 2
            Variables.fontStyle.configure(size=font_size + 2)
            print("Current font size: ", font_size)
            Variables.zoom_error.forget()

    @staticmethod
    def decrease_label_font():
        font_size = Variables.fontStyle['size']
        if font_size < 20:
            Variables.zoom_error.pack(side="top")
        else:
            Variables.labels[19]['font'] = font_size - 2
            Variables.fontStyle.configure(size=font_size - 2)
            print("Current font size: ", font_size)
            Variables.zoom_error.forget()

    # Function for formulae used to calculate the answer
    @staticmethod
    def find():
        try:
            # Vars for number input and unit input
            radius = Variables.radius.get()
            units = Variables.units.get()

            # Input number is > 999 or < -999 display an error
            if radius > 999 or radius < -999:
                Variables.input_error.pack()
            else:
                # Calculations & Equations
                a_in_full = (3.14 * (Variables.radius.get() ** 2))
                a_rounded = str(round(a_in_full, 4))
                Variables.a_result.config(text=f"{a_rounded}")
                Variables.a_result.place(x=400, y=400)

                d_in_full = (2 * Variables.radius.get())
                d_rounded = str(round(d_in_full, 4))
                Variables.d_result.config(text=f"{d_rounded}")
                Variables.d_result.place(x=400, y=500)

                c_in_full = (2 * 3.14 * Variables.radius.get())
                c_rounded = str(round(c_in_full, 4))
                Variables.c_result.config(text=f"{c_rounded}")
                Variables.c_result.place(x=400, y=600)

                # Units must be alphabetical , < 3 characters or empty
                if units.isalpha() and len(units) < 3 or units == "":
                    Variables.a_units.forget()
                    Variables.d_units.forget()
                    Variables.c_units.forget()

                    Variables.a_units.config(text=f"{units}²")
                    Variables.a_units.place(x=520, y=400)

                    Variables.d_units.config(text=f"{units}")
                    Variables.d_units.place(x=520, y=600)

                    Variables.c_units.config(text=f"{units}")
                    Variables.c_units.place(x=520, y=500)

                    # So forget any previous error:
                    Variables.unit_error.forget()

                else:
                    # It's an invalid string to use as units:
                    Variables.unit_error.pack()
                    Variables.a_units.forget()
                    Variables.d_units.forget()
                    Variables.c_units.forget()

                # So forget any previous error:
                Variables.input_error.forget()

        # Handle invalid input:
        except TclError:
            Variables.input_error.pack()


class Help(Tk):

    def __init__(self):
        super(Help, self).__init__()
        self.title("Help Dialogue")

    # Function Help dialogue
    @staticmethod
    def help():
        dia = Toplevel(Variables.app)
        Run.set_resolution(window=dia, div=2, div2=2)

        help_title = Label(dia, text="Help Dialogue", font=Variables.fontStyle)
        aid_1 = Label(dia, text="1. Use the \"Zoom\" + and - icons to "
                                "increase and decrease the size of the "
                                "font on the page")
        aid_2 = Label(dia, text="2. Use the \"Colour\" button to select "
                                "a colour for the text using the built-in "
                                "colour picker")
        aid_3 = Label(dia, text="3. Type a number to calculate with into "
                                "the first entry bar under the \"-Input a "
                                "radius-\" title")
        aid_4 = Label(dia, text="4. Optionally, you can type at most two "
                                "letters in the second entry bar to act "
                                "as units")
        aid_5 = Label(dia, text="5. When you are ready to calculate the "
                                "result, click the button \"Calculate & "
                                "Find Out\"")

        # Append labels for colour and font setting in help dialogue
        Variables.labels.append(help_title)
        Variables.labels.append(aid_1)
        Variables.labels.append(aid_2)
        Variables.labels.append(aid_3)
        Variables.labels.append(aid_4)
        Variables.labels.append(aid_5)

        # Placement of labels in help dialogue
        help_title.pack()
        aid_1.pack()
        aid_2.pack()
        aid_3.pack()
        aid_4.pack()
        aid_5.pack()


# Class for Setup of window instance, variables, fonts, and lists
class Variables:
    def __int__(self):
        super(Variables, self).__init__()

    app = Run()
    radius = DoubleVar()
    units = StringVar()
    labels = []
    circle = PhotoImage(file="resources/circle.png")
    fontStyle = font.Font(family="Times_New_Roman", size=30)
    bold = font.Font(family="Times_New_Roman 10 bold", size=10)
    diagram = Label(app, image=circle)

    # Initialization of all labels
    # Draw Entry box title
    entry_title = Label(app, text="-Input a radius-", font=fontStyle)

    # Draw Entry boxes (Radius & Units)
    entry_box = Entry(app, textvariable=radius, width=15, font=fontStyle)
    entry_box2 = Entry(app, textvariable=units, width=5, font=fontStyle)

    # Draw Entry box subtitles (r= & u=)
    r_subtitle = Label(app, text="radius =", font=fontStyle)
    u_subtitle = Label(app, text="units =", font=fontStyle)

    # Draw Area, Circumference & Diameter result subtitles (=)
    a_subtitle = Label(app, text="Area =", font=fontStyle)
    d_subtitle = Label(app, text="Diameter =", font=fontStyle)
    c_subtitle = Label(app, text="Circumference =", font=fontStyle)

    # Draw Area, Circumference & Diameter's results
    a_result = Label(app, font=fontStyle)
    d_result = Label(app, font=fontStyle)
    c_result = Label(app, font=fontStyle)

    # Draw clickable buttons
    increase_font = Button(app, text="Zoom In +", width=20,
                           command=Run.increase_label_font)
    decrease_font = Button(app, text="Zoom Out -", width=20,
                           command=Run.decrease_label_font)
    color_btn = Button(app, text="Colour", width=20, command=Run.change_colour)
    help_btn = Button(app, text="Help", width=20, command=Help.help)
    find_btn = Button(app, text="Calculate", font=fontStyle,
                      command=Run.find)

    # Draw input units for calculated results (var2)
    a_units = Label(app, font=fontStyle)
    d_units = Label(app, font=fontStyle)
    c_units = Label(app, font=fontStyle)

    # Placeholder label (This was to fix a bug with font size on other labels)
    placeholder = Label(app, text="", font=fontStyle, width=0, height=0)
    placeholder.pack_forget()

    # Append Labels for colour and font setting
    labels.append(entry_title)
    labels.append(entry_box)
    labels.append(entry_box2)

    labels.append(r_subtitle)
    labels.append(u_subtitle)
    labels.append(a_subtitle)
    labels.append(d_subtitle)
    labels.append(c_subtitle)

    labels.append(a_result)
    labels.append(d_result)
    labels.append(c_result)

    labels.append(increase_font)
    labels.append(decrease_font)
    labels.append(color_btn)
    labels.append(help_btn)
    labels.append(find_btn)

    labels.append(a_units)
    labels.append(d_units)
    labels.append(c_units)
    labels.append(placeholder)

    # Set error labels
    zoom_error = Label(app, text="Font size limit "
                                 "reached", font=bold, fg="red")
    input_error = Label(app, text="Please enter a number between -999 and 999",
                        font=bold, fg="red")
    unit_error = Label(app, text="Please enter 1 or 2 LETTER/S for the units",
                       font=bold, fg="red")

    # Placement of labels
    diagram.pack(side="right", anchor=S)
    entry_title.place(x=280, y=100)
    entry_box.place(x=200, y=200)
    entry_box2.place(x=700, y=200)

    r_subtitle.place(x=40, y=200)
    u_subtitle.place(x=560, y=200)
    a_subtitle.place(x=10, y=400)
    d_subtitle.place(x=10, y=500)
    c_subtitle.place(x=10, y=600)

    increase_font.place(x=1, y=1)
    decrease_font.place(x=1, y=40)
    color_btn.place(x=0, y=79)
    help_btn.place(x=0, y=118)
    find_btn.place(x=200, y=300)


if __name__ == '__main__':
    Run.set_resolution(window=Variables.app, div=1, div2=1)
    Variables.app.mainloop()
