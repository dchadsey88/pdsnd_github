import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, Washington, or New York City? ")
        city = city.lower()
        if city == "chicago":
            print("The current city is {}".format(city))
            break
        elif city == "washington":
            print("The current city is {}".format(city))
            break
        elif city == "new york city":
            print("The current city is {}".format(city))
            break
        else:
            print("I'm sorry, the name you entered did not match.  Please try again.")
    df = pd.read_csv(CITY_DATA[city])
    # get user input for month (all, january, february, ... , june)
    while True:
        type_of_filter = input("Would you like to filter the data by month, day, or not at all?  Type \"none\" for no time filter. ")

        if type_of_filter == "month":
            while True:
                month = input("Which month? January, February, March, April, May, or June? ")
                month = month.lower()
                if month in ["january","february","march","april","may","june"]:
                    print("We will filter by {}".format(month.title()))
                    day = "all"
                    break
                else:
                    print("I'm sorry, I cannot recognize that month.  Please try again")
            break
        elif type_of_filter == "day":
            while True:
                day = input("Which day? ")
                day = day.lower()
                if day in ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]:
                    print("We will filter by {}".format(day))
                    month = "all"
                    break
                else:
                    print("I'm sorry, I cannot recognize that day.  Please try again")
            break
        elif type_of_filter == "none":
            print("You have chosen to have no time filter")
            month = "all"
            day = "all"
            break
        else:
            print("I'm sorry, I cannot recognize your answer.  Please try again")

    print("You have chosen the city {}  and will sort by {} month(s) and {} day(s)".format(city, month, day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['Month'] == month]

    if day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)
        df = df.loc[df['Day of Week'] == day]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # display the most common month
    most_common_month = df['Month'].mode()[0]
    most_common_month = calendar.month_name[most_common_month]
    # display the most common day of week
    most_common_dow = df['Day of Week'].mode()[0]
    most_common_dow = calendar.day_name[most_common_dow]

    # display the most common start hour

    most_common_start_hour = df['Hour'].mode()[0]
    print('For your search criteria, the most comon month is {} the most common day of week is {} and the most popular hour is {}'.format(most_common_month, most_common_dow, most_common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print('The most common start station is {} and end station is {}'.format(most_common_start_station, most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_common_combo = df.groupby(['Start Station', 'End Station']).size().reset_index().max()

    print("The most popular start and stop stations respectively are\n", most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} minutes.'.format(total_travel_time))
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: {} "minutes.'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    for i in user_types.index:
        print('The number of', i,' is ', user_types[i])
    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        for i in gender.index:
            print('The number of',i ,'users is ', gender[i])
        # Display earliest, most recent, and most common year of birth
        earliest_dob = df['Birth Year'].min()
        print('The earliest year of birth is:',earliest_dob)
        most_recent_dob = df['Birth Year'].max()
        print('The most recent year of birth is:',most_recent_dob)
        most_common_dob = df['Birth Year'].mode()
        print('The most common year of birth is:',most_common_dob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    #shows the first 5 rows of Data
    print(df.head())
    n = 5
    while True:

        more_data = input('\nWould you like to show the next 5 rows of data?  Enter yes or no.\n')
        if more_data == "no":
            break
        else:
            print(df[n:n+5])
            n = n+5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
