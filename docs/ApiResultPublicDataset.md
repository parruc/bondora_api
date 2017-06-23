# ApiResultPublicDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | Requested Max items in result | [optional] 
**page_nr** | **int** | Requested page nr | [optional] 
**total_count** | **int** | Total number of items found | 
**count** | **int** | Number of items returned | 
**payload** | [**list[PublicDatasetItem]**](PublicDatasetItem.md) | The payload of the response. Type depends on the API request. | [optional] 
**success** | **bool** | Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise. | 
**errors** | [**list[ApiError]**](ApiError.md) | Error(s) accociated with the API request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


