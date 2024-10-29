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

def locate():

    locator = Nominatim(user_agent="myGeocoder")
    place = locator.geocode(place_entry.get())

    output = Label(root, text="")
    output.pack()

    if place:
        output.config(text=f"Location: {place.address}\nLatitude: {place.latitude}, Longitude: {place.longitude}")
    else:
        output.config(text="Location not found")
execute_button = Button(root, text="Locate", command=locate)
execute_button.pack()

root.mainloop()
