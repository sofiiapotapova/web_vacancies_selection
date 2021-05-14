import requests


def get_vac(query, city=None):
    """!@brief Gets vacancy info from rabota.ua

    Gets vacancy info by using API for rabota.ua by searching by key words
    and city code. Collects the result into list of dictionaries.

    @param resp The response of rabota.ua
    @param result The result list of dictionaries
    """
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
