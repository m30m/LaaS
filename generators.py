import random

usernames = [username.strip() for username in open('users.txt').readlines()]
SYMBOLS = '!@#$%^&*_+'
NUMS = '1234567890'
cities = {
    "Tehran": (35.670, 51.430),
    "Mashhad": (36.270, 59.570),
    "Esfahan": (32.680, 51.680),
    "Tabriz": (38.080, 46.300),
    "Shiraz": (29.630, 52.570),
    "Karaj": (35.800, 50.970),
    "Qom": (34.650, 50.950),
    "Ahvaz": (31.280, 48.720),
    "Kermanshah": (34.380, 47.060),
    "Zahedan": (29.500, 60.830),
    "Orumiyeh": (37.530, 45.000),
    "Kerman": (30.300, 57.080),
    "Yazd": (31.920, 54.370),
    "Rasht": (37.300, 49.630),
    "Arak": (34.080, 49.700),
    "Hamadan": (34.770, 48.580),
    "Ardabil": (38.250, 48.300),
    "Qazvin": (36.270, 50.000),
    "Abadan": (30.330, 48.280),
    "Sanandaj": (35.300, 47.020),
    "Zanjan": (36.670, 48.500),
    "Khorramabad": (33.480, 48.350),
    "Bandarabbas": (27.250, 56.250),
    "Eslamshahr": (35.540, 51.200),
    "Borujerd": (33.920, 48.800),
    "Gorgan": (36.830, 54.480),
    "Kashan": (33.980, 51.580),
    "Sabzevar": (36.220, 57.630),
    "Sari": (36.550, 53.100),
    "Neyshabur": (36.220, 58.820),
    "Najafabad": (32.670, 51.350),
    "Sirjan": (29.470, 55.730),
    "Khomeynishahr": (32.700, 51.470),
    "Khoy": (38.530, 44.970),
    "Dezful": (32.380, 48.470),
    "Amol": (36.430, 52.400),
    "Babol": (36.530, 52.700),
    "Bojnurd": (37.470, 57.320),
    "Birjand": (32.880, 59.220),
    "Qarchak": (35.420, 51.580),
    "Qa'emshahr": (36.470, 52.870),
    "Bushehr": (28.920, 50.830),
    "Qods": (35.730, 51.180),
    "Maragheh": (37.420, 46.220),
    "Malayer": (34.320, 48.850),
    "Bukan": (36.530, 46.200),
    "Saqqez": (36.230, 46.280),
    "Rafsanjan": (30.420, 56.020),
    "Gonbad-e qabus": (37.250, 55.170),
    "Zabol": (31.020, 61.480),
    "Mahabad": (36.770, 45.720),
    "Saveh": (35.020, 50.330),
    "Marv dasht": (29.800, 52.830),
    "Shahr-e kord": (32.320, 50.850),
    "Torbat-e heydariyeh": (35.280, 59.220),
    "Ilam": (33.630, 46.430),
    "Varamin": (35.320, 51.650),
    "Shahrud": (36.420, 54.970),
    "Bandar-e anzali": (37.470, 49.450),
    "Jahrom": (28.550, 53.570),
    "Marand": (38.430, 45.770),
    "Miandoab": (36.970, 46.100),
    "Quchan": (37.120, 58.500),
    "Do rud": (33.490, 49.050),
    "Akbarabad": (29.240, 52.770),
    "Semnan": (35.550, 53.380),
    "Masjed-e soleyman": (31.980, 49.300),
    "Iranshahr": (27.200, 60.700),
    "Fasa": (28.970, 53.680),
    "Kazerun": (29.600, 51.670),
    "Shahreza": (32.020, 51.870),
    "Malard": (35.670, 50.990),
    "Do gonbadan": (30.360, 50.780),
    "Bam": (29.080, 58.350),
    "Yasuj": (30.820, 51.680),
    "Shahinshahr": (32.810, 51.540),
    "Andimeshk": (33.450, 48.350),
    "Khorramshahr": (30.430, 48.180),
    "Mianeh": (37.330, 47.700),
    "Ahar": (38.470, 47.060),
    "Shirvan": (37.450, 57.920),
    "Kashmar": (35.180, 58.450),
    "Torbat-e jam": (35.220, 60.620),
    "Borazjan": (29.270, 51.200),
    "Kuhdasht": (33.530, 47.600),
    "Aligudarz": (33.370, 49.720),
    "Jiroft": (28.670, 57.730),
    "Behshahr": (36.720, 53.550),
    "Salmas": (38.180, 44.750),
    "Naqadeh": (36.950, 45.370),
    "Eslamabad": (34.320, 47.120),
    "Bandar-e mahshahr": (30.650, 49.220),
    "Behbahan": (30.580, 50.270),
    "Bonab": (37.330, 46.050),
    "Qorveh": (35.170, 47.800),
    "Abhar": (36.150, 49.220),
    "Marivan": (35.450, 46.200),
    "Parsabad": (39.650, 47.930),
    "Ezeh": (31.800, 49.900),
    "Takestan": (36.070, 49.700),
    "Alvand": (36.320, 49.160),
    "Nahavand": (34.200, 48.370),
    "Shushtar": (32.050, 48.830),
    "Ardakan": (32.320, 54.010),
    "Khuresgan": (32.650, 51.750),
    "Langarud": (37.180, 50.150),
    "Khomeyn": (33.630, 50.050),
    "Baneh": (35.980, 45.920),
    "Lar": (27.680, 54.280),
    "Golara": (32.630, 51.440),
    "Lahijan": (37.200, 50.000),
    "Firuzabad": (28.870, 52.600),
    "Abadeh": (31.180, 52.670),
    "Nurabad": (34.080, 47.970),
    "Darab": (28.750, 54.540),
    "Meshkinshahr": (38.380, 47.680),
    "Meybod": (32.230, 54.010),
    "Zarand": (30.800, 56.580),
    "Damghan": (36.170, 54.350),
    "Zarinshahr": (32.450, 51.590),
    "Pakdasht": (35.470, 51.700),
    "Bandar-e gonaveh": (29.570, 50.520),
    "Saravan": (27.400, 62.580),
    "Minab": (27.150, 57.070),
    "Borujan": (31.970, 51.290),
    "Esfarayen": (37.100, 57.500),
    "Harsin": (34.260, 47.600),
    "Bijar": (35.870, 47.600),
    "Takab": (36.410, 47.100),
    "Nurabad": (30.110, 51.530),
    "Asadabad": (34.790, 48.110),
    "Mobarakeh": (32.490, 51.660),
    "Khash": (28.220, 61.230),
    "Deh dasht": (30.790, 50.550),
    "Taybad": (34.740, 60.770),
    "Kamyaran": (34.800, 46.940),
    "Bandar-e emam khomeyni": (30.430, 49.080),
    "Kangavar": (34.500, 47.950),
    "Omidiyeh": (30.750, 49.710),
    "Bandar-e torkaman": (36.880, 54.070),
    "Rehnan": (32.690, 51.600),
    "Aliabad": (36.900, 54.870),
    "Chalus": (36.660, 51.410),
    "Neyriz": (29.200, 54.330),
    "Chabahar": (25.300, 60.630),
    "Shush": (32.190, 48.240),
    "Golpayegan": (33.450, 50.280),
    "Khorramdarreh": (36.200, 49.180),
    "Shahriyar": (35.660, 51.060),
    "Eqlid": (31.010, 52.710),
    "Fuladshahr": (32.430, 51.380),
    "Abyek": (36.050, 50.530),
    "Oshnaviyeh": (37.050, 45.100),
    "Shahr-e babak": (30.130, 55.150),
    "Babol sar": (36.710, 52.640),
    "Azna": (33.600, 48.960),
    "Sarab": (37.950, 47.570),
    "Khalkhal": (37.630, 48.520),
    "Piranshahr": (36.700, 45.130),
    "Chenaran": (36.650, 59.100),
    "Maku": (39.300, 44.500),
    "Robat karim": (35.480, 51.080),
    "Falavarjan": (32.570, 51.490),
    "Rudsar": (37.130, 50.300),
    "Tuysarkan": (34.550, 48.440),
    "Dargaz": (37.450, 59.100),
    "Talesh": (37.800, 48.920),
    "Azad shahr": (37.090, 55.160),
    "Astaneh-ye ashrafiyeh": (37.270, 49.980),
    "Neka": (36.660, 53.290),
    "Sonqor": (34.780, 47.600),
    "Nushahr": (36.650, 51.550),
    "Gonabad": (34.350, 58.680),
    "Mehriz": (31.580, 54.450),
    "Bafq": (31.580, 55.400),
    "Estehban": (29.120, 54.040),
    "Baft": (29.280, 56.600),
    "Sardasht": (36.150, 45.530),
}


