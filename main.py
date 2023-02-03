from data_manager import DataManager


data_manager = DataManager()


ORIGIN_CITY_IATA = input('Enter your Departure airport IATA Code.')

data_manager.get_destination_data()
data_manager.get_destination_cities()
data_manager.post_destination_cities()