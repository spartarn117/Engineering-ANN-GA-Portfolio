"""Review the metrics published in this portfolio; does NOT retrain ANN/GA."""
from pathlib import Path
import csv

project_dir = Path(__file__).resolve().parents[1] / 'ann-ga-hat-forming' / 'results'
with (project_dir / 'reported_test_r2.csv').open(encoding='utf-8-sig') as f:
    metrics = list(csv.DictReader(f))
assert len(metrics) == 7 and all(-1.0 <= float(m['test_r2']) <= 1.0 for m in metrics)
with (project_dir / 'reported_design_comparison.csv').open(encoding='utf-8-sig') as f:
    designs = {row['output']: row for row in csv.DictReader(f)}
assert len(designs) == 7
spring = designs['Theta2_out']
base_spring = abs(float(spring['baseline_prediction']) - float(spring['target']))
alt_spring = abs(float(spring['springback_priority_prediction']) - float(spring['target']))
base_height = abs(float(designs['H']['baseline_prediction']) - float(designs['H']['target']))
alt_height = abs(float(designs['H']['springback_priority_prediction']) - float(designs['H']['target']))
print('7 published Test R² entries loaded')
print(f'Predicted springback: {base_spring:.4f}° → {alt_spring:.4f}° ({100 * (1 - alt_spring/base_spring):.1f}% decrease)')
print(f'Predicted height absolute error: {base_height:.4f} → {alt_height:.4f} mm')
print('Note: recorded result consistency only; no new ANN training or Abaqus validation.')
