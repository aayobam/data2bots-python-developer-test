import os
import json
import unittest
from main import read_write_json_data


class TestReadDataWriteToSchema(unittest.TestCase):
    def setUp(self):
        self.input_path_data_1 = "./data/data_1.json"
        self.output_dir_schema_1 = "./schema/schema_1.json"
        self.output_path_schema_1 = os.path.join(self.output_dir_schema_1)

        self.input_path_data_2 = "./data/data_2.json"
        self.output_dir_schema_2 = "./schema/schema_2.json"
        self.output_path_schema_2 = os.path.join(self.output_dir_schema_2)

    def test_case_for_data_1_schema_1(self):
        # Run the build_schema function
        read_write_json_data(self.input_path_data_1, self.output_dir_schema_1)

        # Verify that the output file exists
        self.assertTrue(os.path.exists(self.output_path_schema_1))

        # Load the output file and verify its contents
        with open(self.output_path_schema_1) as f:
            output_schema = json.load(f)

        expected_schema = {
            "properties": {
                "participantIds": {
                "type": "string",
                "enum": [
                    "ABCDEFGHIJKLMNOPQRST",
                    "ABCDEFGHIJKLMNOPQRSTUVWXY"
                ],
                "tag": "",
                "description": "",
                "required": False
                }
            }
        }
        self.assertDictEqual(output_schema, expected_schema)

    # Remove the output file
    def tear_down_created_file_for_test_case_1(self):
        if os.path.exists(self.output_path_schema_1):
            os.remove(self.output_path_schema_1)

    def test_case_for_data_2_schema_2(self):
        # Run the build_schema function
        read_write_json_data(self.input_path_data_2, self.output_dir_schema_2 )

        # Verify that the output file exists
        self.assertTrue(os.path.exists(self.output_path_schema_2))

        # Load the output file and verify its contents
        with open(self.output_path_schema_2) as f:
            output_schema = json.load(f)
            
        expected_schema = {
            "properties": {
                "time": {
                    "type": "int",
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "acl": {
                    "type": "string",
                    "enum": [],
                    "tag": "",
                    "description": "",
                    "required": False
                },
                "internationalCountries": {
                    "type": "string",
                    "enum": [
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
                        "ABCDEFGHIJKLMNOPQ",
                        "ABCDEFGHIJKLMNOPQRSTUVW",
                        "ABCDEFGHIJKLMNOPQRSTUVWXY",
                        "ABCDEFGHIJK",
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        "ABCDEFGHIJKLMNOPQR",
                        "ABCDEFG",
                        "ABCDEFGHIJKLM"
                    ],
                    "tag": "",
                    "description": "",
                    "required": False
                }
            }
        }
        self.assertDictEqual(output_schema, expected_schema)

    # Remove the output file
    def tear_down_created_file_for_test_case_2(self):
        if os.path.exists(self.output_path_schema_2):
            os.remove(self.output_path_schema_2)

if __name__ == "__main__":
    #unittest.main()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestReadDataWriteToSchema)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
