# bondora_api.AuctionApi

All URIs are relative to *http://api.bondora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auction_get**](AuctionApi.md#auction_get) | **GET** /api/v1/auction/{id} | Gets Auction info by auction identifier
[**auction_get_active**](AuctionApi.md#auction_get_active) | **GET** /api/v1/auctions | Gets list of active Auctions


# **auction_get**
> ApiResultExtendedAuction auction_get(id)

Gets Auction info by auction identifier

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.AuctionApi()
id = 'id_example' # str | Auction's identifier

try: 
    # Gets Auction info by auction identifier
    api_response = api_instance.auction_get(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuctionApi->auction_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Auction&#39;s identifier | 

### Return type

[**ApiResultExtendedAuction**](ApiResultExtendedAuction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auction_get_active**
> ApiResultAuctions auction_get_active(request_countries=request_countries, request_ratings=request_ratings, request_gender=request_gender, request_sum_min=request_sum_min, request_sum_max=request_sum_max, request_terms=request_terms, request_age_min=request_age_min, request_age_max=request_age_max, request_loan_number=request_loan_number, request_user_name=request_user_name, request_application_date_from=request_application_date_from, request_application_date_to=request_application_date_to, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_credit_scores_ee_mini=request_credit_scores_ee_mini, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_income_total_min=request_income_total_min, request_income_total_max=request_income_total_max, request_model_version=request_model_version, request_expected_loss_min=request_expected_loss_min, request_expected_loss_max=request_expected_loss_max, request_listed_on_utc_from=request_listed_on_utc_from, request_listed_on_utc_to=request_listed_on_utc_to, request_page_size=request_page_size, request_page_nr=request_page_nr)

Gets list of active Auctions

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.AuctionApi()
request_countries = ['request_countries_example'] # list[str] | Two letter iso code for country of origin: EE, ES, FI (optional)
request_ratings = ['request_ratings_example'] # list[str] | Bondora's rating: AA, A, B, C, D, E, F, HR (optional)
request_gender = 56 # int | Borrower's gender: Male 0, Female 1, Unknown 2 (optional)
request_sum_min = 56 # int | Minimal loan amount (optional)
request_sum_max = 56 # int | Maximum loan amount (optional)
request_terms = [56] # list[int] | Loan length: 3, 9, 12, 18, 24, 36, 48, 60 months (optional)
request_age_min = 56 # int | Minimal age (optional)
request_age_max = 56 # int | Maximum age (optional)
request_loan_number = 56 # int | Loan number (optional)
request_user_name = 'request_user_name_example' # str | Username (optional)
request_application_date_from = '2013-10-20T19:20:30+01:00' # datetime | Loan application started date from (optional)
request_application_date_to = '2013-10-20T19:20:30+01:00' # datetime | Loan application started date to (optional)
request_credit_score_min = 56 # int | Minimum credit score (optional)
request_credit_score_max = 56 # int | Maximum credit score (optional)
request_credit_scores_ee_mini = ['request_credit_scores_ee_mini_example'] # list[str] | Credit score for EE loans (optional)
request_interest_min = 1.2 # float | Minimum interest (optional)
request_interest_max = 1.2 # float | Maximum interest (optional)
request_income_total_min = 1.2 # float | Minimal total income (optional)
request_income_total_max = 1.2 # float | Maximum total income (optional)
request_model_version = 56 # int | Model version (optional)
request_expected_loss_min = 1.2 # float | Minimal expected loss (optional)
request_expected_loss_max = 1.2 # float | Maximum expected loss (optional)
request_listed_on_utc_from = '2013-10-20T19:20:30+01:00' # datetime | Date when auction was published from (optional)
request_listed_on_utc_to = '2013-10-20T19:20:30+01:00' # datetime | Date when auction was published to (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Gets list of active Auctions
    api_response = api_instance.auction_get_active(request_countries=request_countries, request_ratings=request_ratings, request_gender=request_gender, request_sum_min=request_sum_min, request_sum_max=request_sum_max, request_terms=request_terms, request_age_min=request_age_min, request_age_max=request_age_max, request_loan_number=request_loan_number, request_user_name=request_user_name, request_application_date_from=request_application_date_from, request_application_date_to=request_application_date_to, request_credit_score_min=request_credit_score_min, request_credit_score_max=request_credit_score_max, request_credit_scores_ee_mini=request_credit_scores_ee_mini, request_interest_min=request_interest_min, request_interest_max=request_interest_max, request_income_total_min=request_income_total_min, request_income_total_max=request_income_total_max, request_model_version=request_model_version, request_expected_loss_min=request_expected_loss_min, request_expected_loss_max=request_expected_loss_max, request_listed_on_utc_from=request_listed_on_utc_from, request_listed_on_utc_to=request_listed_on_utc_to, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuctionApi->auction_get_active: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_countries** | [**list[str]**](str.md)| Two letter iso code for country of origin: EE, ES, FI | [optional] 
 **request_ratings** | [**list[str]**](str.md)| Bondora&#39;s rating: AA, A, B, C, D, E, F, HR | [optional] 
 **request_gender** | **int**| Borrower&#39;s gender: Male 0, Female 1, Unknown 2 | [optional] 
 **request_sum_min** | **int**| Minimal loan amount | [optional] 
 **request_sum_max** | **int**| Maximum loan amount | [optional] 
 **request_terms** | [**list[int]**](int.md)| Loan length: 3, 9, 12, 18, 24, 36, 48, 60 months | [optional] 
 **request_age_min** | **int**| Minimal age | [optional] 
 **request_age_max** | **int**| Maximum age | [optional] 
 **request_loan_number** | **int**| Loan number | [optional] 
 **request_user_name** | **str**| Username | [optional] 
 **request_application_date_from** | **datetime**| Loan application started date from | [optional] 
 **request_application_date_to** | **datetime**| Loan application started date to | [optional] 
 **request_credit_score_min** | **int**| Minimum credit score | [optional] 
 **request_credit_score_max** | **int**| Maximum credit score | [optional] 
 **request_credit_scores_ee_mini** | [**list[str]**](str.md)| Credit score for EE loans | [optional] 
 **request_interest_min** | **float**| Minimum interest | [optional] 
 **request_interest_max** | **float**| Maximum interest | [optional] 
 **request_income_total_min** | **float**| Minimal total income | [optional] 
 **request_income_total_max** | **float**| Maximum total income | [optional] 
 **request_model_version** | **int**| Model version | [optional] 
 **request_expected_loss_min** | **float**| Minimal expected loss | [optional] 
 **request_expected_loss_max** | **float**| Maximum expected loss | [optional] 
 **request_listed_on_utc_from** | **datetime**| Date when auction was published from | [optional] 
 **request_listed_on_utc_to** | **datetime**| Date when auction was published to | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultAuctions**](ApiResultAuctions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

