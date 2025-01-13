from neo4j import GraphDatabase
import csv
from google.colab import userdata
import pandas as pd

# Neo4j connection settings
URI = userdata.get("NEO4J_URI")
USERNAME = userdata.get("NEO4J_USERNAME")
PASSWORD = userdata.get("NEO4J_PASSWORD")

CSV_FILE = "data.csv"

# Neo4j driver setup
driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

df = pd.read_csv(CSV_FILE)

def insert_data(session, member_number, date, item_purchased):
    query = """
    MERGE (m:Member {id: $member_number})
    MERGE (i:Item {name: $item_purchased})
    CREATE (m)-[:PURCHASED {date: $date}]->(i)
    """
    session.run(query, member_number=member_number, date=date, item_purchased=item_purchased)

# Inserting data from DataFrame into Neo4j
with driver.session() as session:
    for index, row in df.iterrows():
        insert_data(session, row['Member_number'], row['Date'], row['itemDescription'])

# Close the driver
driver.close()
