from .functions import api_inputs,api_call,dataframe, calculations, hot_and_cold_graph, daily_avg_graph

(latitude, longitude, start_date, end_date) = api_inputs()
daily_data = api_call(latitude, longitude, start_date, end_date)



weather_df = dataframe(daily_data)

max_temp, min_temp, avg_max_temp, avg_min_temp, avg_temp, hottest_date, coldest_date, temp_range_avg = calculations(weather_df)

print(f"Here are the calculations of temperature made for the dates you have provided us \n Maximum Temperature : {max_temp} \n Minimum Temperature : {min_temp} \n Average Maximum Temperature : {avg_max_temp} \n Average Minimum Temperature : {avg_min_temp} \n Average Temperature : {avg_temp} \n Hottest Date:  {hottest_date} \n Coldest Date: {coldest_date} \n Average of Temperature Ranges: {temp_range_avg}")

hot_and_cold_graph(weather_df)

daily_avg_graph(weather_df)

weather_df.to_csv("data/weather_dataframe.csv")


