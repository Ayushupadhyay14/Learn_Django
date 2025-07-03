Sure! Here are the **main methods** to get a queryset or related data in Django ORM:

✅ **Returns a queryset:**

- `.all()`
- `.filter()`
- `.exclude()`
- `.order_by()`
- `.values()`
- `.values_list()`
- `.annotate()`
- `.distinct()`
- `.select_related()`
- `.prefetch_related()`

⚠ **Does _not_ return a queryset:**

- `.get()` → returns a single object
- `.first()` / `.last()` → returns a single object or None
- `.count()` → returns an integer
- `.exists()` → returns a boolean
- `.aggregate()` → returns a dictionary
- `.create()` → returns a single object
- `.update()` / `.delete()` → return integer (number of rows affected)

If you'd like, I can also explain each in 1–2 lines!

Sure! Let’s explain this clearly and simply:

---

## ✅ **What is “Working with Database Field Lookups” in Django?**

**Definition:**
In Django, **field lookups** are special query expressions that allow you to **filter or query the database** by comparing fields in more advanced ways than just exact matches.

Instead of only checking if a field equals a value, you can use lookups to check:

- If it contains a substring
- If it starts with or ends with something
- If it’s greater than, less than, etc.

These lookups are used with Django ORM methods like `.filter()`, `.exclude()`, and `.get()`.

---

### 🧩 **Example:**

Suppose you have a model:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
```

---

**Using field lookups:**

```python
# Get all books where title contains 'python' (case-insensitive)
Book.objects.filter(title__icontains='python')

# Get books with price greater than 100
Book.objects.filter(price__gt=100)

# Get books whose title starts with 'Django'
Book.objects.filter(title__startswith='Django')

# Get books whose price is between 50 and 150
Book.objects.filter(price__range=(50, 150))
```

---

### ✅ **How it works:**

- `field__lookup=value`
- Examples of common lookups: `exact`, `iexact`, `contains`, `icontains`, `gt` (greater than), `lt` (less than), `range`, `startswith`, etc.

---

**In summary:**

> “Working with database field lookups” means using these built-in query expressions to **filter, search, or retrieve objects from the database** in flexible ways, beyond simple equality checks.

If you'd like,
✅ I can also give a **list of common field lookups** or real-life use cases — just ask! 🚀

Sure! In **Django 5**, if you want to **limit a QuerySet** (i.e., get only a certain number of records from the database), you can simply use **slicing** on the QuerySet.

Here’s how you can do it:

✅ **Example:**

```python
# models.py
from myapp.models import Employee

# Get first 5 employees
employees = Employee.objects.all()[:5]
```

### 🔹 Explanation:

- `Employee.objects.all()` returns all Employee objects.
- `[:5]` slices the QuerySet to return only the first 5 records.
- This will translate to an SQL query with `LIMIT 5`.

---

✅ **To get records between certain positions:**

```python
# Get records from 5th to 10th (index 4 to 9)
employees = Employee.objects.all()[4:10]
```

---

✅ **To skip the first N records (offset):**

```python
# Skip first 10 and get next 5
employees = Employee.objects.all()[10:15]
```

---

⭐ **Important:**

- Slicing works only on ordered QuerySets (Django may add an implicit ordering by primary key if none is defined).
- Using slicing is efficient, as Django adds `LIMIT` and `OFFSET` directly in the SQL query.

If you'd like, I can also show how to combine this with `.filter()`, `.order_by()`, or pagination. Just let me know!
