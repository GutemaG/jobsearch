# jobsearch (Job protal) web based system

## Job portal system
This system is developed using djagno framework

## To use this system follow the following steps:
1. Clone repo
   - ``` git clone https://github.com/GutemaG/jobsearch.git ```
2. create virtual env and activate it
3. cd jobsearch
4. install required packages
   - ``` pip install -r requiremnts.txt ```
5. set you database by default the database is sqlite3
6. create superuser 
   - ```python manage.py createsuperuser ```
   -  use username 'admin' password 'admin'
7. creat fakedate if you want to all with password 'password'
      - **NB: if you want to create fake data you must follow the steps accordingly** 
   1.  create 110 fake user
     - ``` python manage.py createfakeuser ```
   2. create 100 fake applicant
     - ``` python manage.py createfakeapplicant ```
   3. create fake 5 employer
     - ``` python manage.py createfakeemployer ```
   4. create fake 5 company
     - ``` python manage.py createfakecompany```
   5. create 200 fake jobs
     - ``` python manage.py createfakejob```
   6. create 500 fake applications for a users
     - ``` python manage.py createfakeapplication ```
8. run you server
   - ``` python manage.py runserver``` 