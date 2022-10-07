"""Entry point.
"""

import argparse
import logpatent.logger as lg

from kpi_calculator.spark import get_spark_session
from kpi_calculator.engine import reader, calculator, writer


def compute_and_persist_kpi(
    drugs_graph_file_path: str,
    computed_kpi_file_path: str,
    log_format='%(asctime)s::%(env)s::%(levelname)s::%(message)s',
    log_level='INFO',
    env='dev'
):
    logger = lg.Logger(
        log_format=log_format,
        job_name='kpi_calculator',
        env=env,
        log_level=log_level,
    )

    logger.info('Job started')
    logger.info('Reading input data ...')
    spark_session = get_spark_session("drugs_kpi_calculator")
    df_graph = reader.read(spark_session, drugs_graph_file_path)
    df_kpi = calculator.find_most_drugs_mentioning_journal(df_graph)

    logger.info('Persisting kpi results to file ...')
    writer.write(df_kpi, computed_kpi_file_path)

    logger.info('Job successfully ended')


def run():
    parser = argparse.ArgumentParser()

    parser.add_argument('--drugs_graph_file_path', '-g')
    parser.add_argument('--computed_kpi_file_path', '-o')

    args = parser.parse_args()

    compute_and_persist_kpi(
        args.drugs_graph_file_path,
        args.computed_kpi_file_path,
    )

if __name__ == '__main__':
    run()