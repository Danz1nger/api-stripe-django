# api-stripe-django
Установите необходимые пакеты:

pip install djangorestframework

pip install djangorestframework_simplejwt

pip install django-environ

pip install stripe

Настройте переменные окружения:
Создайте файл .env в корневом каталоге проекта:

SECRET_KEY=<your_secret_key>

DEBUG=True

ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

DATABASE_URL=<your_database_url>

STRIPE_PUBLIC_KEY=<your_stripe_public_key>

STRIPE_SECRET_KEY=<your_stripe_secret_key>

STRIPE_CURRENCY=<your_stripe_currency>

STRIPE_CURRENCY_TWO=<your_second_stripe_currency>

При такой настройке Django будет использовать JWT-токены для аутентификации, а клиент сможет получить JWT-токен, отправив POST-запрос к конечной точке аутентификации.
Пользователи могут получить токен доступа, сделав POST-запрос к конечной точке /api/token/, и обновить свой токен доступа, сделав POST-запрос к конечной точке /api/token/refresh/.

Вы можете дополнительно настроить процесс аутентификации и конечные точки, обратившись к документации Django Rest Framework's Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html.
