import mlflow
from mlflow.tracking import MlflowClient

print("MLflow version:", mlflow.__version__)
print("Tracking URI:", mlflow.get_tracking_uri())

# Check experiments
client = MlflowClient()

# Check the experiment that main_1.py used
exp1 = client.get_experiment("0")  # Default experiment
print("\n=== Default Experiment (main_1.py) ===")
print(f"Name: {exp1.name}")
print(f"Artifact Location: {exp1.artifact_location}")

# Check the experiment that main_6.py used
exp2 = client.get_experiment_by_name('Breast-Cancer-Rf-HP-Tuning')
if exp2:
    print("\n=== Breast-Cancer Experiment (main_6.py) ===")
    print(f"Name: {exp2.name}")
    print(f"Artifact Location: {exp2.artifact_location}")

# Check a run from main_6.py
runs = client.search_runs(experiment_ids=[exp2.experiment_id], max_results=1)
if runs:
    print(f"\nRun artifact URI: {runs[0].info.artifact_uri}")