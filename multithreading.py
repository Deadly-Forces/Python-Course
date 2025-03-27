# multithreading = Used to perform multiple task concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.thread(target=my_function)

import threading
import time

def walk_dog(first):  # Expecting a single argument
    time.sleep(1)
    print(f"You finish walking the {first}")

def clean_house():
    time.sleep(3)
    print(f"You finish cleaning the house")

def get_groceries():
    time.sleep(5)
    print(f"You finish getting groceries")


"""walk_dog()
clean_house()
get_groceries()"""

# Creating threads
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore2 = threading.Thread(target=clean_house)
chore3 = threading.Thread(target=get_groceries)

# Starting threads
chore1.start()
chore2.start()
chore3.start()

# Joining threads to ensure they complete
chore1.join()
chore2.join()
chore3.join()

print("All chores are completed.")