# importing all module
from tkinter import *
from tkinter.messagebox import showerror
import requests

# variable define 
window_height = 500
window_width = 600

# function define for get weather 


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temperature = round((temp-32)*5/9, 2)
        final_str = 'City: %s \nConditions: %s \nTemperature: %s (°F)  || %s (°C)' % (name, desc, temp, temperature)
    except Exception as e:
        exception = str(e)
        final_str = 'There was a problem retrieving that information'
        showerror("Error", message=exception+final_str)

    return final_str


def get_weather(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    try:
        response = requests.get(url, params=params)
        weather = response.json()

        result_label['text'] = format_response(weather)

    except Exception as e:
        exception = str(e)
        showerror("Error", message=exception + ". Please, check your internet connection.")

# build gui


root = Tk()
root.title("Weather Checker")           # window title
# bg setup
background = Canvas(root, height=window_height, width=window_width)
background.pack()
background_image = PhotoImage(file="landscape.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
# frame for entry and button
frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# entry box fro getting city name 
entry = Entry(frame, font=40)
entry.place(relheight=1, relwidth=0.65)
# button for weather checking
get_weather_button = Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
get_weather_button.place(relx=0.7, relheight=1, relwidth=0.3)
# frame for showing weather detail
lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
# result_label for displaying the detail
result_label = Label(lower_frame, bg="white")
result_label.place(relwidth=1, relheight=1)
# for window make longer
root.mainloop()
# end code enjoying this software :)
