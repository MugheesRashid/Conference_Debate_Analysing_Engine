import pandas as pd

def load_data(file_path):
    try:
        file = pd.read_csv(file_path)
        df = pd.DataFrame(file)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None