import logging
from threading import Thread
from pathlib import Path
from shutil import copyfile

def copy_file(file):
    suf = file.suffix
    new_path = Path("dist") / suf
    new_path.mkdir(parents=True, exist_ok=True)
    copyfile(file, new_path / file.name)
    logging.info(f'Copied file {file} to {new_path / file.name}')

def file_copy_task(file):
    logging.info(f'Starting to copy file {file}')
    copy_file(file)
    logging.info(f'Finished copying file {file}')

def file_finder(path):
    for file in path.iterdir():
        if file.is_dir():
            logging.info(f'Entering directory {file}')
            file_finder(file)
        else:
            logging.info(f'Found file {file}, starting copy in a new thread')
            thread = Thread(target=file_copy_task, args=(file,))
            thread.start()
            thread.join()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(threadName)s - %(message)s')

    path = Path('hlam')
    logging.info(f'Starting to scan directory {path}')
    file_finder(path)
    logging.info('Finished scanning and copying files')
