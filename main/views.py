import os

import django
import gunicorn
from django.conf import settings
from django.shortcuts import render_to_response

import main


# Create your views here.



def home(request, *args, **kwargs):

    nginx_conf_file = os.path.join(settings.BASE_DIR, "nginx_config", "gunicorn_https.conf")
    with open(nginx_conf_file, "r")as f:
        conf_content = f.read()

    startup_script = os.path.join(settings.BASE_DIR, "run.sh")
    with open(startup_script, "r")as f:
        run_sh_content = f.read()

    context = {
        "app_version": main.__version__,
        "gun_version": gunicorn.__version__,
        "dj_version": django.__version__,
        "request": request,
        "url_scheme": request.environ['wsgi.url_scheme'],
        "nginx_conf": conf_content,
        "run_sh_content": run_sh_content,
    }

    return render_to_response("main/home.html", context)
