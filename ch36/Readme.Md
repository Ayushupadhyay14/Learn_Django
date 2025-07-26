# 📘 Django 5 – `annotate()` Explained
## ✅ What is `annotate()`?
`annotate()` is a **QuerySet method** in Django ORM used to **add calculated fields** to each item in a QuerySet using **aggregation functions** (like `Count`, `Sum`, `Avg`, etc.).

It is useful when you want to perform calculations **across relationships** (like how many books each author has).

---

## 🔧 Syntax

```python
from django.db.models import Count, Sum, Avg, Max, Min
Model.objects.annotate(new_field=AggregateFunction('related_field'))
```
````

---

## 📌 Common Aggregation Functions

| Function  | Description               |
| --------- | ------------------------- |
| `Count()` | Count related objects     |
| `Sum()`   | Sum of numeric fields     |
| `Avg()`   | Average of numeric fields |
| `Max()`   | Maximum value of field    |
| `Min()`   | Minimum value of field    |

---

## 🧪 Basic Example

### Models

```python
# models.py
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### Use `annotate()` to count books per author:

```python
from django.db.models import Count
authors = Author.objects.annotate(book_count=Count('book'))

for author in authors:
    print(author.name, author.book_count)
```

✅ Output:

```
J.K. Rowling → 7
George R.R. Martin → 5
```

---

## 🔁 Multiple Annotations Example

```python
from django.db.models import Count, Avg

Author.objects.annotate(
    book_count=Count('book'),
    avg_price=Avg('book__price')
)
```

Each `Author` object will now include:

- `book_count`: number of books
- `avg_price`: average price of their books

---

## 🔍 Filter + Annotate

```python
Author.objects.filter(book__price__gt=300).annotate(total_books=Count('book'))
```

➡️ Returns authors who have books priced above 300, with the total book count.

---

## 📌 Key Points

- Returns a **new QuerySet** with additional fields.
- Doesn’t modify the database.
- Can be combined with `values()`, `filter()`, `order_by()` for reporting.
- Can use `F()` expressions for advanced annotations.

---

## 🧠 Summary

| Feature      | Description                                   |
| ------------ | --------------------------------------------- |
| Purpose      | Add aggregate field to each QuerySet object   |
| Returns      | New QuerySet with annotated values            |
| Use Cases    | Count, sum, or average on related fields      |
| Aggregations | `Count()`, `Sum()`, `Avg()`, `Max()`, `Min()` |

---

## 🧰 Useful in

- Blog post with comment count
- Product list with review count and avg rating
- User dashboard with activity stats
