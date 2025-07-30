from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))



def calculate_future_date(currdate):
    days = int(input("Enter number of days to add to the current date: "))
    future_date = currdate + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))



def main():
    display_current_datetime()
    current_date = datetime.now()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
