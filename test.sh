#!/bin/bash
mypy . && coverage run manage.py test --failfast --keepdb -v 0 --debug-mode && coverage report
