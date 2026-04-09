# JWT demo

```powershell
py -m venv venv
./venv/Scripts/activate

pip install pyjwt

```

After demonstrating the encode/decode jwt token, we go ahead to use it in FastAPI app

we use `bcrypt` to hash & verify user passwords

```powershell
pip install fastapi uvicorn bcrypt
pip install python-multipart
```
