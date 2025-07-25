# 📘 Django 5 – `JsonResponse` Full Guide
## ✅ What is `JsonResponse`?

`JsonResponse` is a subclass of `HttpResponse` used in Django to send data in **JSON format**.
It’s most commonly used when building APIs or sending responses to frontend apps via **AJAX** or **Fetch API**.

---

## 🔧 How to Use `JsonResponse`

### ✅ Step-by-Step

1. **Import it**:

```python
from django.http import JsonResponse
```

2. **Return it from a view**:

```python
def my_view(request):
    data = {'message': 'Hello from Django'}
    return JsonResponse(data)
```

3. **Allow list/array output**:

```python
def list_view(request):
    data = [{'id': 1}, {'id': 2}]
    return JsonResponse(data, safe=False)
```

> ✅ Note: `safe=True` (default) only allows dictionaries. Use `safe=False` for lists/arrays.

---

## ⚙️ Key Features

| Feature             | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| `safe=True`         | Default. Only allows `dict`. Set `False` to allow lists/arrays. |
| `json_dumps_params` | Customize formatting like indentation, separators, etc.         |
| `status=200`        | Allows sending custom HTTP status code (e.g., 404, 400, 201).   |
| `Content-Type`      | Automatically sets `application/json` header.                   |
| `custom headers`    | You can set headers like `res['X-Custom'] = 'Value'`.           |

---

## 💡 Use Cases

| Scenario                        | Why Use `JsonResponse`?               |
| ------------------------------- | ------------------------------------- |
| AJAX or Fetch API from frontend | Returns JSON to JavaScript apps       |
| RESTful APIs without DRF        | Lightweight JSON-based responses      |
| Return form errors in JSON      | Better UI feedback on form validation |
| Mobile app backend              | Easy to consume JSON APIs             |

---

## 🔁 Advanced Examples

### ✅ 1. JSON with status code

```python
def not_found(request):
    return JsonResponse({'error': 'Not Found'}, status=404)
```

---

### ✅ 2. Pretty JSON Formatting (with indent)

```python
import json

def pretty_json(request):
    data = {'name': 'Ayush'}
    return JsonResponse(data, json_dumps_params={'indent': 2})
```

---

### ✅ 3. Dynamic Response from Model

```python
from .models import Student

def student_list(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)
```

---

### ✅ 4. With Custom Headers

```python
def custom_response(request):
    res = JsonResponse({'message': 'Hi'})
    res['X-Token'] = 'abc123'
    return res
```

---

### ✅ 5. Handling POST Request (with @csrf_exempt)

```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def api_receive(request):
    body = json.loads(request.body)
    name = body.get('name')
    return JsonResponse({'greeting': f'Hello, {name}!'})
```

---

## 🔐 Security Tip

- Always **validate incoming JSON data** before processing it.
- Use `@csrf_exempt` cautiously (only for APIs).
- Avoid sending sensitive info in JSON response.

---

## 🧠 Summary

| ✅ Feature           | 💡 Use It For                         |
| -------------------- | ------------------------------------- |
| `JsonResponse`       | Send JSON data from a Django view     |
| `safe=False`         | When returning lists or arrays        |
| `status=xxx`         | Return appropriate HTTP response code |
| `json_dumps_params`  | Format output JSON nicely             |
| `res['Header'] = ''` | Set custom headers in JSON response   |
