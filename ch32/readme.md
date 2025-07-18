Here are your **Django 5 – `DetailView` Notes** in a clean, exam-ready format 📒:

---

# 📘 Django 5 – DetailView Notes

---

## ✅ What is `DetailView`?

- `DetailView` is a **generic class-based view**.
- Used to **display a single object’s details** (like a blog post, book, etc.).
- Works automatically with `pk` or `slug` in the URL.
- Fetches a single object from the database and sends it to the template.

---

## 🧱 Basic Structure

```python
from django.views.generic.detail import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
```

---

## ✅ Required Elements

| Property              | Purpose                                         |
| --------------------- | ----------------------------------------------- |
| `model`               | The model you want to show data from            |
| `template_name`       | The HTML template to render                     |
| `context_object_name` | The name you use in the template for the object |

---

## 🛠 Steps to Use `DetailView`

### 1️⃣ Define a Model

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
```

---

### 2️⃣ Create the View

```python
# views.py
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
```

---

### 3️⃣ Set up URL

```python
# urls.py
from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
```

✅ You can also use `slug`:

```python
path('book/<slug:slug>/', BookDetailView.as_view(), name='book-detail')
```

---

### 4️⃣ Create the Template

```html
<!-- templates/book_detail.html -->
<h2>{{ book.title }}</h2>
<p><b>Author:</b> {{ book.author }}</p>
<p>{{ book.description }}</p>
```

---

## 🔁 Extra Methods You Can Override

| Method               | Description                               |
| -------------------- | ----------------------------------------- |
| `get_object()`       | Customize object retrieval                |
| `get_context_data()` | Add extra data to the context             |
| `get_queryset()`     | Limit/fetch custom data from the database |

---

## 📌 Summary Table

| Feature             | Description                            |
| ------------------- | -------------------------------------- |
| View Class          | `DetailView`                           |
| Purpose             | Display one record in detail           |
| Uses `pk/slug`      | Yes                                    |
| Context Object Name | Default is `object` (can be renamed)   |
| Template Name       | Required or auto-`<model>_detail.html` |

---

Let me know if you want this as a printable PDF or Word file, or if you want notes for other class-based views like `CreateView`, `UpdateView`, or `DeleteView`. ✅
