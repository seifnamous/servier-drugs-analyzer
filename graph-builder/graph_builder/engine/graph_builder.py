"""Finds the list of drugs mentioned in each publication.
"""

from typing import List

from pyspark.sql.functions import *
from pyspark.sql.types import *


def find_drugs_in_publication_title(publication_title: str, drug_names:  List[str]):
    """_summary_

    Args:
        publication_title (str): _description_
        drug_names (List[str]): _description_

    Returns:
        _type_: _description_
    """
    if not publication_title:
        return []
    else:
        return [
            drug_name.lower() for drug_name in drug_names
            if drug_name.lower() in publication_title.lower()
        ]


def find_drugs_in_publications(df_pubmed, df_clinical_trials, drug_names):
    """_summary_

    Args:
        df_pubmed (_type_): _description_
        df_clinical_trials (_type_): _description_
        drug_names (_type_): _description_

    Returns:
        _type_: _description_
    """
    udf_func = udf(
        lambda x: find_drugs_in_publication_title(x, drug_names), returnType=ArrayType(StringType())
    )

    return df_pubmed \
        .withColumn('mentioned_drugs', udf_func(df_pubmed.title)) \
        .withColumn('publication_type', lit('pubmed')) \
        .union(
            df_clinical_trials \
            .withColumn('mentioned_drugs', udf_func(df_clinical_trials.scientific_title)) \
            .withColumn('publication_type', lit('clinical_trial')) \
            .withColumnRenamed('scientific_title', 'title') \
        ) \
        .withColumnRenamed('title', 'publication_title') \
        .withColumnRenamed('date', 'publication_date') \
        .withColumnRenamed('id', 'publication_id') \
        .withColumnRenamed('journal', 'journal_name') \
        .select(
            'publication_id',
            'publication_type',
            'publication_title',
            'publication_date',
            'journal_name',
            'mentioned_drugs'
        )