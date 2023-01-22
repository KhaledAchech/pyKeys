import tkinter as tk
from tkinter import ttk
from pyKeys import ShortcutsManager

def set_shortcut_command():
    character = character_entry.get()
    key_combination = key_combination_entry.get()
    ShortcutsManager().set_shortcut(character, key_combination)
    update_listbox()

def delete_shortcut_command():
    key_combination = listbox.get(listbox.curselection())
    ShortcutsManager().delete_shortcut(key_combination)
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for key_combination in ShortcutsManager().view_shortcuts():
        listbox.insert(tk.END, key_combination)

root = tk.Tk()

character_label = tk.Label(root, text="Character:")
character_label.pack()

character_entry = tk.Entry(root)
character_entry.pack()

key_combination_label = tk.Label(root, text="Key combination:")
key_combination_label.pack()

key_combination_entry = tk.Entry(root)
key_combination_entry.pack()

set_button = ttk.Button(root, text="Set", command=set_shortcut_command)
set_button.pack()

delete_button = ttk.Button(root, text="Delete", command=delete_shortcut_command)
delete_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

update_listbox()

root.mainloop()