import pyarrow as pa 
import pyarrow.parquet as pq
import pandas as pd

data = pd.read_csv("restaurant-menus.csv")

table = pa.Table.from_pandas(data)

pq.write_table(table, "uberEats-menus.parquet")

