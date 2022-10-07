"""Writes kpi calculation result dataframe to json file.
"""

def write(df_kpi, ouptut_file: str):
    """_summary_

    Args:
        df_kpi (_type_): _description_
        ouptut_file (str): _description_
    """
    df_kpi.write.format('json').save(ouptut_file)
