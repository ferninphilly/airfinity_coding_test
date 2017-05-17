#!/usr/bin/env python3

import csv
import pandas as pd
import glob, os

#Get a list of all csvs in the directory
def list_of_files():
    return glob.glob("DataEngineeringExercise/*.csv")

#Put them into dataframes by appropriate names
def create_dataframes(file_lst):
    dataframe_dict = dict()
    for file in file_lst:
        exten = os.path.basename(file)
        dataframe_dict[os.path.splitext(exten)[0]] = pd.read_csv(file)
    return dataframe_dict

#question: count by event
def events_join(dataframe_dict):
    alpha_event_df = dataframe_dict['alpha'].set_index('eventname').\
                    join(dataframe_dict['event_db'].set_index('name'), how='outer').\
                    drop_duplicates().reset_index()
    beta_event_df = dataframe_dict['beta'].set_index('event_twitter').\
                    join(dataframe_dict['event_db'].set_index('twitter')).\
                    drop_duplicates().reset_index()
    gamma_event_df = dataframe_dict['gamma'].set_index('event_twitter').\
                     join(dataframe_dict['event_db'].set_index('twitter')).\
                    drop_duplicates().reset_index()
    return alpha_event_df, beta_event_df, gamma_event_df

def improve_date(bad_date):
    better_date = str(bad_date).split("/")
    better_date[0] = "0" + better_date[0] if len(better_date[0]) == 1 else better_date[0]
    better_date[1] = "0" + better_date[1] if len(better_date[1]) == 1 else better_date[1]
    return better_date[2] + better_date[0] + better_date[1]

def output_events(dataframe_tuple):
    alpha, beta, gamma = datframe_tuple
    alpha['better_date'] = alpha['date'].dropna().apply(improve_date)
    alpha['event_and_date'] = alpha['index'] + "-" + alpha['better_date']
    for each in alpha['event_and_date'].dropna().unique():
        newdf = alpha.loc[alpha['event_and_date'] == each]
        newdf.to_csv(each + '.csv', index=False)
    #Make separate dataframes
    
    

    pass
