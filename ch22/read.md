### ✅ **What is Middleware in Django 5?**

Middleware is a **lightweight, low-level "plugin"** system that processes requests and responses globally.
They sit between the Django request/response processing pipeline to perform tasks like:

- Security checks
- Session and authentication handling
- Modifying requests/responses
- Adding custom headers, etc.

---

### ⚙️ **How middleware works:**

Each middleware component is a **Python class** with at least one of these methods:

- `__init__(self, get_response)` – runs once when the server starts.
- `__call__(self, request)` – handles the request and must return a response.
- `process_view(self, request, view_func, view_args, view_kwargs)` – called just before the view.
- `process_exception(self, request, exception)` – called if the view raises an exception.
- `process_template_response(self, request, response)` – called if the response has a `render` method.

> In modern Django (including Django 5), you usually just implement `__init__` and `__call__`. The old-style `process_*` methods are still supported but less common.

---

### 📌 **Example: Custom middleware**

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
```

Then add it to your settings:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'myapp.middleware.SimpleMiddleware',
    ...
]
```

---

### 🧰 **Built-in middleware examples in Django 5:**

- `SecurityMiddleware`
- `SessionMiddleware`
- `AuthenticationMiddleware`
- `CsrfViewMiddleware`
- `CommonMiddleware`
- `MessageMiddleware`

---

If you'd like, I can also:
✅ List the default middleware stack in Django 5
✅ Show a real use case (e.g., logging, blocking IPs)
✅ Explain old-style vs new-style middleware

Let me know!
