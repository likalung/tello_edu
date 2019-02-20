import socket, threading, time, pygame
#you will need to install pygame for music play
#before use this file, you need to set the tello IP
#in your router, i use 101 as the first tello IP address
#Just set all the tello in your router

# setup music file
musicfile = "bg.mid" # midi, ogg, mp3 file stored in same folder is OK

# setup tello
telloport = 8889 # default by tello
startip = 101 # set in router
startlocalport = 9010 # just un-use port range
initaltellonumber = 1 #First tello number
totaltellonumber = 20 # Total number of tello
tellolist = [ 1,2,3,5,6 ] #tello number have 
uselist = 0 # 0 use continue tello, 1 using tello in list. 
alltello = ""

if uselist == 1:
    for i in tellolist:
    #   set tello unit identify number
        x = str(i)
        alltello = alltello + x + ','
    #   IP and port of tello
    #   IP addr pre-set in router
        newip = startip - 1 + int(i)
        globals()["tello" + x + "_address"] = ("192.168.1." + str(newip) , telloport)
    #   IP and port of local computer
        newport = startlocalport - 1 + int(i)
        globals()["local" + x + "_address"] = ('', newport)
    #   Create a UDP connection that we'll send the command to
        globals()["sock" + x] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #   Bind to the local address and port
        globals()["sock" + x].bind(eval("local" + x + "_address"))
else :
    for i in range(totaltellonumber):
    #   set tello unit identify number
        x = str(i + initaltellonumber)
        x = str(tellolist[i])
        alltello = alltello + x + ','
        globals()["tello" + x + "_address"] = ("192.168.1." + str(startip) , telloport)
        startip = startip + 1
        globals()["local" + x + "_address"] = ('', startlocalport)
        startlocalport = startlocalport + 1
        globals()["sock" + x] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        globals()["sock" + x].bind(eval("local" + x + "_address"))

# all tello string
alltello = alltello[:-1]

#prepare for pygame music
pygame.mixer.init();
pygame.mixer.music.load(musicfile);

# delay time
def wait(delay):
    try:
        print("wait " + str(delay))
        time.sleep(delay)
    except Exception as e:
        print("Error wait" + str(e))

# send command to swarm
def send(message, target):
    starttime = time.time()
    if target.lower() == "all":
        target = alltello

    try:
        p = target.split(",")
        for x in p:
            x = x.replace(" ","")
            if "-" in x :
                xl = x.split("-")
                for xo in range(int(xl[0]),int(xl[1]) + 1 ):
                    if "tello" + str(xo) + "_address" in globals():
                        sendcmd(xo, message)
            else :
                if "tello" + str(x) + "_address" in globals():
                    sendcmd(x , message)
    except Exception as e:
        print(Message + " error: " + str(e))
    endtime = time.time()
    print (str(round(endtime - starttime , 3)) + "sec")

def sendcmd(xt, message):
    stopcmd = "stop";
    xt = str(xt)
    telloaddr = eval("tello" + xt + "_address")
    sock = eval("sock" + xt )
    try:
        sock.sendto(stopcmd.encode(), telloaddr)
        time.sleep(0.005)
        sock.sendto(message.encode(), telloaddr)
        print("Tello " + xt + ": " + message)
        time.sleep(0.005)
    except Exception as e:
        print("Tello " + xt + " error: " + str(e))



#send( "Command" , tello number eg. "1,2,3-5,6")    

# Put Tello into command mode
send("command", "all")
#open position sensor
send("mon", "all")
# prosition sensor, only 1 freq. 20Hz, 2 10Hz
# 0 bottom sensor only
# 1 front sensor only
# 2 both sensor 
send("mdirection 2", "all")
#start music
pygame.mixer.music.play()
# Send the takeoff command
send("takeoff", "1-10")
wait(4)
send("up 100","1,3")
send("up 150","2")
wait(4)
send("cw 360", "1 ,3")
send("ccw 360", "2")
wait(10)
send("land", "All")
wait(5)
#send("emergency","All")
pygame.mixer.music.stop()
print("Mission completed successfully!")
# Close the socket
for i in range(totaltellonumber):
    x = str(i + initaltellonumber)
# close socket
    globals()["sock" + x].close()

#Pre60)
# jump x y z speed yaw mid1 mid2 (yaw on mid2 1-360)
# mid = Mission Pad, m-1 = random, m-2 = nearest MP
# mdirection (0=downward '20Hz', 1=forward '20Hz', 2=both '10Hz' )
# speed?, battery?
# wifi ssid pass                                                                                                                                                                                                                                                                                                                                                                                     