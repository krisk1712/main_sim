import queue
import pickle
import time

import itertools

red_lin_coun = 0
with open("/media/kannan/SPACE/project/new/sim/tele_met/tmdb.txt", 'rb') as f:
    tmdb_lin = f.readlines()
    while True:
        try:
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
                # conn.send(gettcq)
            red_lin_coun = red_lin_coun + 1 
        except IndexError:
            print("sorry")
            time.sleep(1)
            break  
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # while True:
    #     line = f.readline()
    #     if not line[0:]:
    #         print("mothing")
    #         continue
    #     else:
    #         print(line)
    #         time.sleep(1)