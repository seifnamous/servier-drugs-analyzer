"""entry point.
"""

import argparse

from pyspark.sql.types import *
from pyspark.sql.functions import *

import logpatent.logger as lg

from graph_builder.spark import get_spark_session
from graph_builder.engine.constants import *
from graph_builder.engine import reader, graph_builder, writer


def build_and_persist_graph(
    drugs_file_path: str,
    pubmed_file_path:  str,
    clinical_trials_file_path: str,
    output_graph_file_path: str,
    log_format='%(asctime)s::%(env)s::%(levelname)s::%(message)s',
    log_level='INFO',
    env='dev'
):

    logger = lg.Logger(
        log_format=log_format,
        job_name='drugs_graph_builder',
        env=env,
        log_level=log_level,
    )
    logger.info('Job started')
    logger.info('Reading input data ...')

    spark_session = get_spark_session("drugs_graph_builder")

    df_drugs, df_pubmed , df_clinical_trials  = \
        reader.read(
            spark_session,
            drugs_file_path,
            pubmed_file_path,
            clinical_trials_file_path
        )
    
    # List of drugs that needs to fit in memory
    drugs = df_drugs.\
        filter(col('drug')\
            .isNotNull())\
            .select('drug')\
            .rdd.map(lambda x : x[0])\
            .collect()

    logger.info('Building graph ...')
   
    df_graph = graph_builder.find_drugs_in_publications(
        df_pubmed,
        df_clinical_trials,
        drugs
    )

    logger.info('Persisting graph ...')
    writer.write(df_graph, output_graph_file_path)

    logger.info('Job ended successfully')


def run():
    parser = argparse.ArgumentParser()

    parser.add_argument('--drugs_file_path', '-d')
    parser.add_argument('--pubmed_file_path', '-p')
    parser.add_argument('--clinical_trials_file_path', '-c')
    parser.add_argument('--output_graph_file_path', '-o')

    args = parser.parse_args()

    build_and_persist_graph(
        args.drugs_file_path,
        args.pubmed_file_path,
        args.clinical_trials_file_path,
        args.output_graph_file_path
    )

if __name__ == '__main__':
    run()