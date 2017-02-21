import log

class StatisticMiddleware(object):

    def process_request(self, request):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_kwargs != {}:
            if view_kwargs.get('id', 0) != 0:
                log.writeLog(view_kwargs)

        
        
