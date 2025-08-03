
## 📘 Django Pagination using Function-Based Views (FBV)
### ✅ What is Pagination?

- Pagination means splitting a large list of records into smaller parts (pages).
- Example: Showing 5 or 10 blog posts per page instead of all at once.

---

### 📦 Why Use Pagination?

- ✅ Increases performance by loading fewer records.
- ✅ Improves user experience.
- ✅ Used in posts, product lists, user lists, etc.

---

### 🧱 How to Use Pagination in FBV

#### 🔹 1. Import Paginator

```python
from django.core.paginator import Paginator
```

---

#### 🔹 2. Example Model

```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

---

#### 🔹 3. Function-Based View (views.py)

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list_view(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
```

---

#### 🔹 4. Template (post_list.html)

```html
<h1>Post List</h1>

{% for post in page_obj %}
<h2>{{ post.title }}</h2>
<p>{{ post.content|truncatewords:30 }}</p>
{% endfor %}

<div class="pagination">
  {% if page_obj.has_previous %}
  <a href="?page=1">First</a>
  <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
  {% endif %}

  <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

  {% if page_obj.has_next %}
  <a href="?page={{ page_obj.next_page_number }}">Next</a>
  <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
  {% endif %}
</div>
```

---

### ✅ Pagination Object Attributes

| Attribute                      | Description                               |
| ------------------------------ | ----------------------------------------- |
| `page_obj`                     | Current page object                       |
| `page_obj.has_next`            | Returns `True` if there's a next page     |
| `page_obj.has_previous`        | Returns `True` if there's a previous page |
| `page_obj.number`              | Current page number                       |
| `page_obj.paginator.num_pages` | Total number of pages                     |
| `page_obj.paginator.count`     | Total number of items                     |

---

### 🔁 Summary Flow

1. Get the queryset:

   ```python
   Post.objects.all()
   ```

2. Create a Paginator object:

   ```python
   Paginator(queryset, per_page)
   ```

3. Get page number from URL:

   ```python
   request.GET.get('page')
   ```

4. Get only that page:

   ```python
   paginator.get_page(page_number)
   ```

5. Pass page object to template:

   ```python
   {'page_obj': page_obj}
   ```