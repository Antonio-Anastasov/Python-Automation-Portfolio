import os
import shutil

print("--- Стартиране на организатора ---")


folder_path = r"C:\Users\ADMIN\Desktop\TestAutomation"

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".pdf": "Documents"
}

files = os.listdir(folder_path)

for file in files:
    
    filename, extension = os.path.splitext(file)


    if extension in extensions:

       
        folder_name = extensions[extension]
        new_folder_path = os.path.join(folder_path, folder_name)

        
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(new_folder_path, file)

        shutil.move(old_file_path, new_file_path)
        print(f"Файлът {file} е преместен успешно в папка {folder_name}!")

print("Готово! Провери си папката.")
