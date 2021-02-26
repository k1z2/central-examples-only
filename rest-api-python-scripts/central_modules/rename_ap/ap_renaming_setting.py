from pprint import pprint

# Create the following files by refering to the samples.
csv_filename = "csv_file.csv"
central_filename = "input_token_only.yaml"

# Get instance of ArubaCentralBase from the central_filename
from pycentral.workflows.workflows_utils import get_conn_from_file
central = get_conn_from_file(filename=central_filename)

# Rename AP using the workflow `workflows.config_apsettings_from_csv.py`
from pycentral.workflows.config_apsettings_from_csv import ApSettingsCsv
ApSettingsCsv(conn=central, csv_filename=csv_filename)