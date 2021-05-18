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
    
    return df