# my bae in ilford  51.5577 &  0.0728

from .functions import api_inputs,api_call,dataframe, calculations, hot_and_cold_graph, daily_avg_graph

(latitude, longitude, start_date, end_date) = api_inputs()
daily_data = api_call(latitude, longitude, start_date, end_date)



weather_df = dataframe(daily_data)

max_temp, min_temp, avg_max_temp, avg_min_temp, avg_temp, hottest_date, coldest_date, temp_range_avg = calculations(weather_df)


hot_and_cold_graph(weather_df)

daily_avg_graph(weather_df)


