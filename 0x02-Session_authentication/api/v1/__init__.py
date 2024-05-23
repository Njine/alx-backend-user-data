#!/usr/bin/env python3
"""Initialize Blueprint views."""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Importing views must be at the end to avoid circular imports
from api.v1.views.index import *
from api.v1.views.users import *
