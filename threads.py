from threading import Thread
from pathlib import Path
from shutil import copyfile

def copy_file(file):
    suf = file.suffix
    new_path = Path("dist") / suf
    new_path.mkdir(parents=True, exist_ok=True)
    copyfile(file, new_path / file.name)

def file_copy_task(file):
    copy_file(file)

def file_finder(path):
    for file in path.iterdir():
        if file.is_dir():
            file_finder(file)
        else:
            thread = Thread(target=file_copy_task, args=(file,))
            thread.start()
            thread.join()

path = Path('hlam')
file_finder(path)
