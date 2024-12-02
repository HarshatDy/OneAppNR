FROM python:3.12.7-bookworm

COPY . /app
WORKDIR /app 

RUN python3 -m venv /opt/venv

RUN pip install pip --upgrade 
RUN /opt/venv/bin/pip install -r new_requirements.txt
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]

