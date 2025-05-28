from .extract.extract import extract
from .transform.transform import transform
from .load.load import load
import json
import os


if __name__ == "__main__":
    print("Executando o processo ETL...")
    raw_data = extract()
    updated_data = transform(raw_data=raw_data)
    load(updated_data=updated_data)
    print("Processo ETL concluído.")

    utils_path = os.path.join(os.path.dirname(
        __file__), 'utils', 'btc_coinbase_api.json')
    with open(utils_path, 'r') as f:
        dados_extraidos = json.load(f)
    try:
        quantidade_de_itens = len(dados_extraidos['_default'])
        print(f"O número total de itens anexados é: {quantidade_de_itens}")
    except KeyError:
        print("A chave '_default' não foi encontrada no JSON.")
    except TypeError:
        print("O conteúdo do JSON não é um dicionário ou está mal formatado.")
