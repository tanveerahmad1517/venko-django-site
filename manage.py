#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    ENV = os.environ.get("DJANGO_ENV", "dev")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "venelin.settings.%s" % ENV)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
