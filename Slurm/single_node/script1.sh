#!/bin/bash


#SBATCH -J pwd

#
# Ask for 3 cores

#SBATCH -n 8

#
# Submit with maximum 24 hour walltime HH:MM:SS


#
echo 'Your job is running on node(s):'
echo $SLURM_JOB_NODELIST
echo 'Cores per node:'
echo $SLURM_TASKS_PER_NODE
