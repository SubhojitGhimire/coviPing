import requests
import time
from win10toast import ToastNotifier

API_URL = "https://disease.sh/v3/covid-19/all" # API endpoint for global COVID-19 data.

NOTIFICATION_TITLE = "COVID-19 Global Update"
NOTIFICATION_DURATION_SECONDS = 10 # Duration the notification stays on screen.
REFRESH_INTERVAL_SECONDS = 3600 # Updates and Notifies hourly.

def get_covid_data(url: str) -> dict | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    notifier = ToastNotifier()
    print("Starting COVID-19 notifier. A notification will be shown shortly.")
    print(f"Data will be refreshed every {REFRESH_INTERVAL_SECONDS // 60} minutes.")

    while True:
        print("\nFetching latest COVID-19 data...")
        data = get_covid_data(API_URL)

        if data:
            try:
                message = (
                    f"Confirmed Cases: {data['cases']:,}\n"
                    f"Total Deaths: {data['deaths']:,}\n"
                    f"Total Recovered: {data['recovered']:,}"
                )
                print("Data fetched successfully. Showing notification.")
                
                notifier.show_toast(
                    title=NOTIFICATION_TITLE,
                    msg=message,
                    duration=NOTIFICATION_DURATION_SECONDS,
                    icon_path="corona.ico" # Icon that shows on minimised/hidden tray.
                )
            except KeyError:
                print("Error: API data structure has changed. Unable to parse.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Could not retrieve data. Will try again after the interval.")

        print(f"Sleeping for {REFRESH_INTERVAL_SECONDS} seconds...")
        time.sleep(REFRESH_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()