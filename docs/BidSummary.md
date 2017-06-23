# BidSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Bid unique identifier | [optional] 
**auction_id** | **str** | Id of auction to bid into | [optional] 
**requested_bid_amount** | **float** | Amount that was requested to bid | [optional] 
**actual_bid_amount** | **float** | Amount that is bidded | [optional] 
**requested_bid_minimum_limit** | **float** | Minimum amount that was specified for auction | [optional] 
**bid_requested_date** | **datetime** | When bid was requested | [optional] 
**bid_processed_date** | **datetime** | When bid was processed | [optional] 
**is_request_being_processed** | **bool** | Is request currently processed | [optional] 
**status_code** | **int** | Status of bid              &lt;para&gt;0 Pending&lt;/para&gt;&lt;para&gt;1 Open&lt;/para&gt;&lt;para&gt;2 Successful&lt;/para&gt;&lt;para&gt;3 Failed&lt;/para&gt;&lt;para&gt;4 Cancelled&lt;/para&gt;&lt;para&gt;5 Accepted&lt;/para&gt; | [optional] 
**failure_reason** | **int** | Why bid failed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


