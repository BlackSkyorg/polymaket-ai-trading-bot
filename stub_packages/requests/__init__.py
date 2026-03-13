"""
Stub requests module that makes real HTTP requests using http.client to bypass proxy issues.
"""
import http.client
import json
from urllib.parse import urlparse

class Response:
    def __init__(self, status_code=200, json_data=None, text_data=None):
        self.status_code = status_code
        self.json_data = json_data or {}
        self.text_data = text_data or ""
    
    def json(self):
        return self.json_data
    
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code} error")
    
    @property
    def text(self):
        return self.text_data

def post(url, json=None, headers=None, timeout=30, **kwargs):
    """Make a real HTTP POST request using http.client to bypass proxy issues"""
    try:
        parsed = urlparse(url)
        host = parsed.hostname
        port = parsed.port or (80 if parsed.scheme == 'http' else 443)
        path = parsed.path or '/'
        if parsed.query:
            path += '?' + parsed.query
        
        if json is not None:
            import json as json_module
            data = json_module.dumps(json).encode('utf-8')
            if headers is None:
                headers = {}
            headers['Content-Type'] = 'application/json'
        else:
            data = None
        
        if parsed.scheme == 'https':
            conn = http.client.HTTPSConnection(host, port, timeout=timeout)
        else:
            conn = http.client.HTTPConnection(host, port, timeout=timeout)
        
        try:
            conn.request('POST', path, body=data, headers=headers or {})
            response = conn.getresponse()
            status_code = response.status
            text_data = response.read().decode('utf-8')
            try:
                import json as json_module
                json_data = json_module.loads(text_data)
            except:
                json_data = {"error": f"Failed to parse JSON: {text_data[:200]}"}
            return Response(status_code=status_code, json_data=json_data, text_data=text_data)
        finally:
            conn.close()
    except Exception as e:
        error_msg = str(e)
        return Response(status_code=500, json_data={"error": error_msg}, text_data=error_msg)

def get(url, params=None, headers=None, timeout=30, **kwargs):
    """Make a real HTTP GET request using http.client"""
    try:
        parsed = urlparse(url)
        host = parsed.hostname
        port = parsed.port or (80 if parsed.scheme == 'http' else 443)
        path = parsed.path or '/'
        if params:
            from urllib.parse import urlencode
            path += '?' + urlencode(params)
        if parsed.query:
            path += '&' + parsed.query if '?' in path else '?' + parsed.query
        
        if parsed.scheme == 'https':
            conn = http.client.HTTPSConnection(host, port, timeout=timeout)
        else:
            conn = http.client.HTTPConnection(host, port, timeout=timeout)
        
        try:
            conn.request('GET', path, headers=headers or {})
            response = conn.getresponse()
            status_code = response.status
            text_data = response.read().decode('utf-8')
            try:
                import json as json_module
                json_data = json_module.loads(text_data)
            except:
                json_data = {}
            return Response(status_code=status_code, json_data=json_data, text_data=text_data)
        finally:
            conn.close()
    except Exception as e:
        return Response(status_code=500, json_data={"error": str(e)})

class exceptions:
    class RequestException(Exception):
        pass
