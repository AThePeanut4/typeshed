"""
SocksiPy - Python SOCKS module.

Version 1.00

Copyright 2006 Dan-Haim. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of Dan Haim nor the names of his contributors may be used
   to endorse or promote products derived from this software without specific
   prior written permission.

THIS SOFTWARE IS PROVIDED BY DAN HAIM "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL DAN HAIM OR HIS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMANGE.

This module provides a standard socket-like interface for Python
for tunneling connections through SOCKS proxies.

Minor modifications made by Christopher Gilbert (http://motomastyle.com/) for
use in PyLoris (http://pyloris.sourceforge.net/).

Minor modifications made by Mario Vilas (http://breakingcode.wordpress.com/)
mainly to merge bug fixes found in Sourceforge.
"""

import socket

PROXY_TYPE_SOCKS4: int
PROXY_TYPE_SOCKS5: int
PROXY_TYPE_HTTP: int
PROXY_TYPE_HTTP_NO_TUNNEL: int

class ProxyError(Exception): ...
class GeneralProxyError(ProxyError): ...
class Socks5AuthError(ProxyError): ...
class Socks5Error(ProxyError): ...
class Socks4Error(ProxyError): ...
class HTTPError(ProxyError): ...

def setdefaultproxy(proxytype=None, addr=None, port=None, rdns: bool = True, username=None, password=None) -> None: ...
def wrapmodule(module) -> None: ...

class socksocket(socket.socket):
    def __init__(self, family=..., type=..., proto: int = 0, _sock=None) -> None: ...
    def sendall(self, content, *args): ...
    def setproxy(
        self, proxytype=None, addr=None, port=None, rdns: bool = True, username=None, password=None, headers=None
    ) -> None: ...
    def getproxysockname(self): ...
    def getproxypeername(self): ...
    def getpeername(self): ...
    def connect(self, destpair) -> None: ...
