__author__ = 'zhanyang'


def normalizeCarInfo(features):
    gearbox = int(features["gearbox_type"]) - 1
    use_type = int(features["use_type"])
    is_local = int(features["is_local"]) - 1
    seat_num = int(features["seat_num"]) / 8
    seat_type = 0 if int(features["seat_type"]) == 1 else 1
    gas_type = int(features["gas_type"])
    skylights_type = int(features["skylights_type"])
    gouche_year = (int(features["gouche_year"]) - 1996) / 18
    city = int(features["city"])
    displacement = (int(features["displacement"]) - 1) / 5
    color = int(features["color"])
    mileage = (int(features["mileage"]) - 1) / 4
    price = int(features["day_price"])
    if price <= 100:
        day_price = 0
    elif price <= 150:
        day_price = 0.166
    elif price <= 200:
        day_price = 0.333
    elif price <= 300:
        day_price = 0.5
    elif price <= 500:
        day_price = 0.667
    elif price <= 1000:
        day_price = 0.833
    else:
        day_price = 1
    return [gearbox, use_type, is_local, seat_num, seat_type, gas_type, skylights_type, gouche_year, city,
            displacement, color, mileage, day_price]


