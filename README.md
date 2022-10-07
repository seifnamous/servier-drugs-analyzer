# Drugs Analyzer

Service that analyzes mentions of drugs in publications & journals.

## Description

This service is composed of two single responsability modules:

* graph-builder: takes as input three CSV's (clinical_trials.csv, drugs.csv, pubmed.csv) and outputs a JSON that represents the existing links between drugs, pubmeds, clinical trials and journals.
```
Example of output:
{"publication_id":"1","publication_type":"pubmed","publication_title":"A 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations","publication_date":"01/01/2019","journal_name":"Journal of emergency nursing","mentioned_drugs":["diphenhydramine"]}
{"publication_id":"2","publication_type":"pubmed","publication_title":"An evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.","publication_date":"01/01/2019","journal_name":"Journal of emergency nursing","mentioned_drugs":["diphenhydramine"]}
```
* kpi-calculator: takes as input the graph generated by the previous service and outputs the journal that mentions the largest number of distinct drugs.
```
Example of output:
{"journal_name":"Psychopharmacology","mentioned_drugs":["tetracycline","ethanol"],"number_of_distinct_drugs":2}
```

## Getting Started

### Installing
* Requirements: poetry (dependency management): https://pypi.org/project/poetry/

* To run graph-builder:

```
cd path/graph-builder
poetry install
poetry run build-and-persist-graph \
  -d <path_to_drugs_csv> \
  -p <path_to_pubmed_csv> \
  -c <path_to_clinical_trials_csv> \
  -o <path_to_ouput_graph_json>
```

* To run kpi-calculator:

```
cd path/kpi-calculator
poetry install
poetry run compute-and-persist-kpi \
  -g <path_to_pubmed_csv> \
  -o <path_to_ouput_kpi_json> 
```

# Version History
* 0.1.0
    * Initial Release

# Scalability

* Increase the resources allocated to the computing cluster
* Use an hybrid raw/column-oriented storage format like parquet
* Maximise parallelism by splitting datasets into relevant number of partitions
* Tune shuffle param: spark.sql.shuffle.partitions
* Cache intermediate results
* Use Broadcast Hash Joins

