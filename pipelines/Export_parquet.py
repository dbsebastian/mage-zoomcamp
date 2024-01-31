import pyarrow as pa
import pyarrow.parquet as pq

import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

path_to_export = "//home//src//datalake"

table_name = "green_taxi"

root_path = f"{path_to_export}//{table_name}"


@data_exporter
def export_data(data, *args, **kwargs):

    tabla = pa.Table.from_pandas(data)

    pq.write_to_dataset(
        tabla, 
        root_path=root_path,
        partition_cols=["lpep_pickup_date"]
        )
