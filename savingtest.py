# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd

df = pd.read_excel('20rows.xlsx')
dfout = df

#make the dataframe index equal to the specimen ID so that
#changes can be made by refering to specimen number rather than dataframe row number
df.index = df["Specimen"]
dfout.index = dfout["Specimen"]

#add columns for choice of lat/long
dfout['SelectLat'] = 0
dfout['SelectLong'] = 0

#Prove that index is now specimen ID.
#distance = dfout["distance"]
#distance

#show selected values for specimen ID = 472 only
print(df.loc[472, 'ApLat'], df.loc[472, 'ApLong'])

#dfout

#dfout['distance']


# +
#choices will be either g, o, d, or u (GeoApp, Original, Decide later, or Unknown (i.e. 0))
choice = 'g'
specimen = 472

if choice == "g":
    dfout.loc[specimen, 'SelectLat'] = df.loc[specimen, 'ApLat']
    dfout.loc[specimen, 'SelectLong'] = df.loc[specimen, 'ApLong']
elif choice == "o":
    dfout.loc[specimen, 'SelectLat'] = df.loc[specimen, 'OrigLat']
    dfout.loc[specimen, 'SelectLong'] = df.loc[specimen, 'OrigLong']
elif choice == "d":
    dfout.loc[specimen, 'SelectLat'] = "decide later"
    dfout.loc[specimen, 'SelectLong'] = "decide later"
elif choice == "u":
    dfout.loc[specimen, 'SelectLat'] = 0.0
    dfout.loc[specimen, 'SelectLong'] = 0.0

    
print(dfout.loc[specimen, 'SelectLat'], dfout.loc[specimen, 'SelectLong'])
# -

#save resulting dataframe 
outf = open("ChosenGeolocns.xlsx", "w", encoding="utf-16") #re-write, NOT appending.
dfout.to_excel("ChosenGeolocns.xlsx")
outf.close()

# --------
# sources:
#
# * https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
# * https://www.dataquest.io/cheat-sheet/pandas-cheat-sheet/
