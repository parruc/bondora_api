# bondora_api
Bondora API version 1

- API version: v1
- Package version: 1.0.0
- Build date: 2017-06-20T16:21:41.384+02:00
For more information, please visit [https://www.bondora.com](https://www.bondora.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bondora_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bondora_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
bondora_api.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = bondora_api.AccountApi
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

## Documentation for API Endpoints

All URIs are relative to *http://api.bondora.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_get_active**](docs/AccountApi.md#account_get_active) | **GET** /api/v1/account/investments | Gets list of your investments
*AccountApi* | [**account_get_balance**](docs/AccountApi.md#account_get_balance) | **GET** /api/v1/account/balance | Gets your account balance information
*AccountApi* | [**account_get_event_log**](docs/AccountApi.md#account_get_event_log) | **GET** /api/v1/eventlog | Gets events that have been made with this application (related to current access token)
*AuctionApi* | [**auction_get**](docs/AuctionApi.md#auction_get) | **GET** /api/v1/auction/{id} | Gets Auction info by auction identifier
*AuctionApi* | [**auction_get_active**](docs/AuctionApi.md#auction_get_active) | **GET** /api/v1/auctions | Gets list of active Auctions
*BidApi* | [**bid_cancel_bid**](docs/BidApi.md#bid_cancel_bid) | **POST** /api/v1/bid/{id}/cancel | Cancel the Bid
*BidApi* | [**bid_get_bid**](docs/BidApi.md#bid_get_bid) | **GET** /api/v1/bid/{id} | Get the Bid
*BidApi* | [**bid_get_bid_summaries**](docs/BidApi.md#bid_get_bid_summaries) | **GET** /api/v1/bids | Gets list of bids the investor has made.
*BidApi* | [**bid_make_bids**](docs/BidApi.md#bid_make_bids) | **POST** /api/v1/bid | Makes bid(s) into specified auction(s).
*ReportApi* | [**report_generate_report**](docs/ReportApi.md#report_generate_report) | **POST** /api/v1/report | Request to generate specified report type for set period.
*ReportApi* | [**report_get_public_dataset**](docs/ReportApi.md#report_get_public_dataset) | **GET** /api/v1/publicdataset | Provides daily public dataset of all loan data that is not covered by the data protection laws.
*ReportApi* | [**report_get_report**](docs/ReportApi.md#report_get_report) | **GET** /api/v1/report/{id} | Get report data for specified report identificator.
*ReportApi* | [**report_get_report_list**](docs/ReportApi.md#report_get_report_list) | **GET** /api/v1/reports | List of all reports
*SecondMarketApi* | [**second_market_buy**](docs/SecondMarketApi.md#second_market_buy) | **POST** /api/v1/secondarymarket/buy | Buy loans from secondary market.
*SecondMarketApi* | [**second_market_cancel**](docs/SecondMarketApi.md#second_market_cancel) | **POST** /api/v1/secondarymarket/{id}/cancel | Remove your loans from secondary market.
*SecondMarketApi* | [**second_market_cancel_multiple**](docs/SecondMarketApi.md#second_market_cancel_multiple) | **POST** /api/v1/secondarymarket/cancel | Remove your loans from secondary market.
*SecondMarketApi* | [**second_market_get**](docs/SecondMarketApi.md#second_market_get) | **GET** /api/v1/loanpart/{id} | Gets LoanPartDetails info by identifier
*SecondMarketApi* | [**second_market_get_active**](docs/SecondMarketApi.md#second_market_get_active) | **GET** /api/v1/secondarymarket | Gets list of active secondary market items
*SecondMarketApi* | [**second_market_get_item**](docs/SecondMarketApi.md#second_market_get_item) | **GET** /api/v1/secondarymarket/{id} | Get the secondary market item summary
*SecondMarketApi* | [**second_market_sell**](docs/SecondMarketApi.md#second_market_sell) | **POST** /api/v1/secondarymarket/sell | Sell your loans to secondary market.


## Documentation For Models

 - [ApiBidSummariesRequest](docs/ApiBidSummariesRequest.md)
 - [ApiError](docs/ApiError.md)
 - [ApiResult](docs/ApiResult.md)
 - [ApiResultAuctions](docs/ApiResultAuctions.md)
 - [ApiResultBid](docs/ApiResultBid.md)
 - [ApiResultBids](docs/ApiResultBids.md)
 - [ApiResultCreateReport](docs/ApiResultCreateReport.md)
 - [ApiResultEventLog](docs/ApiResultEventLog.md)
 - [ApiResultExtendedAuction](docs/ApiResultExtendedAuction.md)
 - [ApiResultLoanPartDetails](docs/ApiResultLoanPartDetails.md)
 - [ApiResultMakeBids](docs/ApiResultMakeBids.md)
 - [ApiResultMyAccountBalance](docs/ApiResultMyAccountBalance.md)
 - [ApiResultMyInvestments](docs/ApiResultMyInvestments.md)
 - [ApiResultPublicDataset](docs/ApiResultPublicDataset.md)
 - [ApiResultReport](docs/ApiResultReport.md)
 - [ApiResultReportList](docs/ApiResultReportList.md)
 - [ApiResultSecondMarket](docs/ApiResultSecondMarket.md)
 - [ApiResultSecondMarketItemSummary](docs/ApiResultSecondMarketItemSummary.md)
 - [ApiResultSecondMarketSale](docs/ApiResultSecondMarketSale.md)
 - [Auction](docs/Auction.md)
 - [AuctionExtended](docs/AuctionExtended.md)
 - [AuctionRequest](docs/AuctionRequest.md)
 - [Bid](docs/Bid.md)
 - [BidRequest](docs/BidRequest.md)
 - [BidResponse](docs/BidResponse.md)
 - [BidSummary](docs/BidSummary.md)
 - [BorrowerHistory](docs/BorrowerHistory.md)
 - [Debt](docs/Debt.md)
 - [DebtManagementEvent](docs/DebtManagementEvent.md)
 - [EventLogItem](docs/EventLogItem.md)
 - [EventLogRequest](docs/EventLogRequest.md)
 - [Liability](docs/Liability.md)
 - [LoanPartDetails](docs/LoanPartDetails.md)
 - [LoanTransfer](docs/LoanTransfer.md)
 - [MyAccountBalance](docs/MyAccountBalance.md)
 - [MyInvestmentItem](docs/MyInvestmentItem.md)
 - [MyInvestmentsRequest](docs/MyInvestmentsRequest.md)
 - [Object](docs/Object.md)
 - [PublicDatasetItem](docs/PublicDatasetItem.md)
 - [PublicDatasetRequest](docs/PublicDatasetRequest.md)
 - [Report](docs/Report.md)
 - [ReportCreateRequest](docs/ReportCreateRequest.md)
 - [ReportItem](docs/ReportItem.md)
 - [ReportResponse](docs/ReportResponse.md)
 - [ScheduledPayment](docs/ScheduledPayment.md)
 - [SecondMarketBuyRequest](docs/SecondMarketBuyRequest.md)
 - [SecondMarketCancelRequest](docs/SecondMarketCancelRequest.md)
 - [SecondMarketItem](docs/SecondMarketItem.md)
 - [SecondMarketItemSummary](docs/SecondMarketItemSummary.md)
 - [SecondMarketRequest](docs/SecondMarketRequest.md)
 - [SecondMarketSaleRequest](docs/SecondMarketSaleRequest.md)
 - [SecondMarketSaleResponse](docs/SecondMarketSaleResponse.md)
 - [SecondMarketSell](docs/SecondMarketSell.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://www.bondora.com/oauth/authorize
- **Scopes**: 
 - **Investments**: Get list of user investments
 - **BidsRead**: Get user bids
 - **BidsEdit**: Create or cancel bids
 - **SmSell**: Sell loans in Secondary Market
 - **SmBuy**: Buy loans from Secondary Market
 - **ReportCreate**: Allow to create new report(s)
 - **ReportRead**: Allow to view user's created report items and report details


## Author

parruc@gmail.com
