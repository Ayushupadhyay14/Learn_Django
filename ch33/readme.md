Here are your **Django 5 `FormView` notes** in a clean and easy-to-revise format, perfect for exam prep or interview review:

---

# 📘 Django 5: `FormView` Notes

---

## ✅ What is `FormView`?

A **Generic Class-Based View** in Django used to:

- Display an HTML form (`GET`)
- Handle form submission and validation (`POST`)
- Redirect upon success (`success_url`)
- Process data via `form_valid()`

---

## 📌 Basic Syntax

```python
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # Process form.cleaned_data
        return super().form_valid(form)
```

---

## 🧱 Step-by-Step Setup

### 🔹 Step 1: Define a Form

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---

### 🔹 Step 2: Create a `FormView`

```python
# views.py
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        print("Form Data:", form.cleaned_data)
        return super().form_valid(form)
```

---

### 🔹 Step 3: URL Configuration

```python
# urls.py
from django.urls import path
from .views import ContactFormView

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact'),
]
```

---

### 🔹 Step 4: Template (`contact.html`)

```html
<h2>Contact Us</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Send</button>
</form>
```

---

### 🔹 Step 5: Success Template (`thanks.html`)

```html
<h2>Thanks for contacting us!</h2>
```

---

## 🛠️ Optional Methods to Override

| Method              | Use Case                             |
| ------------------- | ------------------------------------ |
| `form_valid()`      | Handle successful form submission    |
| `form_invalid()`    | Handle form errors                   |
| `get_initial()`     | Provide default form values          |
| `get_form_kwargs()` | Pass extra data (e.g., current user) |

---

## 🎯 Summary Table

| Property        | Description                         |
| --------------- | ----------------------------------- |
| `form_class`    | Form to be displayed                |
| `template_name` | Template used to render the form    |
| `success_url`   | URL to redirect after form is valid |
| `form_valid()`  | Method to process valid form data   |

---

Let me know if you want notes on `ModelFormView` or `UpdateView`.
