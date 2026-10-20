""" This program tracks library books that users borrow.
    Authors: 
        Christopher Moyle - 
        Peter Poli - 
        Samantha Stevens - A00054394
"""

def DaysInMonth(month):
    """ Function that returns the days inside the given month.
        month: Integer value of month
        Returns: Integer of number of days """
    if month == 1: return 31                       # January has 31 days.
    elif month == 2: return 28                     # February has 28 days.
    elif month % 2 == 1 and month < 8: return 31   # There is a hill pattern from March-July, so assign 31 to odd numbers. Any number % 2 will either give a remainder of 0 or 1 (so odd or even).
    elif month % 2 == 0 and month < 8: return 30   # Then assign 30 to even numbers.
    elif month % 2 == 0 and month >= 8: return 31  # The hill pattern flips on august. August is an even number, so assign 31 to even numbers past August.
    else: return 30                                # Finally, assign 30 to odd numbers past August.

def IsLeapYear(year):
    if (year % 4 != 0): return False               # If the year number isn't divisible by four, it's a common year.
    elif (year % 100 != 0): return True            # If the year number isn't divisible by 100, it's a leap year.
    elif (year % 400 != 0): return False           # If the year number isn't divisible by 400, it's a common year.
    else: return True                              # Otherwise, it's a leap year.

