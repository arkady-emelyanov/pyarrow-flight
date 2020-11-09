import pandas as pd
import pyarrow as pa
import pyarrow.flight as fl


def main():
    client = fl.FlightClient(location="grpc://127.0.0.1:9092")
    batch_handler = client.do_get(fl.Ticket('cities')).read_all()
    df = batch_handler.to_pandas()
    print(df)


if __name__ == '__main__':
    main()
