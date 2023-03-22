#!/bin/bash --login

# Specify the queue (also known as a partition)
#SBATCH --partition=amd

# run a single task, using a single CPU core
#SBATCH --ntasks=1

#SBATCH --output=myScript.o%J

#run a program command to print hostname and uptime
/bin/hostname && /bin/uptime
