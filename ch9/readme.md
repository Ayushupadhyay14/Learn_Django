Here’s a full, well-structured **Django Forms Notes** — covering all types of forms, validation, widgets, and styling with Bootstrap — perfect for revision, interview prep, or semester study.

---

# 📘 Django Forms – Complete Notes

---

## 🔶 1. What are Django Forms?

Django Forms handle user input through web forms — they provide:

- Form rendering (HTML)
- Validation (backend-side)
- Cleaned data (`form.cleaned_data`)
- Error handling

---

## 🔸 2. Types of Django Forms

| Type              | Description                                    |
| ----------------- | ---------------------------------------------- |
| `forms.Form`      | For simple, custom form fields (not DB-linked) |
| `forms.ModelForm` | Automatically creates fields from model fields |

---

### ✅ `forms.Form` Example

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---

### ✅ `forms.ModelForm` Example

```python
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
```

---

## 🔹 3. Rendering Forms in Templates

```html
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <!-- or as_table / as_ul -->
  <button type="submit">Submit</button>
</form>
```

---

## 🔸 4. Form Validation

### 🔹 Built-in Validation

- `required=True`
- `max_length`, `min_length`
- `EmailField`, `URLField` auto-validate format

### 🔹 Custom Validation

#### Field-level Validation

```python
def clean_name(self):
    name = self.cleaned_data['name']
    if name.lower() == 'admin':
        raise forms.ValidationError("Invalid name")
    return name
```

#### Form-level Validation

```python
def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    confirm = cleaned_data.get("confirm_password")

    if password != confirm:
        raise forms.ValidationError("Passwords do not match")
```

---

## 🔸 5. Widgets in Django

Widgets control the HTML rendering of form fields.

| Widget                     | Output Type               |
| -------------------------- | ------------------------- |
| `TextInput`                | `<input type="text">`     |
| `Textarea`                 | `<textarea>`              |
| `CheckboxInput`            | `<input type="checkbox">` |
| `RadioSelect`              | Radio buttons             |
| `Select`, `SelectMultiple` | Dropdowns                 |
| `ClearableFileInput`       | File input                |

### Example:

```python
name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
```

---

## 🔸 6. Styling Forms with Bootstrap

### Using `attrs` in Widgets:

```python
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
```

### Render in Template:

```html
<form method="post" class="form">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

---

## 🔸 7. Useful Form Methods

| Method                      | Description                    |
| --------------------------- | ------------------------------ |
| `is_valid()`                | Returns True if form is valid  |
| `cleaned_data`              | Dictionary of validated fields |
| `add_error(field, message)` | Manually adds an error         |
| `save()` (ModelForm)        | Saves form data to database    |

---

## 🧠 Summary Table

| Topic      | Details                                 |
| ---------- | --------------------------------------- |
| Types      | `Form`, `ModelForm`                     |
| Validation | Built-in, custom (`clean_`, `clean()`)  |
| Widgets    | Control HTML rendering                  |
| Styling    | Use `attrs` for Bootstrap CSS           |
| Rendering  | `{{ form.as_p }}`, etc. in templates    |
| Submission | `form.is_valid()` + `form.cleaned_data` |

---

Let me know if you'd like examples with **FormView**, **AJAX form handling**, or **modelformset_factory** included too!
