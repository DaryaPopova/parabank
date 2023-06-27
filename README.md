Test for https://parabank.parasoft.com/parabank/register.htm
 

## Run the project
How to build and run the project

Ensure you have Git and Python3 installed
 
Clone the project 
```bash
git clone https://github.com/DaryaPopova/parabank.git
```
Go to the directory
```bash
cd parabank/
```

Create virtual python environment
```bash
virtualenv venv
```
Activate virtual python environment
```bash
source venv/bin/activate
```
Install all the requirements
```bash
pip install -r requirements.txt
```
Export Python path
```bash
export PYTHONPATH=ui:$PYTHONPATH
```
Run tests
```bash
pytest ui/tests
```
#### Run the project via Docker

Ensure you have Docker installed

Build docker file
```bash
docker build -t parabank_tests  .
```
Run docker file
```bash
docker run parabank_tests
```