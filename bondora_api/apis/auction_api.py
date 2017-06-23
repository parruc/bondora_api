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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AuctionApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def auction_get(self, id, **kwargs):
        """
        Gets Auction info by auction identifier
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auction_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Auction's identifier (required)
        :return: ApiResultExtendedAuction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.auction_get_with_http_info(id, **kwargs)
        else:
            (data) = self.auction_get_with_http_info(id, **kwargs)
            return data

    def auction_get_with_http_info(self, id, **kwargs):
        """
        Gets Auction info by auction identifier
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auction_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Auction's identifier (required)
        :return: ApiResultExtendedAuction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auction_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `auction_get`")

        resource_path = '/api/v1/auction/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'application/xml', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiResultExtendedAuction',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def auction_get_active(self, **kwargs):
        """
        Gets list of active Auctions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auction_get_active(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] request_countries: Two letter iso code for country of origin: EE, ES, FI
        :param list[str] request_ratings: Bondora's rating: AA, A, B, C, D, E, F, HR
        :param int request_gender: Borrower's gender: Male 0, Female 1, Unknown 2
        :param int request_sum_min: Minimal loan amount
        :param int request_sum_max: Maximum loan amount
        :param list[int] request_terms: Loan length: 3, 9, 12, 18, 24, 36, 48, 60 months
        :param int request_age_min: Minimal age
        :param int request_age_max: Maximum age
        :param int request_loan_number: Loan number
        :param str request_user_name: Username
        :param datetime request_application_date_from: Loan application started date from
        :param datetime request_application_date_to: Loan application started date to
        :param int request_credit_score_min: Minimum credit score
        :param int request_credit_score_max: Maximum credit score
        :param list[str] request_credit_scores_ee_mini: Credit score for EE loans
        :param float request_interest_min: Minimum interest
        :param float request_interest_max: Maximum interest
        :param float request_income_total_min: Minimal total income
        :param float request_income_total_max: Maximum total income
        :param int request_model_version: Model version
        :param float request_expected_loss_min: Minimal expected loss
        :param float request_expected_loss_max: Maximum expected loss
        :param datetime request_listed_on_utc_from: Date when auction was published from
        :param datetime request_listed_on_utc_to: Date when auction was published to
        :param int request_page_size: Max items in result, default is 1000
        :param int request_page_nr: Result page nr
        :return: ApiResultAuctions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.auction_get_active_with_http_info(**kwargs)
        else:
            (data) = self.auction_get_active_with_http_info(**kwargs)
            return data

    def auction_get_active_with_http_info(self, **kwargs):
        """
        Gets list of active Auctions
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auction_get_active_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] request_countries: Two letter iso code for country of origin: EE, ES, FI
        :param list[str] request_ratings: Bondora's rating: AA, A, B, C, D, E, F, HR
        :param int request_gender: Borrower's gender: Male 0, Female 1, Unknown 2
        :param int request_sum_min: Minimal loan amount
        :param int request_sum_max: Maximum loan amount
        :param list[int] request_terms: Loan length: 3, 9, 12, 18, 24, 36, 48, 60 months
        :param int request_age_min: Minimal age
        :param int request_age_max: Maximum age
        :param int request_loan_number: Loan number
        :param str request_user_name: Username
        :param datetime request_application_date_from: Loan application started date from
        :param datetime request_application_date_to: Loan application started date to
        :param int request_credit_score_min: Minimum credit score
        :param int request_credit_score_max: Maximum credit score
        :param list[str] request_credit_scores_ee_mini: Credit score for EE loans
        :param float request_interest_min: Minimum interest
        :param float request_interest_max: Maximum interest
        :param float request_income_total_min: Minimal total income
        :param float request_income_total_max: Maximum total income
        :param int request_model_version: Model version
        :param float request_expected_loss_min: Minimal expected loss
        :param float request_expected_loss_max: Maximum expected loss
        :param datetime request_listed_on_utc_from: Date when auction was published from
        :param datetime request_listed_on_utc_to: Date when auction was published to
        :param int request_page_size: Max items in result, default is 1000
        :param int request_page_nr: Result page nr
        :return: ApiResultAuctions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_countries', 'request_ratings', 'request_gender', 'request_sum_min', 'request_sum_max', 'request_terms', 'request_age_min', 'request_age_max', 'request_loan_number', 'request_user_name', 'request_application_date_from', 'request_application_date_to', 'request_credit_score_min', 'request_credit_score_max', 'request_credit_scores_ee_mini', 'request_interest_min', 'request_interest_max', 'request_income_total_min', 'request_income_total_max', 'request_model_version', 'request_expected_loss_min', 'request_expected_loss_max', 'request_listed_on_utc_from', 'request_listed_on_utc_to', 'request_page_size', 'request_page_nr']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auction_get_active" % key
                )
            params[key] = val
        del params['kwargs']

        if 'request_page_size' in params and params['request_page_size'] > 1000.0:
            raise ValueError("Invalid value for parameter `request_page_size` when calling `auction_get_active`, must be a value less than or equal to  `1000.0`")
        if 'request_page_size' in params and params['request_page_size'] < 1.0:
            raise ValueError("Invalid value for parameter `request_page_size` when calling `auction_get_active`, must be a value greater than or equal to `1.0`")
        if 'request_page_nr' in params and params['request_page_nr'] > 2.147483647E9:
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `auction_get_active`, must be a value less than or equal to  `2.147483647E9`")
        if 'request_page_nr' in params and params['request_page_nr'] < 1.0:
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `auction_get_active`, must be a value greater than or equal to `1.0`")
        resource_path = '/api/v1/auctions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'request_countries' in params:
            query_params['request.countries'] = params['request_countries']
        if 'request_ratings' in params:
            query_params['request.ratings'] = params['request_ratings']
        if 'request_gender' in params:
            query_params['request.gender'] = params['request_gender']
        if 'request_sum_min' in params:
            query_params['request.sumMin'] = params['request_sum_min']
        if 'request_sum_max' in params:
            query_params['request.sumMax'] = params['request_sum_max']
        if 'request_terms' in params:
            query_params['request.terms'] = params['request_terms']
        if 'request_age_min' in params:
            query_params['request.ageMin'] = params['request_age_min']
        if 'request_age_max' in params:
            query_params['request.ageMax'] = params['request_age_max']
        if 'request_loan_number' in params:
            query_params['request.loanNumber'] = params['request_loan_number']
        if 'request_user_name' in params:
            query_params['request.userName'] = params['request_user_name']
        if 'request_application_date_from' in params:
            query_params['request.applicationDateFrom'] = params['request_application_date_from']
        if 'request_application_date_to' in params:
            query_params['request.applicationDateTo'] = params['request_application_date_to']
        if 'request_credit_score_min' in params:
            query_params['request.creditScoreMin'] = params['request_credit_score_min']
        if 'request_credit_score_max' in params:
            query_params['request.creditScoreMax'] = params['request_credit_score_max']
        if 'request_credit_scores_ee_mini' in params:
            query_params['request.creditScoresEeMini'] = params['request_credit_scores_ee_mini']
        if 'request_interest_min' in params:
            query_params['request.interestMin'] = params['request_interest_min']
        if 'request_interest_max' in params:
            query_params['request.interestMax'] = params['request_interest_max']
        if 'request_income_total_min' in params:
            query_params['request.incomeTotalMin'] = params['request_income_total_min']
        if 'request_income_total_max' in params:
            query_params['request.incomeTotalMax'] = params['request_income_total_max']
        if 'request_model_version' in params:
            query_params['request.modelVersion'] = params['request_model_version']
        if 'request_expected_loss_min' in params:
            query_params['request.expectedLossMin'] = params['request_expected_loss_min']
        if 'request_expected_loss_max' in params:
            query_params['request.expectedLossMax'] = params['request_expected_loss_max']
        if 'request_listed_on_utc_from' in params:
            query_params['request.listedOnUTCFrom'] = params['request_listed_on_utc_from']
        if 'request_listed_on_utc_to' in params:
            query_params['request.listedOnUTCTo'] = params['request_listed_on_utc_to']
        if 'request_page_size' in params:
            query_params['request.pageSize'] = params['request_page_size']
        if 'request_page_nr' in params:
            query_params['request.pageNr'] = params['request_page_nr']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json', 'application/xml', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiResultAuctions',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))