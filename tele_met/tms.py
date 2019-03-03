# import socket
# import queue
# import pickle
# import time
# import random

# def server_program():
#     host = socket.gethostname()
#     port = 4445
#     server_socket = socket.socket()  
#     server_socket.bind((host, port))
#     server_socket.listen(2)
#     conn, address = server_socket.accept()
#     print("Connection from: " + str(address))
#     sat_stat = ["4EA36B01","83EC",["AA55BB66","1A0E","AFFEC34A","0101"],"1212"]
#     bat_stat=  ["4EA36B01","83EC",["AA55BB66","1A0E","BA53A980","0101"],"1212"]
#     hlth =     ["4EA36B01","83EC",["AA55BB66","1A0E","231876A7","0101"],"1212"]
#     chrg =     ["4EA36B01","83EC",["AA55BB66","1A0E","C4579850","0101"],"1212"] 
#     vars = [sat_stat,bat_stat,hlth,chrg]
#     while True:
#         packt= queue.LifoQueue()
#         packt.put(random.choice(vars))
#         tm = packt.get()
#         telemetry = pickle.dumps(tm)
#         time.sleep(1)
#         conn.send(telemetry)
#         time.sleep(1) 
#         data = conn.recv(1024)
#         print(data)
#         time.sleep(1)

#     conn.close() 

# if __name__ == '__main__':
#     server_program()




import sched, time                                          # advanced libraraies
import signal                                               # advanced library
import select                                               # advanced library
import sys                                                  # advanced library
import socket                                               #the network library
import pickle                                               # the hex code factory library
import queue 
import random                                             




pac_qu = queue.LifoQueue()
s = sched.scheduler(time.time, time.sleep)                  
host = socket.gethostname()
port = 5555  
server_socket = socket.socket()  
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept() 

def telemet_send(s):
    sat_stat = ["4EA36B01","83EC",["AA55BB66","1A0E","AFFEC34A","0101"],"1212"]
    bat_stat=  ["4EA36B01","83EC",["AA55BB66","1A0E","BA53A980","0101"],"1212"]
    hlth =     ["4EA36B01","83EC",["AA55BB66","1A0E","231876A7","0101"],"1212"]
    chrg =     ["4EA36B01","83EC",["AA55BB66","1A0E","C4579850","0101"],"1212"] 
    vars = [sat_stat,bat_stat,hlth,chrg]
    counter = 0 
    while counter < 10:
        print(counter)
        packt= queue.LifoQueue()
        packt.put(random.choice(vars))
        tm = packt.get()
        telemetry = pickle.dumps(tm)
        time.sleep(1)
        conn.send(telemetry)
        time.sleep(1) 
        data = conn.recv(1024)
        print(data)
        time.sleep(1)
        counter = counter + 1
    s.enter(1, 1, telemet_send, (s,)) 
def telecmd_recv(s):
    print("THE TELECOMMAND PART")
    newtc = "THIS IS A TELECOMMAND"
    
with open("/media/kannan/SPACE/project/new/sim/tele_met/tmdb.txt", 'rb') as f:
    tmdb_lin = f.readlines()
try:
    red_lin_coun = 0
    onetc = tmdb_lin[red_lin_coun]
    if not onetc:
        print("THERE IS NO TELECOMMAND.....")
        print("CONTINUING TO TELEMETRY.....")
    else:
        tcq = queue.Queue()
        tcq.put(onetc)
        get_tcq = tcq.get()
        print(get_tcq)
        gettcq = pickle.dumps(get_tcq)
        conn.send(gettcq)
    red_lin_coun = red_lin_coun + 1 
except IndexError:
    print("sorry")
    time.sleep(1)
    break
        
    s.enter(10, 5, telecmd_recv, (s,))                      # calling event scheduler at the 10th second only for the function execution

s.enter(1, 1, telemet_send, (s,))                           # 
s.enter(10, 1, telecmd_recv, (s,))                          #    Function calling on all the side to run the diffrent function 
s.run() 

