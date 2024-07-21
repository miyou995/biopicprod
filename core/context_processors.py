from django.utils.translation import *
from core.models import Client
def base_template(request):
    # base_template = 'rtl/base.html' if request.LANGUAGE_CODE == 'ar' else 'base.html'
    base_template = 'base.html'
    context = {
        'base_template' : base_template,
        'current_lang' : request.LANGUAGE_CODE,
        # 'solutions' : Solution.objects.filter(is_active=True),
        'clients' : Client.objects.filter(is_active=True)
    }

    return context


