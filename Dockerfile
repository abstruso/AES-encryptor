FROM python:3

WORKDIR /usr/src/app

COPY aes_encryptor.py .
COPY aes_methods.py .
COPY hash_methods.py .
COPY number_field_arithmetic.py . 
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","./aes_encryptor.py"]

