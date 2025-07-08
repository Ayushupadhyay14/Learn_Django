## ✅ 1️⃣ **Abstract Base Classes (Abstract Model)**

**Definition:**
Used when you want to put common fields/methods into a base class, but **don’t want to create a separate database table** for the base model.

**Use case:**
Share common fields (like `created_at`, `updated_at`) across multiple models.

**Example:**

```python
from django.db import models

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(CommonInfo):
    name = models.CharField(max_length=50)

class Teacher(CommonInfo):
    name = models.CharField(max_length=50)
```

- `CommonInfo` won’t create its own table.
- `Student` and `Teacher` will each have `created_at` and `updated_at`.

---

## ✅ 2️⃣ **Multi-table Inheritance**

**Definition:**
Each model gets its **own database table**. The child table will have a OneToOne link to the parent table.

**Use case:**
When you want to extend a model and still keep each part in its own table.

**Example:**

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Student(Person):
    roll_number = models.CharField(max_length=20)
```

- `Person` table: stores common fields (`name`).
- `Student` table: stores extra field (`roll_number`) + OneToOne relation to `Person`.

---

## ✅ 3️⃣ **Proxy Models**

**Definition:**
Use the **same database table** as the original model but can change behavior (e.g., add custom methods or modify default manager/queryset).

**Use case:**
When you want to change the Python behavior without changing the database schema.

**Example:**

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class PersonProxy(Person):
    class Meta:
        proxy = True

    def say_hello(self):
        return f"Hello, {self.name}!"
```

- `PersonProxy` doesn’t create a new table.
- Adds a custom method `say_hello()` to the `Person` model.

---

✅ **📌 Summary Table:**

| Type          | Own Table? | Purpose                                 |
| ------------- | ---------- | --------------------------------------- |
| Abstract Base | ❌         | Share fields/methods, no separate table |
| Multi-table   | ✅         | Extend model, separate table for child  |
| Proxy         | ❌         | Change Python behavior, keep same table |

---
