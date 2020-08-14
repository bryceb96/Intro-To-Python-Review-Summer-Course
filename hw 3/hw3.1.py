# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:34:54 2020

@author: Bryce Benjamin
"""

if __name__ == "__main__":
    records = []
    records2 = []
    columns = []
    
    print("1.a")
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:
    
        for line in fin:
            line = line[:-1]
            records.append(line)
        [print(line) for line in records]
            
    print('\n')
    print('----------------------------------------------------------')
    print("1.b")
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:
        for line in fin:
            line = line[:-1]
            line = line.split(":")
            columns.append(line)
        [records2.append(line) for line in columns]
        [print(row) for row in records2]
                 
    
    print('\n')
    print('----------------------------------------------------------')
    print("1.c")
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:   
        r2_copy = records2.copy()
        r2_copy.sort()
        [print(row) for row in r2_copy]	   #prints in ascending order
    
    print('\n')
    print('----------------------------------------------------------')
    print("1.d")
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:
            header = records2[0] #contains first item of records2, aka the header 
            data = records2[1:].copy()
            print(header)
            [print(d) for d in data]
    print('\n')
    print('----------------------------------------------------------')
    print("1.e")  
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:        
            header = records2[0] 
            data = records2[1:].copy()
            for first_item in data:
                first_item[0] = float(first_item[0])
            print(header)
            [print(d) for d in data]
    print('\n')
    print('----------------------------------------------------------')
    print("1.f")  
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:        
            header = records2[0] 
            data = records2[1:].copy()
            for first_item in data:
                first_item[0] = float(first_item[0])
            print(header)
            data.sort()
            [print(d) for d in data]
    print('\n')
    print('----------------------------------------------------------')
    print("1.g")
    
    with open('C:/Users/Bryce/Dropbox/Documents/Grad School/Review to Intro to Python/Homework/hw 3/expenses.txt', 'rt', 
              encoding = 'utf-8') as fin:
            categories = set()
            [categories.add(d[3]) for d in data]
            print('There are', len(categories), 'expense categories:')
            [print(c) for c in categories]
    print('\n')
    print('----------------------------------------------------------')
    print("1.h")
    
    n2s = {'01': 'Jan',
           '02': 'Feb',
           '03': 'Mar',
           '04': 'Apr',
           '05': 'May',
           '06': 'Jun',
           '07': 'Jul',
           '08': 'Aug',
           '09': 'Sep',
           '10': 'Oct',
           '11': 'Nov',
           '12': 'Dec'}
    [print(n, end=' ') for n in n2s.items()]
    