# 📘 **Django Extensions – Notes**
### ✅ **Definition:**

Django Extensions is a third-party Django package that provides **extra management commands** and **tools** to make development faster and easier.

---

### ⚙️ **Installation:**

```bash
pip install django-extensions
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'django_extensions',
]
```

---

### 🔑 **Top Features / Commands:**

| Command              | Description                                         |
| -------------------- | --------------------------------------------------- |
| `shell_plus`         | Opens Django shell with all models auto-imported    |
| `show_urls`          | Displays all registered URLs with views             |
| `graph_models`       | Generates diagram of models (needs Graphviz)        |
| `runscript`          | Runs a custom script inside Django environment      |
| `sqldiff`            | Shows difference between models and database schema |
| `print_settings`     | Prints current Django settings                      |
| `create_command`     | Creates a new custom management command             |
| `show_template_tags` | Lists all available template tags and filters       |
| `validate_templates` | Checks templates for errors or unused variables     |

---

### 💡 **Common Use Cases:**

- Debugging URLs and views
- Working efficiently with the Django shell
- Visualizing complex model relationships
- Running admin/database automation scripts
- Schema comparison and versioning

---

### 🖼️ Example: `runscript`

```bash
python manage.py runscript my_script
```

**my_script.py:**

```python
def run():
    print("Hello from script!")
```

---

### 📌 **Note:**

- Django Extensions are for **development only**, not production.
- Some features (like `graph_models`) need **Graphviz** installed.

---

Let me know if you'd like flashcards, Hindi notes, or real project examples!
