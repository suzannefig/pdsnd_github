import time
import datetime
import pandas as pd
import numpy as np
df = pd.read_csv('chicago.csv')
df = pd.read_csv('new_york_city.csv')
df = pd.read_csv('washington.csv')
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
def get_filters():
    city = ("chicago", "new york", "washington")
    month = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "november", "december", "all")
    day = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all")       
print('Hello! Let\'s explore some US bikeshare data!')
def get_city(): 
    CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }    
    while True:
        city = input("What city would you like to explore?")
        month = input("What month would you like to explore?")
        day = input("Which day would you like to filter by?")
        city_input = ''
        if city.lower() == 'chicago':'chicago.csv'
        if city.lower() == 'new york':'new_york_city.csv'
        if city.lower() == 'washington':'washington.csv'
        if city.lower() not in ("chicago","new york","washington"):
            print('Please enter chicago, new york or washington')
def get_month(df):
    df = df[df['month'] == month]
    df['Start Time'] = pd. to_datetime(df['Start Time'])
while True:
    month = input("What month would you like to filter by?")
    month_input = ''
    months_dict = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',           'december'}
while month_input.lower() not in months_dict.keys( 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
    print('Error')
def get_day(df):
    while True:         
        day = input("Which day would you like to filter by?")
        day_input = ''
        days_dict = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    while day.lower() not in day ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        if city.lower() == 'chicago': 'chicago.csv'
        if city.lower() == 'new york': 'new_york_city.csv'
        if city.lower() == 'washington': 'washington.csv'
def load_data(city, month, day):
    df = pd.read_csv('chicago')
    df = pd.read_csv('new york')
    df = pd.read_csv('washington')
    print( '_' * 40)   
def time_stats(df):
    df = pd.read_csv('chicago.csv')
    df = pd.read_csv('new_york_city.csv')
    df = pd.read_csv('washington.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start-_Time'].dt.hour
popular_hour = df['hour'].mode()[0]
print('Most Popular Start Hour: ', popular_hour)
time_period = get_time_period()
if time_period == 'none':
    df_filtered = df
elif time_period == 'month' or time_period == 'day':
    if time_period == 'month':
        filter_lower, filter_upper = get_month()
elif time_period == 'day':
    filter_lower, filter_upper = get_day()
    df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]      
print('\nCalculating The Most Frequent Times of Travel...\n')
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def station_stats(df):
    popular_stations(df_filtered)
print('\nCalculating The Most Popular Start Stations and Trip...\n')
start_time = time.time()
popular_trip(df_filtered)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def trip_duration_stats(df):
    trip_duration(df_filtered)
print('\nCalculating Trip Duration...\n')
start_time = time.time()
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def user_stats(df):
    users(df_filtered)
print('\nCalculating User Stats...\n')
start_time = time.time()
users(df_filtered)
gender(df_filtered)
birth_years(df_filtered)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
def raw_data(df):
    def is_valid(raw_data):
        if raw_data.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
while valid_input == False:
    display = input('\nWould you like to view individual trip data?''Type \'yes\'or \'no\'.\n')
    valid_input = is_valid(raw_data)
if valid_input == True:

    print('Please type \'yes\'or \'no\'.\n')
def main():
    while True:
     city, month, day = get_filters()
     df = load_data(city, month, day)
     time_stats(df)
     station_stats(df)
     trip_duration_stats(df)
     user_stats(df)
     restart = input('\nWould you like to restart? Enter yes or no.\n')
if restart.lower() != 'yes':
    main()                            
if __name__ == "__main__":
    main()
