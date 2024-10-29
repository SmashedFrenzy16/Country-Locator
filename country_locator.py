from geopy.geocoders import Nominatim
from tkinter import *

root = Tk()

root.title("Country Locator")

label = Label(root, text="Country Locator", font=("Arial", 24))
label.pack()

blank_label = Label(root, text="")
blank_label.pack()

place_entry = Entry(root, width=100, borderwidth=5)
place_entry.pack()

place_entry.insert(0, "Enter in the name of the place you want to locate")

root.mainloop()
