if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


list_of_dates = ["2020-10", "2020-11", "2020-12"]
cols_with_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]


import pandas as pd


def df_loader(date_of_the_file):
    file_to_download = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{date_of_the_file}.csv.gz"

    df = pd.read_csv(
        file_to_download,
        parse_dates=cols_with_dates,
        compression="gzip"
        )
    
    return df



@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    df_final = pd.DataFrame()

    print("Test del df_final")
    print(df_final)
    print("")

    print("final del test de df_final")
    print("")
    print("")

    for file_date in list_of_dates:

        print("")
        print(f"Comienza el LOOP -----{file_date}----------------------")

        print("")
        print("----")
        print("comienza el test del loop")

        df_mes = df_loader(file_date)
        print(f"Se creó el df para {file_date}, contiene un shape de: {df_mes.shape}")
        print("")
        print("")

        print("----")
        print("Comienza el test del concat")
        df_final = pd.concat([df_final, df_mes])
        print("")
        print(f"Hasta acá se hizo el concat hasta {file_date}, y la df_final contiene un shape de: {df_final.shape}")

    print("")
    print("")
    print("------Test Final-----------")
    print("")
    print(f"La df final tiene un shape de: {df_final.shape}")
    print("")
    print(f"Que tipos de datos contiene la df_final?")
    print(f"{df_final.info()}")
    print("")
    print("------fin del test-----------")

    return df_final


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
