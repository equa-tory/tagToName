import os
from mutagen.easyid3 import EasyID3

# Укажите путь к папке с файлами
folder_path = './in'

# Получаем список всех файлов в папке
files = os.listdir(folder_path)

for file in files:
    # Проверяем, что это .mp3 файл
    if file.endswith('.mp3'):
        # Получаем полный путь к файлу
        file_path = os.path.join(folder_path, file)
        
        try:
            # Загружаем метаданные файла
            audio = EasyID3(file_path)
            # Получаем название из ID3 тега
            title = audio.get('title', [None])[0]
            
            if title:
                # Создаем новое имя файла с тем же расширением
                new_file_name = title + '.mp3'
                new_file_path = os.path.join(folder_path, new_file_name)
                
                # Переименовываем файл
                os.rename(file_path, new_file_path)
                print(f'Файл {file} переименован в {new_file_name}')
            else:
                print(f'Не удалось получить название для файла: {file}')
        except Exception as e:
            print(f'Ошибка при обработке файла {file}: {e}')
