from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment'
    
    def ready(self):
        #import procedur obsługi sygnałów
        import payment.signals
        
