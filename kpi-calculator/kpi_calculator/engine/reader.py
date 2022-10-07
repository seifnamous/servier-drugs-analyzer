"""Reads drugs graph.
"""


def read(spark_session, drugs_graph_file_path: str):
    """_summary_

    Args:
        spark_session (_type_): _description_
        drugs_graph_file_path (str): _description_
    """
    return spark_session.read.json(drugs_graph_file_path)
    
    

    