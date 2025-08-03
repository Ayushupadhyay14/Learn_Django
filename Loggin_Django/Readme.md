# 📝 Django Logging Complete Notes
## 📘 What is Logging in Django?

**Logging** is the process of recording events that happen when a program runs. Django uses Python’s built-in `logging` module to log messages for debugging, monitoring, and production diagnostics.

---

## ✅ Why Use Logging?

- ✅ Monitor application behavior
- ✅ Track and fix bugs
- ✅ Replace `print()` in production
- ✅ Log user actions, API calls, exceptions
- ✅ Integrate with tools like **Sentry**, **Logstash**, etc.

---

## 🚦 Logging Levels

| Level      | When to Use                         | Example Use Case            |
| ---------- | ----------------------------------- | --------------------------- |
| `DEBUG`    | Detailed info for debugging         | Print variable values       |
| `INFO`     | General app events                  | User registered, email sent |
| `WARNING`  | Unexpected behavior, not critical   | Missing user email          |
| `ERROR`    | Errors that prevent normal behavior | API call failed, DB error   |
| `CRITICAL` | Very serious error – app may crash  | Payment gateway down        |

---

## ⚙️ Basic Setup (settings.py)

```python
# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

📝 This logs **all Django activity** to a `debug.log` file.

---

## 🧱 Using Logging in Views

```python
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug("This is a debug message")
    logger.info("User accessed my_view")
    logger.warning("Something seems off")
    logger.error("An error occurred")
    logger.critical("Critical system failure!")
    return HttpResponse("Logged!")
```

---

## 🛠️ Practical Use Cases

### 🐛 1. Debugging

```python
logger.debug(f"Form data: {request.POST}")
```

### 🚨 2. Error Handling

```python
try:
    result = external_api_call()
except Exception as e:
    logger.error("API failed", exc_info=True)
```

### 📩 3. Activity Logging

```python
logger.info(f"User {request.user} submitted feedback")
```

---

## 🧪 Testing Logs

Logs are saved in the file specified (`debug.log`). You can check log outputs there for debugging.

---

## 🧰 Bonus: Logging to Console (Development Only)

```python
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
}
```

---

## 🔁 Summary Workflow

```txt
Action Happens → Logging Statement → Handler (File/Console/Email) → Stored Log
```

---

## 📦 Advanced Logging Tools

- 🔧 [Sentry](https://sentry.io/) – Real-time error tracking
- 📄 [Logstash](https://www.elastic.co/logstash/) – Part of the ELK stack
- 📊 Cloudwatch / Datadog – For large-scale apps

