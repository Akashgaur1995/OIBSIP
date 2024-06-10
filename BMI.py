from tkinter import *
import tkinter as tk

win=tk.Tk()
win.title("BMI calculator")
win.config(background="violet")
win.geometry("500x500")


title = tk.Label(win, text="Know Your BMI",background="violet", foreground="dark red", font=("Arial",25,"bold"))
title.pack()

height=tk.Label(win, text="Enter Height(in cm.)", font=("Times New Roman", 14, 'bold'))
height.pack() 
height.place(x=90, y=70, height=40, width=170)

height_input=tk.Entry(win,font=("Times New Roman", 14, 'bold') )
height_input.pack()
height_input.place(x=280, y=70, height=40, width=120)

weight=tk.Label(win, text="Enter weight(in kg.)", font=("Times New Roman", 14, 'bold'))
weight.pack() 
weight.place(x=90, y=120, height=40, width=170)

weight_input=tk.Entry(win,font=("Times New Roman", 14, 'bold'))
weight_input.pack()
weight_input.place(x=280, y=120, height=40, width=120)

def calculate_bmi():
    height = float(height_input.get()) / 100  
    weight = float(weight_input.get())
    bmi = weight / (height * height)
    output_lable.config(text="Your BMI is {:.2f}".format(bmi))


calculate_button=tk.Button(win, text="Calculate", font=("Times New Roman", 15, "bold"), command=calculate_bmi)
calculate_button.pack()
calculate_button.place(x=200, y=180, height=35, width=100)

output_lable=tk.Label(win,text="", font=("Times New Roman", 15 , 'bold'))
output_lable.pack()
output_lable.place(x=160, y=240, height=50, width=180)

details= tk.Label(win, text="""To convert a height from feet to centimeters, you can use the following steps:\n Convert feet to inches: 1 feet = 12 inches
Convert inches to centimeters: inches * 2.54 centimeters
BMI below 18.5: Underweight
BMI 18.5 to 24.9: Normal weight
BMI 25 to 29.9: Overweight
BMI 30 and above: Obese""", font=("times new roman", 12), bg="yellow")
details.pack()
details.place(x=20, y=300)




win.mainloop()

