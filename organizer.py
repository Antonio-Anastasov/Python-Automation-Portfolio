import os
import shutil

print("--- Стартиране на организатора ---")

# ВАЖНО: Тук трябва да сложиш пътя до твоята папка на лаптопа.
# Пример: r"C:\Users\ТвоетоИме\Desktop\TestAutomation"
folder_path = r"C:\Users\ADMIN\Desktop\TestAutomation"

# Речник с правилата
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".pdf": "Documents"
}

# Взимаме всички файлове от папката
files = os.listdir(folder_path)

for file in files:
    # Разделяме името от разширението
    filename, extension = os.path.splitext(file)

    # 1. Проверяваме дали разширението е в нашия списък с правила
    if extension in extensions:

        # 2. Взимаме името на новата папка (напр. "Images" или "Documents")
        folder_name = extensions[extension]
        new_folder_path = os.path.join(folder_path, folder_name)

        # 3. Проверяваме дали тази папка вече съществува. Ако не - я създаваме.
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        # 4. Подготвяме точните адреси и местим самия файл
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(new_folder_path, file)

        shutil.move(old_file_path, new_file_path)
        print(f"Файлът {file} е преместен успешно в папка {folder_name}!")

print("Готово! Провери си папката.")