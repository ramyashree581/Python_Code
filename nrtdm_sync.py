# cat nrtdm_sync.py
import MySQLdb, time, logging
import graphitesend
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/root/nrtdm_sync.log',
                    filemode='a')
mydb_host="17.103.24.37"
mydb_user="rtdm"
mydb_pass="realtime"
mydb_name="sds_realtime"
mydb_port=3306