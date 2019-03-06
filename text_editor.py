# Imports
from tkinter import Tk, Menu, scrolledtext, filedialog, END

# Root for the main window
root = Tk(className=" Text Editor")

# Fullscreen by default
root.state('zoomed')

# Filename variable
filename = None

#--------- FUNCTIONS ----------#

# Open function
def open_file():
    file = filedialog.askopenfile(parent = root, mode="rb", title = "Please select a text file")

    if file != None:
        file_contents = file.read()
        text_area.delete('1.0', END)
        text_area.insert('1.0', file_contents)
        file.close()

def save_file():
    global filename

    if not filename:
        file = filedialog.asksaveasfile(mode = "w", defaultextension  = ".txt")
        data = text_area.get("1.0", END +'-1c')
        file.write(data)
        file.close()
        filename = file
    else:
        file = open(filename, "w")
        data = text_area.get("1.0", END + '-1c')
        file.write(data)
        file.close()



# Quit function
def quit():
    root.quit()
    root.destroy()
    exit()

# Creates text_area to type in
text_area = scrolledtext.ScrolledText(root, width="1920", height="1080")
text_area.pack()

# Menu options
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
editMenu = Menu(menu_bar, tearoff = 0)
helpMenu = Menu(menu_bar, tearoff = 0)

# Menu parent buttons
menu_bar.add_cascade(label = "File", menu = file_menu)
menu_bar.add_cascade(label = "Edit", menu = editMenu)
menu_bar.add_cascade(label = "Help", menu = helpMenu)

# File sub buttons
file_menu.add_command(label = "New")
file_menu.add_command(label = "Open...", command = open_file)
file_menu.add_command(label="Save...", command = save_file)
file_menu.add_command(label="Save as...")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Help sub buttons
helpMenu.add_command(label="View Help")


# Main Loop
root.mainloop()