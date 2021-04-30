import requests


def get_vac(query, city=None):
    resp = requests.get(
        "https://api.rabota.ua/vacancy/search",
        params={"keyWords": query,
                "mode": "json",
                "cityId": 17
                }
    )
    vacancy_dict = {}
    result = []
    data = resp.json()
    doc = data['documents']
    for i in doc:
        result.append(
            {'name': i['name'], 'description': i['shortDescription'], 'city': i['cityName'], 'salary': i['salary'],
             'webSite': 'Rabota.ua'})

    return result
