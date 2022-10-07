"""Finds journal with biggest number of mentioned drugs.
"""

from pyspark.sql.functions import *
from pyspark.sql.types import *

import functools


def fudf(val):
    return functools.reduce(lambda x, y:x+y, val)

flattenUdf = udf(fudf, ArrayType(StringType()))


def find_most_drugs_mentioning_journal(df_graph):
    return df_graph \
            .select('journal_name', 'mentioned_drugs') \
            .groupBy("journal_name").agg(collect_list("mentioned_drugs")) \
            .select("journal_name", flattenUdf("collect_list(mentioned_drugs)")) \
            .withColumnRenamed('fudf(collect_list(mentioned_drugs))', 'mentioned_drugs') \
            .withColumn("number_of_distinct_drugs", size(array_distinct("mentioned_drugs"))) \
            .orderBy(desc('number_of_distinct_drugs')) \
            .limit(1)
