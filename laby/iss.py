import requests
import plotly.express as px

if __name__ == '__main__':
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    print(data["iss_position"])

    fig = px.scatter_map(lat=[float(data["iss_position"]["latitude"])], lon=[float(data["iss_position"]["longitude"])])
    fig.show()