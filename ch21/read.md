### ✅ What is a **Signal** in Django?

**Signal** in Django is a way to run some code **automatically** when a certain event happens in your app.

> 💡 **Example:** When a new user is created, you can automatically create a profile for that user using a signal.

---

### 🔔 Why Use Signals?

- Keep code **clean and separate**
- Handle actions like:

  - After saving a model
  - Before deleting a model
  - On user login/logout

---

### ✅ Most Used Signals

| Signal Name      | Trigger                  |
| ---------------- | ------------------------ |
| `post_save`      | After a model is saved   |
| `pre_save`       | Before a model is saved  |
| `post_delete`    | After a model is deleted |
| `user_logged_in` | When a user logs in      |

---

## ✅ How to Use a Signal in Django (Step-by-Step)

---

### 📌 Example: Auto-create Profile when a User is created

---

### ✅ 1. Create Models

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
```

---

### ✅ 2. Create Signal File

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

### ✅ 3. Connect Signal in `apps.py`

```python
# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # 👈 This connects the signal
```

---

### ✅ 4. Update `settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyAppConfig',  # Use AppConfig, not just 'myapp'
]
```

---

### 🔄 What Happens Now?

- You create a new user → Django saves it
- `post_save` signal is triggered
- `create_profile()` is called automatically
- A Profile is created for that user

---

## ✅ Summary

| Term          | Meaning                                        |
| ------------- | ---------------------------------------------- |
| **Signal**    | A notification system in Django                |
| **Sender**    | The model that sends the signal (e.g., `User`) |
| **Receiver**  | The function that handles the signal           |
| **@receiver** | Decorator to connect signal to function        |

---

Would you like a small Django project with signals implemented for practice?
