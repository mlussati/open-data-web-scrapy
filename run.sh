#!/bin/bash
###########################################################
# Script configuration

GET_DATA_INSTANCES=0

# End of Setup Area
##########################################################


get_data_process="[g]et_file_price_oil"
#source /home/manilson/anaconda3/etc/profile.d/conda.sh
source ~/anaconda3/etc/profile.d/conda.sh
conda activate open-data

echo Starting Process Management
cd /home/manilson/Documents/workspace/open-data-web-scrapy

echo 'Checking Monitoring'
get_data_process=`ps -ef | grep $get_data_process | wc -l`
if [ $get_data_process -lt 1 ]; then
	echo Starting Get Data for Server
	python -u get_file_price_oil.py 
fi