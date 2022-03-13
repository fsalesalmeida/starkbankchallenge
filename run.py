import logging
from src.helpers import scheduler
from src.utils import environment

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

environment.set_env()
logging.info("Running Invoice Task...")
scheduler.run_task()
