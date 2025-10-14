import os

# Bind to the port Render expects
bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"

# Worker configuration
workers = 4
worker_class = 'sync'

# Timeout configuration
timeout = 120

# Access log configuration
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Error log configuration
errorlog = '-'
loglevel = 'info'
