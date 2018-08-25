import json
import os

import django
import gunicorn
from django.conf import settings
from django.shortcuts import render_to_response

import main


def home(request, *args, **kwargs):
    nginx_conf_file = os.path.join(settings.BASE_DIR, "config", "nginx.conf")
    with open(nginx_conf_file, "r")as f:
        nginx_config_content = f.read()

    gunicorn_conf_file = os.path.join(settings.BASE_DIR, "config", "gunicorn.py")
    with open(gunicorn_conf_file, "r")as f:
        gunicorn_config_content = f.read()

    startup_script = os.path.join(settings.BASE_DIR, "run.sh")
    with open(startup_script, "r")as f:
        run_sh_content = f.read()

    context = {
        "app_version": main.__version__,
        "gun_version": gunicorn.__version__,
        "dj_version": django.__version__,
        "request": request,
        "meta_blacklist": ['PATH', 'VIRTUAL_ENV'],
        "url_scheme": request.environ['wsgi.url_scheme'],
        "nginx_conf": nginx_config_content,
        "gunicorn_conf": gunicorn_config_content,
        "run_sh_content": run_sh_content,
    }

    return render_to_response("main/home.html", context)
