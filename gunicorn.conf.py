import os

# Bind to PORT environment variable
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

# Worker configuration
workers = 4
worker_class = 'sync'

# Timeout configuration
timeout = 120

# Logging configuration
accesslog = '-'
errorlog = '-'
loglevel = 'info'
