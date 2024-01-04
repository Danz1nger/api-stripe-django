# api-stripe-django
Install the required packages:

pip install djangorestframework
pip install djangorestframework_simplejwt
pip install django-environ
pip install stripe

With this setup, Django will use JWT tokens for authentication, and the client will be able to obtain a JWT token by sending a POST request to the authentication endpoint.
Users can obtain an access token by making a POST request to the /api/token/ endpoint and refresh their access token by making a POST request to the /api/token/refresh/ endpoint.

You can further customize the authentication process and the endpoints by referring to the Django Rest Framework's Simple JWT documentation: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html
