# Testing in Python

```powershell
py -m venv venv
.\venv\Scripts\activate
pip install pytest

```

## Coverage

```powershell
pip install pytest-cov # includes coverage
# or
pip install coverage

pytest --cov
# or
coverage run -m pytest
coverage html
```
