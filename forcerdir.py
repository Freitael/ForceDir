import os
import requests
from concurrent.futures import ThreadPoolExecutor

print()
def banner():
        print("""███████╗ ██████╗ ██████╗  ██████╗███████╗██████╗ ██╗██████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗
█████╗  ██║   ██║██████╔╝██║     █████╗  ██║  ██║██║██████╔╝
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ██║  ██║██║██╔══██╗
██║     ╚██████╔╝██║  ██║╚██████╗███████╗██████╔╝██║██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝""")
banner()

print()

print('Por: https://github.com/Freitaszito')

print()

def check_url(base_url, word):
    url = f"{base_url}/{word}"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[+] Encontrado: {url} (Status: {response.status_code})")
        elif response.status_code == 301:
            print(f"[+] Redirecionado: {url} (Status: {response.status_code})")

    except requests.exceptions.RequestException:

        pass

def brute_force_directories(base_url, wordlist_path, threads=10):

    try:
        with open(wordlist_path, 'r') as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("Erro: O arquivo wordlist não foi encontrado.")
        return


    with ThreadPoolExecutor(max_workers=threads) as executor:
        for word in words:
            executor.submit(check_url, base_url, word)

if __name__ == "__main__":

    base_url = input("Digite a URL base (exemplo: http://example.com): ").strip()


    if not base_url.endswith("/"):
        base_url += "/"


    wordlist_path = input("Digite o caminho para o wordlist: ").strip()


    if not os.path.isfile(wordlist_path):
        print("Erro: O arquivo wordlist não existe ou o caminho está incorreto.")
    else:

        threads = input("Número de threads (recomenda-se 10 ou mais): ").strip()
        try:
            threads = int(threads)
        except ValueError:
            threads = 10


        brute_force_directories(base_url, wordlist_path, threads)
