if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def id_replacer(col_name):
    col_name = col_name.replace("ID", "_id")
    col_name =col_name.lower()
    return col_name


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    
    print(f"--------Data antes del filtro ---- su shape es: {data.shape}")

    data = data[data["passenger_count"] > 0]
    data = data[data["trip_distance"] > 0]

    print("")
    print(f"--------Data despues del filtro ---- su shape es: {data.shape}")


    print("")

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(f" Tipos de datos en Data - {data.info()}")

    print("")
    print("")
    print("-- Q5 Homework --")
    print("")
    print("")

    print(f"Los valores en VendorID (unique) son: {data.VendorID.unique()}")
    print("")

    print("-------------------------------------")
    print("")
    print("")

    print("Data columns:")
    print(f"{data.columns}")

    data.rename(id_replacer, axis="columns", inplace=True)

    # data.rename(str.lower, axis="columns", inplace=True)


    print("")
    print("")
    print("--+-+--+-+--+-+--+-+--+-+--+-+--+-+")
    print("")
    print("")
    print(f"---------nuevas cols name")
    print("")
    print(f"{data.columns}")
    print("")
    print("")

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_vendor(output, *args) -> None:
    assert output.vendor_id is not None, 'No existe vendor_id'

@test
def test_passenger_count(output, *args) -> None:
    assert output["passenger_count"].isin([0]).sum() == 0, 'hay viajes con 0 pasajeros'

@test
def test_trip_distance(output, *args) -> None:
    assert output["trip_distance"].isin([0]).sum() == 0, 'hay viajes con 0 distancia'
