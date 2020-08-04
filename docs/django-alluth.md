# Integrating Django-Allauth

Django-allauth comes with support for authenticating against a wide array of APIs
(see [providers](https://django-allauth.readthedocs.io/en/latest/providers.html))
as well as many other useful features. Most of these features can be enabled by
setting a few settings in your projects `settings.py` file. The
[documentation](https://django-allauth.readthedocs.io/en/latest/index.html) for
django-allauth provides clear instructions on using each of its features.

## Initial Configuration (See [Installation](https://django-allauth.readthedocs.io/en/latest/installation.html))

Open up `settings.py` and ensure that 
`'django.contrib.auth.backends.ModelBackend'` is listed under
`AUTHENTICATION_BACKENDS`. It should already be there. Next, add
`'allauth.account.auth_backends.AuthenticationBackend'` to it to enable
authentication with allauth.

Under `INSTALLED_APPS` add the following if they are not already there.

  * `'django.contrib.auth'`
  * `'django.contrib.messages'`
  * `'django.contrib.sites'`
  * `'allauth'`
  * `'allauth.account'`
  * `'allauth.socialaccount'`
 
These are required.
 
Next, add any
[providers](https://django-allauth.readthedocs.io/en/latest/providers.html) you
want to use to `INSTALLED_APPS`.
 
For the last modification to the `settings.py` file, ensure that you set
`SITE_ID` equal to some positive integer matching your site
(see [Django sites documentation](https://docs.djangoproject.com/en/3.0/ref/contrib/sites/))
in `Site` (e.g., `SITE_ID = 1`). You **MUST** set this variable, otherwise
Django will throw an error such as 
`django.contrib.sites.models.Site.DoesNotExist: Site matching query does not exist.`

Finally, add `path('accounts/', include('allauth.urls'))` to your `urls.py` and
run `python manage.py migrate`.

## Settings (see [Configuration](https://django-allauth.readthedocs.io/en/latest/configuration.html))

To force users to authenticate using email, simply set the following in
`settings.py`:
```python
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
```
 
## Account Recovery
 
Django-allauth comes with password recovery support out of the box. There is no
special configuration you have to do.
