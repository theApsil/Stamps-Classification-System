import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from data_processing import read_json_file

input_types = {
    'Логический': tk.Checkbutton,
    'Интервальный': tk.Entry,
    'Качественный': ttk.Combobox
}


def get_combobox_values(data_type: str, input_types) -> set:
    values = set()
    for dataset in input_types["Классы"].values():
        if isinstance(dataset, dict):
            values = values.union(set(dataset.get(data_type, {})))

    return values



class App:
    def __init__(self, root):
        self.root = root
        # setting title
        root.title("ИНТЕЛЛЕКТУАЛЬНАЯ СИСТЕМА ДЛЯ ОПРЕДЕЛЕНИЯ ТИПА ПОЧТОВЫХ МАРОК")
        # setting window size
        width = 700
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        GLabel_277 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=18, weight='bold')
        GLabel_277["font"] = ft
        GLabel_277["fg"] = "#333333"
        GLabel_277["justify"] = "center"
        GLabel_277["text"] = "Система классификации марок"
        GLabel_277.place(x=150, y=10, width=395, height=48)

        GButton_340 = tk.Button(root)
        GButton_340["activebackground"] = "#f7ed95"
        GButton_340["bg"] = "#ffebcd"
        ft = tkFont.Font(family='Arial', size=18)
        GButton_340["font"] = ft
        GButton_340["fg"] = "#000000"
        GButton_340["justify"] = "center"
        GButton_340["text"] = "Классификация марок"
        GButton_340.place(x=410, y=130, width=259, height=73)
        GButton_340["command"] = self.GButton_340_command

        Gbutton_341 = tk.Button(root)
        Gbutton_341["activebackground"] = "#b8b8b8"
        Gbutton_341["bg"] = "#b8b8b8"
        ft = tkFont.Font(family='Arial', size=18)
        Gbutton_341["font"] = ft
        Gbutton_341["fg"] = "#000000"
        Gbutton_341["justify"] = "center"
        Gbutton_341["text"] = "Выход"
        Gbutton_341.place(x=230, y=400, width=259, height=73)
        Gbutton_341["command"] = self.GButton_341_command

        GButton_161 = tk.Button(root)
        GButton_161["bg"] = "#ffebcd"
        ft = tkFont.Font(family='Arial', size=18)
        GButton_161["font"] = ft
        GButton_161["fg"] = "#000000"
        GButton_161["justify"] = "center"
        GButton_161["text"] = "Редактор базы знаний"
        GButton_161.place(x=410, y=240, width=261, height=74)
        GButton_161["command"] = self.GButton_161_command

        GLabel_282 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=14)
        GLabel_282["font"] = ft
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "left"
        GLabel_282["text"] = "1. Классификация марок. \nСистема классифицирует марку\nпо введённым значениям признаков"
        GLabel_282.place(x=30, y=120, width=370, height=108)

        GLabel_717 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=14)
        GLabel_717["font"] = ft
        GLabel_717["fg"] = "#333333"
        GLabel_717["justify"] = "left"
        GLabel_717[
            "text"] = "2. Редактор базы знаний. \nСистема позволяет вносить изм-\nенения в базу знаний.          "
        GLabel_717.place(x=15, y=240, width=370, height=108)

    def GButton_340_command(self):
        self.root.withdraw()

        new_root = tk.Tk()
        new_root.title("Определение класса марки по её признакам")
        width = 700
        height = 500
        screenwidth = new_root.winfo_screenwidth()
        screenheight = new_root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_root.geometry(alignstr)
        new_root.resizable(width=True, height=True)
        label = tk.Label(new_root, text="Определение класса марки по её признакам", font=("Arial", 20, 'bold'))
        label.pack(pady=20)

        def go_back():
            new_root.destroy()
            self.root.deiconify()

        back_button = tk.Button(new_root, command=go_back)
        back_button["bg"] = "#b8b8b8"
        ft = tkFont.Font(family='Arial', size=22)
        back_button["font"] = ft
        back_button["fg"] = "#000000"
        back_button["justify"] = "center"
        back_button["text"] = "Назад"
        back_button.place(x=230, y=400, width=259, height=73)

        json_data = read_json_file('data_knowledge.json')
        classes = json_data.get("Классы", {}).get("Стандартные")
        data_types = read_json_file('datatypes.json').get("Базовые типы данных")



        tree = ttk.Treeview(new_root, columns=("Data Type", "Value"))
        tree.heading("#0", text="Признак")
        tree.heading("Data Type", text="Тип данных")
        tree.heading("Value", text="Значение")

        for class_name, data in data_types.items():
            field = input_types[data]
            tree.insert('', 'end', text=class_name, values=(data, field()))

        tree.pack(expand=False, fill="both")
        new_root.mainloop()

    def GButton_341_command(self):
        exit()

    def GButton_161_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
