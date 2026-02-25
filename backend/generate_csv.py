def generate_csv(RESULTS_DIR, record,processed_records):
    import csv
    import os
    
    csv_path = os.path.join(RESULTS_DIR, "usuarios_corporativos.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=record.keys())
            writer.writeheader()
            writer.writerows(processed_records)