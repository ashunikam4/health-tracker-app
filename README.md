# Health Tracker App

This is a simple health tracking app made using **Python**. It is basically a **command line tool** which takes user workout data input from **stdin**, and outputs various **statistics** based on the data. 

This work was done as part of the capstone project for a **Core Python training course**.

## Prerequisites
* Python 3
* Python-venv

## Build
```bash
~$ git clone https://github.com/ashunikam4/health-tracker-app.git
~$ python3 -m venv health_tracker_env
~$ source health_tracker_env/bin/activate
~$ cd health-tracker-app
~$ pip install -r requirements.txt
```

## Usage
```
~$ python health_tracker.py
```
### Input
1. User will be prompted to enter : *name, gender, age, weight and height*
2. Then user will be prompted to enter daily workout records
3. Record input format : *day_id, steps, duration*

    * *day_id* : 1 for Monday, 2 for Tuesday, and so on
    * *steps* : number of steps taken that day
    * *duration* : time taken for *steps*
4. Once user has given enough records, they can press ENTER to get output

### Output
1. **BMI and weight category**.
2. Workout statistics over **last 7 days, last 30 days and over entire period**. Statistics consists of:
    * Minimum, Maximum, and Average speed
    * Minimum, Maximum and Average distance
2. **Badge based on workout data**: The badge types and conditions for badge assignment are given below:
    * *No Badge* : If breaks in last 7 days
    * *APPRENTICE* : No breaks in last 14 days.
    * *PILGRIM* : No breaks in last 7 days.
    * *CHAMP* : Maximum 2 breaks in last 30 days.
    * *HERO* : Maximum 2 breaks in last 60 days.
    * *MONK* : Maximum 2 breaks in last 120 days.
    * *BEAST* : Maximum 2 breaks in last 240 days.
3. **Streaks**: shows current streak length, best streak length over last 30 days and best streak length overall.

### Sample 
```
$ python health_tracker.py
Welcome to the Health Tracker App!

Please enter the following details:
Enter your name: Thor Odinson
Enter your gender(M/F/O): M
Enter your age(years): 1057
Enter your weight(kgs): 290.3
Enter your height(cms): 198.1

Please enter the workout records:
Refer tracker docs for record format
Enter day 1 workout details, press ENTER to finish:1, 7500, 1:02:05 
Enter day 2 workout details, press ENTER to finish:2, 8500, 1:06:12 
Enter day 3 workout details, press ENTER to finish:3, 3500, 0:52:25
Enter day 4 workout details, press ENTER to finish:4, 4250, 0:59:35 
Enter day 5 workout details, press ENTER to finish:5, 7800, 1:01:55 
Enter day 6 workout details, press ENTER to finish:6, 8500, 1:12:15 
Enter day 7 workout details, press ENTER to finish:7, 9500, 1:15:25 

Enter day 8 workout details, press ENTER to finish:
Hi, Thor Odinson
Your BMI : 74.0
You need to urgently cut down weight,otherwise you might suffer from heart diseases

------- Workout stats over last 7 days -------
Max distance (km): 7.24
Min distance (km): 2.67
Avg distance (km): 5.39
Max speed (km/h) : 5.87
Min speed (km/h) : 3.05
Avg spped (km/h) : 4.94

------- Workout stats over last 30 days -------
Max distance (km): 7.24
Min distance (km): 2.67
Avg distance (km): 5.39
Max speed (km/h) : 5.87
Min speed (km/h) : 3.05
Avg spped (km/h) : 4.94

------- Overall Workout stats -------
Max distance (km): 7.24
Min distance (km): 2.67
Avg distance (km): 5.39
Max speed (km/h) : 5.87
Min speed (km/h) : 3.05
Avg spped (km/h) : 4.94

Your current badge: APPRENTICE
Lets keep at this, and get to the next badge

------- Streaks data ------
Current streak : 7
Best streak in last 30 days: 7
Best overall streak : 7

```

## Run Tests
1. Check `tests/input/*.txt` for testcases
2. Run tests
    ```
    ~$ bash tests/test.sh
    ```
3. Check `tests/output/*.txt` for results