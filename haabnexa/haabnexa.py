#!/usr/bin/env python

import socket,getopt,sys,time,syslog


def main(argv):
   syslog.openlog("haabnexa_module", syslog.LOG_PID|syslog.LOG_CONS, syslog.LOG_USER)

   sock_port = ''
   command = ''
   host ="10.127.11.50"
   client= '' 
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
   try:
      opts, args = getopt.getopt(argv,"hp:c:i:",["port=","com=","int="])
   except getopt.GetoptError:
      print 'home_commander.py -p port -c command'
      sys.exit(2)
   if len(sys.argv) < 4:
	print 'home_commander.py -p port -c command'
	print len(sys.argv)
	sys.exit(2) 
   for opt, arg in opts:
      if opt == '-h':
         print 'home_commander.py -p <port> -c <command>'
         sys.exit()
      elif opt in ("-p", "--port"):
         sock_port = arg
      elif opt in ("-c", "--com"):
         command = arg
      elif opt in ("-i", "--int"):
	     client = arg
   	
   syslog.syslog('Got a command from: '+client)
   s.connect((host,5697))

   if command=='ALL':
   	port.write("501")
	time.sleep(1)
	port.write("511")
	time.sleep(1)
        port.write("901")
	time.sleep(1)
        port.write("911")
	time.sleep(1)
        port.write("921")

   elif command=='SLEEP':
	port.write("500")
	time.sleep(1)
	port.write("510")
        time.sleep(1)
        port.write("900")
        time.sleep(1)
        port.write("910")
        time.sleep(1)
        port.write("920")

   elif command=='111':
        port.write("500")
        time.sleep(1)
        port.write("510")
        time.sleep(1)
        port.write("900")
        time.sleep(1)
        port.write("910")
        time.sleep(1)
        port.write("920")


   else:
	s.send(command)
	s.close
   
   print 'OK'
 

if __name__ == "__main__":
   main(sys.argv[1:])

