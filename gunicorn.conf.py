import multiprocessing
import gevent

bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = multiprocessing.cpu_count() * 1000
backlog = 1024