# SecondMarketItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Item unique identifier | [optional] 
**loan_part_id** | **str** | LoanPart unique identifier | [optional] 
**amount** | **float** | Investment amount | [optional] 
**auction_id** | **str** | Auction unique identifier | [optional] 
**auction_name** | **str** | Auction name | [optional] 
**auction_number** | **int** | Auction number | [optional] 
**auction_bid_number** | **int** | Auction bid number | [optional] 
**country** | **str** | Residency of the borrower | [optional] 
**credit_score** | **float** | &lt;para&gt;    1000 No previous payments problems&lt;/para&gt;  &lt;para&gt;    900 Payments problems finished 24-36 months ago&lt;/para&gt;  &lt;para&gt;    800 Payments problems finished 12-24 months ago&lt;/para&gt;  &lt;para&gt;    700 Payments problems finished 6-12 months ago&lt;/para&gt;  &lt;para&gt;    600 Payment problems finished &amp;lt;6 months ago&lt;/para&gt;  &lt;para&gt;    500 Active payment problems&lt;/para&gt; | [optional] 
**rating** | **str** | Bondora Rating issued by the Rating model | [optional] 
**interest** | **float** | Interest rate | [optional] 
**use_of_loan** | **int** | Use of loan | [optional] 
**income_verification_status** | **int** | Income verification type | [optional] 
**loan_status_code** | **int** | Loan status code              &lt;para&gt;2 Current&lt;/para&gt;&lt;para&gt;100 Overdue&lt;/para&gt;&lt;para&gt;5 60+ days overdue&lt;/para&gt;&lt;para&gt;4 Repaid&lt;/para&gt;&lt;para&gt;8 Released&lt;/para&gt; | [optional] 
**loan_status_active_from** | **datetime** | Loan status active from | [optional] 
**latest_debt_management_stage_type** | **int** | Latest debt management stage type | [optional] 
**latest_debt_management_date** | **datetime** | Latest debt management date | [optional] 
**user_name** | **str** | Borrower&#39;s username | [optional] 
**gender** | **int** | Borrower&#39;s Gender | [optional] 
**date_of_birth** | **datetime** | Borrower&#39;s date of birth | [optional] 
**signed_date** | **datetime** | Loan issued date | [optional] 
**re_scheduled_on** | **datetime** | Last rescheduling date | [optional] 
**debt_occured_on** | **datetime** | Debt occured on date | [optional] 
**debt_occured_on_for_secondary** | **datetime** | Debt occured on date | [optional] 
**next_payment_nr** | **int** | Next scheduled payment number | [optional] 
**next_payment_date** | **datetime** | Next scheduled payment date | [optional] 
**next_payment_sum** | **float** | Next scheduled payment amount | [optional] 
**nr_of_scheduled_payments** | **int** | Total number of scheduled payments | [optional] 
**last_payment_date** | **datetime** | Last payment date | [optional] 
**principal_repaid** | **float** | Total principal repaid amount | [optional] 
**interest_repaid** | **float** | Total interest repaid amount | [optional] 
**late_amount_paid** | **float** | Total late charges paid amount | [optional] 
**principal_remaining** | **float** | Remaining principal amount | [optional] 
**principal_late_amount** | **float** | Principal debt amount | [optional] 
**interest_late_amount** | **float** | Interest debt amount | [optional] 
**penalty_late_amount** | **float** | Late charges debt amount | [optional] 
**late_amount_total** | **float** | Late amount total | [optional] 
**principal_write_off_amount** | **float** | Total amount of principal written off | [optional] 
**interest_write_off_amount** | **float** | Total amount of interest written off | [optional] 
**penalty_write_off_amount** | **float** | Total amount of penalty written off | [optional] 
**debt_servicing_cost_main_amount** | **float** | Total amount of principal debt servicing cost | [optional] 
**debt_servicing_cost_interest_amount** | **float** | Total amount of interest debt servicing cost | [optional] 
**debt_servicing_cost_penalty_amount** | **float** | Total amount of penalty debt servicing cost | [optional] 
**price** | **float** | Outstanding principal balance +/- discount or mark-up | [optional] 
**fee** | **float** | Secondary market purchase fee paid to Bondora | [optional] 
**total_cost** | **float** | Total amount paid for purchase | [optional] 
**outstanding_payments** | **float** | Total amount still to be repaid by the borrower. This includes the principal balance, accrued interest and late charges as well as any future scheduled interest payments | [optional] 
**desired_discount_rate** | **float** | Discount rate percent | [optional] 
**xirr** | **float** | XIRR (extended internal rate of return) is a methodology to calculate the net return using the loan issued date and amount,               loan repayment dates and amounts and the principal balance according to the original repayment date.               All overdue principal payments are written off immediately. No provisions for future losses are made and only received (not accrued or scheduled)               interest payments are taken into account. | [optional] 
**listed_on_date** | **datetime** | Date when item was published | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

