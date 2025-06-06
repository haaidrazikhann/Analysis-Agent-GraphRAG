from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from retrieve_data import llm

def analyze_data(data, user_query):
    prompt_template = """
    You are an AI assistant that helps analyze purchase behavior data and identify patterns.
    Here's a list of purchases made by different members:
    {data}

    The user wants to know: {user_query}

    Based on this data, provide insights and analysis relevant to the user's query.
    """

    formatted_data = "\n".join([f"Member {record['MemberID']} bought {record['ItemPurchased']} on {record['PurchaseDate']}" for record in data])

    # Set up the prompt and LLM
    prompt = PromptTemplate(input_variables=["data", "user_query"], template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)

    # Generate the analysis
    analysis = chain.run(data=formatted_data, user_query=user_query)
    return analysis