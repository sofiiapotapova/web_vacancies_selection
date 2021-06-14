from neo4j import GraphDatabase
from .models import Competence

uri = "neo4j://localhost:11003"
driver = GraphDatabase.driver(uri, auth=("sofiiapotapova", "1234"))


def create_vacancy(tx, vac_name):
    tx.run("CREATE (n:NeoVacancy {name: $name})", name=vac_name)


def create_competence(tx, com_name):
    tx.run("CREATE (n:NeoCompetence {name: $name_competence})", name_competence=com_name)


def create_requirement(tx, vac_name, com_name):
    tx.run("MATCH (a:NeoVacancy) WHERE a.name = $name "
           "CREATE (a)-[:REQUIRES]->(:NeoCompetence {name: $name_competence})",
           name=vac_name, name_competence=com_name)


def graph_add(info):
    with driver.session() as session:
        session.write_transaction(create_vacancy, info['vac_name'])
        for competence in info['com_name']:
            # session.write_transaction(create_competence, competence)
            session.write_transaction(create_requirement, info["vac_name"], competence)


def get_percent(comp_list_filter, comp_num, vacancy):
    coincidence = 0
    percent = 0
    level = 0
    vac_competencies = []
    with driver.session() as session:
        result = session.run("MATCH (:NeoVacancy {name: $vacancy})-[:REQUIRES]->(competence:NeoCompetence) RETURN "
                             "competence.name AS comp", vacancy = vacancy)
        for record in result:
            vac_competencies.append(record['comp'])

        for comp in comp_list_filter:
            if comp[0] in vac_competencies:
                coincidence = coincidence + 1
                level = level + comp[1]
        if coincidence == 0:
            return None
        else:
            coef = (level/coincidence)/100
            percent = coincidence/comp_num
            result = coef + percent
            per = round(result, 2)
            return per*100


driver.close()
