# 이모콘 2016 F/W
`이모콘`은 [이상한모임](http://blog.weirdx.io)에서 봄, 가을에 개최하는 온라인 컨퍼런스입니다.
이 소스는 `이모콘 2016 F/W`에서 시연을 위해 작성한 것입니다.

# Heroku Django Starter Template
[Django](www.djangoproject.com) 로 만든 블로그를 [Heroku](www.hreoku.com)에 올려 서비스 해볼 수 있습니다.

# Tutorial
[이모콘 발표용 Keynote](https://github.com/chiyodad/emocon2016-django/blob/master/emocon_django_43.key.zip)를 참고해주세요.
단, 모든 내용은 `macOS`가 기준입니다.

# 아래 내용은 heroku template 을 통해 django 프로젝트를 시작하는 방법입니다.

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld .

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create [앱이름]
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## 더 읽을거리

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
