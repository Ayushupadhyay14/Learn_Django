Django Caching Guide: Database & File-Based
Part 1: Database Caching in Django

Step 1: Enable db cache backend in settings.py
CACHES = {
'default': {
'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
'LOCATION': 'my_cache_table',
}
}

Step 2: Create the Cache Table
Run the following commands:

python manage.py createcachetable
python manage.py migrate

Step 3: Use Cache in Your View

from django.core.cache import cache
from django.http import HttpResponse

def db_cached_view(request):
data = cache.get('my_key')
if not data:
data = "This is expensive data from DB or logic"
cache.set('my_key', data, timeout=60)
return HttpResponse(data)

Part 2: File-Based Caching in Django
Step 1: Set File-Based Cache in settings.py

CACHES = {
'default': {
'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
'LOCATION': 'D:/Ayush- upadhyay/django_cache_files/',
}
}

Step 2: Make sure the folder exists:
mkdir D:/Ayush- upadhyay/django_cache_files
Step 3: Use Cache in Views

from django.core.cache import cache
from django.http import HttpResponse

def file_cached_view(request):
data = cache.get('file_data')
if not data:
data = "Heavy operation result saved in file"
cache.set('file_data', data, timeout=60)
return HttpResponse(data)

Clear Cache (Both Types)

from django.core.cache import cache

def clear_cache(request):
cache.clear()
return HttpResponse("Cache Cleared!")

Template Fragment Caching

{% load cache %}
{% cache 120 "box-data" %}

<div>This part is cached using file/db!</div>
{% endcache %}

Summary Table

| Type             | Setting (BACKEND)                                     | Where it's stored  | Use Case                      |
| ---------------- | ----------------------------------------------------- | ------------------ | ----------------------------- |
| Database Cache   | 'django.core.cache.backends.db.DatabaseCache'         | Database Table     | Persistent, safe              |
| File-Based Cache | 'django.core.cache.backends.filebased.FileBasedCache' | Disk (file system) | Local development, easy debug |

Which One Should I Use?

| Situation                      | Use This          |
| ------------------------------ | ----------------- |
| Development, easy setup        | File-Based        |
| Small app, needs persistence   | Database Cache    |
| High performance in production | Redis / Memcached |
