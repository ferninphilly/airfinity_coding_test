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
    event_db = dataframe_dict.pop('event_db', 'missing')
    return dataframe_dict, event_db

#sanitize and get all columns looking the same
def matchall_columns(dataframe_dict, event_db):
    for key in dataframe_dict.keys():
        for name in dataframe_dict[key].columns:
            if "name" in name:
                dataframe_dict[key].rename(columns={name: "event_name"}, inplace=True)
            elif name != "event_twitter" and "twitter" in name:
                dataframe_dict[key].rename(columns={name: "person_twitter"}, inplace=True)
            elif "date" in name:
                dataframe_dict[key].rename(columns={name: "event_date"}, inplace=True)
    event_db.rename(columns={'twitter': "event_twitter"}, inplace=True)
    event_db.rename(columns={'date': 'event_date'}, inplace=True)
    event_db.rename(columns={'name': 'event_name'}, inplace=True)
    return dataframe_dict, event_db

#join the dataframes as appropriate
def events_join(dataframe_dict, event_db):
    joined_data = dict()
    for key in dataframe_dict.keys():
        index = set(dataframe_dict[key].columns).intersection(event_db.columns)
        df_up = dataframe_dict[key].set_index(list(index)).drop_duplicates()
        join_df = df_up.join(event_db.set_index(list(index)), how='outer')
        join_df = join_df.reset_index()
        if 'event_date' in join_df.columns:
            join_df['better_date'] = join_df['event_date'].dropna().apply(improve_date)
        joined_data[key] = join_df
    missing = [x for x in joined_data['alpha'].columns if x not in joined_data['beta'].columns]
    more = [x for x in joined_data['gamma'].columns if x not in joined_data['beta'].columns]
    missing_set = set(missing + more)
    full_join = joined_data['beta'].set_index('person_twitter').join(joined_data['gamma'].\
                        set_index('person_twitter')['site'])
    return full_join.reset_index().drop('event_month',1)

#Quick function to improve the date format for titles
def improve_date(bad_date):
    better_date = str(bad_date).split("/")
    better_date[0] = "0" + better_date[0] if len(better_date[0]) == 1 else better_date[0]
    better_date[1] = "0" + better_date[1] if len(better_date[1]) == 1 else better_date[1]
    better_date[2] = "20" + better_date[2] if len(better_date[2]) == 2 else better_date[2]
    return better_date[2] + better_date[0] + better_date[1]

#output to csvs
def output_events(join_df):
    join_df['event_and_date'] = join_df['event_name'] + "-" + join_df['better_date']
    for each in join_df['event_and_date'].dropna().unique():
        newdf = join_df.loc[join_df['event_and_date'] == each].drop_duplicates()
        newdf.to_csv(each + '.csv', index=False)

if __name__ == '__main__':
    file_lst = list_of_files()
    df_dict, event_db = create_dataframes(file_lst)
    cor_df_dict, cor_event_db = matchall_columns(df_dict, event_db)
    joined_df = events_join(cor_df_dict, cor_event_db)
    output_events(joined_df)
    
    
    
    
    

    
