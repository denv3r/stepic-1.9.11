# import urllib.parse
import urlparse

def wsgi_application(environ, start_response):

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # query_dict = urllib.parse.parse_qs(environ['QUERY_STRING'])
    query_dict = urlparse.parse_qs(environ['QUERY_STRING'])
    body = []
    for param, value in query_dict.items():
        print(param + '=' + value[0])
        body.append(param + '=' + value[0])
    print body
    
    start_response(status, headers)
    return body
