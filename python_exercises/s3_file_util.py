import boto3
import botocore
import io
import os
import logging
import traceback
import json

s3 = boto3.resource('s3')
BUCKET_NAME = 'c12e-nbc-landingzone'
class IllegalArgumentError(ValueError):
    pass
class S3_File_Util(object):

    def update_file_if_exists(self,bucket_name,key, file_path):
        if not key or not file_path or not bucket_name:
            raise IllegalArgumentError("Empty key or file_path")       
        temp_location="update_profile_tmp_file.txt"
        try:
            existedFileObj = s3.Object(bucket_name,key)
            existedFileIoBytes = io.BytesIO(existedFileObj.get()["Body"].read())
            #Open temporary file as bytes write existed file data
            tempOut = open(temp_location,'wb')
            tempOut.write(existedFileIoBytes.read())
            current_file_out = open(file_path,'rb')
            #write current file data write at last(append)
            current_file_data = current_file_out.read()
            tempOut.write(current_file_data)
            tempOut.close()
            current_file_out.close()
            tempOut = open(temp_location,'rb')
            s3.Bucket(bucket_name).put_object(Key=key, Body=tempOut)
            tempOut.close()
            os.remove(temp_location)
        except botocore.errorfactory.ClientError as e:
            tempOut = open(file_path,'rb')
            s3.Bucket(bucket_name).put_object(Key=key, Body=tempOut)
            tempOut.close()

        os.remove(file_path)
                    
    def check_file_exists_in_bucket(self,bucket_name,key):
        try:
            print("Checking on: " + bucket_name + ", " + key)
            existedFileObj = s3.Object(bucket_name,key).load()
            return True;
        except botocore.errorfactory.ClientError as e:
            return False;
            
    def upload_file(self, bucket_name, key, file_path):
        try:
            if not key or not file_path or not bucket_name:
                raise IllegalArgumentError("Empty key or file_path")
            tempOut = open(file_path,'rb')
            full_key = key + '/' + file_path
            s3 = boto3.resource('s3')
            obj = s3.Object(bucket_name, full_key)
            obj.put(Body=tempOut)
            tempOut.close()
        except Exception as e:
            traceback.print_exc()
            raise
                
    def download_file(self,bucket_name,key,file_path_to_save):
        try:
            s3.Bucket(bucket_name).download_file(key,file_path_to_save)
        except Exception as e:
            traceback.print_exc()
            raise

    def convert_query_to_file(self, query, filepath, header):
        file = open(filepath, 'w')
        if header is not None:
            file.write('\t'.join(header))
        for i in range(len(query)):
            file.write('\t'.join(map(str,query[i].tolist())) + '\n')


    def get_profile_from_guid(self, guid):
        file_name = guid + '.tsv'
        my_key = 'profiles/' + file_name
        self.download_file(BUCKET_NAME, my_key, file_name)
        return file_name

    def save_file_with_data(self, bucket_name, key, data):
        logging.debug("save_file_with_data bucket_name = {}, key = {}, data = {}", bucket_name, key, data)
        """The code below will create a file (if it doesn’t exist, or overwrite it otherwise) with named specified
        key and put it in bucket."""
        try:
            if not bucket_name or not key or not data:
                raise ValueError("Passed input params are empty.")
            obj = s3.Object(bucket_name, key)
            obj.put(Body=data)

        except Exception as e:
            logging.error(str(e))
            raise

