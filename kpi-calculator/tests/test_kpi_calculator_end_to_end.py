"""_summary_
"""

from pathlib import Path

from kpi_calculator.spark import get_spark_session
from kpi_calculator.runner import compute_and_persist_kpi


BASE_PATH = str(Path(__file__).parent)


def test_compute_and_persist_kpi():
    spark_session = get_spark_session("drugs_graph_builder")
    compute_and_persist_kpi(
        f'{BASE_PATH}/resources/drugs_graph.json',
        f'{BASE_PATH}/resources/calculated_kpi.json'
    )
    calculated_kpi = spark_session.read.json(f'{BASE_PATH}/resources/calculated_kpi.json').collect()
    expected_kpi = spark_session.read.json(f'{BASE_PATH}/resources/expected_kpi.json').collect()
    assert calculated_kpi == expected_kpi
