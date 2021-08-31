#!/usr/bin/env python
import os
import sys
import ptvsd
from django.conf import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_app.settings")

    from django.core.management import execute_from_command_line

    if settings.DEBUG and (os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN')):
        ptvsd.enable_attach(address = ('0.0.0.0', 34404))
        print("Attached remote debugger")

    execute_from_command_line(sys.argv)
