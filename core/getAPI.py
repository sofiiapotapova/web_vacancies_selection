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
             'webSite': 'Work.ua'})
        # vacancy_dict['name'] = i['name']
        # vacancy_dict['description'] = i['shortDescription']
        # vacancy_dict['city'] = i['cityName']
        # vacancy_dict['salary'] = i['salary']
        # vacancy_dict['webSite'] = 'Work.ua'
        # print(vacancy_dict)
        # result.append(vacancy_dict)
    return result
