from .models import Company


def company_data(request):
    data=Company.objects.last()
    return {'data': data}