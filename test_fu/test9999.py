import threading


class MyThread(threading.Thread):
    def __init__(self,theadID,name):
        threading.Thread.__init__(self)
        self.threadID = theadID
        self.name = name
    def run(self):
        currentThreadname = threading.current_thread()
        print('running in',currentThreadname)

thread = MyThread(1,'mythread')
thread.run()
print('********************')
thread.start()