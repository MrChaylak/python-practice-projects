from tkinter import *


def btn_click():
    km_result_lbl.config(text=str(round(float(miles_entry.get()) * 1.60934, 2)))


window = Tk()
window.title("Miles to Km Convertor")
window.minsize(width=380, height=180)
window.config(padx=20, pady=20)

equal_to_lbl = Label(text="is equal to", font=("Arial", 20))
equal_to_lbl.grid(column=0, row=1)

miles_entry = Entry(width=7, font=("Arial", 20), justify='center')
miles_entry.grid(column=1, row=0)

km_result_lbl = Label(text="0", font=("Arial", 20))
km_result_lbl.grid(column=1, row=1)

calculate_button = Button(text="Calculate", font=("Arial", 18), command=btn_click)
calculate_button.grid(column=1, row=2)

miles_lbl = Label(text="Miles", font=("Arial", 20))
miles_lbl.grid(column=2, row=0)

km_lbl = Label(text="Km", font=("Arial", 20))
km_lbl.grid(column=2, row=1)

window.mainloop()
