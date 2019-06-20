from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
        storage_client = storage.Client()
        source_bucket = storage_client.get_bucket(bucket_name)
        blob = source_bucket.blob(blob_name)
       
	blob.download_to_filename(destination_file_name)

download_blob("anisha-demo-1", "abc.py", "anisha")
