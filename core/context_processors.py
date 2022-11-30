from order.models import Basket
from .models import Contact
def base_data(request):
    data = {}
    data['contacts'] = Contact.objects.all()
    quantity = 0
    if request.user.is_authenticated:
        shopping_card = Basket.objects.filter(user = request.user.id).last()
        if shopping_card:
            all_products = shopping_card.items.all()
            for product in all_products:
                quantity += product.quantity
            data["quantity"] = quantity
    return data