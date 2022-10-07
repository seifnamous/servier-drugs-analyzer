"""Definition of input data schemas.
"""


from pyspark.sql.types import *

from graph_builder.engine.constants import *


clinical_trials_schema = StructType([
        StructField(CLINICAL_TRIALS_ID_COLUMN_NAME, StringType(), True),
        StructField(CLINICAL_TRIALS_TITLE_COLUMN_NAME, StringType(), True),
        StructField(CLINICAL_TRIALS_DATE_COLUMN_NAME, StringType(), True),
        StructField(CLINICAL_TRIALS_JOURNAL_COLUMN_NAME, StringType(), True),
])

drugs_schema = StructType([
        StructField(DRUGS_ATCCODE_COLUMN_NAME, StringType(), True),
        StructField(DRUGS_NAME_COLUMN_NAME, StringType(), True)
])

pubmed_schema = StructType([
        StructField(PUBMED_ID_COLUMN_NAME, StringType(), True),
        StructField(PUBMED_TITLE_COLUMN_NAME, StringType(), True),
        StructField(PUBMED_DATE_COLUMN_NAME, StringType(), True),
        StructField(PUBMED_JOURNAL_COLUMN_NAME, StringType(), True),
])