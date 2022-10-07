"""Reads input csv data.
"""

from graph_builder.engine.schemas import *


def read(spark_session, drugs_file_path: str, pubmed_file_path:  str, clinical_trials_file_path: str):
    """_summary_

    Args:
        spark_session (_type_): _description_
        drugs_file_path (str): _description_
        pubmed_file_path (str): _description_
        clinical_trials_file_path (str): _description_

    Returns:
        _type_: _description_
    """
    
    df_drugs = spark_session.read.option('header', 'true').\
        csv(drugs_file_path, schema=drugs_schema)

    df_pubmed = spark_session.read.option('header', 'true').\
        csv(pubmed_file_path, schema=pubmed_schema)

    df_clinical_trials = spark_session.read.option('header', 'true').\
        csv(clinical_trials_file_path, schema=clinical_trials_schema)

    return df_drugs, df_pubmed, df_clinical_trials
    
    

    