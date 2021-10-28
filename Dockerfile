FROM python

WORKDIR /docs
ADD requirements.txt /docs
ADD build /docs/build
COPY source /docs/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m sphinx source/suite build/suite
RUN python -m sphinx source/landing build/landing
RUN python -m sphinx source/carbonio build/carbonio
