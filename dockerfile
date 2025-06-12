FROM python:alpine

WORKDIR /usr/app

COPY main.py ./
COPY templates templates/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5002

# Run main.py when the container launches forreal
CMD ["python", "main.py"]