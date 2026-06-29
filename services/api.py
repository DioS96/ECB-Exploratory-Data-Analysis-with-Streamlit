import requests

def ecb_api(
                 indicator="",
                 country="",
                 startperiod=None,
                 endperiod=None,
                 format="jsondata"):
    
    base_url="https://data-api.ecb.europa.eu/service/data"

    ecb_map = {
    "GDP": f"/MNA/Q.N.{country}.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.LR.N",

    "DEFICIT": f"/GFS/Q.N.{country}.W0.S13.S1._Z.B.B9._Z._Z._Z.XDC_R_B1GQ_CY._Z.S.V.CY._T",

    "HICP": f"/HICP/M.{country}.N.000000.4D0.ANR"
    }

    url=base_url+ecb_map[indicator]

    parameters={"format":format}

    if startperiod:
        parameters["startPeriod"]=startperiod
    if endperiod:
        parameters["endPeriod"]=endperiod

    try:
        response=requests.get(
            url=url,
            params=parameters
            )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e: 
        print(f"ECB API error:{e}")
        return None



