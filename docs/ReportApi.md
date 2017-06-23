# bondora_api.ReportApi

All URIs are relative to *http://api.bondora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_generate_report**](ReportApi.md#report_generate_report) | **POST** /api/v1/report | Request to generate specified report type for set period.
[**report_get_public_dataset**](ReportApi.md#report_get_public_dataset) | **GET** /api/v1/publicdataset | Provides daily public dataset of all loan data that is not covered by the data protection laws.
[**report_get_report**](ReportApi.md#report_get_report) | **GET** /api/v1/report/{id} | Get report data for specified report identificator.
[**report_get_report_list**](ReportApi.md#report_get_report_list) | **GET** /api/v1/reports | List of all reports


# **report_generate_report**
> ApiResultCreateReport report_generate_report(request)

Request to generate specified report type for set period.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.ReportApi()
request = bondora_api.ReportCreateRequest() # ReportCreateRequest | 

try: 
    # Request to generate specified report type for set period.
    api_response = api_instance.report_generate_report(request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportApi->report_generate_report: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ReportCreateRequest**](ReportCreateRequest.md)|  | 

### Return type

[**ApiResultCreateReport**](ApiResultCreateReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_public_dataset**
> ApiResultPublicDataset report_get_public_dataset(request_loan_ids=request_loan_ids, request_countries=request_countries, request_ratings=request_ratings, request_loan_date_from=request_loan_date_from, request_loan_date_to=request_loan_date_to, request_page_size=request_page_size, request_page_nr=request_page_nr)

Provides daily public dataset of all loan data that is not covered by the data protection laws.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bondora_api.ReportApi()
request_loan_ids = ['request_loan_ids_example'] # list[str] | Specific loans to search (optional)
request_countries = ['request_countries_example'] # list[str] | Two letter iso code for country of origin: EE, ES, FI (optional)
request_ratings = ['request_ratings_example'] # list[str] | Bondora's rating: AA, A, B, C, D, E, F, HR (optional)
request_loan_date_from = '2013-10-20T19:20:30+01:00' # datetime | Loan start date from (optional)
request_loan_date_to = '2013-10-20T19:20:30+01:00' # datetime | Loan start date to (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Provides daily public dataset of all loan data that is not covered by the data protection laws.
    api_response = api_instance.report_get_public_dataset(request_loan_ids=request_loan_ids, request_countries=request_countries, request_ratings=request_ratings, request_loan_date_from=request_loan_date_from, request_loan_date_to=request_loan_date_to, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportApi->report_get_public_dataset: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_loan_ids** | [**list[str]**](str.md)| Specific loans to search | [optional] 
 **request_countries** | [**list[str]**](str.md)| Two letter iso code for country of origin: EE, ES, FI | [optional] 
 **request_ratings** | [**list[str]**](str.md)| Bondora&#39;s rating: AA, A, B, C, D, E, F, HR | [optional] 
 **request_loan_date_from** | **datetime**| Loan start date from | [optional] 
 **request_loan_date_to** | **datetime**| Loan start date to | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultPublicDataset**](ApiResultPublicDataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_report**
> ApiResultReport report_get_report(id)

Get report data for specified report identificator.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.ReportApi()
id = 'id_example' # str | ReportId

try: 
    # Get report data for specified report identificator.
    api_response = api_instance.report_get_report(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportApi->report_get_report: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ReportId | 

### Return type

[**ApiResultReport**](ApiResultReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_get_report_list**
> ApiResultReportList report_get_report_list()

List of all reports

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.ReportApi()

try: 
    # List of all reports
    api_response = api_instance.report_get_report_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportApi->report_get_report_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResultReportList**](ApiResultReportList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

