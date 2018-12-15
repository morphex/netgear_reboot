#!/bin/bash

GECKODRIVER_PATH=$HOME/bin
RUN_DIRECTORY=$HOME/netgear_reboot
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin:/usr/local/sbin
PATH=$PATH:$GECKODRIVER_PATH
export PATH
cd $RUN_DIRECTORY
python br.py $1 >> br.log
