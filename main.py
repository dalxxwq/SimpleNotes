filename = "notes.txt"

# Запис у файл
with open(filename, "a", encoding="utf-8") as file:
    text = input("Що запишемо у файл? ")
    file.write(text + "\n")

# Читання з файлу
print("\nОсь що вже є у файлі:")
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
