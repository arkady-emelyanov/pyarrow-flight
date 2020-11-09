import pandas as pd
import pyarrow as pa
import pyarrow.flight as fl


class FlightServer(fl.FlightServerBase):
    def __init__(self):
        location = "grpc://127.0.0.1:9092"
        super(FlightServer, self).__init__(location=location)
        self.datasets = {}
        self.load_tickets()
        print("Listening on:", location)

    def load_tickets(self):
        df = pd.read_json("./data.jsonlines", lines=True)
        df_schema = pa.schema([
            pa.field("city", pa.string()),
            pa.field("population", pa.int64())
        ])

        self.datasets['cities'] = pa.Table.from_pandas(df, schema=df_schema)

    def do_get(self, context, ticket):
        dataset_name = ticket.ticket.decode('utf-8')
        print("Ticket:", dataset_name)
        if dataset_name not in self.datasets:
            raise fl.FlightUnavailableError

        dataset = self.datasets[dataset_name]
        return fl.RecordBatchStream(dataset)


def main():
    f = FlightServer()
    f.serve()


if __name__ == '__main__':
    main()
