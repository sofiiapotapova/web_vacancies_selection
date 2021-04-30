from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
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


driver.close()
