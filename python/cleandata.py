import pandas as pd
import numpy as np

# Add partei_clean
def transform_partei(p):

    if type(p) == str:
        p = p.lower()

    if p == 'die mitte': p = 'cvp'

    if p in ['parteilos', 'fdp', 'evp', 'svp', 'sp', 'cvp', 'glp', 'grüne', 'bdp', 'al', 'edu']:
        return p
    return 'verschiedene'

def clean(df):
    # Transform data
    df.loc[df.partei_nicht_zugeordnet == 1, 'partei_nicht_zugeordnet'] = True
    df['partei_nicht_zugeordnet'] = df['partei_nicht_zugeordnet'].fillna(False)

    df.loc[df.jahrgang_nicht_zugeordnet == 1, 'jahrgang_nicht_zugeordnet'] = True
    df['jahrgang_nicht_zugeordnet'] = df['jahrgang_nicht_zugeordnet'].fillna(False)

    # Alter berechnen
    df['Alter'] = 2021 - df['Jahrgang']

    print("Jahrgänge nicht zugeordnet: %s" % len(df[df.jahrgang_nicht_zugeordnet == True]))
    print("Partei nicht zugeordnet: %s" % len(df[df.partei_nicht_zugeordnet == True]))
    print("Keine Jahrgänge: %s" % len(df[df.Jahrgang.isna()]))
    
    # Clean Party
    df['partei_c'] = df['Partei'].apply(transform_partei)
    df.loc[df.Name.str.lower() == 'vakant', 'partei_c'] = 'vacant'
    
    return df

def stadt_land(df):
    # Define which ones are cities (not Gemeinden)
    stadtrat = ['Adliswil', 'Affoltern am Albis', 'Bülach', 'Dietikon', 'Dübendorf', 'Illnau-Effretikon', 'Kloten', 'Opfikon', 'Schlieren', 'Uster', 'Wädenswil', 'Wetzikon', 'Winterthur', 'Zürich']

    df['type'] = 'land'
    df.loc[df.Gemeinde.isin(stadtrat), 'type'] = 'stadt'
    return df

def add_bfs(df):
    df_bfs = pd.read_csv('../data/bfs_name.csv', sep=';')

    df_bfs.rename(columns={'BFS': 'bfs'}, inplace=True)

    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.strip()

    # Clean Names
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('a.A.', 'am Albis', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('a.I.', 'am Irchel', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('a.d.Th.', 'an der Thur', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('a.S.', 'am See', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('a.d.L.', 'an der Limmat', regex=False)

    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Zell', 'Zell (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Schlatt', 'Schlatt (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Rüti', 'Rüti (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Wald', 'Wald (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Wetzikon', 'Wetzikon (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Kilchberg', 'Kilchberg (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Erlenbach', 'Erlenbach (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Gossau', 'Gossau (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Rickenbach', 'Rickenbach (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Weiningen', 'Weiningen (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Birmensdorf', 'Birmensdorf (ZH)', regex=False)
    df_bfs.loc[df_bfs.Gemeinden == 'Wil', 'Gemeinden'] = 'Wil (ZH)'
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Buchs', 'Buchs (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Benken', 'Benken (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Küsnacht', 'Küsnacht (ZH)', regex=False)
    df_bfs['Gemeinden'] = df_bfs['Gemeinden'].str.replace('Aesch', 'Aesch (ZH)', regex=False)

    df = df.merge(df_bfs, how='left', left_on = 'Gemeinde', right_on='Gemeinden')
    df.drop(columns='Gemeinden', inplace=True)

    return df

