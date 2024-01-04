# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:52:32 2024

@author: jtazioli
"""

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(row=1,column=3)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=2,column=3)

verb_label = Label(text="is equal to ")
verb_label.grid(row=2,column=1)

km_output_label = Label(text="0")
km_output_label.grid(row=2,column=2)


#Buttons
def miles_to_km():
    miles = float(miles_entry.get())
    km = str(round( miles * 1.60934,2))
    km_output_label.config(text=km)

#calls action() when pressed
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=3,column=2)

#Entries
miles_entry = Entry(width=8)
#Add some text to begin with
miles_entry.insert(END, string="0")
miles_entry.grid(row=1,column=2)



window.mainloop()