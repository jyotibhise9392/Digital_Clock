import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: HH:MM:SS (24-hour)
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every second

# Creating GUI window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x150")
window.resizable(False, False)

label = tk.Label(window, font=("Helvetica", 50), fg="cyan", bg="black")
label.pack(fill="both", expand=True)

update_time()  # Start clock

window.mainloop()
