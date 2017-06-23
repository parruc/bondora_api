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


class Debt(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, start_date=None, end_date=None, amount=None, max_amount=None, industry=None, reporter=None):
        """
        Debt - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',
            'end_date': 'datetime',
            'amount': 'str',
            'max_amount': 'str',
            'industry': 'str',
            'reporter': 'str'
        }

        self.attribute_map = {
            'start_date': 'StartDate',
            'end_date': 'EndDate',
            'amount': 'Amount',
            'max_amount': 'MaxAmount',
            'industry': 'Industry',
            'reporter': 'Reporter'
        }

        self._start_date = start_date
        self._end_date = end_date
        self._amount = amount
        self._max_amount = max_amount
        self._industry = industry
        self._reporter = reporter

    @property
    def start_date(self):
        """
        Gets the start_date of this Debt.
        Start

        :return: The start_date of this Debt.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Debt.
        Start

        :param start_date: The start_date of this Debt.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Debt.
        End

        :return: The end_date of this Debt.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Debt.
        End

        :param end_date: The end_date of this Debt.
        :type: datetime
        """

        self._end_date = end_date

    @property
    def amount(self):
        """
        Gets the amount of this Debt.
        Amount

        :return: The amount of this Debt.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Debt.
        Amount

        :param amount: The amount of this Debt.
        :type: str
        """

        self._amount = amount

    @property
    def max_amount(self):
        """
        Gets the max_amount of this Debt.
        Max amount

        :return: The max_amount of this Debt.
        :rtype: str
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """
        Sets the max_amount of this Debt.
        Max amount

        :param max_amount: The max_amount of this Debt.
        :type: str
        """

        self._max_amount = max_amount

    @property
    def industry(self):
        """
        Gets the industry of this Debt.
        Industry

        :return: The industry of this Debt.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """
        Sets the industry of this Debt.
        Industry

        :param industry: The industry of this Debt.
        :type: str
        """

        self._industry = industry

    @property
    def reporter(self):
        """
        Gets the reporter of this Debt.
        Reporter

        :return: The reporter of this Debt.
        :rtype: str
        """
        return self._reporter

    @reporter.setter
    def reporter(self, reporter):
        """
        Sets the reporter of this Debt.
        Reporter

        :param reporter: The reporter of this Debt.
        :type: str
        """

        self._reporter = reporter

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
