
# Project Structure

* project/

  - .venv/  -- virtual environment (ignored by Git) so dependencies are local to the project
  
  - requirements.txt  -- reproducible, frozen dependency list checked into Git
  
  - src/  -- put your package/module code here (enables the modern "source" layout to avoid accidental imports from the repository root)
  
  - notebooks/  -- exploration and reports; bind them to the project kernel 

  - tests/  -- even a single sanity test prevents regressions


## Create .venv

Create virtual environment like this:
```
python3 -m venv .venv

source .venv/bin/activate
# on windows: .venv\Scripts\activate.bat

python -m pip install --upgrade pip

python -m pip install -r requirements.txt
```
