"""Main file for Health tracker app"""

import sys
from utils import input_positive, parse_record
from user import WeightCategory, User
from record_db import WorkoutRecordDB

# Take user details (stdout)
print('Welcome to the Health Tracker App!\n')
print('Please enter the following details:')
uname =  input('Enter your name: ')
usex =  input('Enter your gender(M/F/O): ')
uage = int(input_positive('age(years)'))
uweight = input_positive('weight(kgs)')
uheight = input_positive('height(cms)')
print()
user = User(uname, usex, uage, uweight, uheight)

# Take workout details (stdin)
print('Please enter the workout records:')
print('Refer tracker docs for record format')
irec = 1
db = WorkoutRecordDB()
while True:
    rec = input('Enter day {} workout details, press ENTER to finish:'.format(irec))
    if not rec:
        break
    rec = parse_record(rec)
    db.add_record(rec)  # Add each record to db
    irec += 1

if not db.db:
    print("No workout data entered. Exiting ...\n")
    sys.exit(0)

# Build dataframe from the added data
db.build_db()
print()

# Output various stats (stdout)
print('Hi, {}'.format(user.name))
print('Your BMI : {0:.1f}'.format(user.get_bmi()))
wcategory = user.get_category()
if wcategory == WeightCategory.UNDERWEIGHT:
    print('Try putting on some weight\n')
elif wcategory == WeightCategory.NORMAL:
    print('Your weight is perfect. Keep it up!\n')
elif wcategory == WeightCategory.OVERWEIGHT:
    print('You need to lose some weight\n')
else:
    print('You need to urgently cut down weight,' +  
            'otherwise you might suffer from heart diseases\n')

print('------- Workout stats over last 7 days -------')
stats = db.get_week_stats()
print('Max distance (km): {0:.2f}'.format(stats.max_dist))
print('Min distance (km): {0:.2f}'.format(stats.min_dist))
print('Avg distance (km): {0:.2f}'.format(stats.avg_dist))
print('Max speed (km/h) : {0:.2f}'.format(stats.max_speed))
print('Min speed (km/h) : {0:.2f}'.format(stats.min_speed))
print('Avg spped (km/h) : {0:.2f}'.format(stats.avg_speed))
print()

print('------- Workout stats over last 30 days -------')
stats = db.get_month_stats()
print('Max distance (km): {0:.2f}'.format(stats.max_dist))
print('Min distance (km): {0:.2f}'.format(stats.min_dist))
print('Avg distance (km): {0:.2f}'.format(stats.avg_dist))
print('Max speed (km/h) : {0:.2f}'.format(stats.max_speed))
print('Min speed (km/h) : {0:.2f}'.format(stats.min_speed))
print('Avg spped (km/h) : {0:.2f}'.format(stats.avg_speed))
print()

print('------- Overall Workout stats -------')
stats = db.get_overall_stats()
print('Max distance (km): {0:.2f}'.format(stats.max_dist))
print('Min distance (km): {0:.2f}'.format(stats.min_dist))
print('Avg distance (km): {0:.2f}'.format(stats.avg_dist))
print('Max speed (km/h) : {0:.2f}'.format(stats.max_speed))
print('Min speed (km/h) : {0:.2f}'.format(stats.min_speed))
print('Avg spped (km/h) : {0:.2f}'.format(stats.avg_speed))
print()

# Refer docs for logic behind badge assignment
badge = db.get_badge()
if badge is None:
    print('You do not have any badges at this moment.')
    print('Show more consistency to win badges.')
else:
    print('Your current badge: {}'.format(badge))
    if badge != 'BEAST':
        print('Lets keep at this, and get to the next badge')
print()

print('------- Streaks data ------')
print('Current streak : {}'.format(db.get_current_streak()))
print('Best streak in last 30 days: {}'.format(db.get_month_streak()))
print('Best overall streak : {}'.format(db.get_overall_streak()))
print()