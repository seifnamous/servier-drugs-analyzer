"""Instantiates a spark session.
"""

from pyspark.sql import SparkSession


def get_spark_session(appname="app"):
    """_summary_

    Args:
        appname (str, optional): _description_. Defaults to "app".

    Returns:
        _type_: _description_
    """
    return (
        SparkSession
            .builder
            .appName(appname)
            .getOrCreate()
    )