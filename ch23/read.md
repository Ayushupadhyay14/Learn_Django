Here you go!
I’ve prepared a **clean, interview-ready document** in **Word format style** (text below)
that you can copy into Word (`.docx`) or Google Docs.

---

## 📄 **Django ORM: Using `.all()` and `.filter()` (Returns New QuerySet)**

---

### ✅ **What is a QuerySet?**

- A **QuerySet** is a collection of database records built by Django ORM.
- It represents the SQL query, but **doesn’t run it immediately** (lazy loading).

---

### ⚙ **Using `.all()`**

- `Model.objects.all()` returns a QuerySet containing **all records**.

```python
students = Student.objects.all()
```

---

### ⚙ **Using `.filter()`**

- Returns a new QuerySet containing only matching records.

```python
active_students = Student.objects.filter(is_active=True)
```

---

### 🔧 **Chaining filters (new QuerySets)**

Each filter creates a new QuerySet:

```python
qs = Student.objects.all()
qs2 = qs.filter(city='Indore')
qs3 = qs2.filter(is_active=True)
```

Original `qs` stays unchanged.

---

### 📌 **Other common QuerySet methods**

| Method                 | What it does                           | Example                                          |
| ---------------------- | -------------------------------------- | ------------------------------------------------ |
| `.exclude()`           | Exclude records                        | `Student.objects.exclude(city='Indore')`         |
| `.order_by()`          | Sort results                           | `Student.objects.order_by('name')`               |
| `.count()`             | Count number of records                | `Student.objects.filter(is_active=True).count()` |
| `.first()` / `.last()` | Get first / last record                | `Student.objects.first()`                        |
| `.get()`               | Get single record (raises error if >1) | `Student.objects.get(id=1)`                      |

---

### ✅ **Why Django returns new QuerySets (Key points)**

- QuerySets are **immutable** → safe to reuse.
- Supports **chaining**: build complex queries step by step.
- **Lazy evaluation** → actual DB hit only when data is used.
- Keeps code clean and efficient.

---

### 🧠 **Interview summary (say this):**

> “In Django, methods like `.all()`, `.filter()`, `.exclude()` don’t modify the existing QuerySet; they return a **new QuerySet**.
> This makes QuerySets immutable, supports chaining, and helps delay database access until needed.
> It’s an efficient and clean way to build complex queries.”

---

✅ **Tip:**
Always start from `Model.objects` (the manager) and chain filters as needed.

---

If you'd like,
I can **generate and send you this as an actual `.docx` Word file**
Just say:

