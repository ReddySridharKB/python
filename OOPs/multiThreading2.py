import threading
import time

def download(file, seconds):
    print(f"Downloading {file}")
    time.sleep(seconds)
    print(f"{file} downloaded")

t1 = threading.Thread(
    target=download,
    args=("file1", 2)
)

t2 = threading.Thread(
    target=download,
    args=("file2", 3)
)

t1.start()
t2.start()

t1.join()
t2.join()

print("All downloads completed")