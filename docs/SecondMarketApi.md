# bondora_api.SecondMarketApi

All URIs are relative to *http://api.bondora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**second_market_buy**](SecondMarketApi.md#second_market_buy) | **POST** /api/v1/secondarymarket/buy | Buy loans from secondary market.
[**second_market_cancel**](SecondMarketApi.md#second_market_cancel) | **POST** /api/v1/secondarymarket/{id}/cancel | Remove your loans from secondary market.
[**second_market_cancel_multiple**](SecondMarketApi.md#second_market_cancel_multiple) | **POST** /api/v1/secondarymarket/cancel | Remove your loans from secondary market.
[**second_market_get**](SecondMarketApi.md#second_market_get) | **GET** /api/v1/loanpart/{id} | Gets LoanPartDetails info by identifier
[**second_market_get_active**](SecondMarketApi.md#second_market_get_active) | **GET** /api/v1/secondarymarket | Gets list of active secondary market items
[**second_market_get_item**](SecondMarketApi.md#second_market_get_item) | **GET** /api/v1/secondarymarket/{id} | Get the secondary market item summary
[**second_market_sell**](SecondMarketApi.md#second_market_sell) | **POST** /api/v1/secondarymarket/sell | Sell your loans to secondary market.


# **second_market_buy**
> ApiResult second_market_buy(buy_request)

Buy loans from secondary market.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
buy_request = bondora_api.SecondMarketBuyRequest() # SecondMarketBuyRequest | 

try: 
    # Buy loans from secondary market.
    api_response = api_instance.second_market_buy(buy_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_buy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_request** | [**SecondMarketBuyRequest**](SecondMarketBuyRequest.md)|  | 

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_cancel**
> ApiResult second_market_cancel(id)

Remove your loans from secondary market.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
id = 'id_example' # str | 

try: 
    # Remove your loans from secondary market.
    api_response = api_instance.second_market_cancel(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_cancel: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_cancel_multiple**
> ApiResult second_market_cancel_multiple(cancel_request)

Remove your loans from secondary market.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
cancel_request = bondora_api.SecondMarketCancelRequest() # SecondMarketCancelRequest | 

try: 
    # Remove your loans from secondary market.
    api_response = api_instance.second_market_cancel_multiple(cancel_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_cancel_multiple: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_request** | [**SecondMarketCancelRequest**](SecondMarketCancelRequest.md)|  | 

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_get**
> ApiResultLoanPartDetails second_market_get(id)

Gets LoanPartDetails info by identifier

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
id = 'id_example' # str | LoanPartDetails's identifier

try: 
    # Gets LoanPartDetails info by identifier
    api_response = api_instance.second_market_get(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| LoanPartDetails&#39;s identifier | 

### Return type

[**ApiResultLoanPartDetails**](ApiResultLoanPartDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_get_active**
> ApiResultSecondMarket second_market_get_active(request_loan_issued_date_from=request_loan_issued_date_from, request_loan_issued_date_to=request_loan_issued_date_to, request_principal_min=request_principal_min, request_principal_max=request_principal_max, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_length_max=request_length_max, request_length_min=request_length_min, request_has_debt=request_has_debt, request_loan_status_code=request_loan_status_code, request_loan_debt_management_stage_type=request_loan_debt_management_stage_type, request_loan_debt_management_date_active_from=request_loan_debt_management_date_active_from, request_loan_debt_management_date_active_to=request_loan_debt_management_date_active_to, request_late_principal_amount_min=request_late_principal_amount_min, request_late_principal_amount_max=request_late_principal_amount_max, request_price_min=request_price_min, request_price_max=request_price_max, request_use_of_loan=request_use_of_loan, request_has_new_schedule=request_has_new_schedule, request_countries=request_countries, request_ratings=request_ratings, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_user_name=request_user_name, request_gender=request_gender, request_age_min=request_age_min, request_age_max=request_age_max, request_income_verification_status=request_income_verification_status, request_show_my_items=request_show_my_items, request_auction_id=request_auction_id, request_listed_on_date_from=request_listed_on_date_from, request_listed_on_date_to=request_listed_on_date_to, request_debt_occured_on_from=request_debt_occured_on_from, request_debt_occured_on_to=request_debt_occured_on_to, request_debt_occured_on_for_secondary_from=request_debt_occured_on_for_secondary_from, request_debt_occured_on_for_secondary_to=request_debt_occured_on_for_secondary_to, request_defaulted_date_from=request_defaulted_date_from, request_defaulted_date_to=request_defaulted_date_to, request_rescheduled_from=request_rescheduled_from, request_rescheduled_to=request_rescheduled_to, request_last_payment_date_from=request_last_payment_date_from, request_last_payment_date_to=request_last_payment_date_to, request_next_payment_date_from=request_next_payment_date_from, request_next_payment_date_to=request_next_payment_date_to, request_desired_discount_rate_min=request_desired_discount_rate_min, request_desired_discount_rate_max=request_desired_discount_rate_max, request_xirr_min=request_xirr_min, request_xirr_max=request_xirr_max, request_page_size=request_page_size, request_page_nr=request_page_nr)

Gets list of active secondary market items

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
request_loan_issued_date_from = '2013-10-20T19:20:30+01:00' # datetime | Loan issued start date from (optional)
request_loan_issued_date_to = '2013-10-20T19:20:30+01:00' # datetime | Loan issued start date to (optional)
request_principal_min = 1.2 # float | Remaining principal amount min (optional)
request_principal_max = 1.2 # float | Remaining principal amount max (optional)
request_interest_min = 1.2 # float | Interest rate min (optional)
request_interest_max = 1.2 # float | Interest rate max (optional)
request_length_max = 56 # int | Loan lenght min (optional)
request_length_min = 56 # int | Loan lenght max (optional)
request_has_debt = true # bool | Is overdue (optional)
request_loan_status_code = [56] # list[int] | Loan status code              <para>2 Current</para><para>100 Overdue</para><para>5 60+ days overdue</para> (optional)
request_loan_debt_management_stage_type = 56 # int | Latest debt management stage type (optional)
request_loan_debt_management_date_active_from = '2013-10-20T19:20:30+01:00' # datetime | Latest debt management date active from (optional)
request_loan_debt_management_date_active_to = '2013-10-20T19:20:30+01:00' # datetime | Latest debt management date active to (optional)
request_late_principal_amount_min = 1.2 # float | Principal debt amount min (optional)
request_late_principal_amount_max = 1.2 # float | Principal debt amount max (optional)
request_price_min = 1.2 # float | Price amount min (optional)
request_price_max = 1.2 # float | Price amount max (optional)
request_use_of_loan = 56 # int | Use of loan (optional)
request_has_new_schedule = true # bool | Has been rescheduled (optional)
request_countries = ['request_countries_example'] # list[str] | Two letter iso code for country of origin: EE, ES, FI (optional)
request_ratings = ['request_ratings_example'] # list[str] | Bondora's rating: AA, A, B, C, D, E, F, HR (optional)
request_credit_score_min = 56 # int | Minimum credit score (optional)
request_credit_score_max = 56 # int | Maximum credit score (optional)
request_user_name = 'request_user_name_example' # str | Borrower's username (optional)
request_gender = 56 # int | Borrower's gender: Male 0, Female 1, Unknown 2 (optional)
request_age_min = 56 # int | Minimal age (optional)
request_age_max = 56 # int | Maximum age (optional)
request_income_verification_status = 56 # int | Income verification type (optional)
request_show_my_items = true # bool | Can find your own items from market: Value Null = ALL, True = only your items, False = other user items (optional)
request_auction_id = 'request_auction_id_example' # str | Can find specific auction from market (optional)
request_listed_on_date_from = '2013-10-20T19:20:30+01:00' # datetime | Date when item was published from (optional)
request_listed_on_date_to = '2013-10-20T19:20:30+01:00' # datetime | Date when item was published to (optional)
request_debt_occured_on_from = '2013-10-20T19:20:30+01:00' # datetime | Principal debt started date from (optional)
request_debt_occured_on_to = '2013-10-20T19:20:30+01:00' # datetime | Principal debt started date to (optional)
request_debt_occured_on_for_secondary_from = '2013-10-20T19:20:30+01:00' # datetime | Interest debt started date from (optional)
request_debt_occured_on_for_secondary_to = '2013-10-20T19:20:30+01:00' # datetime | Interest debt started date to (optional)
request_defaulted_date_from = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date from (optional)
request_defaulted_date_to = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date to (optional)
request_rescheduled_from = '2013-10-20T19:20:30+01:00' # datetime | Rescheduled date from (optional)
request_rescheduled_to = '2013-10-20T19:20:30+01:00' # datetime | Rescheduled date to (optional)
request_last_payment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Last payment date from (optional)
request_last_payment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Last payment date to (optional)
request_next_payment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Next payment date from (optional)
request_next_payment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Next payment date to (optional)
request_desired_discount_rate_min = 1.2 # float | Minimal DesiredDiscountRate (optional)
request_desired_discount_rate_max = 1.2 # float | Maximal DesiredDiscountRate (optional)
request_xirr_min = 1.2 # float | Minimal Xirr (optional)
request_xirr_max = 1.2 # float | Maximal Xirr (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Gets list of active secondary market items
    api_response = api_instance.second_market_get_active(request_loan_issued_date_from=request_loan_issued_date_from, request_loan_issued_date_to=request_loan_issued_date_to, request_principal_min=request_principal_min, request_principal_max=request_principal_max, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_length_max=request_length_max, request_length_min=request_length_min, request_has_debt=request_has_debt, request_loan_status_code=request_loan_status_code, request_loan_debt_management_stage_type=request_loan_debt_management_stage_type, request_loan_debt_management_date_active_from=request_loan_debt_management_date_active_from, request_loan_debt_management_date_active_to=request_loan_debt_management_date_active_to, request_late_principal_amount_min=request_late_principal_amount_min, request_late_principal_amount_max=request_late_principal_amount_max, request_price_min=request_price_min, request_price_max=request_price_max, request_use_of_loan=request_use_of_loan, request_has_new_schedule=request_has_new_schedule, request_countries=request_countries, request_ratings=request_ratings, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_user_name=request_user_name, request_gender=request_gender, request_age_min=request_age_min, request_age_max=request_age_max, request_income_verification_status=request_income_verification_status, request_show_my_items=request_show_my_items, request_auction_id=request_auction_id, request_listed_on_date_from=request_listed_on_date_from, request_listed_on_date_to=request_listed_on_date_to, request_debt_occured_on_from=request_debt_occured_on_from, request_debt_occured_on_to=request_debt_occured_on_to, request_debt_occured_on_for_secondary_from=request_debt_occured_on_for_secondary_from, request_debt_occured_on_for_secondary_to=request_debt_occured_on_for_secondary_to, request_defaulted_date_from=request_defaulted_date_from, request_defaulted_date_to=request_defaulted_date_to, request_rescheduled_from=request_rescheduled_from, request_rescheduled_to=request_rescheduled_to, request_last_payment_date_from=request_last_payment_date_from, request_last_payment_date_to=request_last_payment_date_to, request_next_payment_date_from=request_next_payment_date_from, request_next_payment_date_to=request_next_payment_date_to, request_desired_discount_rate_min=request_desired_discount_rate_min, request_desired_discount_rate_max=request_desired_discount_rate_max, request_xirr_min=request_xirr_min, request_xirr_max=request_xirr_max, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_get_active: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_loan_issued_date_from** | **datetime**| Loan issued start date from | [optional] 
 **request_loan_issued_date_to** | **datetime**| Loan issued start date to | [optional] 
 **request_principal_min** | **float**| Remaining principal amount min | [optional] 
 **request_principal_max** | **float**| Remaining principal amount max | [optional] 
 **request_interest_min** | **float**| Interest rate min | [optional] 
 **request_interest_max** | **float**| Interest rate max | [optional] 
 **request_length_max** | **int**| Loan lenght min | [optional] 
 **request_length_min** | **int**| Loan lenght max | [optional] 
 **request_has_debt** | **bool**| Is overdue | [optional] 
 **request_loan_status_code** | [**list[int]**](int.md)| Loan status code              &lt;para&gt;2 Current&lt;/para&gt;&lt;para&gt;100 Overdue&lt;/para&gt;&lt;para&gt;5 60+ days overdue&lt;/para&gt; | [optional] 
 **request_loan_debt_management_stage_type** | **int**| Latest debt management stage type | [optional] 
 **request_loan_debt_management_date_active_from** | **datetime**| Latest debt management date active from | [optional] 
 **request_loan_debt_management_date_active_to** | **datetime**| Latest debt management date active to | [optional] 
 **request_late_principal_amount_min** | **float**| Principal debt amount min | [optional] 
 **request_late_principal_amount_max** | **float**| Principal debt amount max | [optional] 
 **request_price_min** | **float**| Price amount min | [optional] 
 **request_price_max** | **float**| Price amount max | [optional] 
 **request_use_of_loan** | **int**| Use of loan | [optional] 
 **request_has_new_schedule** | **bool**| Has been rescheduled | [optional] 
 **request_countries** | [**list[str]**](str.md)| Two letter iso code for country of origin: EE, ES, FI | [optional] 
 **request_ratings** | [**list[str]**](str.md)| Bondora&#39;s rating: AA, A, B, C, D, E, F, HR | [optional] 
 **request_credit_score_min** | **int**| Minimum credit score | [optional] 
 **request_credit_score_max** | **int**| Maximum credit score | [optional] 
 **request_user_name** | **str**| Borrower&#39;s username | [optional] 
 **request_gender** | **int**| Borrower&#39;s gender: Male 0, Female 1, Unknown 2 | [optional] 
 **request_age_min** | **int**| Minimal age | [optional] 
 **request_age_max** | **int**| Maximum age | [optional] 
 **request_income_verification_status** | **int**| Income verification type | [optional] 
 **request_show_my_items** | **bool**| Can find your own items from market: Value Null &#x3D; ALL, True &#x3D; only your items, False &#x3D; other user items | [optional] 
 **request_auction_id** | **str**| Can find specific auction from market | [optional] 
 **request_listed_on_date_from** | **datetime**| Date when item was published from | [optional] 
 **request_listed_on_date_to** | **datetime**| Date when item was published to | [optional] 
 **request_debt_occured_on_from** | **datetime**| Principal debt started date from | [optional] 
 **request_debt_occured_on_to** | **datetime**| Principal debt started date to | [optional] 
 **request_debt_occured_on_for_secondary_from** | **datetime**| Interest debt started date from | [optional] 
 **request_debt_occured_on_for_secondary_to** | **datetime**| Interest debt started date to | [optional] 
 **request_defaulted_date_from** | **datetime**| Defaulted date from | [optional] 
 **request_defaulted_date_to** | **datetime**| Defaulted date to | [optional] 
 **request_rescheduled_from** | **datetime**| Rescheduled date from | [optional] 
 **request_rescheduled_to** | **datetime**| Rescheduled date to | [optional] 
 **request_last_payment_date_from** | **datetime**| Last payment date from | [optional] 
 **request_last_payment_date_to** | **datetime**| Last payment date to | [optional] 
 **request_next_payment_date_from** | **datetime**| Next payment date from | [optional] 
 **request_next_payment_date_to** | **datetime**| Next payment date to | [optional] 
 **request_desired_discount_rate_min** | **float**| Minimal DesiredDiscountRate | [optional] 
 **request_desired_discount_rate_max** | **float**| Maximal DesiredDiscountRate | [optional] 
 **request_xirr_min** | **float**| Minimal Xirr | [optional] 
 **request_xirr_max** | **float**| Maximal Xirr | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultSecondMarket**](ApiResultSecondMarket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_get_item**
> ApiResultSecondMarketItemSummary second_market_get_item(id)

Get the secondary market item summary

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
id = 'id_example' # str | SecondaryMarket item identificator

try: 
    # Get the secondary market item summary
    api_response = api_instance.second_market_get_item(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_get_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SecondaryMarket item identificator | 

### Return type

[**ApiResultSecondMarketItemSummary**](ApiResultSecondMarketItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **second_market_sell**
> ApiResultSecondMarketSale second_market_sell(sale_request)

Sell your loans to secondary market.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.SecondMarketApi()
sale_request = bondora_api.SecondMarketSaleRequest() # SecondMarketSaleRequest | 

try: 
    # Sell your loans to secondary market.
    api_response = api_instance.second_market_sell(sale_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SecondMarketApi->second_market_sell: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_request** | [**SecondMarketSaleRequest**](SecondMarketSaleRequest.md)|  | 

### Return type

[**ApiResultSecondMarketSale**](ApiResultSecondMarketSale.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

