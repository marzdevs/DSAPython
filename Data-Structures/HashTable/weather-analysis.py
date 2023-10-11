import csv

class WeatherAnalysis:
    def readThis(self):
        total_temperature = 0  # Initialize the total temperature
        max_temperature = None  # Initialize the maximum temperature to None

        with open('nyc_weather.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for index, row in enumerate(csvreader):
                temperature = float(row['temperature(F)'])  # Convert temperature to a float
                total_temperature += temperature  # Add the temperature to the total

                if index == 0 or temperature > max_temperature:
                    max_temperature = temperature  # Update max_temperature if a higher temperature is encountered

        average_temperature = total_temperature / (index + 1)  # Calculate the average
        print(f'Average temperature for the week: {average_temperature:.2f}°F')

        print(f'Maximum temperature for the week: {max_temperature:.2f}°F')




if __name__ == '__main__':
    t = WeatherAnalysis()
    t.readThis()
