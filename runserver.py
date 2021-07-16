#!/usr/bin/env python
# runserver.py

from django.core.management import call_command
from boot_django import boot_django

boot_django()
call_command("runserver",)