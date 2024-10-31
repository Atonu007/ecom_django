from multiprocessing import cpu_count

workers = cpu_count() * 2 +1
bind = "0.0.0.0:8010"
worker_class = "gthread"
thread = workers + 1

daemon = False