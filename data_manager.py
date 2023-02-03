import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/7c30210397895aa36f9a0ab7fbbbe7d6/flightdeals/prices'



class DataManager:

    def _init_(self):
        self.destination_data = {}
        self.destinations = []
        self.destination_budgets = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        self.destinations = [x['city'] for x in self.destination_data]
        return self.destination_data

    def get_destination_cities(self):
        no_of_cities = int(input('Enter how many no. of cities you wanna travel?'))
        dest_city = []
        dest_budget = []
        for i in range(no_of_cities):
            city = input(f'Enter City Name{i+1}')
            if city in self.destinations:
                print("City alredy in List")
                break
            else:
                budget = input(f"Enter your Budget for {city}")
            dest_city.append(city)
            dest_budget.append(budget)
        self.destinations = dest_city
        self.destination_budgets = dest_budget


    def post_destination_cities(self):
        for city in range(len(self.destinations)):
            new_data = {
                "price": {
                    "city": self.destinations[city],
                    "lowestprice": self.destination_budgets[city]
                }
            }
            response = requests.post(
                url=f"{SHEETY_PRICES_ENDPOINT}",
                json=new_data
            )
            print(response.text)