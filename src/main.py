import os

from dotenv import load_dotenv
from time import sleep

load_dotenv()

from connectors import YandexDiskConnector

yandex_disk = YandexDiskConnector()

yandex_disk.token = os.getenv("YANDEX_TOKEN")
yandex_disk.yandex_disk_path = os.getenv("YANDEX_DISK_PATH")
yandex_disk.local_path = "/home/lenovo/github-repo/Sevise-files-sync/src"

# try:
#     yandex_disk.load_file("test_file_to_sync.txt") # запись 1-го файла
# except Exception as e:
#     print(str(e))
# try:
#     yandex_files = yandex_disk.info() # получение списка файлов
# except Exception as e:
#     print(str(e))
# yandex_disk.delete("test_file_to_sync.txt")
