
import gcloud
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
	storage_client = storage.Client()
 	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.blob(destination_blob_name)

	blob.upload_from_filename(source_file_name)

	print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))
	

upload_blob("anisha-demo-1", "bs3.sh", "upload.sh")
 
