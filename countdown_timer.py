import time
import tkinter as tk
from tkinter import messagebox

# function to display the timer in a user-friendly format
def display_timer(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

# function to update the timer label
def update_timer():
    global seconds
    if seconds and not paused:
        timer_label.config(text=display_timer(seconds))
        seconds -= 1
        timer_label.after(1000, update_timer)
    elif not seconds:
        timer_label.config(text='Time is up!')
        pause_resume_button.config(state='disabled')
    else:
        timer_label.config(text=display_timer(seconds))

# function to start the timer
def start_timer():
    global seconds, paused
    try:
        seconds = int(entry.get())
        if seconds < 1:
            raise ValueError
        paused = False
        timer_label.config(text=display_timer(seconds))
        pause_resume_button.config(state='normal')
        reset_button.config(text='Stop', command=stop_timer, state='normal')
        start_button.config(state='disabled')
        entry.config(state='disabled')
        update_timer()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Only positive integer values accepted.")


# function to pause or resume the timer
def pause_resume_timer():
    global paused
    if not paused:
        paused = True
        pause_resume_button.config(text='Resume')
    else:
        paused = False
        pause_resume_button.config(text='Pause')
        update_timer()

# function to stop the timer
def stop_timer():
    global seconds, paused
    seconds = 0
    paused = False
    timer_label.config(text='00:00:00')
    start_button.config(state='normal')
    pause_resume_button.config(state='disabled', text='Pause')
    reset_button.config(text='Reset', command=reset_timer)
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.insert(0, 0)

# function to reset the timer
def reset_timer():
    global seconds, paused
    seconds = 0
    paused = False
    timer_label.config(text='00:00:00')
    start_button.config(state='normal')
    pause_resume_button.config(state='disabled', text='Pause')
    reset_button.config(text='Reset', command=reset_timer, state='disabled')
    entry.config(state='normal')
    entry.delete(0, tk.END)
    entry.insert(0, 0)

# main program
seconds = 0
paused = False

# create the window and widgets
root = tk.Tk()
root.title('Countdown Timer')
timer_label = tk.Label(root, font=('Arial', 24), text='00:00:00', borderwidth=1, relief='groove')
timer_label.pack(pady=20)
entry_label = tk.Label(root, font=('Arial', 12), text='Enter the number of seconds:')
entry_label.pack()
entry = tk.Entry(root, font=('Arial', 24), width=10)
entry.pack()
start_button = tk.Button(root, text='Start', font=('Arial', 16), command=start_timer, bg="green", fg="white")
start_button.pack(pady=20, side="left")
pause_resume_button = tk.Button(root, text='Pause', font=('Arial', 16), command=pause_resume_timer, state='disabled', bg="orange", fg="white")
pause_resume_button.pack(pady=10, side="left")
reset_button = tk.Button(root, text='Reset', font=('Arial', 16), command=reset_timer, state='disabled', bg="red", fg="white")
reset_button.pack(pady=10, side="left")

# start the main loop
root.mainloop()
