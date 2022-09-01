# Django-quiz-app

This is a simple quiz application.(Not meant for production deployment)

 Primary requirements:
  1. Python>=3.8
  2. pip 

To get started run following commands step by step on your terminal.


   1. ```git clone ```
   
   2. ```cd Django-quiz-app```
   
   3. ```pip install virtualenv```
   
   4. ```virtualenv venv```
   
   5. ```source venv/Scripts/activate``` (when on bash terminal on windows) 
   
      ```source venv/bin/activate``` (when on bash terminal on linux based OS)
      
      ```.\venv\Scripts\activate``` (when on windows powershell)
      
   6. ``` pip install -r requirements.txt```
   
   7. ```python manage.py makemigrations```
   
   8. ```python manage.py migrate ```
   
   9. ```python manage.py createsuperuser```(enter id and password for admin user when prompted)
   
   10. ```python manage.py runserver```
   
After the server has sucessfully started go to http://localhost:8000/admin 

login using id password you created on step 9 and start adding your category, questions, their options and marks per question.

Then go to http://localhost:8000 and start answering your questions.
   
