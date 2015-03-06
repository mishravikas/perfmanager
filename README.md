#perfmanager
Mozilla perfomance alerts manager
##Ubuntu 14.04 Development Build Instructions
    #retrieve latest apt-get list
    $sudo apt-get update

    #Install virtualenv and pip
    $sudo apt-get install python-pip python-virtualenv
    
    #Fork perfmanager
    http://github.com/<your_user_name>/perfmanager

    #Clone your forked repo
    $git clone https://github.com/<your_user_name>/perfmanager.git

    #Create and activate a virtualenv
    $virtualenv venv
    $source venv/bin/activate

    #Install the dependencies
    $cd perfmanager
    $pip install -r requirements.txt
    
    #Create a mysql database 'perfdb'

    #Create local_settings.py from local_settings_sample.py with your own details.

    #Instantiate database
    $python manage.py syncdb
    
    #Start the development server
    $python manage.py runserver



