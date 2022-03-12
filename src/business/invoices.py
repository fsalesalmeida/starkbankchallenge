import starkbank
import random
import names
from datetime import datetime, timedelta
from src.utils import random_cpf


def create(invoice_quantity: int):

    for i in range(invoice_quantity):
        starkbank.invoice.create([
            starkbank.Invoice(
                amount=random.randint(10000, 99999),
                name=names.get_full_name(),
                tax_id=random_cpf.generate(),
                due=datetime.utcnow() + timedelta(days=3),
                expiration=timedelta(hours=3).total_seconds(),
                fine=5,  # 5%
                interest=2.5,  # 2.5% per month
                tags=["Invoice Test"]
            )
        ])
