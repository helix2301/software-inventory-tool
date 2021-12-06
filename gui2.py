import tkinter as tk


parent = tk.Tk()
parent.geometry("300x200")
parent.wm_title("Software Inventory")
frame = tk.Frame(parent)
frame.pack()

label = tk.Label(frame, wraplength=100, height=10, width=50, bg="white", text="Once you have clicked on *Inventory* click open to view list of all software.")
label.pack()

text_disp= tk.Button(frame,
                   text="Intentory",
                   command="write_text"
                   )

text_disp.pack(side=tk.LEFT)

text_disp= tk.Button(frame,
                   text="View List",
                   command="write_text"
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="Exit",
                   fg="green",
                   command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()
