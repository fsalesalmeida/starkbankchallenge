import logging
import starkbank
import os


def create():
    logging.info("Creating webhook...")
    starkbank.webhook.create(
        url=os.environ.get('WEBHOOK'),
        subscriptions=["invoice"],
    )
