import os

def child():
   print ('A new child ',  os.getpid( ))
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print ("parent: {}, child: {}".format(pids[0], pids[1]))
      if input( ) == 'q': break

parent()