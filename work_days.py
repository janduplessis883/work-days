import sys
import datetime

# List of holidays to exclude from workdays calculation
holidays = [datetime.date(2023, 4, 14), datetime.date(2023, 5, 1), datetime.date(2023, 6, 5)]

def workdays_between_dates(start_date, end_date):
    days = (end_date - start_date).days + 1  # Add 1 to include both start and end dates
    weekdays = 0
    for i in range(days):
        date = start_date + datetime.timedelta(days=i)
        if date.weekday() < 5 and date not in holidays:
            weekdays += 1
    return weekdays

if len(sys.argv) == 3:
    start_date = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
    workdays = workdays_between_dates(start_date, end_date)
    print(f"Number of workdays between {start_date} and {end_date}: {workdays}")
else:
    print("Please provide start_date and end_date as command-line arguments.")
