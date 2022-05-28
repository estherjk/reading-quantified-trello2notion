import numpy as np
import pandas as pd

def main():
    df_trello = pd.read_csv('_data/trello.csv', index_col='Card ID')
    df_heroku = pd.read_csv('_data/heroku.csv', index_col='trello_id')

    # Join the two data frames based on the Trello card ID
    df_new = df_trello.join(df_heroku)

    # Keep only unarchived cards
    df_new = df_new[(df_new['Archived'] == False)]

    # Replace NaN with empty string
    df_new = df_new.replace(np.nan, '', regex=True)

    # Save to CSV...
    # Keep only a subset of columns; also exclude the index column
    df_new.filter(items=[
        'Card Name',
        'Labels',
        'Attachment Links',
        'List Name',
        'date_started',
        'date_finished',
        'created_at',
        'updated_at'
    ]).to_csv('output.csv', index=False)

if __name__ == '__main__':
    main()