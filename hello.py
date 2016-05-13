import urllib.parse

def wsgi_application(environ, start_response):

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    query_dict = urllib.parse.parse_qs(environ['QUERY_STRING'])
    body = []
    for param, value in query_dict.items():
        print(param + '=' + value[0])
        body.append(param + '=' + value[0])
    
    start_response(status, headers )
    return body