⏰ Digital Clock – Python Tkinter

A simple digital clock application created using Python and Tkinter. This project displays the current system time in a modern digital style and updates every second. It is a beginner-friendly GUI project and a great way to get started with desktop applications in Python.

🚀 Features

Real-time clock display

Updates every second

Clean and simple graphical interface

No external libraries required

Works on Windows, macOS, and Linux

🛠️ Technologies Used

Python 3

Tkinter (built-in Python GUI library)

📦 Installation & Setup
1️⃣ Check Python Installation

Make sure Python is installed:

python --version


If Python is not installed, download it from:
https://www.python.org/downloads/

2️⃣ Clone or Download this Repository
git clone https://github.com/your-username/digital-clock.git


or simply download the ZIP file and extract it.

3️⃣ Navigate to the Project Folder
cd digital-clock

4️⃣ Run the Application
python clock.py

📁 Project Structure
digital-clock/
│
├── clock.py      # Main application source code
└── README.md     # Project documentation

💻 Source Code
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x150")
window.resizable(False, False)

label = tk.Label(window, font=("Helvetica", 50), fg="cyan", bg="black")
label.pack(fill="both", expand=True)

update_time()
window.mainloop()

🌟 Future Enhancements

Possible improvements:

Display date

Add alarm function

Add stopwatch or timer

Theme customization

Neon LED styled digits
