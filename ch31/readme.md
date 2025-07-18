Sure! Here's a full, **easy-to-understand academic-style note** on **`RedirectView`** in Django 5, covering **definitions, usage, syntax, all related details**, and **how to use it in real Django apps**.

---

# 📘 Django 5 Notes – `RedirectView`

---

## ✅ Definition

> **`RedirectView`** is a **Generic Class-Based View (GCBV)** in Django used to **redirect the user to another URL** (internal or external).
> It simplifies redirection tasks that would otherwise require writing custom logic using `HttpResponseRedirect`.

---

## 🧠 Why Use `RedirectView`?

- To redirect from **old URLs to new ones**.
- To send users to **external websites**.
- To create **dynamic redirects** (e.g., user profile redirect).
- To use **built-in redirect logic** instead of writing your own `HttpResponseRedirect`.

---

## 🔩 Syntax (Basic Structure)

```python
from django.views.generic.base import RedirectView

class MyRedirectView(RedirectView):
    url = '/target-url/'
```

Or directly in `urls.py`:

```python
path('old/', RedirectView.as_view(url='/new/'))
```

---

## 🧩 Important Parameters of `RedirectView`

| Parameter            | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| `url`                | The target URL to which the user is redirected (can be relative or full).      |
| `pattern_name`       | Uses Django's `reverse()` to redirect to a named URL pattern.                  |
| `permanent`          | If `True`, uses **301 redirect**; if `False`, uses **302 redirect** (default). |
| `query_string`       | If `True`, preserves the original request’s query parameters.                  |
| `get_redirect_url()` | Override this method to dynamically generate the redirect URL.                 |

---

## 📂 Where to Use It?

1. In `views.py`: for custom logic using `get_redirect_url()`.
2. In `urls.py`: for simple or static redirects (no need to define a class separately).

---

## 🔁 Status Code Explained

| Code | Name               | Use Case                          |
| ---- | ------------------ | --------------------------------- |
| 301  | Permanent Redirect | When the URL is changed forever   |
| 302  | Temporary Redirect | When redirection is not permanent |

---

## ✅ Use Cases

| Use Case                    | Example URL       | Redirects To             |
| --------------------------- | ----------------- | ------------------------ |
| External website            | `/google/`        | `https://www.google.com` |
| Old blog page to new one    | `/old-article/`   | `/new-article/`          |
| Named URL redirection       | `/go-home/`       | URL pattern name `home`  |
| Redirect with query strings | `/move/?q=django` | `/target/?q=django`      |
| Dynamic redirection         | `/my-profile/`    | `/users/<username>/`     |

---

## 🧪 Examples

### 📌 1. **Basic Redirect in `urls.py`**

```python
from django.views.generic.base import RedirectView
from django.urls import path

urlpatterns = [
    path('old/', RedirectView.as_view(url='/new/', permanent=True)),
]
```

🔁 Redirects `/old/` to `/new/` permanently.

---

### 📌 2. **Redirect to External Website**

```python
path('google/', RedirectView.as_view(url='https://www.google.com')),
```

🔁 Redirects to Google.

---

### 📌 3. **Redirect Using `pattern_name`**

```python
path('go-home/', RedirectView.as_view(pattern_name='home')),
path('', HomeView.as_view(), name='home'),
```

🔁 Redirects `/go-home/` to the view named `home`.

---

### 📌 4. **Redirect with Query String**

```python
path('move/', RedirectView.as_view(url='/target/', query_string=True))
```

🔁 `/move/?id=7` → `/target/?id=7`

---

### 📌 5. **Dynamic Redirect (Override `get_redirect_url`)**

```python
# views.py
from django.views.generic.base import RedirectView

class ProfileRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        username = self.request.user.username
        return f'/users/{username}/'
```

```python
# urls.py
path('my-profile/', ProfileRedirectView.as_view()),
```

🔁 Automatically redirects to `/users/<current-username>/`.

---

## ✅ Summary Table

| Feature            | Description                            |
| ------------------ | -------------------------------------- |
| **`RedirectView`** | GCBV for redirection                   |
| **Static URL**     | Use `url='/some-url/'`                 |
| **Named URL**      | Use `pattern_name='home'`              |
| **Query String**   | Preserves original `?id=123` if `True` |
| **Status Code**    | 301 if `permanent=True`, else 302      |
| **Dynamic**        | Override `get_redirect_url()`          |

---

## ✅ Tip for Interview or Exam

> `RedirectView` is often used to redirect old URLs to new paths or forward users to dynamically determined destinations without writing explicit logic using `HttpResponseRedirect`.

---

Let me know if you'd like to download these notes as a **PDF**, get similar notes for `TemplateView`, `FormView`, or `DetailView`, or combine them all into one file.
