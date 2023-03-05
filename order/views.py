from django.views.generic.base import TemplateView, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Basket
from .payments import BirKartPayment
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from products.models import ProductCategory
from .xml import XMLConnecter
from django.http import JsonResponse


class Cart(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    model = Basket

    def get_context_data(self, **kwargs):
        context = super(Cart, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        user_basket = Basket.objects.filter(user = self.request.user.id).first()
        grand_total = 0
        if user_basket:
            all_products = user_basket.items.all()
            context['products'] = all_products
            for product in all_products:
                grand_total += product.get_subtotal()
            context['grand_total'] = grand_total
        return context


    def post(self, request, *args, **kwargs):
        user_basket = Basket.objects.filter(user=self.request.user.id).first()
        grand_total = 0
        if user_basket:
            all_products = user_basket.items.all()
            for product in all_products:
                quantity = f"quantity-{product.id}"

                if quantity in request.POST:
                    # do some process about cart
                    grand_total += product.get_subtotal()

        description = "Basket Item Payment"
        payment_url = BirKartPayment(
            amount=float(grand_total), description=description
        )._prepare_payment_url()
        return HttpResponseRedirect(payment_url)



def test_payment_view(request):
    amount = request.GET.get("amount", 1)
    description = "Test payment"
    payment_url = BirKartPayment(
        amount=amount, description=description
    )._prepare_payment_url()
    return HttpResponseRedirect(payment_url)



def get_data_xml_view(request):
    code = request.POST.get("code")
    data = XMLConnecter().convert_xml_to_dict(code)
    return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):

    def get(self, request, *args, **kwargs):
        print("GET method -->", request.GET)
        return HttpResponse("Hello World")

    def post(self, request, *args, **kwargs):
        print("POST method -->", request.POST)
        return redirect("payment-callback")