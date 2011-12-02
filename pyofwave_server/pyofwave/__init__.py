
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

def start(settings_mod=None):
    # Setup the configuration using a configuration file
    from conf import setup_environ
    setup_environ(settings_mod)
    
    from twisted.internet import reactor
    import protocols

    # Protocol interface
    protocol_server = reactor.listenTCP(8080, protocols.http.factory)

    # Internet
    internet_server = reactor.listenTCP(9283, protocols.client.factory)
    
    reactor.run()

