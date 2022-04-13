FROM python:3.9.10

# Create Python Virtual environment
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH ="$VIRTUAL_ENV/bin:$PATH"

COPY . .

# Install packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "run.py"]
