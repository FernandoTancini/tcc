from base.profiling import Profiling

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


class MonitorMiddleware(BaseMiddleware):
    def __call__(self, request):
        Profiling.start()
        response = self.get_response(request)
        Profiling.log()
        return response