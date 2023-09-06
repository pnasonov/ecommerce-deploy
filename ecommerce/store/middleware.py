class MyMiddleware: # not using 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["SECURE_CROSS_ORIGIN_OPENER_POLICY"] = "same-origin-allow-popups"
        return response
