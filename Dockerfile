FROM joyzoursky/python-chromedriver:3.9-alpine-selenium
ADD requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH=ui:$PYTHONPATH
ADD ui ui
CMD ["pytest", "ui/tests"]
