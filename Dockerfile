FROM rapidfort/python-chromedriver
WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src
CMD python -m pytest -n4