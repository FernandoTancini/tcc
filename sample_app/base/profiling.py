import time
from django.db import connection, reset_queries


class Query:
    total_queries = {}

    @staticmethod
    def start(label='default'):
        reset_queries()
        if not Query.total_queries.get(label):
            Query.total_queries[label] = 0

    @staticmethod
    def pause(label='default'):
        if Query.total_queries.get(label) is not None:
            Query.total_queries[label] += len(connection.queries)
        reset_queries()

    @staticmethod
    def log(label='default'):
        Query.pause(label)
        queries = Query.total_queries.get(label, 0)
        print(f'Query {label}: {queries} queries')
        Query.total_queries[label] = None
        Query.start(label)


class Timer:
    start_time = {}
    total_time = {}

    @staticmethod
    def start(label='default'):
        Timer.start_time[label] = time.time()
        if not Timer.total_time.get(label):
            Timer.total_time[label] = 0

    @staticmethod
    def pause(label='default'):
        start = Timer.start_time.get(label)
        elapsed_time = (time.time() - start) if start else 0
        Timer.start_time[label] = None
        Timer.total_time[label] = Timer.total_time.get(label, 0) + elapsed_time

    @staticmethod
    def log(label='default'):
        Timer.pause(label)
        elapsed_time = round(1000 * Timer.total_time[label])
        print(f'Timer {label}: {elapsed_time} ms')
        Timer.total_time[label] = None
        Timer.start(label)


class Profiling:
    @staticmethod
    def start(label='default'):
        Timer.start(label)
        Query.start(label)

    @staticmethod
    def pause(label='default'):
        Timer.pause(label)
        Query.pause(label)

    @staticmethod
    def log(label='default'):
        print()
        Timer.log(label)
        Query.log(label)
        print()
