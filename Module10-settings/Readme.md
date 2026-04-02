# Settings Demo

```powershell
PS > $env:MY_VALUE="444"
PS > py .\main_os.py
Hello None, from Python     # if a value is not set in OS environment, then default to None
Value is 444  # value is a string

```

to verify the value is a string, can change the code to be

```python
print(f"Value is {value - 4}")  # expect to see an error
```

However, Boolean value is based on Truthy/Falsy.

The command line cannot set boolean values

```powershell
PS > $env:IS_PROD=false
false : The term 'false' is not recognized as the name of a cmdlet, function, script file, or
operable program. Check the spelling of the name, or if a path was included, verify that the
path is correct and try again.
At line:1 char:14

- $env:IS_PROD=false
-              ~~~~~

  - CategoryInfo : ObjectNotFound: (false:String) [], CommandNotFoundException
  - FullyQualifiedErrorId : CommandNotFoundException
```

```powershell

PS > $env:IS_PROD="false"
PS > py .\main_os.py
Hello None, from Python
Value is 77
Prod: false
PS >
```
