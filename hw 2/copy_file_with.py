# File: copy_file_with.py    Author: John K. Ostlund

with open('C:/Users/Bryce/Dropbox/Review to Intro to Python/Homework/hw 2/expenses.txt', 'rt',
          encoding = 'utf-8') as fin:
    with open('C:/Users/Bryce/Dropbox/Review to Intro to Python/Homework/hw 2/expenses_copy2.txt', 'wt',
              encoding = 'utf-8') as fout:
        for line in fin:
            fout.write(line)



            
# close of fin and fout is automatic!

        
