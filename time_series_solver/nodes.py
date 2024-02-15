from aineko.core.node import AbstractNode
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from tbats import TBATS
import numpy as np
import matplotlib.pyplot as plt
import time


class TimeSeriesPredictor(AbstractNode):

    def _pre_loop_hook(self, params=None):
        self.sample_period = params.get('sample_period', 7)
        self.sample_freq_hours = params.get('sample_freq_hours', 'H')
        self.model_type = params.get('model_type', 'ARIMA')
        self.timeseries_data_output_png = params.get('timeseries_data_output_png', 'timeseries_prediction.png')

    def _execute(self, params=None):
        cleaned_data_message = self.consumers['cleaned_historical_demand'].consume()
        if cleaned_data_message is None:
            return
        cleaned_data = cleaned_data_message.get('message')
        df = pd.DataFrame(cleaned_data, columns=['Date', 'Demand']).sort_values(by='Date').reset_index(drop=True)
        df1 = pd.DataFrame({'Demand': df.Demand.values}, index=pd.to_datetime(df.Date.values))

        if self.model_type == 'ARIMA':
            model = SARIMAX(df1['Demand'], order=(self.sample_period, 1, 0), seasonal_order=(self.sample_period, 1, 0, 24))
            results = model.fit()
            prediction = results.get_forecast(steps=7 * self.sample_period)
            forecasted_demand_list = prediction.predicted_mean.tolist()
        elif self.model_type == 'TBATS':
            estimator = TBATS(seasonal_periods=[self.sample_period])
            fitted_model = estimator.fit(df1['Demand'])
            forecasted_demand_list = fitted_model.forecast(steps=7 * self.sample_period)
        else:
            raise ValueError('Unsupported model type')

        forecasted_date = pd.date_range(start=df1.index.max(), periods=7 * self.sample_period, freq=self.sample_freq_hours)
        forecasted_date_str = forecasted_date.astype('str').to_list()

        self.producers['forecasted_demand'].produce({'Date': forecasted_date_str, 'Demand': forecasted_demand_list})

        plt.figure(figsize=(16, 6))
        plt.plot(df1.index, df1['Demand'], '.--', label='historical data')
        plt.plot(forecasted_date, forecasted_demand_list, '.--', color='#00c698', label='predicted data')
        plt.fill_between(forecasted_date, np.min(forecasted_demand_list) * 0.95, np.max(forecasted_demand_list) * 1.05, color='#00c698', alpha=0.1)
        plt.legend(loc='best')
        plt.xlabel('Date')
        plt.ylabel('Demand')
        plt.savefig(self.timeseries_data_output_png)
        self.log(f'SAVED FIGURE TO FILE {self.timeseries_data_output_png}')