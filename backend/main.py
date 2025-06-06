from retrieve_data import retrieve_data
from analyze_data import analyze_data
from retrieve_data import driver

def main():
    data = retrieve_data()

    user_query = input(">> ")
    analysis = analyze_data(data, user_query)
    return analysis

if __name__=="__main__":
    main()
    
driver.close()