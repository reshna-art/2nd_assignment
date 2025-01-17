import csv

# Function to read and process the CSV file
def read_and_process_csv(file_path):
    try:
        # Open the CSV file
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Process each row
            print("Employees older than 30:")
            for row in reader:
                if int(row['age']) > 30:
                    print(row['name'])
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except KeyError as e:
        print(f"Missing column in CSV file: {e}")
    except ValueError:
        print("Invalid data format in CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'employees.csv'  # Replace with the path to your CSV file
read_and_process_csv(file_path)