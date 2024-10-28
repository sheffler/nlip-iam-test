# NLIP IAM TEST

This project was created to illustrate using the nlip-iam OAuth server.  It uses Django and a library called `Authlib` to authenticate.

This project uses source cloned from 

   https://github.com/authlib/demo-oauth-client
   
and modified the `django-google-login` example.  It essentially replaces the Google authentication server, with the NLIP-IAM server running at http://127.0.0.1:9000/.

## Install

1. Create a virtual environment for this project and activate it

        $ python3 -m venv ~/virtualenvs/nlip-iam-test
	    $ . ~/virtualenvs/nlip-iam-test/bin/activate

2. Install the requirements

        $ pip install -U Django Authlib requests

    You should see Django, Authlib and other modules being installed.
	
3. Migrate the database to create the models.  This will create a sqlite database.

        $ cd nlipiamtest
		$ python manage.py migrate

4. Put the ClientID and ClientSECRET you created in the OAuth server into the appropriate place in the file

		nlipiamtest/nlipiamtest/settings.py

5. Start the server with:

        $ python manage.py runserver

6. Try it out.  Make sure the `nlip-iam` server is running and that it is on port 9000. 

        http://127.0.0.1:8000/

