FROM python

WORKDIR /docs
ADD requirements.txt /docs
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
