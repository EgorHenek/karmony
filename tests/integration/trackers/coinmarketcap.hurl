GET https://sandbox-api.coinmarketcap.com/v2/tools/price-conversion
X-CMC_PRO_API_KEY: b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c 
[QueryStringParams]
amount: 1
symbol: BTC
convert: USD
HTTP 200
[Asserts]
jsonpath "$.data.BTC.quote.USD.price" exists
