## 📘 Django Debug Toolbar – Notes

### ✅ What is it?

The **Django Debug Toolbar** is a development tool that shows debugging information for each request directly in your browser. It helps you inspect:

- SQL queries
- Templates
- Headers
- Logs
- Middleware
- Signals
- And more!

---

### 📦 Installation

```bash
pip install django-debug-toolbar
```

---

### ⚙️ Basic Setup (in `settings.py`)

1. **Add to `INSTALLED_APPS`:**

```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

2. **Add middleware (top of the list):**

```python
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]
```

3. **Set internal IPs (for local access):**

```python
INTERNAL_IPS = [
    "127.0.0.1",
]
```

---

### 🔗 URLs Setup (`urls.py`)

```python
from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

---

### 🧪 Common Debug Panels

| Panel     | Purpose                         |
| --------- | ------------------------------- |
| SQL       | See executed SQL queries        |
| Templates | View template names and context |
| Timer     | Check request processing time   |
| Request   | See GET, POST, Cookies, Session |
| Settings  | List of all Django settings     |
| Cache     | Cache hits, misses, and keys    |
| Headers   | View request/response headers   |
| Logging   | Displays logs triggered         |
| Signals   | Shows signals fired             |
| Versions  | Python and Django versions      |

---

### ⚠️ Important Notes

- ⚠️ **Use only in development** (not safe for production).
- You can enable/disable it conditionally using:

```python
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: request.user.is_superuser,
    "INTERCEPT_REDIRECTS": False,
}
```

---

### 💡 Benefits

- Instant debugging info in the browser
- Detect slow queries
- Improve performance by fixing template/rendering issues
- Visual trace of the request lifecycle
