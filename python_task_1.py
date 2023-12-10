import pandas as pd
import numpy as np
def generate_car_matrix(df)->pd.DataFrame:

    csv_file_path = 'C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
    df = pd.read_csv(csv_file_path)
    """
    Creates a DataFrame for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Creating dataframe -

    new_df = pd.DataFrame(df['car'])

    # Pivot the DataFrame
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car')

    # Display the result
    pivot_df.values[[np.arange(len(pivot_df))] * 2] = 0
    print(pivot_df)
    return df


def get_type_count(df)->dict:
    csv_file_path = 'C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
    df = pd.read_csv(csv_file_path)
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    bins = [-float('inf'), 15, 25, float('inf')]
    labels = ['low', 'medium', 'high']

    df['car_type'] = pd.cut(df['car'], bins=bins, labels=labels, right=False, include_lowest=True)
    # Define a mapping of car types
    car_type_counts = df['car_type'].value_counts().to_dict()
    sorted_car_type_counts = dict(sorted(car_type_counts.items()))
    print(sorted_car_type_counts)
    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    csv_file_path = 'C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
    df = pd.read_csv(csv_file_path)

    def find_indices(df):
        mean_value = df['car'].mean()
        indices = df[df['car'] > 2 * mean_value].index
        return sorted(indices)

    result_indices = find_indices(df)
    print(result_indices)
    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    csv_file_path = 'C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
    df = pd.read_csv(csv_file_path)

    def filter_and_sort_routes(df):
        filtered_df = df[df['truck'].mean() > 7]
        sorted_routes = sorted(filtered_df['route'].tolist())
        return sorted_routes

    result_routes = filter_and_sort_routes(df)
    print(result_routes)
    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    csv_file_path = 'C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-1.csv'
    df = pd.read_csv(csv_file_path)
    column_data = df['id_2'].tolist()
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car')
    pivot_df = pivot_df.fillna(0)
    print(df)
    def multiply_matrix(value):
         if value > 20:
             return value * 0.75
         else:
             return value * 1.25

    df_result = pivot_df.applymap(multiply_matrix)
    # print("\nDataFrame after custom multiplication:")
    # print(df_result)
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    csv_file_path = pd.read_csv('C:/Users/Dr. Vaidya/Desktop/MapUp/MapUp-Data-Assessment-F/datasets/dataset-2.csv')
    df = pd.read_csv(csv_file_path)

    return pd.Series()
