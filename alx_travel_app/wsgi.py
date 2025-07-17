import os
from dotenv import load_dotenv

# Set the project base directory
project_folder = '/home/KHEMBO/alx_travel_app_0x02/alx_travel_app'
load_dotenv(os.path.join(project_folder, '.env'))

# Correct settings path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
