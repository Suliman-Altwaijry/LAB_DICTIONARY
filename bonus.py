from datetime import date
from math import isfinite

weather = {}


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if any(c.isalpha() for c in text):
            return text
        print("Please enter a name or description containing letters.")


def read_date():
    while True:
        text = input("Date (YYYY-MM-DD, for example 2026-10-25): ").strip()
        try:
            if date.fromisoformat(text).isoformat() == text:
                return text
        except ValueError:
            pass
        print("Please enter a real date in YYYY-MM-DD format.")


def read_number(prompt, humidity=False):
    while True:
        try:
            number = float(input(prompt))
            if isfinite(number) and (not humidity or 0 <= number <= 100):
                return number
        except ValueError:
            pass
        print("Enter a number from 0 to 100." if humidity
              else "Enter a valid temperature, for example 25 or -3.5.")


def add_weather(update=False):
    print("\nUpdate a weather record" if update else "\nAdd a weather record")
    city = read_text("City name: ").title()
    day = read_date()
    # Challenge: update
    if update and day not in weather.get(city, {}):
        print(f"No record for {city} on {day}. Choose 1 to add it.")
        return

    temperature = read_number("Temperature in Celsius: ")
    humidity = read_number("Humidity (0-100%): ", humidity=True)
    condition = read_text("Weather condition (e.g., sunny or rainy): ")

    records = weather.setdefault(city, {})
    action = "Updated" if day in records else "Saved"
    records[day] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print(f"{action} weather for {city} on {day}.")


# Challenge: delete 
def delete_weather():
    print("\nDelete a weather record")
    city = read_text("City name: ").title()
    day = read_date()
    if day not in weather.get(city, {}):
        print(f"No record for {city} on {day}.")
        return

    
    del weather[city][day]

    if not weather[city]:
        del weather[city]
    print(f"Deleted weather for {city} on {day}.")


def query_weather():
    if not weather:
        print("\nNo records yet. Choose 1 to add your first weather record.")
        return
    print("\nAvailable cities: " + ", ".join(sorted(weather)))
    city = read_text("Enter a city name: ").title()
    if city not in weather:
        print(f"No records for {city}. Choose 1 to add weather for this city.")
        return
    print(f"\nWeather in {city}")
    for day, details in sorted(weather[city].items()):
        print(f"\nDate: {day}\n"
              f"Temperature: {details['temperature']:g} C\n"
              f"Humidity: {details['humidity']:g}%\n"
              f"Condition: {details['condition']}")


def main():
    print("Welcome to your Weather Book!")
    print("Records are kept until you close the program.")
    print("Adding the same city and date updates its record.")
    while True:
        print("\n1. Add weather\n2. Find weather by city"
              "\n3. Update weather\n4. Delete weather\n5. Exit")
        choice = input("Enter a choice (1-5): ").strip()
        if choice == "1":
            add_weather()
        elif choice == "2":
            query_weather()
        elif choice == "3":
            # Challenge: update 
            add_weather(update=True)
        elif choice == "4":
            # Challenge: delete 
            delete_weather()
        elif choice == "5":
            print("Goodbye😄")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
