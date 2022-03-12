from dotenv import load_dotenv
import os
from src.utils.generate_keys import generate_keys
from src.utils import credentials
from src.helpers import scheduler

load_dotenv()

if not os.path.isfile(os.environ.get('PRIVATE_KEY')):
    generate_keys()
credentials.get_project_credentials()
credentials.set_default_user()
scheduler.run_task()
