# jobsearch (Job protal) web based system

## Job portal system
This system is developed using djagno framework

## To use this system follow the following steps:
1. Clone repo or download zip from the repo
   - ``` git clone https://github.com/GutemaG/jobsearch.git ```
2. if you downlaod zip extract it
3. create virtual env and activate it
   - ``` python3 -m venv env ``` 
   - ``` env\Scripts\activate ```
   - when you activate you must in the directory where **env** folder belongs 
4. cd jobsearch
5. cd jobsearch-master
6. install required packages
   - ``` pip install -r requiremnts.txt ```
7. set you database by default the database is sqlite3
8. migrate your database
   1. ``` python manage.py makemigrations```
   2. ``` python manage.py migrate ```
9.  create superuser 
       - ```python manage.py createsuperuser ```
       -  use username **admin** password **admin**

10.  create fakedate if you want to all with password 'password'
     -  This is not necessary
     -  **NB: if you want to create fake data you must follow the steps accordingly**
     1.  create 60 fake user
            - ``` python manage.py createfakeuser ```
      2. create 50 fake applicant
         - ``` python manage.py createfakeapplicant ```
      3. create fake 5 employer
         - ``` python manage.py createfakeemployer ```
      4. create fake 5 company
         - ``` python manage.py createfakecompany```
      5. create 200 fake jobs
         - ``` python manage.py createfakejob```
      6. create 00 fake applications for a users
         - ``` python manage.py createfakeapplication ```
11.  run you server
      - ``` python manage.py runserver```