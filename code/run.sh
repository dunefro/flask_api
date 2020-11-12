#!/bin/bash

DATABASE="data.db"
if [ -f $DATABASE ]
then
    rm -rf $DATABASE
fi
export FLASK_APP=main.py
export FLASK_ENV=development
PYTHONHOME='/home/ubuntu/workspace/flask_api/code'

#In Flask when we use debug mode it runs twice so that is why --no-reload option is added
flask run -h 0.0.0.0 --no-reload