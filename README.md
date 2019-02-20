This is a example of tello edu swarm.

Before you start:
1. Before you use this file, you need to install the pygame for music play in the python.you can refer to https://www.pygame.org/wiki/GettingStarted for how to install pygame.
2. Set all the tello mac address in to the router and give a fixed ip address for them. So everytime you play, you can easily know which tello edu you use. I use 101 as the started IP address for first tello edu. so the second tello edu will be 102.

Choosing mode:
<<<<<<< HEAD
You can use continue IP address's tello edu (set uselist as 0, put the first tello edu number in initaltellonumber and the total number of tello you use in totaltellonumber) or randomly choose tello edu as you like, just put the tello number in to the tellolist and set uselist as 1.
=======
You can use continue IP address's tello edu (set uselist as 0) or randomly choose tello edu as you like, just put the tello number in to the tellolist and set uselist as 1.
>>>>>>> d1f4846754551bea01ef8d40fdd7b5f7334fcdc1

Plan your swarm:
you can set your swarm command after the command example line, the command is very easy to understand. send("command", "1,2,4-6,10") means that tello number 1,2,4,5,6,10 will receive the command line "command".
To start the swarm, you must first ask the tello to command mode. and for better position, you should ask the tello edu to start the position sensor, and better both open. then you can start takeoff and do what you want.

