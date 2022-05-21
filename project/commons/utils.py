from datetime import datetime
import pandas as pd

from project.commons.constants import DATA_FILES_DIR


def get_timenow_str():
    return datetime.utcnow().strftime("%Y%m%d%H%M%S%f")[:-5]


def get_headers_from_csv(csv_file):
    csv_path = f"{DATA_FILES_DIR}/{csv_file}"
    return pd.read_csv(csv_path).columns.to_list()
