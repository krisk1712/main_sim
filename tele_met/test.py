import queue
import pickle
import time

red_lin_coun = 0
while True:
    with open("/media/kannan/SPACE/project/new/sim/tele_met/tmdb.txt","r") as tmdb:
        line = tmdb.readlines()
    if line in ['\n', '\r\n']:
        print("THERE IS NO TELECOMMAND.....")
        print("CONTINUING TO TELEMETRY.....")
    else:
        tcq = queue.Queue()
        tcq.put(line)
        get_tcq = tcq.()
        time.sleep(1)
        print(get_tcq)
        time.sleep(1)
        gettcq = pickle.dumps(get_tcq)
        print(gettcq)
    red_lin_coun = red_lin_coun + 1