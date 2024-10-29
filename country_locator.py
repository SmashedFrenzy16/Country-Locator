from geopy.geocoders import Nominatim
from tkinter import *

root = Tk()

root.title("Country Locator")

label = Label(root, text="Country Locator", font=("Arial", 24))
label.pack()

blank_label = Label(root, text="")
blank_label.pack()

root.mainloop()
