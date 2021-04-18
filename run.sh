###########################################################
# Script configuration

GET_DATA_INSTANCES=0

# End of Setup Area
##########################################################

get_data_process="[g]et_file_price_oil"

source /home/mlussati/anaconda3/etc/profile.d/conda.sh
conda activate /root/anaconda3/envs/openda-data
python_path=/home/mlussati/anaconda3/bin/python

echo Starting Process Management
cd /home/mlussati/Documents/workspace/open-data-scripts

echo 'Checking Monitoring'
get_data_process=`ps -ef | grep $get_data_process | wc -l`
if [ $get_data_process -lt 1 ]; then
	echo Starting Get Data for Server
	python -u get_file_price_oil.py >> logs/get_data_process.log 2>&1 &
fi