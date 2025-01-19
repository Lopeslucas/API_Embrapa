# api/importacao.py
from app.services.services import get_data_for_category

def handler(request):
    try:
        data = get_data_for_category('importacao')
        return {
            "statusCode": 200,
            "body": data
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Erro ao processar o arquivo: {str(e)}"
        }
