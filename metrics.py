import os
while True:
  print('I run!')
  hostname = os.uname()[1]
  print(hostname)

  import socket
  print(socket.gethostbyname(socket.gethostname()))
  print(socket.gethostbyname(socket.getfqdn()))

  import shutil
  total, used, free = shutil.disk_usage("/")
  print("Total: %d GiB" % (total // (2**30)))
  print("Used: %d GiB" % (used // (2**30)))
  print("Free: %d GiB" % (free // (2**30)))

  f = open('index.html', 'w')
  f.write('network info' + '\n')
  f.write(hostname + '\n')
  f.write(socket.gethostbyname(socket.gethostname()) + '\n')
  f.write(socket.gethostbyname(socket.getfqdn()) + '\n')
  f.write('Disk Info' + '\n')
  f.write("Total: %d GiB" % (total // (2**30)) + '\n')
  f.write("Used: %d GiB" % (used // (2**30)) + '\n')
  f.write("Free: %d GiB" % (free // (2**30)) + '\n')
#  break
#print('Not in loop!')
