
#
# PyOfWave Server
# Copyright (C) 2011 'alcinnz'
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging

logger = logging.getLogger("pyofwave.server")

def start(settings_mod=None):
    # Setup the configuration using a configuration file
    from conf import setup_environ
    setup_environ(settings_mod)
    
    from twisted.internet import reactor

    import storage # Initialize data stores
    import protocols

    # Protocol interface
    protocol_server_port = 8080
    logger.debug("Starting http protocol server on port %s..." % protocol_server_port)
    protocol_server = reactor.listenTCP(protocol_server_port, 
                                        protocols.http.factory)
    logger.info("HTTP protocol server started on %s" % protocol_server.getHost())
    
    # Internet
    internet_server_port = 9283
    logger.debug("Starting internet/client server on port %s..." % internet_server_port)
    internet_server = reactor.listenTCP(internet_server_port, 
                                        protocols.client.factory)
    logger.info("HTTP internet server started on %s" % internet_server.getHost())

    reactor.run()

