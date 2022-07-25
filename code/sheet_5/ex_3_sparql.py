from rdflib import Graph

g = Graph()
g.parse("sheet_5/exercise3.ttl")

father_of_alan = """
ASK {
    <http://ifisexamples.com/Alan_Turing> rel:childOf <http://ifisexamples.com/Julius_Turing> .
}"""

grandchildren = """
SELECT DISTINCT ?a
WHERE{
    ?a rel:childOf/rel:childOf <http://ifisexamples.com/Ethel_Turing> .
}"""

born_before_1880 = """
SELECT DISTINCT ?a
WHERE{
    ?a rel:birthYear ?birthYear .
    FILTER(?birthYear < 1880)
}"""

qres_a = g.query(father_of_alan)
for stmt in qres_a:
    print(stmt)

qres_b = g.query(grandchildren)
for stmt in qres_b:
    print(stmt)


qres_c = g.query(born_before_1880)
for stmt in qres_c:
    print(stmt)