FROM ubuntu

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
# ENV FLASK_DEBUG=1
# ENV FLASK_APP=app.py

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src ./