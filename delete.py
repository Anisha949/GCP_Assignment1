from google.cloud import storage

def delete_blob(bucket_name, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()


delete_blob("anisha-demo-1",'abc.py')

