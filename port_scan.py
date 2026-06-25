#takes cli input
import sys

user_input = sys.argv[1:]

if len(user_input) == 0:
    exit("Missing Correct Amount of Input. Please Set (-Host=) at the min and an optional (-Port=) if you want")

HOST = ""
h_tmp = []
PORT = ""

if len(user_input[0]) > 5:
    #this should be HOST or PORT
    cmd = user_input[0][:6]
    if cmd.lower() == "-host=":
        h_tmp = user_input[0][6:].split(",")      
    else:
        #-[0]host[1:4]
        if cmd[0] != "-":
            exit("The CLI argument option needs to start with a '-'")
        elif cmd[1:5].lower() != "host" and cmd[1:5].lower() != "port":
            exit("The CLI arguement option only accpets -host and -port")
        elif cmd[5:6] != "=":
            exit("Following -Host or -Port must be a '=' before inputting argument")
else:
    exit("Issue in the CLI argument set up")
            
import socket

def probe_port(host, port, timeout=.2) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        
        result = sock.connect_ex((host, port))
        
        return result == 0
    
import threading
import tqdm
pbar = tqdm.tqdm(65536 *len(h_tmp),desc="Scanning",unit="",total=65536 *len(h_tmp))
expose_bar = []
def fetch_result(host, port):
        result = probe_port(host, port)
        if result:
            expose_bar.append([host, port])
        pbar.update(1)
        
def start_scan(j):
    for i in range(1, 65536, 5):
    # for i in range(1, 6, 5):
        t1 = threading.Thread(
            target=fetch_result,
            args=[j, i],
            daemon=True
        )
        t2 = threading.Thread(
            target=fetch_result,
            args=[j, i+1],
            daemon=True
        )
        t3 = threading.Thread(
            target=fetch_result,
            args=[j, i+2],
            daemon=True
        )
        t4 = threading.Thread(
            target=fetch_result,
            args=[j, i+3],
            daemon=True
        )
        t5 = threading.Thread(
            target=fetch_result,
            args=[j, i+4],
            daemon=True
        )
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

if not PORT:
    for j in h_tmp:
        j = j.strip()
        if j[-1] == "*":
            for i in range(1, 255):
                start_scan(j[:-1] + str(i))
        else:
            start_scan(j)
    
for i in expose_bar:
    print(f"Host: {i[0]}, Port: {i[1]}. Exposed")