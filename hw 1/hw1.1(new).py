# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:35:00 2020
@author
 Bryce Benjamin
"""
import statistics

'''
Date    Hi(F)  Lo(F)  %Hum
AUG 30     79     64    60
AUG 31     82     66    20
SEP  1     85     68    20
SEP  2     85     68    30
SEP  3     87     69    30
SEP  4     87     69    20
SEP  5     87     69    20

SEP  6     85     67    20
SEP  7     81     63    30
SEP  8     79     61    20
SEP  9     77     61    20
SEP 10     77     59    20
SEP 11     77     59    20
SEP 12     77     59    20
SEP 13     77     59    50
'''
dt = ['AUG 30', 'AUG 31', 'SEP 1', 'SEP 2', 'SEP 3', 'SEP 4', 'SEP 5', 'SEP 6', 'SEP 7', 'SEP 8', 'SEP 9', 'SEP 10', 'SEP 11', 'SEP 12', 'SEP 13']

hi = [79, 82, 85, 86, 87, 87, 87, 85, 81, 79, 77, 77, 77, 77, 77]

lo = [64, 66, 68, 68, 69, 69, 69, 67, 63, 61, 61, 59, 59, 59, 59]

hm = [60, 20, 20, 30, 30, 20, 20, 20, 30, 20, 20, 20, 20, 20, 50]



def convert_to_celsius_for_question_1(f_temp):
        c_temp = (f_temp - 32) / 1.8000
        print('{:0d} degrees Fahrenheit is {:<.2f} Celsius\n'.format(f_temp, c_temp))

def convert_to_fahrenheit_question_1(c_temp):
    f_temp = (c_temp *1.8000) + 32.00
    print('{:0d} degrees Celsius is {:<.2f} Fahrenheit\n'.format(c_temp, f_temp))

def convert_to_celsius(f_temp):
        c_temp = (f_temp - 32) / 1.8000
        return c_temp
       
def convert_to_fahrenheit(c_temp):
    f_temp = (c_temp *1.8000) + 32.00
    print (" ", c_temp, "degrees Celsius is", f_temp, "Fahrenheit") 

def calculate_cube_root(var1):
    var1 **= 3
    return var1

def calculate_square_root(var1):
    var1 **= 2
    return var1 

def calculate_square_value(var1):
    var1 *= var1
    return var1 

def calculate_cube_value(var1):
    var1 = var1 * var1 * var1
    return var1

def calculate_mean_median_sd (high_temps, low_temps, humidity_values):
    
    high_temps_copy = high_temps.copy()
    low_temps_copy = low_temps.copy()
    humidity_values_copy = humidity_values.copy()
    high_temps_copy.sort()
    low_temps_copy.sort()
    humidity_values_copy.sort()
    #high temp mean, median, and standard deviation
    high_temps_mean = statistics.mean(high_temps_copy)
    high_temps_median = statistics.median(high_temps_copy)
    high_temps_sd = statistics.stdev(high_temps_copy, high_temps_mean)
    #low temp mean, median, and standard deviation
    low_temps_mean = statistics.mean(low_temps_copy)
    low_temps_median = statistics.median(low_temps_copy)
    low_temps_sd = statistics.stdev(low_temps_copy, low_temps_mean)
    #humidity mean, median, and standard deviation
    humidity_values_mean = statistics.mean(humidity_values_copy)
    humidity_values_median = statistics.median(humidity_values_copy)
    humidity_values_sd = statistics.stdev(humidity_values_copy, humidity_values_mean)
    # printing the values for high, low, and humidity
    print("\nThe high temp mean is:",high_temps_mean,", the high temp median is:",high_temps_median,", and the high temp standard deviation is:",high_temps_sd)
    print("\nThe low temp mean is:",low_temps_mean,", the low temp median is:",low_temps_median,", and the low temp standard deviation is:",low_temps_sd)
    print("\nThe humidity mean is:",humidity_values_mean,", the humidity median is",humidity_values_median,", and the humidity standard deviation is:",humidity_values_sd)
    
'''

    Date    Hi(F)  Lo(F)  %Hum
    AUG 30     79     64    60
    AUG 31     82     66    20
    SEP  1     85     68    20
    SEP  2     85     68    30
    SEP  3     87     69    30
    SEP  4     87     69    20
    SEP  5     87     69    20
    SEP  6     85     67    20
    SEP  7     81     63    30
    SEP  8     79     61    20
    SEP  9     77     61    20
    SEP 10     77     59    20
    SEP 11     77     59    20
    SEP 12     77     59    20
    SEP 13     77     59    50
'''


int_row_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
cube_root_list = []
square_root_list = []
int_value_list = []
square_value_list = []
cube_value_list = []

if __name__ == "__main__":
    
    #1.a and 1.b
    convert_to_celsius_for_question_1(0)
    convert_to_celsius_for_question_1(32) 
    convert_to_celsius_for_question_1(45) 
    convert_to_celsius_for_question_1(60) 
    convert_to_celsius_for_question_1(70) 
    convert_to_celsius_for_question_1(95) 
    convert_to_celsius_for_question_1(212)
    convert_to_fahrenheit_question_1(0)
    convert_to_fahrenheit_question_1(10)
    convert_to_fahrenheit_question_1(15)
    convert_to_fahrenheit_question_1(20)
    convert_to_fahrenheit_question_1(25)
    convert_to_fahrenheit_question_1(30)
    convert_to_fahrenheit_question_1(100)
    
    print("1.d")
    print('Date    Hi(F)  Lo(F)  %Hum')
    num_days = len(dt)
    [print(dt[i], hi[i], lo[i], hm[i]) for i in range(num_days)]
        

    print("\n")
    print("---------------------------------------------")
    
    print("1.e and 1.f")
    print('Date    Hi(F)  Lo(F)  %Hum')
    num_days = len(dt)
    [print(dt[i], '   ', hi[i], '   ', lo[i], '  ', hm[i]) for i in range(num_days)]
    
    calculate_mean_median_sd(hi, lo, hm)
    print("\n")
    print("---------------------------------------------")
    print("1.g")
    dt2 = dt.copy()
    hi2 = hi.copy()
    lo2 = lo.copy()
    hm2 = hm.copy()
    print('{:<6s}{:>7s}{:>7s}{:>6s}'.format(
          'Date', 'Hi(F)', 'Lo(F)', '%Hum'))
    num_days = len(dt2)
    for i in range(num_days):
        [print('{:<6s}{:>7d}{:>7d}{:>6d}'.format(dt2[i], hi2[i], lo2[i], hm2[i]))]
    print("\n")
    print("---------------------------------------------")
    print("1.h")
    print('{:<6s}{:>7s}{:>7s}{:>7s}'.format(
              'Date', 'Hi(C)', 'Lo(C)', '%Hum'))
    num_days = len(dt2)
    for i in range(num_days):
        hi2[i] = convert_to_celsius(hi2[i])
        lo2[i] = convert_to_celsius(lo2[i])
        print('{:<6s}{:>7.2f}{:>7.2f}{:>6d}'.format(dt2[i], hi2[i], lo2[i], hm2[i]))

   
    print("\n")
    print("---------------------------------------------")
    print("1.j")
    for i in int_row_list:
        cube_root_list.append(calculate_cube_root(i))
        square_root_list.append(calculate_square_root(i))
        int_value_list.append(i)
        square_value_list.append(calculate_square_value(i))
        cube_value_list.append(calculate_cube_value(i))

    print('{:<10s}{:>15s}{:>15s}{:>17s}{:>10s}{:>10s}'.format(
       'Integer', ' Cube Root', ' Square Root', ' Integer Value', ' Squared', ' Cubed'))
    num_int = len(int_row_list)
    for i in range(num_int):
        print('{:<10d}{:>15.6f}{:>15.6f}{:>12d}{:>12d}{:>12d}'.format(int_row_list[i], cube_root_list[i], square_root_list[i], int_value_list[i],
                                                               square_value_list[i], cube_value_list[i]))
       
   
     
    

   
 

    


