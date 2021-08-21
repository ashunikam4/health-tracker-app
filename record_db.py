import pandas as pd
import numpy as np 
from enum import Enum
from collections import namedtuple

# Namedtuple for workout stats entity
WOStats = namedtuple('WOStats', ['max_dist', 'min_dist', 'avg_dist', \
                        'max_speed', 'min_speed', 'avg_speed'])

class WorkoutRecordDB(object):
    """Object for storing/processing workout records."""

    def __init__(self):
        self.db = []
        self.streak = None

    def add_record(self, rec):
        """Store record."""
        self.db.append(rec)

    def build_db(self):
        """Build dataframe for further processing."""
        self.db = pd.DataFrame(self.db, columns=['day', 'steps', 'duration'])

        # 0 values -> missing data 
        self.db = self.db.replace(0, np.NaN)

        # Computing distance (kms) assuming 0.762 m per step 
        self.db = self.db.assign(distance = self.db['steps'] * 0.000762)

        # Computing speed
        self.db = self.db.assign(speed = self.db['distance'].divide(self.db['duration']))
    
    def __get_stats_on_series(self, ser):
        """Series stats util method"""
        return ser.max(), ser.min(), ser.mean()

    def __get_wo_stats(self, df):
        """Get distance & speed stats in a given period"""
        max_dist, min_dist, avg_dist = self.__get_stats_on_series(df["distance"])
        max_speed, min_speed, avg_speed = self.__get_stats_on_series(df["speed"])
        return WOStats(max_dist, min_dist, avg_dist, max_speed, min_speed, avg_speed)

    def get_week_stats(self):
        """Get week stats"""
        return self.__get_wo_stats(self.db[-7:])

    def get_month_stats(self):
        """Get month stats"""
        return self.__get_wo_stats(self.db[-30:])

    def get_overall_stats(self):
        """Get overall stats"""
        return self.__get_wo_stats(self.db)

    def __count_breaks(self, period):
        """Count number of no-workout days in a period"""
        # Should have provided data for the entire period
        if len(self.db) < period: 
            return float('inf')
        return self.db.loc[-period:, 'steps'].isna().sum()

    def get_badge(self):
        """Assign badge based on duration and breaks in workouts"""
        if self.__count_breaks(7) > 0:
            return None
        if self.__count_breaks(14) > 0:
            return 'APPRENTICE'
        elif self.__count_breaks(30) > 2:
            return 'PILGRIM'
        elif self.__count_breaks(60) > 2:
            return 'CHAMP'
        elif self.__count_breaks(120) > 2:
            return 'HERO'
        elif self.__count_breaks(240) > 2:
            return 'MONK'
        else:
            return 'BEAST'

    def __get_streaks(self):
        """Calculate streaks length based on workout continuity"""
        if self.streak is None:
            t = self.db['steps'].notna()  # db['steps'] = NaN means no-workout
            
            # streak calculation
            t1 = t.ne(t.shift())
            t1 = t1.cumsum()
            t1 = t1.groupby(t1).cumcount() + 1
            
            # remove streaks of no-workout days
            self.streak = t1 * t
        return self.streak

    def get_current_streak(self):
        """Get current streak length"""
        return self.__get_streaks().iloc[-1]

    def get_month_streak(self):
        """Get max streak length over last month"""
        return self.__get_streaks().iloc[-30:].max()

    def get_overall_streak(self):
        """Get max overall streak length"""
        return self.__get_streaks().max()

