###### Level 1
print('======= Level 1 ======')
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    # for all notify method, you need to know how to send message
    def send(self, message: str):
        pass

# Define two notifiers, and these notifiers must have to know how to send messsage
# 1. Email
class EmailNotifier(Notifier): # get from the father definition of Notifier
    def send(self, message: str):
        print(f"Sending EMAIL:{message}")
# 2. SMS
class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")
# # 3. Wrong
# class wrongnotifier(Notifier):
#     def show_wrong_send(self, message):
#         print(f"wrong notifier: {message}")

def notify_user(notifier):
    notifier.send("your order is ready")

notify_user(EmailNotifier())
notify_user(SMSNotifier())
# notify_user(wrongnotifier())

##### Level 2
print('====== Level 2 ======')
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Define two payment method
class StripePayment(PaymentGateway):
    def pay(self, amount: float):
        print(f"Stripe paid ${amount}")
class RazorpayPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Razorpay pair ${amount}")

# Define the user of the payment system
class CheckoutService:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway
    
    def checkout(self, amount: float):
        self.gateway.pay(amount)

# 1. stripe
gateway_stripe = StripePayment() 
checkout_stripe = CheckoutService(gateway_stripe) # interface
checkout_stripe.checkout(100)
# 2. razorpay
gateway_razorpay = RazorpayPayment()
checkout_razorpay = CheckoutService(gateway_razorpay)
checkout_razorpay.checkout(100)