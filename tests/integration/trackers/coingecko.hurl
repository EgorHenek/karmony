GET https://api.coingecko.com/api/v3/simple/price
[QueryStringParams]
ids: bitcoin
vs_currencies: usd
HTTP 200
[Asserts]
jsonpath "$.bitcoin.usd" exists
