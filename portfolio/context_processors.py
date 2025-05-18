from .models import Visitor
from django.core.cache import cache

def visitor_counter(request):
    if not request.session.session_key:
        request.session.save()
    sk = request.session.session_key

    if not Visitor.objects.filter(session_key=sk).exists():
        Visitor.objects.create(session_key=sk)
        total = cache.get('visitor_count', 0) + 1
        cache.set('visitor_count', total)

    count = cache.get('visitor_count')
    if count is None:
        count = Visitor.objects.count()
        cache.set('visitor_count', count)

    return {'visitor_count': count}
