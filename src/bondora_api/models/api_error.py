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

from pprint import pformat
from six import iteritems
import re


class ApiError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, message=None, details=None):
        """
        ApiError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'message': 'str',
            'details': 'str'
        }

        self.attribute_map = {
            'code': 'Code',
            'message': 'Message',
            'details': 'Details'
        }

        self._code = code
        self._message = message
        self._details = details

    @property
    def code(self):
        """
        Gets the code of this ApiError.
        Code of the error. For machine reading.

        :return: The code of this ApiError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ApiError.
        Code of the error. For machine reading.

        :param code: The code of this ApiError.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ApiError.
        The error message for human reading.

        :return: The message of this ApiError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ApiError.
        The error message for human reading.

        :param message: The message of this ApiError.
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """
        Gets the details of this ApiError.
        Error details, if any.               For example the non valid Field's name or the Id of the failed object.

        :return: The details of this ApiError.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ApiError.
        Error details, if any.               For example the non valid Field's name or the Id of the failed object.

        :param details: The details of this ApiError.
        :type: str
        """

        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
