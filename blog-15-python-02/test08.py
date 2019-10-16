import Queue

queue = Queue.Queue()

for i in range(10):
    queue.put(i)
print(queue.empty())
print(queue.qsize())

#取数据 get依次取出里面的数据
print(queue.get())
print(queue.get())
