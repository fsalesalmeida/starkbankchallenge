# Stark Bank Challenge
Issues 8 to 12 invoices every 3 hours to random people for 24 hours, Receives the webhook callback of the Invoice credit and sends the received amount
(minus eventual fees) to an account using a Transfer.

## Requirements:
- Python >= 3.8

## How to run:
- Clone the repository. After that, make a virtualenv in root folder of the downloaded project.
Into the virtualenv, install all the dependencies
```sh
pip install -r requirements.txt
```

- Edit the .env file with your project-id and webhook address. I made my local tests using Ngrok(https://ngrok.com/) to forward Flask URL to a public URL, and creating the webhook on Stark Bank Challenge Dashboard. 

- Run the following files in that order:
```sh
(Run the API Listener)
python -m run_listener.py
```
```sh
(Run the random invoice issuer scheduler)
python -m run.py
```

