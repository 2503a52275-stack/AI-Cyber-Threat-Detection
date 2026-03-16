import pandas as pd
from sklearn.ensemble import IsolationForest
import sys

# Check if a file path is provided (uploaded file)
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = "dataset/logs.csv"

# Load dataset
data = pd.read_csv(file_path)

# Create Isolation Forest model
model = IsolationForest(contamination=0.2, random_state=42)

# Train model
model.fit(data)

# Predict anomalies
predictions = model.predict(data)

# Count results
normal = list(predictions).count(1)
threat = list(predictions).count(-1)

# Print report
print("AI Cyber Threat Detection Report")
print("--------------------------------")
print("Total Logs:", len(predictions))
print("Normal Activity:", normal)
print("Threats Detected:", threat)