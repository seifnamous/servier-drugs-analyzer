"""Write dataframe to json file.
"""


def write(df_graph, ouptut_file: str):
    """_summary_

    Args:
        df_graph (_type_): _description_
        ouptut_file (str): _description_
    """
    df_graph.write.format('json').save(ouptut_file)
