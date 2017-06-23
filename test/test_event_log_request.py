# coding: utf-8

"""
    Bondora API V1

    Bondora API version 1

    OpenAPI spec version: v1
    Contact: investor@bondora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import bondora_api
from bondora_api.rest import ApiException
from bondora_api.models.event_log_request import EventLogRequest


class TestEventLogRequest(unittest.TestCase):
    """ EventLogRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventLogRequest(self):
        """
        Test EventLogRequest
        """
        model = bondora_api.models.event_log_request.EventLogRequest()


if __name__ == '__main__':
    unittest.main()
