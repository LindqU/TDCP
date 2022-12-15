"""validationのファイルを読み込む関数"""
from logging import getLogger, INFO

# setting logging
logger = getLogger(__name__)
logger.setLevel(INFO)


def read_file(file_path) -> list:
    """file_read module

    Args:
        file_path (_type_): input_file path

    Returns:
        list: file_values
    """
    file_values = list()
    with open(file_path, encoding="utf-8") as file:
        ex_outputs = file.read().splitlines()
        logger.info("ex outputs : %s", ex_outputs)
        file_values.append(ex_outputs)
    return file_values
