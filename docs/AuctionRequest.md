# AuctionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **list[str]** | Two letter iso code for country of origin: EE, ES, FI | [optional] 
**ratings** | **list[str]** | Bondora&#39;s rating: AA, A, B, C, D, E, F, HR | [optional] 
**gender** | **int** | Borrower&#39;s gender: Male 0, Female 1, Unknown 2 | [optional] 
**sum_min** | **int** | Minimal loan amount | [optional] 
**sum_max** | **int** | Maximum loan amount | [optional] 
**terms** | **list[int]** | Loan length: 3, 9, 12, 18, 24, 36, 48, 60 months | [optional] 
**age_min** | **int** | Minimal age | [optional] 
**age_max** | **int** | Maximum age | [optional] 
**loan_number** | **int** | Loan number | [optional] 
**user_name** | **str** | Username | [optional] 
**application_date_from** | **datetime** | Loan application started date from | [optional] 
**application_date_to** | **datetime** | Loan application started date to | [optional] 
**credit_score_min** | **int** | Minimum credit score | [optional] 
**credit_score_max** | **int** | Maximum credit score | [optional] 
**credit_scores_ee_mini** | **list[str]** | Credit score for EE loans | [optional] 
**interest_min** | **float** | Minimum interest | [optional] 
**interest_max** | **float** | Maximum interest | [optional] 
**income_total_min** | **float** | Minimal total income | [optional] 
**income_total_max** | **float** | Maximum total income | [optional] 
**model_version** | **int** | Model version | [optional] 
**expected_loss_min** | **float** | Minimal expected loss | [optional] 
**expected_loss_max** | **float** | Maximum expected loss | [optional] 
**listed_on_utc_from** | **datetime** | Date when auction was published from | [optional] 
**listed_on_utc_to** | **datetime** | Date when auction was published to | [optional] 
**page_size** | **int** | Max items in result, default is 1000 | [optional] 
**page_nr** | **int** | Result page nr | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


