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


class SecondMarketSell(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, loan_part_id=None, desired_discount_rate=None):
        """
        SecondMarketSell - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'loan_part_id': 'str',
            'desired_discount_rate': 'int'
        }

        self.attribute_map = {
            'loan_part_id': 'LoanPartId',
            'desired_discount_rate': 'DesiredDiscountRate'
        }

        self._loan_part_id = loan_part_id
        self._desired_discount_rate = desired_discount_rate

    @property
    def loan_part_id(self):
        """
        Gets the loan_part_id of this SecondMarketSell.
        LoanPart unique identifier

        :return: The loan_part_id of this SecondMarketSell.
        :rtype: str
        """
        return self._loan_part_id

    @loan_part_id.setter
    def loan_part_id(self, loan_part_id):
        """
        Sets the loan_part_id of this SecondMarketSell.
        LoanPart unique identifier

        :param loan_part_id: The loan_part_id of this SecondMarketSell.
        :type: str
        """

        self._loan_part_id = loan_part_id

    @property
    def desired_discount_rate(self):
        """
        Gets the desired_discount_rate of this SecondMarketSell.
        Desired discount rate

        :return: The desired_discount_rate of this SecondMarketSell.
        :rtype: int
        """
        return self._desired_discount_rate

    @desired_discount_rate.setter
    def desired_discount_rate(self, desired_discount_rate):
        """
        Sets the desired_discount_rate of this SecondMarketSell.
        Desired discount rate

        :param desired_discount_rate: The desired_discount_rate of this SecondMarketSell.
        :type: int
        """

        if not desired_discount_rate:
            raise ValueError("Invalid value for `desired_discount_rate`, must not be `None`")
        if desired_discount_rate > 40.0:
            raise ValueError("Invalid value for `desired_discount_rate`, must be a value less than or equal to `40.0`")
        if desired_discount_rate < -100.0:
            raise ValueError("Invalid value for `desired_discount_rate`, must be a value greater than or equal to `-100.0`")

        self._desired_discount_rate = desired_discount_rate

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
