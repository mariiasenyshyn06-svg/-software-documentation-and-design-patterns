import csv

class DataReader:
    def read(self, file_path):
        data = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append({
                    "borough": row.get("BORO", "UNKNOWN"),
                    "count": 1
                })

        return data