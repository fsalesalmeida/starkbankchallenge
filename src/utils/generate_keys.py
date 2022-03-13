import starkbank
import logging


def generate_keys():
    logging.info("Generating Public and Private Keys...")
    starkbank.key.create("src/utils/keys/")
