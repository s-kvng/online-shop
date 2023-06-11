from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
        Task to send email notification 
        when an order is successfully created
    """

    order = Order.objects.get(id=order_id)
    subject = f"Order no.{order.id}"
    message = f"Dear {Order.first_name},\n\n"\
              f"You have successfully placed an order."\
              f"Your order ID id {order.id}"
    mail_sent = send_mail(subject,message,'admin@myshop.com',[order.email])

    return mail_sent 