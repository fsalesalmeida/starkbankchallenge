import os
import starkbank


def get_cert():
    with open(os.environ.get('PRIVATE_KEY'), 'r') as file:
        private_key_content = file.read()
    return private_key_content


def get_project_credentials():
    project = starkbank.Project(
        environment="sandbox",
        id=os.environ.get('PROJECT_ID'),
        private_key=get_cert()
    )
    return project


def set_default_user():
    starkbank.user = get_project_credentials()
    balance = starkbank.balance.get()
    return balance
