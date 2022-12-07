"""validationのファイルを読み込む関数"""


def read_file(file_path) -> list:
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        list: _description_
    """    
    file_values = list()
    with open(file_path, encoding="utf-8") as file:
        for line in file.readline():
            file_values.append(line.strip())
    return file_values
