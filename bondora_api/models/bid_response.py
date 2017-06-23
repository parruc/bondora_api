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


class BidResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, auction_id=None, amount=None, min_amount=None):
        """
        BidResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'auction_id': 'str',
            'amount': 'float',
            'min_amount': 'float'
        }

        self.attribute_map = {
            'id': 'Id',
            'auction_id': 'AuctionId',
            'amount': 'Amount',
            'min_amount': 'MinAmount'
        }

        self._id = id
        self._auction_id = auction_id
        self._amount = amount
        self._min_amount = min_amount

    @property
    def id(self):
        """
        Gets the id of this BidResponse.
        Item unique identifier

        :return: The id of this BidResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BidResponse.
        Item unique identifier

        :param id: The id of this BidResponse.
        :type: str
        """

        self._id = id

    @property
    def auction_id(self):
        """
        Gets the auction_id of this BidResponse.
        Auction unique identifier

        :return: The auction_id of this BidResponse.
        :rtype: str
        """
        return self._auction_id

    @auction_id.setter
    def auction_id(self, auction_id):
        """
        Sets the auction_id of this BidResponse.
        Auction unique identifier

        :param auction_id: The auction_id of this BidResponse.
        :type: str
        """

        self._auction_id = auction_id

    @property
    def amount(self):
        """
        Gets the amount of this BidResponse.
        Amount to bid into Auction

        :return: The amount of this BidResponse.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this BidResponse.
        Amount to bid into Auction

        :param amount: The amount of this BidResponse.
        :type: float
        """

        self._amount = amount

    @property
    def min_amount(self):
        """
        Gets the min_amount of this BidResponse.
        Not used. Will always be NULL.

        :return: The min_amount of this BidResponse.
        :rtype: float
        """
        return self._min_amount

    @min_amount.setter
    def min_amount(self, min_amount):
        """
        Sets the min_amount of this BidResponse.
        Not used. Will always be NULL.

        :param min_amount: The min_amount of this BidResponse.
        :type: float
        """

        self._min_amount = min_amount

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