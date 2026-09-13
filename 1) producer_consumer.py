import threading
import time

Buffer_Size = 5
Total_Items = 10

Buffer = [None] * Buffer_Size

in_pos = 0
out_pos = 0
items_in_the_buffer = 0

lock = threading.Lock()

space_available = threading.Condition(lock)
item_available = threading.Condition(lock)


def producer():
    global in_pos, items_in_the_buffer

    for value in range(1, Total_Items + 1):

        with space_available:
            while items_in_the_buffer == Buffer_Size:
                print("Producer waiting: buffer is full.")
                space_available.wait()

            Buffer[in_pos] = value
            print(f"Produced {value} at position {in_pos}")

            in_pos = (in_pos + 1) % Buffer_Size
            items_in_the_buffer += 1

            item_available.notify()

        time.sleep(0.3)


def consumer():
    global out_pos, items_in_the_buffer

    for _ in range(Total_Items):

        with item_available:
            while items_in_the_buffer == 0:
                print("Consumer waiting: buffer is empty.")
                item_available.wait()

            value = Buffer[out_pos]
            Buffer[out_pos] = None

            print(f"Consumed {value} from position {out_pos}")

            out_pos = (out_pos + 1) % Buffer_Size
            items_in_the_buffer -= 1

            space_available.notify()

        time.sleep(0.5)


producer_thread = threading.Thread(target=producer, name="ProducerThread")
consumer_thread = threading.Thread(target=consumer, name="ConsumerThread")

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("\nExecution completed successfully!!!")