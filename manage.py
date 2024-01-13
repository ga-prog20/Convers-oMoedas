import os
from django.core.management import execute_from_command_line

if _name_ == "_main_":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    execute_from_command_line(os.argv)