from tkinter import *
from tkinter import messagebox
import threading
import time
import pygame.mixer as mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time = user_input.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error Message", "Please Enter a Value")
    else:
        threading.Thread(target=wait_and_play, args=(alarm_time,)).start()

def wait_and_play(alarm_time):
    counter = 0  # Initialize the counter variable
    while counter < 15:  # Loop 15 times
        current_time = time.strftime("%H:%M")
        if alarm_time == current_time:
            play_music()
            counter += 1  # Increment the counter
        time.sleep(1)

def play_music():
    mixer.init()
    mixer.music.load('ALM.mp3')
    mixer.music.play()

    stop_button.config(state=NORMAL)  # Enable the Stop button when alarm starts

    snooze_button.config(state=NORMAL)  # Enable the Snooze button when alarm starts

def stop_alarm():
    mixer.music.stop()

    stop_button.config(state=DISABLED)  # Disable the Stop button after stopping the alarm

    snooze_button.config(state=DISABLED)  # Disable the Snooze button after stopping the alarm

def snooze_alarm():
    snooze_time = 60  # Snooze for 30 seconds
    time.sleep(snooze_time)
    play_music()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update time every second (1000 milliseconds)

root = Tk()
root.title("Alarm Clock")
root.geometry("900x700")

# Create a custom font for the title
title_font = ("Arial", 36, "bold")

canvas = Canvas(root, width=600, height=380)
image = ImageTk.PhotoImage(Image.open("alm.png"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

header = Frame(root, bg="#4287f5")  # Set a custom background color using a hexadecimal color code
box1 = Frame(root, bg="#ebebeb")  # Set a custom background color
box1.place(x=350, y=450, width=600, height=80)
box2 = Frame(root, bg="#ebebeb")  # Set a custom background color
box2.place(x=350, y=550, width=200, height=50)


# Time taken by User as Input
user_input = Entry(box1, font=('Arial Narrow', 30), width=15)
user_input.grid(row=0, column=0, padx=10)
user_input.config(bg="white")  # Set background color for the entry widget

# Set Alarm Button
start_button = Button(box2, text="Set Alarm", font=('Arial Narrow', 16, 'bold'), command=alarm)
start_button.grid(row=0, column=0)
start_button.config(bg="#32cd32", fg="white")  # Set custom background and foreground (text) colors

# Stop Alarm Button
stop_button = Button(box2, text="Stop", font=('Arial Narrow', 10), command=stop_alarm)
stop_button.grid(row=0, column=1, padx=10)
stop_button.config(state=DISABLED)  # Initially disabled

# Snooze Alarm Button
snooze_button = Button(box2, text="Snooze", font=('Arial Narrow', 10), command=snooze_alarm)
snooze_button.grid(row=0, column=2)
snooze_button.config(state=DISABLED)  # Initially disabled



# Create a label to display current time
time_label = Label(root, text="", font=('Arial', 24))
time_label.pack(pady=20)

header.pack(fill=X)

# Update time every second
update_time()

root.mainloop()