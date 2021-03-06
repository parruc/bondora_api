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


class ApiResultMyInvestments(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, page_size=None, page_nr=None, total_count=None, count=None, payload=None, success=None, errors=None):
        """
        ApiResultMyInvestments - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'page_size': 'int',
            'page_nr': 'int',
            'total_count': 'int',
            'count': 'int',
            'payload': 'list[MyInvestmentItem]',
            'success': 'bool',
            'errors': 'list[ApiError]'
        }

        self.attribute_map = {
            'page_size': 'PageSize',
            'page_nr': 'PageNr',
            'total_count': 'TotalCount',
            'count': 'Count',
            'payload': 'Payload',
            'success': 'Success',
            'errors': 'Errors'
        }

        self._page_size = page_size
        self._page_nr = page_nr
        self._total_count = total_count
        self._count = count
        self._payload = payload
        self._success = success
        self._errors = errors

    @property
    def page_size(self):
        """
        Gets the page_size of this ApiResultMyInvestments.
        Requested Max items in result

        :return: The page_size of this ApiResultMyInvestments.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this ApiResultMyInvestments.
        Requested Max items in result

        :param page_size: The page_size of this ApiResultMyInvestments.
        :type: int
        """

        if not page_size:
            raise ValueError("Invalid value for `page_size`, must not be `None`")
        if page_size > 2.147483647E9:
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `2.147483647E9`")
        if page_size < 0.0:
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `0.0`")

        self._page_size = page_size

    @property
    def page_nr(self):
        """
        Gets the page_nr of this ApiResultMyInvestments.
        Requested page nr

        :return: The page_nr of this ApiResultMyInvestments.
        :rtype: int
        """
        return self._page_nr

    @page_nr.setter
    def page_nr(self, page_nr):
        """
        Sets the page_nr of this ApiResultMyInvestments.
        Requested page nr

        :param page_nr: The page_nr of this ApiResultMyInvestments.
        :type: int
        """

        if not page_nr:
            raise ValueError("Invalid value for `page_nr`, must not be `None`")
        if page_nr > 2.147483647E9:
            raise ValueError("Invalid value for `page_nr`, must be a value less than or equal to `2.147483647E9`")
        if page_nr < 1.0:
            raise ValueError("Invalid value for `page_nr`, must be a value greater than or equal to `1.0`")

        self._page_nr = page_nr

    @property
    def total_count(self):
        """
        Gets the total_count of this ApiResultMyInvestments.
        Total number of items found

        :return: The total_count of this ApiResultMyInvestments.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this ApiResultMyInvestments.
        Total number of items found

        :param total_count: The total_count of this ApiResultMyInvestments.
        :type: int
        """

        if not total_count:
            total_count = 0
            # raise ValueError("Invalid value for `total_count`, must not be `None`")
        if total_count > 2.147483647E9:
            raise ValueError("Invalid value for `total_count`, must be a value less than or equal to `2.147483647E9`")
        if total_count < 0.0:
            raise ValueError("Invalid value for `total_count`, must be a value greater than or equal to `0.0`")

        self._total_count = total_count

    @property
    def count(self):
        """
        Gets the count of this ApiResultMyInvestments.
        Number of items returned

        :return: The count of this ApiResultMyInvestments.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ApiResultMyInvestments.
        Number of items returned

        :param count: The count of this ApiResultMyInvestments.
        :type: int
        """

        if not count:
            count = 0
            # raise ValueError("Invalid value for `count`, must not be `None`")
        if count > 2.147483647E9:
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `2.147483647E9`")
        if count < 0.0:
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0.0`")

        self._count = count

    @property
    def payload(self):
        """
        Gets the payload of this ApiResultMyInvestments.
        The payload of the response. Type depends on the API request.

        :return: The payload of this ApiResultMyInvestments.
        :rtype: list[MyInvestmentItem]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this ApiResultMyInvestments.
        The payload of the response. Type depends on the API request.

        :param payload: The payload of this ApiResultMyInvestments.
        :type: list[MyInvestmentItem]
        """

        self._payload = payload

    @property
    def success(self):
        """
        Gets the success of this ApiResultMyInvestments.
        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.

        :return: The success of this ApiResultMyInvestments.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ApiResultMyInvestments.
        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.

        :param success: The success of this ApiResultMyInvestments.
        :type: bool
        """

        self._success = success

    @property
    def errors(self):
        """
        Gets the errors of this ApiResultMyInvestments.
        Error(s) accociated with the API request.

        :return: The errors of this ApiResultMyInvestments.
        :rtype: list[ApiError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ApiResultMyInvestments.
        Error(s) accociated with the API request.

        :param errors: The errors of this ApiResultMyInvestments.
        :type: list[ApiError]
        """

        self._errors = errors

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
