import json

usa_states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HA',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Rhode Island': 'RI',
    'Pennsylvania': 'PA',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'District of Columbia': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

canada_states = {
    'Alberta': 'AB',
    'British Columbia': 'BC',
    'Manitoba': 'MB',
    'New Brunswick': 'NB',
    'Newfoundland and Labrador': 'NL',
    'Nova Scotia': 'NS',
    'Ontario': 'ON',
    'Prince Edward Island': 'PE',
    'Quebec': 'QC',
    'Saskatchewan': 'SK',
}

countries = [
    'Australia',
    'Austria',
    'Belarus',
    'Belgium',
    'Brazil',
    'Canada',
    'Chile',
    'Croatia',
    'Czech Republic',
    'Denmark',
    'England',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Hungary',
    'Iceland',
    'Ireland',
    'Italy',
    'Japan',
    'Lithuania',
    'Mexico',
    'Netherlands',
    'New Zealand',
    'Norway',
    'Online',
    'Philippines',
    'Poland',
    'Portugal',
    'Russia',
    'Scotland',
    'Serbia',
    'Singapore',
    'Slovakia',
    'South Africa',
    'Spain',
    'Sweden',
    'Switzerland',
    'USA',
    'United Kingdom',
    'Wales',
]

country_aliases = {
    'United States': 'USA',
    'Slovak Republic': 'Slovakia',
    'South Australia': 'Australia',
    'Russian Federation': 'Russia',
    'Belorussia': 'Belarus',
    'Online -- Lackey': 'Online',
}

fixes = {
    'D.C.': {
        'Washington': ['Washington (DC)', 'USA'],
    },
    'Victoria': {
        'Melbourne': ['Melbourne', 'Australia'],
    },
    'Modena': {
        'Italy': ['Modena', 'Italy'],
    },
    'United Kingdom': {
        'Leeds': ['Leeds', 'England'],
        'Liverpool': ['Liverpool', 'England'],
        'Newcastle Upon Tyne': ['Newcastle upon Tyne', 'England'],
    },
    'Philadelphia': ['Philadelphia (PA)', 'USA'],
}

cities_fixes = {
    'Bad Naumheim': 'Bad Nauheim',
    'Bad\u00eda del Vall\u00e9s': 'Badia del Vallès',
    'Badia del Vall\u00e8s': 'Badia del Vallès',
    'Bailleau le Pin': 'Bailleau-le-Pin',
    'Barceloma': 'Barcelona',
    'Bourg La Reine': 'Bourg-la-Reine',
    'Bourg la Reine': 'Bourg-la-Reine',
    'Bruxelles': 'Brussels',
    'Burton on Trent': 'Burton upon Trent',
    'Burton-on-Trent': 'Burton upon Trent',
    'Bystricka': 'Bystrička',
    'Cincinatti (OH)': 'Cincinnati (OH)',
    'Columbus Convention Centre (OH)': 'Columbus (OH)',
    'Duboicze Cerkiewne': 'Dubicze Cerkiewne',
    'Espoo (Helsinki)': 'Espoo',
    'Gatineau': 'Gatineau (QC)',
    'Gen\u00e8ve': 'Geneva',
    'Genova': 'Genoa',
    'Goteborg': 'Gothenburg',
    'Hradec Kr\u00e1lov\u00e9': 'Hradec Králové',
    'Hradec Kralove': 'Hradec Králové',
    'Katalinpuszta-Szendehely': 'Katalinpuszta',
    'Kecskemet': 'Kecskemét',
    'Lisboa': 'Lisbon',
    'Massa Carrara': 'Massa',
    'Matar\u00f3': 'Mataró',
    'Mataro': 'Mataró',
    'Milano': 'Milan',
    'Moskow': 'Moscow',
    'Newcastle (New South Wales)': 'Newcastle',
    'Palma de Malloca': 'Palma de Mallorca',
    'Palma de Malorca': 'Palma de Mallorca',
    'Pozna\u0144': 'Poznań',
    'Poznan': 'Poznań',
    'Praha': 'Prague',
    'S\u00e3o Paulo': 'São Paulo',
    'Sa\u00f5 Paulo': 'São Paulo',
    'Toluca de Lerdo': 'Toluca',
    'Veszpr\u00e9m': 'Veszprém',
    'Veszprem': 'Veszprém',
    'Warszawa': 'Warsaw',
    'Wheatridge (CO)': 'Wheat Ridge (CO)',
}


with open("twda.json", "r") as twda_file, open("locations.json", "w") as locations_file:
    twda = json.load(twda_file)

    for deck in twda:
        location = deck['place'].split(', ')
        country = location[-1]
        city = location[-2] if len(location) > 1 else None
        other = location[-3] if len(location) > 2 else None

        if country in usa_states.keys():
            state = country
            city = f"{city} ({usa_states[state]})"
            country = 'USA'
        elif country in canada_states.keys():
            state = country
            city = f"{city} ({canada_states[state]})"
            country = 'Canada'
        elif country in country_aliases.keys():
            country = country_aliases[country]
        elif country in fixes.keys():
            if city:
                [city, country] = fixes[country][city]
            else:
                [city, country] = fixes[country]
        elif country not in countries:
            print('WARNING! COUNTRY NOT IN LIST:', deck['id'], deck['place'])

        if city in cities_fixes.keys():
            city = cities_fixes[city]

        place = f""
        if other:
            place += f"{other}, "
        if city:
            place += f"{city}, "

        place += f"{country}\n"

        with open(f"decks/{deck['id']}.txt", "r") as input_file, open(f"decks_fixed/{deck['id']}.txt", "w") as output_file:
            data = input_file.readlines()
            data[1] = place
            output_file.writelines(data)
