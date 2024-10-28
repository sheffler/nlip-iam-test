import json
from django.urls import reverse
from django.shortcuts import render, redirect
from authlib.integrations.django_client import OAuth

# CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
CONF_URL = 'http://localhost:9000/o/.well-known/openid-configuration'
oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
#        'scope': 'openid email profile'
        'scope': 'openid read write'
    },
    # TOM: docs.authlib.org/en/v0.12/client/django.html
    code_challenge_method='S256',
)


def home(request):
    user = request.session.get('user')
    if user:
        user = json.dumps(user)
    return render(request, 'home.html', context={'user': user})


def login(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.google.authorize_redirect(request, redirect_uri)


def auth(request):
    token = oauth.google.authorize_access_token(request)
    print(f'TOKEN:{token}')
    print(f'USERINFO:{token["userinfo"]}')
    # TOM: 2024-10-24 - we did not enable OIDC
    request.session['user'] = token['userinfo']
    # request.session['user'] = 'Hello Tom'
    return redirect('/')


def logout(request):
    request.session.pop('user', None)
    return redirect('/')
