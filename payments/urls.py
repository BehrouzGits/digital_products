from django.urls import path

from .views import PaymentView, GatewayView

urlpatterns = [
    path('payments/', PaymentView.as_view()),
    path('gateways/', GatewayView.as_view())
]