from .models import Option

def all_cakes(request):
    return {"all_cakes": Option.objects.all()}