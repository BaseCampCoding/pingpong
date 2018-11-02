def cors_headers(get_response):
    def middleware(request):
        response = get_response(request)
        response._headers['access-control-allow-origins'] = (
            'Access-Control-Allow-Origin', '*')
        response._headers['access-control-allow-headers'] = (
            'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response

    return middleware
