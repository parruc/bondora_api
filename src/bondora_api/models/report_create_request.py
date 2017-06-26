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


class ReportCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, report_type=None, period_start=None, period_end=None):
        """
        ReportCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'report_type': 'int',
            'period_start': 'datetime',
            'period_end': 'datetime'
        }

        self.attribute_map = {
            'report_type': 'ReportType',
            'period_start': 'PeriodStart',
            'period_end': 'PeriodEnd'
        }

        self._report_type = report_type
        self._period_start = period_start
        self._period_end = period_end

    @property
    def report_type(self):
        """
        Gets the report_type of this ReportCreateRequest.


        :return: The report_type of this ReportCreateRequest.
        :rtype: int
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """
        Sets the report_type of this ReportCreateRequest.


        :param report_type: The report_type of this ReportCreateRequest.
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if report_type not in allowed_values:
            raise ValueError(
                "Invalid value for `report_type` ({0}), must be one of {1}"
                .format(report_type, allowed_values)
            )

        self._report_type = report_type

    @property
    def period_start(self):
        """
        Gets the period_start of this ReportCreateRequest.


        :return: The period_start of this ReportCreateRequest.
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """
        Sets the period_start of this ReportCreateRequest.


        :param period_start: The period_start of this ReportCreateRequest.
        :type: datetime
        """

        self._period_start = period_start

    @property
    def period_end(self):
        """
        Gets the period_end of this ReportCreateRequest.


        :return: The period_end of this ReportCreateRequest.
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """
        Sets the period_end of this ReportCreateRequest.


        :param period_end: The period_end of this ReportCreateRequest.
        :type: datetime
        """

        self._period_end = period_end

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