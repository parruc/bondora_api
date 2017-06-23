# bondora_api.AccountApi

All URIs are relative to *http://api.bondora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_active**](AccountApi.md#account_get_active) | **GET** /api/v1/account/investments | Gets list of your investments
[**account_get_balance**](AccountApi.md#account_get_balance) | **GET** /api/v1/account/balance | Gets your account balance information
[**account_get_event_log**](AccountApi.md#account_get_event_log) | **GET** /api/v1/eventlog | Gets events that have been made with this application (related to current access token)


# **account_get_active**
> ApiResultMyInvestments account_get_active(request_loan_issued_date_from=request_loan_issued_date_from, request_loan_issued_date_to=request_loan_issued_date_to, request_principal_min=request_principal_min, request_principal_max=request_principal_max, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_length_max=request_length_max, request_length_min=request_length_min, request_late_principal_amount_min=request_late_principal_amount_min, request_late_principal_amount_max=request_late_principal_amount_max, request_debt_occured_on_from=request_debt_occured_on_from, request_debt_occured_on_to=request_debt_occured_on_to, request_debt_occured_on_for_secondary_from=request_debt_occured_on_for_secondary_from, request_debt_occured_on_for_secondary_to=request_debt_occured_on_for_secondary_to, request_defaulted_date_from=request_defaulted_date_from, request_defaulted_date_to=request_defaulted_date_to, request_rescheduled_from=request_rescheduled_from, request_rescheduled_to=request_rescheduled_to, request_sold_date_from=request_sold_date_from, request_sold_date_to=request_sold_date_to, request_purchase_date_from=request_purchase_date_from, request_purchase_date_to=request_purchase_date_to, request_next_payment_date_to=request_next_payment_date_to, request_next_payment_date_from=request_next_payment_date_from, request_last_payment_date_from=request_last_payment_date_from, request_last_payment_date_to=request_last_payment_date_to, request_countries=request_countries, request_ratings=request_ratings, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_user_name=request_user_name, request_loan_status_code=request_loan_status_code, request_income_verification_status=request_income_verification_status, request_loan_debt_management_stage=request_loan_debt_management_stage, request_loan_debt_management_stage_type=request_loan_debt_management_stage_type, request_loan_debt_management_date_active_from=request_loan_debt_management_date_active_from, request_loan_debt_management_date_active_to=request_loan_debt_management_date_active_to, request_auction_bid_type=request_auction_bid_type, request_sales_status=request_sales_status, request_is_in_repayment=request_is_in_repayment, request_page_size=request_page_size, request_page_nr=request_page_nr)

Gets list of your investments

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.AccountApi()
request_loan_issued_date_from = '2013-10-20T19:20:30+01:00' # datetime | Loan issued start date from (optional)
request_loan_issued_date_to = '2013-10-20T19:20:30+01:00' # datetime | Loan issued start date to (optional)
request_principal_min = 1.2 # float | Remaining principal amount min (optional)
request_principal_max = 1.2 # float | Remaining principal amount max (optional)
request_interest_min = 1.2 # float | Interest rate min (optional)
request_interest_max = 1.2 # float | Interest rate max (optional)
request_length_max = 56 # int | Loan lenght min (optional)
request_length_min = 56 # int | Loan lenght max (optional)
request_late_principal_amount_min = 1.2 # float | Principal debt amount min (optional)
request_late_principal_amount_max = 1.2 # float | Principal debt amount max (optional)
request_debt_occured_on_from = '2013-10-20T19:20:30+01:00' # datetime | Principal debt started date from (optional)
request_debt_occured_on_to = '2013-10-20T19:20:30+01:00' # datetime | Principal debt started date to (optional)
request_debt_occured_on_for_secondary_from = '2013-10-20T19:20:30+01:00' # datetime | Interest debt started date from (optional)
request_debt_occured_on_for_secondary_to = '2013-10-20T19:20:30+01:00' # datetime | Interest debt started date to (optional)
request_defaulted_date_from = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date from (optional)
request_defaulted_date_to = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date to (optional)
request_rescheduled_from = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date from (optional)
request_rescheduled_to = '2013-10-20T19:20:30+01:00' # datetime | Defaulted date to (optional)
request_sold_date_from = '2013-10-20T19:20:30+01:00' # datetime | When it was sold on Secondary market from (optional)
request_sold_date_to = '2013-10-20T19:20:30+01:00' # datetime | When it was sold on Secondary market to (optional)
request_purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | When you received the investment Auctions/Secondary market from (optional)
request_purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | When you received the investment Auctions/Secondary market to (optional)
request_next_payment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Next payment date to (optional)
request_next_payment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Next payment date from (optional)
request_last_payment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Last payment date from (optional)
request_last_payment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Last payment date to (optional)
request_countries = ['request_countries_example'] # list[str] | Two letter iso code for country of origin: EE, ES, FI (optional)
request_ratings = ['request_ratings_example'] # list[str] | Bondora's rating: AA, A, B, C, D, E, F, HR (optional)
request_credit_score_min = 56 # int | Minimum credit score (optional)
request_credit_score_max = 56 # int | Maximum credit score (optional)
request_user_name = 'request_user_name_example' # str | Borrower's username (optional)
request_loan_status_code = [56] # list[int] | Loan status code              <para>2 Current</para><para>3 Cancelled</para><para>100 Overdue</para><para>5 60+ days overdue</para><para>4 Repaid</para><para>8 Released</para> (optional)
request_income_verification_status = 56 # int | Income verification type (optional)
request_loan_debt_management_stage = 56 # int | Latest debt management stage (optional)
request_loan_debt_management_stage_type = 56 # int | Latest debt management stage type (optional)
request_loan_debt_management_date_active_from = '2013-10-20T19:20:30+01:00' # datetime | Latest debt management date active from (optional)
request_loan_debt_management_date_active_to = '2013-10-20T19:20:30+01:00' # datetime | Latest debt management date active to (optional)
request_auction_bid_type = 56 # int | Auction bid type (optional)
request_sales_status = 56 # int | Second market sale status              <para>NULL All active</para><para>0 Bought investments</para><para>1 Sold investments</para><para>2 Investment is on sale</para><para>3 Investment is not on sale</para> (optional)
request_is_in_repayment = true # bool | Search only active in repayment loans, StatusCodes (2, 5, 100) (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Gets list of your investments
    api_response = api_instance.account_get_active(request_loan_issued_date_from=request_loan_issued_date_from, request_loan_issued_date_to=request_loan_issued_date_to, request_principal_min=request_principal_min, request_principal_max=request_principal_max, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_length_max=request_length_max, request_length_min=request_length_min, request_late_principal_amount_min=request_late_principal_amount_min, request_late_principal_amount_max=request_late_principal_amount_max, request_debt_occured_on_from=request_debt_occured_on_from, request_debt_occured_on_to=request_debt_occured_on_to, request_debt_occured_on_for_secondary_from=request_debt_occured_on_for_secondary_from, request_debt_occured_on_for_secondary_to=request_debt_occured_on_for_secondary_to, request_defaulted_date_from=request_defaulted_date_from, request_defaulted_date_to=request_defaulted_date_to, request_rescheduled_from=request_rescheduled_from, request_rescheduled_to=request_rescheduled_to, request_sold_date_from=request_sold_date_from, request_sold_date_to=request_sold_date_to, request_purchase_date_from=request_purchase_date_from, request_purchase_date_to=request_purchase_date_to, request_next_payment_date_to=request_next_payment_date_to, request_next_payment_date_from=request_next_payment_date_from, request_last_payment_date_from=request_last_payment_date_from, request_last_payment_date_to=request_last_payment_date_to, request_countries=request_countries, request_ratings=request_ratings, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_user_name=request_user_name, request_loan_status_code=request_loan_status_code, request_income_verification_status=request_income_verification_status, request_loan_debt_management_stage=request_loan_debt_management_stage, request_loan_debt_management_stage_type=request_loan_debt_management_stage_type, request_loan_debt_management_date_active_from=request_loan_debt_management_date_active_from, request_loan_debt_management_date_active_to=request_loan_debt_management_date_active_to, request_auction_bid_type=request_auction_bid_type, request_sales_status=request_sales_status, request_is_in_repayment=request_is_in_repayment, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountApi->account_get_active: %s\n" % e
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
 **request_late_principal_amount_min** | **float**| Principal debt amount min | [optional] 
 **request_late_principal_amount_max** | **float**| Principal debt amount max | [optional] 
 **request_debt_occured_on_from** | **datetime**| Principal debt started date from | [optional] 
 **request_debt_occured_on_to** | **datetime**| Principal debt started date to | [optional] 
 **request_debt_occured_on_for_secondary_from** | **datetime**| Interest debt started date from | [optional] 
 **request_debt_occured_on_for_secondary_to** | **datetime**| Interest debt started date to | [optional] 
 **request_defaulted_date_from** | **datetime**| Defaulted date from | [optional] 
 **request_defaulted_date_to** | **datetime**| Defaulted date to | [optional] 
 **request_rescheduled_from** | **datetime**| Defaulted date from | [optional] 
 **request_rescheduled_to** | **datetime**| Defaulted date to | [optional] 
 **request_sold_date_from** | **datetime**| When it was sold on Secondary market from | [optional] 
 **request_sold_date_to** | **datetime**| When it was sold on Secondary market to | [optional] 
 **request_purchase_date_from** | **datetime**| When you received the investment Auctions/Secondary market from | [optional] 
 **request_purchase_date_to** | **datetime**| When you received the investment Auctions/Secondary market to | [optional] 
 **request_next_payment_date_to** | **datetime**| Next payment date to | [optional] 
 **request_next_payment_date_from** | **datetime**| Next payment date from | [optional] 
 **request_last_payment_date_from** | **datetime**| Last payment date from | [optional] 
 **request_last_payment_date_to** | **datetime**| Last payment date to | [optional] 
 **request_countries** | [**list[str]**](str.md)| Two letter iso code for country of origin: EE, ES, FI | [optional] 
 **request_ratings** | [**list[str]**](str.md)| Bondora&#39;s rating: AA, A, B, C, D, E, F, HR | [optional] 
 **request_credit_score_min** | **int**| Minimum credit score | [optional] 
 **request_credit_score_max** | **int**| Maximum credit score | [optional] 
 **request_user_name** | **str**| Borrower&#39;s username | [optional] 
 **request_loan_status_code** | [**list[int]**](int.md)| Loan status code              &lt;para&gt;2 Current&lt;/para&gt;&lt;para&gt;3 Cancelled&lt;/para&gt;&lt;para&gt;100 Overdue&lt;/para&gt;&lt;para&gt;5 60+ days overdue&lt;/para&gt;&lt;para&gt;4 Repaid&lt;/para&gt;&lt;para&gt;8 Released&lt;/para&gt; | [optional] 
 **request_income_verification_status** | **int**| Income verification type | [optional] 
 **request_loan_debt_management_stage** | **int**| Latest debt management stage | [optional] 
 **request_loan_debt_management_stage_type** | **int**| Latest debt management stage type | [optional] 
 **request_loan_debt_management_date_active_from** | **datetime**| Latest debt management date active from | [optional] 
 **request_loan_debt_management_date_active_to** | **datetime**| Latest debt management date active to | [optional] 
 **request_auction_bid_type** | **int**| Auction bid type | [optional] 
 **request_sales_status** | **int**| Second market sale status              &lt;para&gt;NULL All active&lt;/para&gt;&lt;para&gt;0 Bought investments&lt;/para&gt;&lt;para&gt;1 Sold investments&lt;/para&gt;&lt;para&gt;2 Investment is on sale&lt;/para&gt;&lt;para&gt;3 Investment is not on sale&lt;/para&gt; | [optional] 
 **request_is_in_repayment** | **bool**| Search only active in repayment loans, StatusCodes (2, 5, 100) | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultMyInvestments**](ApiResultMyInvestments.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_balance**
> ApiResultMyAccountBalance account_get_balance()

Gets your account balance information

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.AccountApi()

try: 
    # Gets your account balance information
    api_response = api_instance.account_get_balance()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountApi->account_get_balance: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResultMyAccountBalance**](ApiResultMyAccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_event_log**
> ApiResultEventLog account_get_event_log(request_event_date_from=request_event_date_from, request_event_date_to=request_event_date_to, request_event_type=request_event_type, request_ip_address=request_ip_address, request_page_size=request_page_size, request_page_nr=request_page_nr)

Gets events that have been made with this application (related to current access token)

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.AccountApi()
request_event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Start datetime (optional)
request_event_date_to = '2013-10-20T19:20:30+01:00' # datetime | end datetime (optional)
request_event_type = 56 # int | Event type (optional)
request_ip_address = 'request_ip_address_example' # str | IP address (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Gets events that have been made with this application (related to current access token)
    api_response = api_instance.account_get_event_log(request_event_date_from=request_event_date_from, request_event_date_to=request_event_date_to, request_event_type=request_event_type, request_ip_address=request_ip_address, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountApi->account_get_event_log: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_event_date_from** | **datetime**| Start datetime | [optional] 
 **request_event_date_to** | **datetime**| end datetime | [optional] 
 **request_event_type** | **int**| Event type | [optional] 
 **request_ip_address** | **str**| IP address | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultEventLog**](ApiResultEventLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

