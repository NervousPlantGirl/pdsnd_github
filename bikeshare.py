import time
import pandas as pd
import numpy as np

#Credits: Github repo by okaysidd and aritra96 were super helpful in getting me started and showed the many ways to answer the questions
#Credits: Udacity's 3 practice questions is establishing a base for those function bodies
#Credits: My local library's collection on python including: Python programming, Begin to code with python, Coding projects in python
#Credits: My husband's high school coding experience

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}

WEEK_DATA = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6, 'all': 7}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city = CITY_DATA[city]:
        print('Would you like to see data for Chicago, Washington or New York City?')
        city = input('Chicago, New York City, or Washington? ').lower()
        print('You have chosen {}.'.format(city))
        if city not in CITY_DATA:
            print('Invalid input. Please try again.')
        if 'Washington':
            print('WARNING! Lack of user data for Washington')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while month = MONTH_DATA[month]:
        print('What month would you like to filter by? Or all months?')
        month = input('january, february, march, april, may, june, all').lower()
        print('You have chosen {}.'.format(month))
        if month not in MONTH_DATA:
           print('Invalid input. Please try again.')
           continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day = DAY_DATA[day]:
        print('Which day of the week would you like to filter by? Or all days?)
        day = input('monday, tuesday, wednesday, thursday, friday, saturday, sunday, all').lower()
        print('You have chosen {}.'.format(day))
        if day not in WEEK_DATA:
           print('Invalid input. Please try again.')
           continue

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
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
       df = df[df['day_of_week'] == day]
    if month != 'all':
       df = df[df['month'] == month]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the most popular times of travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==pop_month:
            pop_month = num.title()
    print('The most common month for travel is {}'.format(pop_month))

    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num]==pop_day:
            pop_day = num.title()
    print('The most common day of week for travel is {}'.format(pop_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most popular stations and and trips...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print('The most common start station was {}.'.format(pop_start_station))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('The most common end station was {}.'.format(pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    pop_trip = df['Start Station'] + ' to ' + df['End Station'].mode()[0]
    print('The most common trip from start to end was {}.'.format(pop_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating trip duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel = df['Trip Duration'].sum()
    tot_mins = divmod(tot_travel, 60)
    print('The total travel time was {} minutes.'.format(tot_mins))

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    avg_mins = divmod(avg_travel, 60)
    print('The average travel time was {} minutes.'.format(avg_mins))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating user information...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df('User Type').count()
    print('The count of each user type are {}.'.format(user_type_count))

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('No gender data for this city')
    else:
        user_gender = df('Gender').count()
        print('The count of each gender are {}.'.format(user_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No birthday data for this city.')
    else:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_pop = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is {}.'.format(earliest))
        print('The most recent year of birth is {}.'.format(most_recent))
        print('The most common year of birth is {}.'.format(most_pop))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   #function that displays raw data upon request by the user
   def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None."""

    print('Would you like to read some of the raw data? Yes/No')

    rdata = input().lower()
    if choice=='yes' : choice=True
    elif choice=='no' : choice=False
    else:
        print('Invalid input. Please try again.')
        return

    if choice:
        while rdata:
            print(df.head()).range(5)
            choice = input('Would you like to see another five rows? Yes/No ').lower()
            if choice=='yes' :
                continue
            elif choice=='no' :
                break
            else:
                print('Invalid input. Please try again.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart?')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
