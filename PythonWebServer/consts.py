from typing import (Dict , List)
from builtins import (int , str)


CONST_COLORS : List[Dict[int , str]] = [
    {
        0 : "#1D2934" ,
        1 : "#ffffff" ,
        2 : "#00C300" ,
        3 : "#000000" ,
        4 : "#33485B"
    }
]

HOST : str = ""
PORT : int = 8080
CONTENT_TYPE : str = "Content-type: text/html\n"
HTTP_TYPE : str = "HTTP/1.0 200 OK\n"
ENCODE : str = "iso-8859-1"
