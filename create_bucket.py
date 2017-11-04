#!/usr/bin/python3
import os, sys
import logging
import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from lib.boto_base import BotoBase
from common.connection import Connector

LOG_FILE = "logs/api_create_bucket_"+str(time.strftime('%Y-%m-%d_%H-%M-%S'))+".log"
logging.basicConfig(filename=LOG_FILE, filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
print("\n\n Log file name :: " + LOG_FILE)

BUCKET_NAME = "autotestbucket"

class CreateBucket():

    def test_create(self):
        self.logger = logging
        self.logger.info('Connecting to DAM using S3 API')
        self.connectionObj = Connector()        
        self.connection = self.connectionObj.connect()    
        self.botobaseObj = BotoBase(self.connection, self.logger)

        print('\n Bucket Name::' + BUCKET_NAME)
        self.botobaseObj.createbucket(BUCKET_NAME)
        self.logger.info("Bucket Created")
        print("Bucket created")

obj = CreateBucket()
obj.test_create()
