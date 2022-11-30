from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Basket

class Cart(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    model = Basket

    def get_context_data(self, **kwargs):
        context = super(Cart, self).get_context_data(**kwargs)
        user_basket =  Basket.objects.filter(user = self.request.user.id).first()
        grand_total = 0
        if user_basket:
            all_products = user_basket.items.all()
            context['products'] = all_products
        if user_basket:
            for product in all_products:
                grand_total += product.get_subtotal()
            context['grand_total'] = grand_total
        return context
