# Imports
from tkinter import Tk, Menu, scrolledtext, filedialog, END

# Root for the main window
root = Tk(className=" Text Editor")

# Fullscreen by default
root.state('zoomed')

# Filename variable
filename = None

#--------- FUNCTIONS ----------#

# New text document function

def new_file():
    global filename

    text_area.delete('1.0', END)
    filename = None

# Open function
def open_file():
    global filename
    filename = filedialog.askopenfilename(title = "Please select a text file",
                                      defaultextension = ".txt",
                                      filetypes = [("All Files", "*.*"),
                                                   ("Text Files", "*.txt"),
                                                   ("Python Scripts", "*.py"),
                                                   ("Markdown Documents", "*.md"),
                                                   ("JavaScript Files", "*.js"),
                                                   ("HTML Documents", "*.html"),
                                                   ("CSS Documents", "*.css")])

    if filename:
        text_area.delete('1.0', END)
        with open(filename, "r") as f:
            text_area.insert('1.0', f.read())
        f.close()


# Save function
def save_file():

    global filename

    if filename:
        try:
            content = text_area.get('1.0', END + '-1c')
            with open(filename, "w") as f:
                f.write(content)

            f.close()
        except Exception as e:
            print(e)
    else:
        save_as_file()


def save_as_file():

    global filename
    try:
        new_file = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                            ("Text Files", "*.txt"),
                            ("Python Scripts", "*.py"),
                            ("Markdown Documents", "*.md"),
                            ("JavaScript Files", "*.js"),
                            ("HTML Documents", "*.html"),
                            ("CSS Documents", "*.css")])
        content = text_area.get('1.0', END + '-1c')
        with open(new_file, "w") as f:
            f.write(content)

        f.close()
        filename = new_file
    except Exception as e:
        print(e)


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
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open...", command = open_file)
file_menu.add_command(label="Save...", command = save_file)
file_menu.add_command(label="Save as...", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Help sub buttons
helpMenu.add_command(label="View Help")


# Main Loop
root.mainloop()