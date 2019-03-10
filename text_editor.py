# Imports
from tkinter import Tk, Menu, scrolledtext, filedialog, END, Frame, Text, PhotoImage, Toplevel, Label, Checkbutton, Entry, IntVar

# Root for the main window
root = Tk(className=" Text Editor")

# Fullscreen by default
root.state('zoomed')

# Variables
filename = None

# Preferences
show_line_num = True
show_cursor_location = True
highlight_line = True
theme = "Default"

# Images
save_icon = PhotoImage(file = "icons/save_icon.png")

# --------- TOOLBAR ------------ #

toolbar = Frame(root, height=30, bg="light gray")
toolbar.pack(expand="1", fill="x")

# --------- LINE NUMBER BAR ---- #

line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0, background="light yellow", state="disabled", wrap="none")
line_number_bar.pack(side="left", fill="y")

# --------- TEXT AREA ---------- #

text_area = scrolledtext.ScrolledText(root, width="1920", height="1080")
text_area.pack()


# --------- FUNCTIONS ---------- #

# New text document function
def new_file():
    global filename

    text_area.delete('1.0', END)
    filename = None


# Open function
def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Please select a text file", defaultextension=".txt")

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
        new_file = filedialog.asksaveasfilename(defaultextension=".txt")
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

# Undo Function
def undo():
    text_area.event_generate("<<Undo>>")
    return "break"

# Redo function
def redo(event = None):
    text_area.event_generate("<<Redo>>")
    return "break"

# Cut function
def cut():
    text_area.event_generate("<<Cut>>")
    return "break"

# Copy function
def copy():
    text_area.event_generate("<<Copy>>")
    return "break"

# Paste Function
def paste():
    text_area.event_generate("<<Paste>>")
    return "break"

# Select all function
def select_all(event = None):
    text_area.tag_add("sel", "1.0", END + "-1c")
    return "break"

# Find function
def find(event = None):
    search_popup = Toplevel(root)
    search_popup.title("Find text")
    search_popup.transient(root)
    search_popup.resizable(False, False)
    Label(search_popup, text = "Find All:").grid(row = 0, column = 0, sticky = "e")
    search_entry = Entry(search_popup, width = 25).grid(row = 0, column = 1, padx = 2, pady = 2, sticky = "we")
    search_entry.focus_set()
    ignore_case = IntVar
    Checkbutton(search_popup, text="Ignore Case", variable = ignore_case).grid(row = 1, column = 1, sticky = "e", padx = 2, pady = 2)

# Menu options
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)
themes_menu = Menu(view_menu, tearoff=0)

# Menu parent buttons
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="View", menu=view_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# File sub buttons
file_menu.add_command(label="New", command=new_file, accelerator="         Ctrl + N", compound="left")
file_menu.add_command(label="Open...", command=open_file, accelerator="         Ctrl + O", compound="left")
file_menu.add_command(label="Save...", command=save_file, accelerator="         Ctrl + S", compound="left", image = save_icon )
file_menu.add_command(label="Save as...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Edit sub buttons
edit_menu.add_command(label = "Undo", command = undo, accelerator = "         Ctrl + Z", compound = "left")
edit_menu.add_command(label = "Redo", command = redo, accelerator = "         Ctrl + Y", compound = "left")
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command = cut, accelerator = "         Ctrl + X", compound = "left")
edit_menu.add_command(label = "Copy", command = copy, accelerator = "         Ctrl + C", compound = "left")
edit_menu.add_command(label = "Paste", command = paste, accelerator = "         Ctrl + V", compound = "left")
edit_menu.add_separator()
edit_menu.add_command(label = "Find", command = find, accelerator = "         Ctrl + F", compound = "left")
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = select_all, underline = 7, accelerator = "         Ctrl + A", compound = "left")

# View sub buttons
view_menu.add_checkbutton(label="Show line number", variable=show_line_num)
view_menu.add_checkbutton(label="Show cursor location", variable=show_cursor_location)
view_menu.add_checkbutton(label="Highlight current line", variable=highlight_line)
view_menu.add_cascade(label="Themes", menu=themes_menu)

themes_menu.add_radiobutton(label="Default", variable=theme)
themes_menu.add_radiobutton(label="Aquamarine", variable=theme)
themes_menu.add_radiobutton(label="Bold Beige", variable=theme)
themes_menu.add_radiobutton(label="Cobalt Blue", variable=theme)
themes_menu.add_radiobutton(label="Dark Mode", variable=theme)
themes_menu.add_radiobutton(label="Olive Green", variable=theme)


# Help sub buttons
help_menu.add_command(label="View Help")

# Fixing binding issues
text_area.bind("Control-y", redo)
text_area.bind("Control-Y", redo)
text_area.bind("Control-a", select_all)
text_area.bind("Control-A", select_all)

# Main Loop
root.mainloop()
