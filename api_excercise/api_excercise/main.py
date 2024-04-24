from check_bigquery_table import check_table_exists
from check_cloud_storage import check_bucket_file

def main():
    choice = input("Do you want to check for the existence of a table on BigQuery (B) or find a file in a bucket on Cloud Storage (C)? ").upper()

    if choice == "B":
        project_id = input("Enter your Google Cloud project ID: ")
        dataset_id = input("Enter your dataset ID: ")
        table_id = input("Enter your table: ")

        if not project_id or not dataset_id or not table_id:
            print("Error: Make sure you provide all the requested details.")
            return

        if check_table_exists(project_id, dataset_id, table_id):
            print(f"The table {table_id} exists on BigQuery.")
        else:
            print(f"Table {table_id} does not exist on BigQuery.")
    elif choice == "C":
        bucket_name = input("Enter the name of the bucket on Cloud Storage: ")
        file_name = input("Enter the name of the file to search for: ")

        if not bucket_name or not file_name:
            print("Error: Make sure you provide all the requested details.")
            return

        if check_bucket_file(bucket_name, file_name):
            print(f"File {file_name} found in bucket {bucket_name}.")
        else:
            print(f"File {file_name} not found in bucket {bucket_name}.")
    else:
        print("Invalid choice. Choose 'B' for BigQuery or 'C' for Cloud Storage.")

if __name__ == "__main__":
    main()

#project = training-gcp-309207
#dataset = dataset_1
#table = company_ris
#bucket = bucket_angelo
#file = yob2014.txt
