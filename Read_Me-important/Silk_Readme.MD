## 🚀 Getting Started with Django Silk – A Django App Profiling Tool

**Django Silk** is a powerful open-source tool to **profile and inspect performance** in Django apps. It helps you detect slow SQL queries, HTTP requests, view performance, and more.

---

### 📦 1. Installation

Install via pip:

```bash
pip install django-silk
```

---

### ⚙️ 2. Configuration

Update your **`settings.py`**:

#### ✅ Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'silk',
]
```

#### ✅ Add Middleware at the **end** of the list:

```python
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',  # Add this last
]
```

---

### 🛣️ 3. Add URLs

In your **project’s `urls.py`**:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('silk/', include('silk.urls', namespace='silk')),
]
```

---

### 📊 4. What Django Silk Tracks

| Feature             | Description                          |
| ------------------- | ------------------------------------ |
| ✅ SQL Queries      | Detects slow queries and duplicates  |
| ✅ HTTP Requests    | Profiles all request/response cycles |
| ✅ Views            | Profiles Django view performance     |
| ✅ Execution Time   | Helps you find bottlenecks           |
| ✅ Query Parameters | Tracks all params and context        |
| ✅ Stack Traces     | Helps identify where queries are run |

---

### 🧪 5. Run Migrations

After setup, run:

```bash
python manage.py migrate
```

---

### 🧑‍💻 6. Access the Dashboard

Visit:

```
http://127.0.0.1:8000/silk/
```

This opens the **Silk Dashboard** where you can inspect queries, profiles, timings, and more.

---

### ⚙️ 7. Optional Configs

```python
SILKY_META = True  # stores request/response meta

SILKY_PYTHON_PROFILER = True  # enables Python-level profiling
SILKY_PYTHON_PROFILER_BINARY = True  # save .prof files for download
SILKY_MAX_REQUEST_BODY_SIZE = -1  # store full request body
SILKY_MAX_RESPONSE_BODY_SIZE = -1  # store full response body
SILKY_ANALYZE_QUERIES = True  # enables SQL query analysis
```

---

### 📌 8. Profiling Specific Functions (Manual)

You can manually profile any function using a **decorator**:

```python
from silk.profiling.profiler import silk_profile

@silk_profile(name='my_custom_profile')
def my_function():
    ...
```

---

### 🐘 9. Use Cases

- Detecting **N+1 SQL problems**
- Monitoring **view performance**
- Tracking **API endpoint delays**
- Debugging **ORM inefficiencies**
- Analyzing request payloads

---

### ❌ Do NOT Use in Production

> ⚠️ Django Silk is for **development** and profiling **only**.
> Disable it in production for security and performance.

---

### ✅ Summary

| Feature                      | Benefit                                           |
| ---------------------------- | ------------------------------------------------- |
| 🔍 SQL Profiling             | Track, sort, and analyze all SQL queries          |
| ⏱️ View Timing               | Detect slow views and endpoints                   |
| 🔁 Duplicate Query Detection | Fix performance bottlenecks                       |
| 💾 Data Storage              | Data is stored in the database for later analysis |
| 🧪 Custom Profiling          | Add decorators to profile any Python code         |
