import os
import time
import socket
import shutil

while True:
  hostname = os.uname()[1]
  total, used, free = shutil.disk_usage("/")
  f = open('index.html', 'w')
  f.write('network info' + '\n')
  f.write(hostname + '\n')
  f.write(socket.gethostbyname(socket.gethostname()) + '\n')
  f.write(socket.gethostbyname(socket.getfqdn()) + '\n')
  f.write('Disk Info' + '\n')
  f.write("Total: %d GiB" % (total // (2**30)) + '\n')
  f.write("Used: %d GiB" % (used // (2**30)) + '\n')
  f.write("Free: %d GiB" % (free // (2**30)) + '\n')

  print('I run!')
  print(hostname)

  print(socket.gethostbyname(socket.gethostname()))
  print(socket.gethostbyname(socket.getfqdn()))

  print("Total: %d GiB" % (total // (2**30)))
  print("Used: %d GiB" % (used // (2**30)))
  print("Free: %d GiB" % (free // (2**30)))

  time.sleep(10)
#  break
#print('Not in loop!')
