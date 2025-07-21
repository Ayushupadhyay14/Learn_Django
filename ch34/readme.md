
# 🧠 Django 5 – Generic Views (Class-Based)

Generic views provide **built-in logic** for common tasks like listing, creating, updating, or deleting objects. They help you **write less code** by using **predefined class-based views** from Django.

---

## ✅ Common Generic Views

| View Class   | Purpose                            |
| ------------ | ---------------------------------- |
| `ListView`   | Display a list of objects          |
| `DetailView` | Display details of a single object |
| `CreateView` | Create a new object                |
| `UpdateView` | Update an existing object          |
| `DeleteView` | Delete an object                   |

---

## 🔹 Example: ListView

### `views.py`:

```python
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
```

### `urls.py`:

```python
from .views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
]
```

### `student_list.html`:

```html
<h2>All Students</h2>
<ul>
  {% for student in students %}
  <li>{{ student.name }}</li>
  {% endfor %}
</ul>
```

---

## 🔹 Example: DetailView

```python
# views.py
from django.views.generic import DetailView
from .models import Student

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
```

```python
# urls.py
path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
```

---

## 🔹 Example: CreateView

```python
# views.py
from django.views.generic.edit import CreateView
from .models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'age']
    template_name = 'student_form.html'
    success_url = '/students/'
```

---

## 🔹 Required Template Files

For Create, Update, and Delete views, Django looks for:

- `model_form.html` → `modelname_form.html`
- `model_confirm_delete.html` → `modelname_confirm_delete.html`

---

## ✅ Summary Table – Generic Views

| Generic View | URL Pattern Example   | Purpose                      |
| ------------ | --------------------- | ---------------------------- |
| `ListView`   | `/students/`          | List all entries             |
| `DetailView` | `/students/3/`        | Detail of a specific student |
| `CreateView` | `/students/add/`      | Create a new student         |
| `UpdateView` | `/students/3/edit/`   | Update student details       |
| `DeleteView` | `/students/3/delete/` | Delete a student             |

---

## 📁 Optional: Override Behavior in Generic Views

```python
def get_queryset(self):
    return Student.objects.filter(active=True)

def form_valid(self, form):
    # Custom logic before saving
    return super().form_valid(form)
```

---

Would you like notes on:

- Django REST API views (`APIView`, `ModelViewSet`)
- Handling forms with `CreateView` & `UpdateView`
- Custom validation in CBVs
- Function vs Generic views interview questions?

Just let me know!
