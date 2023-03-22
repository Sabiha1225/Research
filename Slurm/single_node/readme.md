## Installation Process
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

## Commands
- slurmd -c
- squeue
- sinfo
- /var/log/slurm/slurmctld.log
- delete the clustername file
- /var/lib/slurm/slurmctld/clustername

- Give loads 
- srun -n8 -l hostname
- srun -n8 -l pwd

###### Run a Script:
sbatch script1.sh

###### See the details for a particular job
scontrol show job «jobid»
