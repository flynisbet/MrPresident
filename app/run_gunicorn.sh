#!/bin/bash

cd /Users/flynnnisbet/Desktop/CSC-342/semesterProject/app
source ../.venv/bin/activate
gunicorn --reload --workers 3 --capture-output --log-level debug --bind unix:project.sock -m 007 wsgi:app
