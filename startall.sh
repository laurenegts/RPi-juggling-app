#!/bin/bash


devices="/dev/ttyACM*"
command="/home/pi/AeroUp/src/aeroup"
run_args=""
#empty quotes set the variable to 0

for device in $devices
do
   run_args=$run_args" -o "$device
done
#above is a loop that checks the number of devices and prints out the
#necessary commands
#run_args run the code

echo Running command: $command$run_args
$command$run_args
#echo prints out the command
