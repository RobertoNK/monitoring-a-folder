import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import glob

def on_created(event):
    os.chdir("D:/server/www/test_folder")
    list_of_files = glob.glob("*.txt")
    list_of_files.sort(key=os.path.getmtime)
    last_file = list_of_files[len(list_of_files)-1]
    print(last_file)
    #print(last_file)
    print("created")
        
def on_deleted(event):
    print("deleted")
        
def on_modified(event):
    print("modified")
        
def on_moved(event):
    print("moved")


if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    # calling functions
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved


    path = "D:/server/www/test_folder"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("Monitoreando")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("terminado")
    observer.join()
    