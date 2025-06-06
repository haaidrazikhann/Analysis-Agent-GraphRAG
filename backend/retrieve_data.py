from langchain_groq import ChatGroq
from neo4j import GraphDatabase
import os

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
groq_api_key= os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0.7, api_key=groq_api_key,model="llama3-8b-8192")

# Neo4j driver setup
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def retrieve_data():
    query = """
    MATCH (m:Member)-[r:PURCHASED]->(i:Item)
    RETURN m.id AS MemberID, i.name AS ItemPurchased, r.date AS PurchaseDate
    """

    with driver.session() as session:
        result = session.run(query)
        data = [{"MemberID": record["MemberID"], "ItemPurchased": record["ItemPurchased"], "PurchaseDate": record["PurchaseDate"]} for record in result]

    return data