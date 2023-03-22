#!/bin/bash --login

# Specify the queue (also known as a partition)
#SBATCH --partition=LocalQ

# run a single task, using a single CPU core
#SBATCH --ntasks=4

#SBATCH --output=script2.o%J

#run a program command to print hostname and uptime
/bin/hostname && /bin/uptime
