import threading
import time
def print_numbers():
    for i in range(3):
        print(f"Thread: {i}")
        time.sleep(1)
t1 = threading.Thread(target=print_numbers)
t1.start()
t1.join()
print("Done!")