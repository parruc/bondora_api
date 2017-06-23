# bondora_api.BidApi

All URIs are relative to *http://api.bondora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bid_cancel_bid**](BidApi.md#bid_cancel_bid) | **POST** /api/v1/bid/{id}/cancel | Cancel the Bid
[**bid_get_bid**](BidApi.md#bid_get_bid) | **GET** /api/v1/bid/{id} | Get the Bid
[**bid_get_bid_summaries**](BidApi.md#bid_get_bid_summaries) | **GET** /api/v1/bids | Gets list of bids the investor has made.
[**bid_make_bids**](BidApi.md#bid_make_bids) | **POST** /api/v1/bid | Makes bid(s) into specified auction(s).


# **bid_cancel_bid**
> ApiResult bid_cancel_bid(id)

Cancel the Bid

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.BidApi()
id = 'id_example' # str | Bid identificator

try: 
    # Cancel the Bid
    api_response = api_instance.bid_cancel_bid(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BidApi->bid_cancel_bid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bid identificator | 

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid_get_bid**
> ApiResultBid bid_get_bid(id)

Get the Bid

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.BidApi()
id = 'id_example' # str | Bid identificator

try: 
    # Get the Bid
    api_response = api_instance.bid_get_bid(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BidApi->bid_get_bid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bid identificator | 

### Return type

[**ApiResultBid**](ApiResultBid.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid_get_bid_summaries**
> ApiResultBids bid_get_bid_summaries(request_bid_status_code=request_bid_status_code, request_start_date=request_start_date, request_end_date=request_end_date, request_page_size=request_page_size, request_page_nr=request_page_nr)

Gets list of bids the investor has made.

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.BidApi()
request_bid_status_code = 56 # int | Bid status code (optional)
request_start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (optional)
request_end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (optional)
request_page_size = 56 # int | Max items in result, default is 1000 (optional)
request_page_nr = 56 # int | Result page nr (optional)

try: 
    # Gets list of bids the investor has made.
    api_response = api_instance.bid_get_bid_summaries(request_bid_status_code=request_bid_status_code, request_start_date=request_start_date, request_end_date=request_end_date, request_page_size=request_page_size, request_page_nr=request_page_nr)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BidApi->bid_get_bid_summaries: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_bid_status_code** | **int**| Bid status code | [optional] 
 **request_start_date** | **datetime**| Start date | [optional] 
 **request_end_date** | **datetime**| End date | [optional] 
 **request_page_size** | **int**| Max items in result, default is 1000 | [optional] 
 **request_page_nr** | **int**| Result page nr | [optional] 

### Return type

[**ApiResultBids**](ApiResultBids.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bid_make_bids**
> ApiResultMakeBids bid_make_bids(bid_request)

Makes bid(s) into specified auction(s).

### Example 
```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bondora_api.BidApi()
bid_request = bondora_api.BidRequest() # BidRequest | 

try: 
    # Makes bid(s) into specified auction(s).
    api_response = api_instance.bid_make_bids(bid_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling BidApi->bid_make_bids: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bid_request** | [**BidRequest**](BidRequest.md)|  | 

### Return type

[**ApiResultMakeBids**](ApiResultMakeBids.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

