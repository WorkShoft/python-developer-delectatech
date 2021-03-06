SINGLE_QUERY_RESULT = {
    "name": "Empanadas Malvon",
    "street_address": "Calle de Sant Vicent Màrtir",
    "latitude": 39.467078,
    "longitude": -0.3809601,
    "city_name": "Valencia",
    "popularity_rate": 7.49,
    "satisfaction_rate": 8.55,
    "total_reviews": 139,
    "uidentifier": "09bf3785-283b-41c4-9bc3-8a4a97dcf614",
    "average_price": 40.0,
}

MANY_QUERY_RESULT = [
    {
        "name": "FANTASTIC V",
        "street_address": "Corredera Alta de San Pablo",
        "latitude": 40.4244549,
        "longitude": -3.7020316,
        "city_name": "Madrid",
        "popularity_rate": 7.05,
        "satisfaction_rate": 8.89,
        "total_reviews": 107,
        "uidentifier": "b7bac5ea-4e36-467a-b8de-9095dd0f08b8",
        "average_price": 10.0,
    },
    {
        "name": "Empanadas Malvon",
        "street_address": "Calle de Sant Vicent Màrtir",
        "latitude": 39.467078,
        "longitude": -0.3809601,
        "city_name": "Valencia",
        "popularity_rate": 7.49,
        "satisfaction_rate": 8.55,
        "total_reviews": 139,
        "uidentifier": "09bf3785-283b-41c4-9bc3-8a4a97dcf614",
        "average_price": 40.0,
    },
    {
        "name": "La Fonda del Port Olímpic",
        "street_address": "Moll de Gregal 8, 9",
        "latitude": 41.3886556,
        "longitude": 2.2007284,
        "city_name": "Barcelona",
        "popularity_rate": 8.04,
        "satisfaction_rate": 8.3,
        "total_reviews": 110,
        "uidentifier": "a23d43a0-7004-4703-991d-864a3502f1b7",
        "average_price": 30.0,
    },
    {
        "name": "Restaurante Italiano Rossini",
        "street_address": "Plaza Reial",
        "latitude": 41.379963,
        "longitude": 2.175821,
        "city_name": "Barcelona",
        "popularity_rate": 7.97,
        "satisfaction_rate": 8.69,
        "total_reviews": 145,
        "uidentifier": "0be2771f-1dfe-44a1-b778-4a79b5552d34",
        "average_price": 35.4,
    },
    {
        "name": "La Choza de Manuela",
        "street_address": "Calle Menendez Pidal",
        "latitude": 37.3666667,
        "longitude": -6.0856732,
        "city_name": "Bormujos",
        "popularity_rate": 7.8,
        "satisfaction_rate": 8.33,
        "total_reviews": 122,
        "uidentifier": "364cbd2d-b2d7-431f-9151-87a003379d5f",
        "average_price": 43.95,
    },
]

VERY_SMALL_SEGMENT = {
    "name": "Small Segment",
    "uidentifier": "e12345df-e471-4f66-85af-2bacfd9d2e65",
}

PARAMS = {
    "popularity_rate": {"gt": 5.5},
    "satisfaction_rate": {"ne": None},
}
