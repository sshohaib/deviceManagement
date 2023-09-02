# deviceManagement
A tool for companies for managing devices among the its employees

!!!!Please read this before execution!!!!

superuser{
      username: 'shoha'
      password: 'repliq1234'
}

Getting Started
Open terminal using Ctrl + Alt + T. Run the following command

   git clone https://github.com/Agha-Muqarib/Library-Management-System.git 

   
Create and activate virtual environment using

    virtualenv -p python3 devicemanage

    devicemanage\Scripts\activate



Run Steps

    cd devicemanaging
            
    python manage.py makemigrations
   
    python manage.py migrate
   
    python manage.py runserver
