# -----Библиотеки---------------
from tkinter import *
from tkinter import filedialog

# ------Базовые настройки----------------------------------------------
window = Tk()
window.geometry("400x700")
window.title("Делитель книг by StephanBro_YT")
window.resizable(False, False)


# -------------Обработка ctrl+v, ctrl+c на русской раскладке----------
def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


window.bind_all("<Key>", _onKeyRelease, "+")


# -------------Команды----------------------------------
def add():
    global tst
    text = "123"
    # .insert(END, text)
    # .delete(0, END)
    # .delete(0, END)


def clear():
    book.delete(0.0, END)
    podelenoe.delete(0.0, END)
    nazvanie.delete(0.0, END)


def load():
    file = filedialog.askopenfile(
        title="Load", filetypes=(("txt", "*.txt"), ("all", "*.*"))
    )
    text = file.read()
    clear()
    book.insert(END, text)


def save():
    text = podelenoe.get(0.0, END)
    file = filedialog.asksaveasfilename(
        defaultextension=".stendhal",
        filetypes=[("Stendhal files", "*.stendhal"), ("All files", "*.*")],
    )
    if file:
        with open(file, "w") as file:
            file.write(text)


def split_text():
    input_text = book.get("1.0", END)
    title = nazvanie.get("1.0", END).strip()
    author = "StephanBro_YT program"
    page_size = 250

    # Разбиваем текст на страницы по 200 символов
    pages = [
        input_text[i : i + page_size] for i in range(0, len(input_text), page_size)
    ]

    output_text = f"title: {title}\nauthor: {author}\npages:\n"
    for i, page_content in enumerate(pages):
        output_text += f"#- {page_content}\n"

    podelenoe_lines = output_text.split("\n")[:-2]
    output_text_updated = "\n".join(podelenoe_lines)

    podelenoe.delete(0.0, END)
    podelenoe.insert(END, output_text_updated)
    # ----------------------------------
    input_text = book.get("1.0", END)

    # Разбиваем текст на страницы по 200 символов
    pages = [
        input_text[i : i + page_size] for i in range(0, len(input_text), page_size)
    ]

    output_text = f""
    for i, page_content in enumerate(pages):
        output_text += f"\n{page_content}\n"

    podelenoe_lines = output_text.split("\n")[:-2]
    output_text_updated = "\n".join(podelenoe_lines)

    podelenoe_nostelh.delete(0.0, END)
    podelenoe_nostelh.insert(END, output_text_updated)


# ------------Виджеты-----------------------------------------
book = Text(width=45, height=10)
lod = Button(text="Загрузить команду из .txt", command=load)
nazvanie = Text(width=15, height=1)
obrabotat = Button(text="Обработать", command=split_text)
savecod = Button(text="Экспорт", command=save)
delbut = Button(text="Очистить все", command=clear)
podelenoe = Text(width=45, height=10)
nazvanietext = Label(text="Имя файла:")
podelenoe_nostelh = Text(width=45, height=10)
podelenoe_stelhtext = Label(text="Для .stendhal:")
podelenoe_nostelhtext = Label(text="Для ручной вставки:")

# -----------------Расположение виджетов-------------------------
book.place(x=10, y=10)
lod.place(x=10, y=180)
savecod.place(x=170, y=180)
obrabotat.place(x=299, y=180)
nazvanie.place(x=80, y=250)
delbut.place(x=294, y=250)
podelenoe.place(x=10, y=310)
nazvanietext.place(x=10, y=250)
podelenoe_nostelh.place(x=10, y=510)
podelenoe_nostelhtext.place(x=10, y=480)
podelenoe_stelhtext.place(x=10, y=285)


window.mainloop()
