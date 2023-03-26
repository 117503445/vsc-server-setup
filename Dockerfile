FROM python
WORKDIR /root
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python" , "main.py"]