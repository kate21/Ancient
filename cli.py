#User client

#Input - month, department

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="A script to process birthday and anniversary reports by departments.")
    parser.add_argument("month", help="Month to filter data (e.g., april)")
    parser.add_argument("department", help="department to filter data(e.g.HR)")
    args = parser.parse_args()

    base_url = "http://localhost:5000"

    def get_birthdays(month, department):
        url = f"{base_url}/birthdays"
        params = {"month": month, "department": department}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            print("Birthdays:")
            print(response.json())
        elif response.status_code == 404:
            print("No birthdays found for the given criteria.")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    def get_anniversaries(month, department):
        url = f"{base_url}/anniversaries"
        params = {"month": month, "department": department}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            print("Anniversaries:")
            print(response.json())
        elif response.status_code == 404:
            print("No anniversaries found for the given criteria.")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    print(f"Fetching birthdays and anniversaries for {args.month} in {args.department} department:")
    get_birthdays(args.month, args.department)
    get_anniversaries(args.month, args.department)

if __name__ == '__main__':
    main()