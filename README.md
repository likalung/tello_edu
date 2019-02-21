This is a example of tello edu swarm.

Before you start:
1. Before you use this file, you need to install the pygame for music play in the python.you can refer to https://www.pygame.org/wiki/GettingStarted for how to install pygame. If you no need background music, just delete all the lines about the pygame.
2. Set all the tello mac address in to the router and give a fixed ip address for all of them. Just give some mark on the tello edu, so you know what IP it have. So everytime you play, you can easily know which tello edu you are using. I use 101 as the started IP address for first tello edu. so the second tello edu will be 102.

Choosing mode:
You can use continue IP address's tello edu (set uselist as 0, put the first tello edu number in initaltellonumber and the total number of tello you use in totaltellonumber ) or randomly choose tello edu as you like, just put the tello number in to the tellolist and set uselist as 1.
You can use continue IP address's tello edu (set uselist as 0) or randomly choose tello edu as you like, just put the tello number in to the tellolist and set uselist as 1.

Plan your swarm:
you can set your swarm command after the command example line, the command is very easy to understand. send("command", "1,2,4-6,10") means that tello number 1,2,4,5,6,10 will receive the command line "command". if no tello number, Then all tello will receive the command.

To start the swarm, you must first ask the tello to enter command mode. And for better positioning, you should ask the tello edu to start the position sensor, and better both open. Then you can start takeoff and do what you want.

