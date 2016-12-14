import threading
import time


class CountdownThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        # get lock to synchronize threads
        thread_lock.acquire()
        print_time(self.name, self.counter, 3)
        # free lock to release next thread
        thread_lock.release()


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print "[%s] %s:  counting down %s" % (time.ctime(time.time()), thread_name, counter)
        counter -= 1

threads = []
thread_lock = threading.Lock()

# create new threads
thread1 = CountdownThread(1, "Thread-1", 1)
thread2 = CountdownThread(2, "Thread-2", 2)

# start new threads
thread2.start()
thread1.start()

# add threads to thread list
threads.append(thread1)
threads.append(thread2)

# wait for all threads to complete
for t in threads:
    t.join()

print "Exiting Main Thread"
