# 
FROM python:3.9

# 
WORKDIR ~/docker/fastapi

# 
COPY . ~/docker/fastapi

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
CMD ["fastapi", "run", "main.py", "--port", "80"]