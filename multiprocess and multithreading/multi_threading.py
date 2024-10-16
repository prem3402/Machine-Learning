# when to use -> IO bound tasks
import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letters():
    for letter in "abcdefg":
        time.sleep(2)
        print(f"Letter: {letter}")


# creating two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
start_time = time.time()

# print_numbers()
# print_letters()

# starting threads

t1.start()
t2.start()


# waiting for threads to complete
t1.join()
t2.join()

end_time = time.time() - start_time
print(f"{end_time:.2f}")
