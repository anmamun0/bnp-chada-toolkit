import time
import subprocess
from watchdog.observers import Observer  # ফোল্ডার পর্যবেক্ষণের জন্য
from watchdog.events import FileSystemEventHandler  # ফাইল তৈরি/ডিলিট/মোডিফাই ইভেন্ট ধরতে

EXE_PATH = r"E:\_Programing\.Python\BNP-চাদা-project\launch_bnp_gui.exe"  #GUI file

# এখানে আপনার প্রকল্প ফোল্ডারের সঠিক পথ দিন
folder_to_watch = r"E:\_Programing\.Python\BNP-চাদা-project"

class FileCreateHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file created: {event.src_path}")
            subprocess.Popen(EXE_PATH)

event_handler = FileCreateHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_watch, recursive=True)
observer.start()

try:
    print(f"Watching folder: {folder_to_watch}")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
