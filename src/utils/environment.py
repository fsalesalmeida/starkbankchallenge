import logging
import os

from dotenv import load_dotenv
from src.utils import credentials
from src.utils.generate_keys import generate_keys


def set_env():
    logging.info("Loading Environment Variables...")
    load_dotenv()

    logging.info("Loading Private Key...")
    if not os.path.isfile(os.environ.get('PRIVATE_KEY')):
        generate_keys()

    logging.info("Setting Up Credentials...")
    credentials.get_project_credentials()
    logging.info("Setting Up Default User...")
    credentials.set_default_user()
