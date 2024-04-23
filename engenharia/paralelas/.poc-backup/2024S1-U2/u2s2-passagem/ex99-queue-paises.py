import requests
import json
from multiprocessing import Process, Queue

# Função para buscar os países que começam com A, B e C
def get_countries():
    print("Buscando países...")
    response = requests.get("https://restcountries.com/v3.1/all?fields=name")
    data = response.json()
    
    countries = [country['name']['common'] for country in data if country['name']['common'][0] in ['A', 'B', 'C']]
    
    countries_a = [country for country in countries if country[0] == 'A']
    countries_b = [country for country in countries if country[0] == 'B']
    countries_c = [country for country in countries if country[0] == 'C']
    
    return countries_a, countries_b, countries_c

# Função para processar uma lista de países
def get_official_name(country_list, result_queue):
    for country in country_list:
        print(f"Buscando nome oficial de {country}...")
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()
        official_name = data[0]['name']['official']
        result_queue.put({country: official_name})

if __name__ == "__main__":
    # Busca os países com nomes comuns que começam com A, B e C
    countries_a, countries_b, countries_c = get_countries()
    
    queue = Queue()
    
    processes = []
    
    # Cria um processo para buscar o nome oficial de cada país em paralelo
    for country_list in [countries_a, countries_b, countries_c]:
        process = Process(target=get_official_name, args=(country_list, queue))
        processes.append(process)
        process.start()
    
    # Espera todos os processos serem finalizados
    for process in processes:
        process.join()
    
    print("\nNomes oficiais dos países encontrados:")
    # Exibe o resultado da busca do nome oficial de cada país
    while not queue.empty():
        result = queue.get()
        for country, official_name in result.items():
            print(f"{country}: {official_name}")