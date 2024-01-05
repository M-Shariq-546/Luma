from django.core.cache import cache
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse

class Testing_view(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        users = cache.get('all_users')
        if not users:
            print("no data found in cache let's store it")
            users = User.objects.all()
            cache.set('all_users', users)
            users_cache_data = cache.get('all_users')
            if users_cache_data:
                print("Found Users Data", users_cache_data.values("first_name", "email", "username"))
        return HttpResponse("Testing Successfully Done")