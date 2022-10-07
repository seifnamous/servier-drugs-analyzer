"""_summary_
"""

from pathlib import Path

from graph_builder.spark import get_spark_session
from graph_builder.runner import build_and_persist_graph


BASE_PATH = str(Path(__file__).parent)


def test_build_and_persist_graph():
    spark_session = get_spark_session("drugs_graph_builder")
    build_and_persist_graph(
        f'{BASE_PATH}/resources/drugs.csv',
        f'{BASE_PATH}/resources/pubmed.csv',
        f'{BASE_PATH}/resources/clinical_trials.csv',
        f'{BASE_PATH}/resources/generated_drugs_graph.json'
    )
    generated_graph = spark_session.read.json(f'{BASE_PATH}/resources/generated_drugs_graph.json').collect()
    expected_graph = spark_session.read.json(f'{BASE_PATH}/resources/expected_drugs_graph.json').collect()
    assert generated_graph == expected_graph
