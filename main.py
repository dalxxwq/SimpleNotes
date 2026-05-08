filename = "notes.txt"

# Запис у файл
def add_text():
    with open(filename, "a", encoding="utf-8") as file:
        text = input("Що запишемо у файл? ")
        file.write(text + "\n")

# Читання з файлу
def read_file():
    print("\nОсь що вже є у файлі:")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

while True:  # Нескінченний цикл
    answer = input("Wanna add some text or just read it? (add/read/exit): ").lower()

    if answer == "add":
        add_text()
        # Тут цикл почнеться спочатку, можна знову вибрати дію
    elif answer == "read":
        read_file()
    elif answer == "exit":
        print("Goodbye!")
        break  # Вихід з циклу і завершення програми
    else:
        print("❌ Invalid input! Please type only 'add', 'read' or 'exit'.")
