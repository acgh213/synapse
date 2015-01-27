# -*- coding: utf-8 -*-
# Copyright 2015 OpenMarket Ltd
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

from twisted.internet import defer


class Filtering(object):

    def __init__(self, hs):
        super(Filtering, self).__init__()
        self.store = hs.get_datastore()

    def get_user_filter(self, user_localpart, filter_id):
        return self.store.get_user_filter(user_localpart, filter_id)

    def add_user_filter(self, user_localpart, definition):
        # TODO(paul): implement sanity checking of the definition
        return self.store.add_user_filter(user_localpart, definition)

    # TODO(paul): surely we should probably add a delete_user_filter or
    #   replace_user_filter at some point? There's no REST API specified for
    #   them however