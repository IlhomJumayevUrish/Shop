from .models import*
from .ajax import cart_init
def cart_context(request):
    cart=cart_init(request)
    return {'cart':cart}