def get_username():
    return random.choice(usernames)


def get_email(username):
    domains = ['@gmail.com', '@live.com', '@yahoo.com', '@ymail.com', '@outlook.com', '@mail.com']
    return username + random.choice(domains)


def get_year():
    return str(random.randint(1330, 1380))


def get_mobile():
    prefixes = []
    for i in range(10):
        prefixes.append('091' + str(i))
        prefixes.append('093' + str(i))
    return random.choice(prefixes) + ''.join([random.choice(NUMS) for i in range(7)])


def get_password(username):
    if random.random() < 0.5:
        y = get_year()
        return y + y + random.choice(SYMBOLS)
    else:
        if random.random() < 0.5:
            y = get_year()
            y_username = y + username
            if random.random() < 0.2:
                y_username = y_username.upper()
            return y_username
        else:
            return ''.join([random.choice(NUMS) for i in range(random.randint(8, 10))])


def digikala():
    username = get_username()
    return {
        'username': username,
        'password': get_password(username),
        'email': get_email(username),
        'credit': random.randint(0, 1000) * 1000,
        'purchases': random.randint(0, 100),
        'mobile': get_mobile()
    }


def cafe():
    username = get_username()
    return {
        'username': username,
        'password': get_password(username),
        'email': get_email(username),
        'credit': random.randint(0, 1000) * 1000,
        'installs': random.randint(0, 100),
        'subscriptions': random.randint(0, 10),
        'city': random.choice(list(cities.keys())),
        'mobile': get_mobile()
    }


def snapp():
    username = get_username()
    lat, long = random.choice(list(cities.values()))
    return {
        'username': username,
        'password': get_password(username),
        'email': get_email(username),
        'credit': random.randint(0, 100) * 1000,
        'trips': random.randint(0, 100),
        'snappboxes': random.randint(0, 10),
        'gender': random.choice(['M', 'F', '']),
        'avg_rating': random.random() * 5,
        'city': random.choice(list(cities.keys())),
        'mobile': get_mobile(),
        'lat': lat,
        'long': long,
        'has_tap30': random.choice([True, False])
    }


def tap30():
    username = get_username()
    lat, long = random.choice(list(cities.values()))
    return {
        'username': username,
        'password': get_password(username),
        'email': get_email(username),
        'credit': random.randint(0, 100) * 1000,
        'trips': random.randint(0, 100),
        'avg_rating': random.random() * 10,
        'city': random.choice(list(cities.keys())),
        'mobile': get_mobile(),
        'lat': lat,
        'long': long,
        'has_snapp': random.choice([True, False])
    }
