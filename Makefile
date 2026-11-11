PYTHON ?= python3

P01 := projects/01_data_quality_pipeline
P02 := projects/02_imbalance_encoding_scaling
P03 := projects/03_anomaly_detection_isolation_forest
P04 := projects/04_lead_time_xgboost
P05 := projects/05_cv_segmentation_metrics
P06 := projects/06_llm_guardrails_agent

.PHONY: run-01 run-02 run-03 run-04 run-05 run-06 test test-01 test-02 test-03 test-04 test-05 test-06

run-01:
	$(PYTHON) -m pip install -r $(P01)/requirements.txt
	$(PYTHON) $(P01)/run.py

run-02:
	$(PYTHON) -m pip install -r $(P02)/requirements.txt
	$(PYTHON) $(P02)/run.py

run-03:
	$(PYTHON) -m pip install -r $(P03)/requirements.txt
	$(PYTHON) $(P03)/run.py

run-04:
	$(PYTHON) -m pip install -r $(P04)/requirements.txt
	$(PYTHON) $(P04)/run.py

run-05:
	$(PYTHON) -m pip install -r $(P05)/requirements.txt
	$(PYTHON) $(P05)/run.py

run-06:
	$(PYTHON) $(P06)/run.py

test: test-01 test-02 test-03 test-04 test-05 test-06

test-01:
	$(PYTHON) -m pip install -r $(P01)/requirements.txt
	PYTHONPATH=$(P01) $(PYTHON) -m unittest discover -s $(P01)/tests -v

test-02:
	$(PYTHON) -m pip install -r $(P02)/requirements.txt
	PYTHONPATH=$(P02) $(PYTHON) -m unittest discover -s $(P02)/tests -v

test-03:
	$(PYTHON) -m pip install -r $(P03)/requirements.txt
	PYTHONPATH=$(P03) $(PYTHON) -m unittest discover -s $(P03)/tests -v

test-04:
	$(PYTHON) -m pip install -r $(P04)/requirements.txt
	PYTHONPATH=$(P04) $(PYTHON) -m unittest discover -s $(P04)/tests -v

test-05:
	$(PYTHON) -m pip install -r $(P05)/requirements.txt
	PYTHONPATH=$(P05) $(PYTHON) -m unittest discover -s $(P05)/tests -v

test-06:
	PYTHONPATH=$(P06) $(PYTHON) -m unittest discover -s $(P06)/tests -v