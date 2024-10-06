import pandas as pd

def read_csv(file_path):
    """Read a CSV file and return a DataFrame."""
    return pd.read_csv(file_path)

def find_unique_values(df1, df2, column='entity_id'):
    """Find unique values in df1 that are not in df2."""
    return set(df1[column]) - set(df2[column])

def save_unique_values(unique_values, output_file):
    """Save unique values to a CSV file."""
    pd.DataFrame(list(unique_values), columns=['entity_id']).to_csv(output_file, index=False)

def compare_and_save_unique(file_path1, file_path2, output_file1, output_file2):
    """Compare two CSV files and save unique values to separate files."""
    df1 = read_csv(file_path1)
    df2 = read_csv(file_path2)
    
    unique_in_1 = find_unique_values(df1, df2)
    unique_in_2 = find_unique_values(df2, df1)
    
    save_unique_values(unique_in_1, output_file1)
    save_unique_values(unique_in_2, output_file2)

def filter_file(file_path, entity_ids_path, output_file):
    """Filter a file based on entity IDs and save the result."""
    df_entity_ids = read_csv(entity_ids_path)
    df_file = read_csv(file_path)

    ids_to_remove = set(df_entity_ids['entity_id'])
    filtered_df = df_file[~df_file['entity_id'].isin(ids_to_remove)]

    filtered_df.to_csv(output_file, index=False)
    print(f"Filtering complete. Results saved to {output_file}")

def filter_by_description(file_path, description, output_file):
    """Filter a file by description and save the result."""
    df_file = read_csv(file_path)
    filtered_df = df_file[df_file['description'] == description]
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtering complete. Results saved to {output_file}")

def filter_other_payments(file_path, exclude_descriptions, output_file):
    """Filter payments excluding specified descriptions and save the result."""
    df_file = read_csv(file_path)
    other_payments = df_file[~df_file['description'].isin(exclude_descriptions)]
    other_payments.to_csv(output_file, index=False)
    print(f"Filtering complete. Results saved to {output_file}")


compare_and_save_unique('data/razorpay.csv', 'data/platform.csv', 'unique_in_razorpay.csv', 'unique_in_platform.csv')

# Entity_ids are additional ids that are in platform entries but not in razorpay entries
# filter_file('data/razorpay.csv', 'unique_in_razorpay.csv', 'filtered_file_razorpay2.csv')

# filter_by_description('filtered_file_razorpay2.csv', '{description}', '{output_file}')

# filter_other_payments('filtered_file_razorpay2.csv', ['QRv2 Payment', 'FOSS United Event'], 'other_payments.csv')

