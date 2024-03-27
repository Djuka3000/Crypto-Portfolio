import requests

class CoinGeckoAPIWrapper():
    def __init__(self,API_KEY_COINGECKO): 
        self.API_KEY_COINGECKO = API_KEY_COINGECKO #API key nije neophodan program radi i ako se ukloni &x_cg_demo_api_key={self.API_KEY_COINGECKO} ali onda nije konzistentan umjesto float ili int izbacuje ponekad nonetype
  
    def get_token_id(self,name):
        url = f"https://api.coingecko.com/api/v3/search?query={name}"
        response = requests.get(url)
        data = response.json()
        if data and 'coins' in data and data['coins']:
            return data['coins'][0]['id']
        else:
            return None

    def get_token_price(self,name):
     
        token_id=self.get_token_id(name)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd&x_cg_demo_api_key={self.API_KEY_COINGECKO}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if token_id in data:
                return data[token_id]['usd']
            else:
                return None
        else:
            print('Error:', response.status_code)
            return None