import os

from dotenv import load_dotenv

from datetime import datetime, timezone

load_dotenv()

from connectors import YandexDiskConnector

yandex_disk = YandexDiskConnector()

yandex_disk.token = os.getenv("YANDEX_TOKEN")
yandex_disk.yandex_disk_path = os.getenv("YANDEX_DISK_PATH")
local_path = "/home/lenovo/github-repo/Sevise-files-sync/src"
yandex_disk.local_path = local_path


yandex_disk_files: dict = {}

local_files = {} # файлы из локальной папки

# yandex_disk.load_file("test_file_to_sync.txt") # запись 1-го файла на YANDEX DISK

# yandex_disk.delete("test_file_to_sync.txt") # удаление файла из YANDEX DISK

for name in os.listdir(local_path):
    # Полный путь к файлу или папки
    full_path = os.path.join(local_path, name)
    # Проверяем, что это файл (а не папка)
    if os.path.isfile(full_path):
        local_files[name] = int(os.path.getmtime(name))

if yandex_disk_files != local_files:
    # получение списка файлов из YANDEX DISK
    yandex_disk_files: dict = yandex_disk.info_files()

    # Удаление файлов
    yandex_dell_files: list = []
    for name in yandex_disk_files:
        if name not in local_files:
            yandex_dell_files.append(name)

    if len(yandex_dell_files) > 0:
        for yandex_file in yandex_dell_files:
            yandex_disk.delete_file(yandex_file)

    # Запись новых файлов
    yandex_load_files: list = []
    for name in local_files:
        if name not in yandex_dell_files:
            yandex_load_files.append(name)

    if len(yandex_load_files) > 0:
        for yandex_file in yandex_load_files:
            yandex_disk.load_file(yandex_file)

    # Перезапись измененных файлов
    yandex_existing_files: list = []
    for name in yandex_disk_files:
        # сравниваем время изменения - mtime
        if local_files[name] != yandex_disk_files[name]:
            yandex_disk.load_file(name)
