# First FastAPI app

```bash
python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
```

Create a Python file `api.py` with code.

```python
from fastapi import FastAPI

app = FastAPI()
```

```bash
uvicorn api:app --reload
```

After everything is looking good, make a `requirements.txt` file before commit.

```powershell
pip freeze > requirements.txt
```
