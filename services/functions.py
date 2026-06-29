import pandas as pd



def clean_df(dataframe,indicator):

    dataframe["year"]=dataframe["period"].str.split("-").str[0].astype(str)

    if indicator=="HICP":

        dataframe["month"]=dataframe["period"].str.split("-").str[1].astype(int)
        dataframe.drop('period',axis=1,inplace=True)
        dataframe["quartal"] = pd.cut(
        dataframe["month"],
        bins=[0, 3, 6, 9, 12],
        labels=["Q1", "Q2", "Q3", "Q4"]
        ).astype(str)
        dataframe["period"]=dataframe["year"].astype(str)+"-"+dataframe["quartal"].astype(str)
    
    else:

        dataframe["quartal"]=dataframe["period"].str.split("-").str[1].astype(str)
    
    return dataframe



def join_df(df_list,join_how,primary_key):

    if len(df_list) < 2:
        raise ValueError(
            "At least two DataFrames are required."
        )

    merged_df=df_list[0]

    for df in df_list[1:]:
        
        merged_df=pd.merge(merged_df,
                           df,
                           how=join_how,
                           on=primary_key)
    
    return merged_df



def groupby_df(dataframe,groupby_column,value_column,aggregation_value):

    dataframe=dataframe.groupby(groupby_column, as_index= False).agg(
        {value_column:aggregation_value}
    )

    return dataframe


def growth_rate(dataframe,column,periods):

    dataframe[f"{column}_growth"]=dataframe[column].pct_change(periods)*100

    return dataframe
