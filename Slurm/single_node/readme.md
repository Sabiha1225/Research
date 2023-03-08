Setup Slurm on Ubuntu for single node

- sudo apt update -y
- sudo apt install slurmd slurmctld -y


Check cpu cores available in your machine 

lscpu

Check  Memory

free -mt

Copy the slurm.conf file in /etc/slurm directory with modified cpu core number and real memory for compute node section

Strat the services

- sudo systemctl start slurmctld
- sudo systemctl start slurmd
