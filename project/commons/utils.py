from datetime import datetime


def get_timenow_str():
    return datetime.utcnow().strftime("%Y%m%d%H%M%S%f")[:-5]
