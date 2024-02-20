# Christine Hampton 
# 2/20/2024
# GUI final project- source code
# This GUI application is a calendar for your desktop. 

#Importing tkinter module
from tkinter import*
#importing calendar module
import calendar

#function to show calendar of the given year 
def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("calendar for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop

    #Driver code 
    if '_name_'=='_main_':
     new = Tk()
    new.config(background = 'grey')
    new.title("Calendar")
    new.geometry("250x140")
    cal = Label( new, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year= Label(new, text="Enter year", bg='darkgrey')
    year_field=Entry(new)
    button = Button(new, text='show Calendar',
                    fg='black', bg='blue', command=showCalendar)
    
#putting widgets in postion
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    exit.grid(row=6, column=1)
    new.mainloop

#output