from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import requests

frame=Tk()
frame.title("Oasis Weather App ")
frame.config(bg="blue")
frame.geometry("600x600")

my_img= ImageTk.PhotoImage(Image.open("C:\\Users\\LENOVO\\Downloads\\oasis_infobyte_logo2.jpg"))
my_lable = Label(image=my_img, bg="dark blue")
my_lable.pack()
my_lable.place(x=20, y=20, height=140, width=110)
lable_name=Label(text=("Live Weather Information"), font=("Times New Roman",28,"bold",))
lable_name.place(x=130, y=20, height=140, width=437)
def fetch_weather(city):
    api_key = "123cc67517f820e74e2c1a9eebb0e338"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_data = {
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        display_weather(weather_data)
    else:
        output_label.config(text="City not found.")

def display_weather(data):
    output_label.config(text=f"Weather: {data['description']}\nTemperature: {data['temperature']}°C\nHumidity: {data['humidity']}%\nWind Speed: {data['wind_speed']} m/s")

input_label = tk.Label(frame, text="Enter City:", font=("Times New Roman",18, "bold"))
input_label.pack()
input_label.place(x=230, y=170, height=45, width=170)

city_entry = tk.Entry(frame, font=("Times New Roman", 20))
city_entry.pack()
city_entry.place(x=200, y=230, height=50, width=230)

fetch_button = tk.Button(frame, text="Get Weather", command=lambda: fetch_weather(city_entry.get()))
fetch_button.pack()
fetch_button.place(x=280, y=300)

output_label = tk.Label(frame, text="", font=("Times New Roman", 15))
output_label.pack()
output_label.place(x=175, y=350, height=120, width=280)


frame.mainloop()
