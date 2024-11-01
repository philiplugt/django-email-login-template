# Email login with Django
The Django framework by default uses username to sign in, changing this to email can be quite tricky. This repository provides template files needed to make this change when starting a new project.

These files will make email login default. Username is now on optional field to be set in the profile. The Django admin dashboard is modified to keep Group and User under the same section.

### Versioning
This code has been tried and tested with Django 4.2.4 (2023-08-23)

### How to use
Create a new Django project 

```python
# Make a new python virtual environment and install Django
> mkdir env
> python -m venv env/your-project-name
> source env/project-name/bin/activate
(env)> pip install --upgrade pip
(env)> pip install Django

# Create a new django project and app
(env)> django-admin startproject your-project-name
(env)> cd project-name
(env)> python manage.py startapp your-app-name
```

Once a default Django project has been setup you may replace the files in this repository with the files in your app `your-app-name` folder. There are 3 files to add/replace: models.py, admin.py and apps.py.

Edit the your-project-name/settings.py file to include the app. But also add the new custom User model, by adding the following line at the bottom of the file `AUTH_USER_MODEL = 'your-app-name.User'`

> [!NOTE]
> The `AUTH_USER_MODEL` variable is always formatted as `app_label.ModelName`. If your users app is nested inside another folder the formatting doesn't change. Django finds your model via the `INSTALLED_APPS` setting (which must contain the correct path of your app).

You can now migrate the database and test the changes.

```python
(env)> python manage.py makemigrations
(env)> python manage.py migrate

# Create a superuser
(env)> python manage.py createsuperuser

# Launch the server to test the admin panel
(env)> python manage.py runserver
```

Test it by going to http://127.0.0.1:8000/admin/

> [!IMPORTANT]   
> This repository uses `users` as app name, instead of `your-app-name`. If your app name is different, such as `accounts`, make sure to replace references to `users` appropriately.

### File changes explained

#### your-app-name/models.py

In models.py new models are created that inherit from code Django file related to User. Changes are then made to use email instead of username for login purposes. Firstly, a new UserManager which inherits from BaseUserManager is created. The UserManager defines functions such as `create_user` which is used to create a new user with commands like `python manage.py createsuperuser`. 

Also a new User model is created in which the username field is no longer required and is optional.

Lastly, a proxy Group model is created for display purposes in the admin panel (see below).

#### your-app-name/admin.py

By creating a custom `User` model, the admin panel will place this model separately outside of _Authentication and Authorization_ section and away from the default `Group` model. This is not elegant. 

Having created a `Group` proxy in models.py, we edit the admin.py. The default Group model, imported as `OldGroup`, is unregistered. While the new (proxy) Group and User models are registered together so that they will now fall under the same section in the admin panel.

#### your-app-name/apps.py

In the app.py, the `verbose_name` variable was added, this changes the section name in the admin panel. By default this is named after the app name, but since the app name `Users` can easily be confused with `User` is was changed to accounts.

### Sample screenshots
<div align="center">
    <img width="400" alt="Screenshot Django admin login" src="https://github.com/pxv8780/django-email-sign-in/assets/22942635/4d51889c-d894-47af-8310-ed7cb81cf533">
    <p><sup>Note the former 'Username' field is now labelled as 'Email'</sup></p>
    <br>
</div>

<div align="center">
    <img align="center" width="600" alt="Screenshot Django admin dashboard" src="https://github.com/pxv8780/django-email-sign-in/assets/22942635/f775d8a7-3ea2-4661-9e97-69943bd38634">
    <p><sup>Note the former 'Username' field is now labelled as 'Email'</sup></p>
    <br>
</div>

### Sources and useful links
- https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
- https://www.youtube.com/watch?v=IdpwReLHrbk
  - _Code Aura - Use Email Instead of Username in Django Authentication | Email Login_
- https://djangocentral.com/authentication-using-an-email-address/
- https://rahmanfadhil.com/django-login-with-email/
- https://velog.io/@holawan/Django-Custom-User-Model-Test
