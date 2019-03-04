import tkinter as tk


class Menubar:

    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="Nuovo File",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Apri File",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Salva",
                                  command=parent.save)
        file_dropdown.add_command(label="Salva con Nome",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci",
                                  command=parent.master.destroy)

        menubar.add_cascade(label="File", menu=file_dropdown)



class PyText:

    def __init__(self, master):
        master.title("Untitled - PyText")
        master.geometry("1200x700")

        font_specs = ("ubuntu", 18)

        self.master = master

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def set_window_title(self):
        pass

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
