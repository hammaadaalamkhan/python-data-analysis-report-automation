import csv


def read_data(filepath):
    data = []

    try:
        with open('data/customers-100.csv', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row['Sales'] = int(row['Sales'])
                    data.append(row)
                except ValueError:
                    print("Invalid sales value found.")

    except FileNotFoundError:
        print("CSV file not found.")

    return data
