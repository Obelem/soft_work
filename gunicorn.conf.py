# gunicorn.conf.py
bind = "0.0.0.0:5000"
workers = 3
# Access log - records incoming HTTP requests
accesslog = "./log/gunicorn.access.log"
# Error log - records Gunicorn server goings-on
errorlog = "./log/gunicorn.error.log"
# Whether to send flask output to the error log 
capture_output = True
# How verbose the Gunicorn error logs should be 
loglevel = "info"