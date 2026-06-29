from .api import ecb_api
import pandas as pd

def api_to_PandasDataframe(indicator,country,startperiod=None,endperiod=None):

    """
    Fetches ECB Government Surplus/Deficit data
    and returns a pandas DataFrame.
    """

    response =ecb_api(indicator=indicator,country=country,startperiod=startperiod,endperiod=endperiod)

    if response is None:
        print("response from API call is None. Please check the API function.")
        return pd.DataFrame()

    series_key=next(iter(response["dataSets"][0]["series"]))
    observations=response["dataSets"][0]["series"][series_key]['observations']

    dates=response["structure"]["dimensions"]["observation"][0]['values']
    periods_metadata=[date['id'] for date in dates]
    obs_values=[observation[0] for observation in observations.values()]

    df=pd.DataFrame(
        {
            "period":periods_metadata,
            indicator:obs_values
        }
    )

    return df

