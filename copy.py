from google.cloud import storage

def copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
        storage_client = storage.Client()
        source_bucket = storage_client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.get_bucket(new_bucket_name)
        new_blob = source_bucket.copy_blob(source_blob, destination_bucket, new_blob_name)

copy_blob("anisha-demo-1", "abc.py", "pe-pradnya", "anisha")

