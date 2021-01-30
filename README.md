# Mini System Monitor


-----------

1. Add "mini-system-monitor" to your INSTALLED_APPS setting like this::
```python
    INSTALLED_APPS = [
        ...
        'mini-system-monitor',
    ]
```

3. Run ```python manage.py migrate``` to create the mini-system-monitor models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled).