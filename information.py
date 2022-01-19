import pandas as pd
import json

def extract(guildname):
    filename = 'data.csv'
    df = pd.read_csv(filename)

    # Refresh the dataset
    initial = {}

    with open(f'{guildname}Data.json', 'w') as jsonFile:
        json.dump(initial, jsonFile, indent=4)

    # Open file as source
    f = open(f'{guildname}Data.json')
    data = json.load(f)

    # Defining Suffix
    suffix = '>'

    # Function to count
    def count(receiver, sender):
        if sender in data:
            # True
            if receiver in data[sender][0]:
                data[sender][0][receiver] += 1
            else:
                data[sender][0][receiver] = 1
        else:
            # False
            data[sender] = [{}]
            data[sender][0][receiver] = 1

    # Read second column Pandas
    for i in range(len(df)):
        j = df.iloc[i][1].split()
        for k in j:
            if k.startswith("<@!"):
                line_new = k[3:]
                # line_new = line_new[:-len(suffix)]
                line_new = line_new[:18]
                # line_new = str(line_new)
                authorTemp = str(df.iloc[i][3])
                count(line_new, authorTemp)
            elif k.startswith("<@&"):
                line_new = k[3:]
                line_new = line_new[:18]
                # line_new = line_new[:-len(suffix)]
                # line_new = str(line_new)
                authorTemp = str(df.iloc[i][3])
                count(line_new, authorTemp)
            elif k.startswith("<@"):
                line_new = k[2:]
                line_new = line_new[:18]
                # line_new = line_new[:-len(suffix)]
                # line_new = str(line_new)
                authorTemp = str(df.iloc[i][3])
                count(line_new, authorTemp)
            else:
                pass

    # Over write the data here
    with open(f'{guildname}Data.json', 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

    f.close()