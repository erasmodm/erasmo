import sys
import unittest
from unittest.mock import patch, MagicMock
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))


from api_excercise.check_bigquery_table import check_table_exists
from api_excercise.check_cloud_storage import check_bucket_file

class TestCheckBigQueryTable(unittest.TestCase):
    @patch("google.cloud.bigquery.Client")
    def test_check_table_exists(self, mock_client):
        # Set the mock behavior of the get_table method
        mock_table = MagicMock()
        mock_client.return_value.get_table.return_value = mock_table

        # Calling the function with an existing table
        result = check_table_exists("training-gcp-309207", "dataset_1", "company_ris")
        self.assertTrue(result)

        # Function call with a non-existent table
        mock_client.return_value.get_table.side_effect = Exception("Table not found")
        result = check_table_exists("training-gcp-309207", "dataset_1", "company_ri")
        self.assertFalse(result)

class TestCheckCloudStorage(unittest.TestCase):
    @patch("google.cloud.storage.Client")
    def test_check_bucket_file(self, mock_client):
        # Set the mock behavior of the list_blobs method
        mock_blob = MagicMock()
        mock_blob.name = "yob2014.txt"
        mock_bucket = MagicMock()
        mock_bucket.list_blobs.return_value = [mock_blob]
        mock_client.return_value.get_bucket.return_value = mock_bucket

        # Calling the function with an existing file
        result = check_bucket_file("bucket_angelo", "yob2014.txt")
        self.assertTrue(result)

        # Function call with a non-existent file
        result = check_bucket_file("bucket_angelo", "yo2014.txt")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
