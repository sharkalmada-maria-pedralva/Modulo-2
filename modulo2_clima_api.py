from requests import get
from json import loads

api = "6e175c0971b04da5a27132533252506"
local = input("Escolha um distrito ou estado para ver a temperatura atual \n>")

url = f"https://api.weatherapi.com/v1/current.json?key={api}&q={local}&lang=pt"

try:
    response = get(url)
    download = True
except:
    download = False

if download and response.ok:
    data = loads(response.text)
    country = data.get("location", {}).get("country")
    temperatura = data.get("current", {}).get("temp_c")
    estado_do_ceu = data.get("current", {}).get("condition", {}).get("text")
    ultimo_update = data.get("location", {}).get("localtime")

    print(f"Estado do tempo em {local},", country)
    print(f"{temperatura: .1f} ºC")
    print(estado_do_ceu)
    print(f"Data e hora: {ultimo_update}")

else:
    print(f"Erro em {local}, tente novamente" )


