from api import ecb_api_gov_surplus_or_deficit

response=ecb_api_gov_surplus_or_deficit(freq="Q",country="GR",startperiod="01.01.2015", endperiod="01.01.2025")

print(type(response))