from decimal import Decimal

import stripe

from config.settings import SECRET_API_KEY


stripe.api_key = SECRET_API_KEY

def create_stripe_product(product):
    """Создаем продукт в страйпе"""

    title_product = (
        product.payment_course if product.payment_course else product.payment_lesson
    )
    stripe_product = stripe.Product.create(name=title_product)
    return stripe_product.get("id")


def create_stripe_price(amount, product_id):
    """Создаем цену в страйпе"""

    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(Decimal(amount) * 100),
        product_data={"name": product_id},
    )
    return price


def create_stripe_session(price):
    """Создаем сессию для оплаты в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
