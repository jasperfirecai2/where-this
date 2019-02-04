#!/bin/sh

### BEGIN INIT INFO
# Provides:        Startup
# Required-Start:    networking
# Default-Start:    2 3 4 5
# Default-Stop:        S 0 1 6
# Short-Description:    gitpull of pi
# Description:        Starts/Stops/Restarts the where-this program
### END INIT INFO
#to be honest I don't know if I'll get this to work

cd "/home/pi/Wedstrijd/" && git pull -f --rebase=false origin master
