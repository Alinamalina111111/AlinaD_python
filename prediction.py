import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
from datetime import datetime
from statistics import ClientDatabase
 
class Prediction:
    def __init__(self, db_name):
        self.db = ClientDatabase(db_name)
        self.db.create_table()
 
    def load_data(self, csv_file):
        df = pd.read_csv(csv_file)
        return df
 
    def preprocess_data(self, df):
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.strftime('%Y-%m')
        return df
 
    def predict(self, df):
        df = df.rename(columns={'month': 'ds', 'visits': 'y'})
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=12, freq='M')
        forecast = model.predict(future)
        return forecast
 
    def visualize(self, forecast):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(forecast['ds'], forecast['yhat'], label='Predicted', color='b')
        ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='lightblue')
        ax.set_xlabel('Date')
        ax.set_ylabel('Visits')
        plt.legend()
        plt.show()
 
    def run(self, csv_file):
        df = self.load_data(csv_file)
        df = self.preprocess_data(df)
        self.db.insert_client("Example Client", 100, "2023-01")  # Добавим пример данных в базу
        data = self.db.fetch_data()
        df = pd.DataFrame(data, columns=["ds", "y"])
        forecast = self.predict(df)
        self.visualize(forecast)
 
if __name__ == "__main__":
    prediction = Prediction("client_data.db")
    prediction.run("client_data.csv")
