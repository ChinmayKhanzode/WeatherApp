import tkinter as tk
from tkinter import ttk
import manage
import threading

def get_data():
    entered_text = input_entry.get()
    result = manage.main(entered_text)
    result_label.config(text=result)
    progress_bar.stop()
    progress_bar.grid_remove()

def display_input():
    progress_bar.grid()
    progress_bar.start()
    threading.Thread(target=get_data).start()
    

root = tk.Tk()
root.title("Weather Information App")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

input_entry = ttk.Entry(main_frame, width=30)
input_entry.grid(row=0, column=0, padx=(0, 10))

submit_button = ttk.Button(main_frame, text="Submit", command=display_input)
submit_button.grid(row=0, column=1)

result_label = ttk.Label(main_frame, text="")
result_label.grid(row=1, column=0, columnspan=2, pady=(10, 0))

progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
progress_bar.grid(row=2, column=0, columnspan=2, pady=(10, 0))
progress_bar.grid_remove()

root.mainloop()
