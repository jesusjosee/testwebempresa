#1.function that allows to extend the context
# 2.Next  step is put it on in context_procesors of TEMPLATES in file settings.py
#3. send to the template base.html
# import class Link
from .models import Link

def ctx_dict(request):
    ctx= {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx