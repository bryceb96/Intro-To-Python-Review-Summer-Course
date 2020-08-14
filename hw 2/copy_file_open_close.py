# File: copy_file_open_close.py    Author: John K. Ostlund

fin = open('C:/Users/Bryce/Dropbox/Review to Intro to Python/Homework/hw 2/expenses.txt', # pathname
           'rt',                # read text
           encoding = 'utf-8')  # Unicode, with ASCII

fout = open('C:/Users/Bryce/Dropbox/Review to Intro to Python/Homework/hw 2/expenses_copy1.txt',
            'wt',               # write text
            encoding = 'utf-8')

for line in fin:    # line is a str
    fout.write(line)

fin.close()     # so you can open again later
fout.close()    # do not forget!

        
