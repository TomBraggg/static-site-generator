export PYTHONPATH=$(pwd)
python3 mdconvert/main.py
cd public && python3 -m http.server 8888