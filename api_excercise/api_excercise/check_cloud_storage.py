from google.cloud import storage

def check_bucket_file(bucket_name, file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    for blob in blobs:
        if blob.name == file_name:
            return True
    return False
