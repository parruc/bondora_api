# LoanPartDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_part_id** | **str** | LoanPart unique identifier | [optional] 
**amount** | **float** | Investment amount | [optional] 
**auction_id** | **str** | Auction unique identifier | [optional] 
**auction_name** | **str** | Auction name | [optional] 
**auction_number** | **int** | Auction number | [optional] 
**auction_bid_number** | **int** | Auction bid number | [optional] 
**country** | **str** | Residency of the borrower | [optional] 
**credit_score** | **float** | &lt;para&gt;    1000 No previous payments problems&lt;/para&gt;  &lt;para&gt;    900 Payments problems finished 24-36 months ago&lt;/para&gt;  &lt;para&gt;    800 Payments problems finished 12-24 months ago&lt;/para&gt;  &lt;para&gt;    700 Payments problems finished 6-12 months ago&lt;/para&gt;  &lt;para&gt;    600 Payment problems finished &amp;lt;6 months ago&lt;/para&gt;  &lt;para&gt;    500 Active payment problems&lt;/para&gt; | [optional] 
**credit_score_es_micro_l** | **str** | A score that is specifically designed for risk classifying subprime borrowers (defined by Equifax as borrowers that do not have access to bank loans).               A measure of the probability of default one month ahead.              &lt;para&gt;The score is given on a 10-grade scale, from the best score to the worst:&lt;/para&gt;&lt;para&gt;M1, M2, M3, M4, M5, M6, M7, M8, M9, M10&lt;/para&gt; | [optional] 
**credit_score_es_equifax_risk** | **str** | Generic score for the loan applicants that do not have active past due operations in ASNEF.              A measure of the probability of default one year ahead.               The score is given on a 6-grade scale.              &lt;para&gt;AAA Very low&lt;/para&gt;&lt;para&gt;AA Low&lt;/para&gt;&lt;para&gt;A Average&lt;/para&gt;&lt;para&gt;B Average High&lt;/para&gt;&lt;para&gt;C High&lt;/para&gt;&lt;para&gt;D Very High&lt;/para&gt; | [optional] 
**credit_score_fi_asiakas_tieto_risk_grade** | **str** | Credit Scoring model for Finnish Asiakastieto              &lt;para&gt;RL1 Very low risk 01-20&lt;/para&gt;&lt;para&gt;RL2 Low risk 21-40&lt;/para&gt;&lt;para&gt;RL3 Average risk 41-60&lt;/para&gt;&lt;para&gt;RL4 Big risk 61-80&lt;/para&gt;&lt;para&gt;RL5 Huge risk 81-100&lt;/para&gt; | [optional] 
**credit_score_ee_mini** | **str** | Credit scoring for Estonian loans              &lt;para&gt;1000 No previous payments problems&lt;/para&gt;&lt;para&gt;900 Payments problems finished 24-36 months ago&lt;/para&gt;&lt;para&gt;800 Payments problems finished 12-24 months ago&lt;/para&gt;&lt;para&gt;700 Payments problems finished 6-12 months ago&lt;/para&gt;&lt;para&gt;600 Payment problems finished &amp;lt;6 months ago&lt;/para&gt;&lt;para&gt;500 Active payment problems&lt;/para&gt; | [optional] 
**rating** | **str** | Bondora Rating issued by the Rating model | [optional] 
**initial_interest** | **float** | Initial interest rate | [optional] 
**interest** | **float** | Current interest rate | [optional] 
**use_of_loan** | **int** | Use of loan | [optional] 
**income_verification_status** | **int** | Income verification type | [optional] 
**loan_id** | **str** | Loan unique identifier | [optional] 
**loan_status_code** | **int** | Loan status code              &lt;para&gt;2 Current&lt;/para&gt;&lt;para&gt;100 Overdue&lt;/para&gt;&lt;para&gt;5 60+ days overdue&lt;/para&gt;&lt;para&gt;4 Repaid&lt;/para&gt;&lt;para&gt;8 Released&lt;/para&gt; | [optional] 
**user_name** | **str** | Borrower&#39;s username | [optional] 
**gender** | **int** | Borrower&#39;s Gender | [optional] 
**date_of_birth** | **datetime** | Borrower&#39;s date of birth | [optional] 
**signed_date** | **datetime** | Loan issued date | [optional] 
**re_scheduled_on** | **datetime** | Last rescheduling date | [optional] 
**debt_occured_on** | **datetime** | Debt occured on date | [optional] 
**debt_occured_on_for_secondary** | **datetime** | Debt occured on date | [optional] 
**loan_duration** | **int** | Loan original lenght | [optional] 
**next_payment_nr** | **int** | Next scheduled payment number | [optional] 
**next_payment_date** | **datetime** | Next scheduled payment date | [optional] 
**next_payment_sum** | **float** | Next scheduled payment amount | [optional] 
**nr_of_scheduled_payments** | **int** | Total number of scheduled payments | [optional] 
**last_payment_date** | **datetime** | Last scheduled payment date | [optional] 
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
**write_off_total** | **float** | Write off total | [optional] 
**debt_servicing_cost_main_amount** | **float** | Total amount of principal debt servicing cost | [optional] 
**debt_servicing_cost_interest_amount** | **float** | Total amount of interest debt servicing cost | [optional] 
**debt_servicing_cost_penalty_amount** | **float** | Total amount of penalty debt servicing cost | [optional] 
**debt_servicing_cost_total** | **float** | Debt servicing cost total | [optional] 
**repaid_principal_current_owner** | **float** | Total principal repaid amount to current note owner | [optional] 
**repaid_interests_current_owner** | **float** | Total interest repaid amount to current note owner | [optional] 
**late_charges_paid_current_owner** | **float** | Late charges paid amount to current note owner | [optional] 
**repaid_total_current_owner** | **float** | Total repaid amount to current note owner | [optional] 
**total_repaid** | **float** | Total repaid amount | [optional] 
**debt_managment_events** | [**list[DebtManagementEvent]**](DebtManagementEvent.md) | Debt managment event collection | [optional] 
**loan_transfers** | [**list[LoanTransfer]**](LoanTransfer.md) | Collection of all loan payments | [optional] 
**scheduled_payments** | [**list[ScheduledPayment]**](ScheduledPayment.md) | Collection of all loan scheduled payments.               Contains previous period values before rescheduling was made | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

