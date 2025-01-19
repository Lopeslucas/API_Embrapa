from app.services import get_data_for_category

def handler(request):
    try:
        # Aqui, 'producao' seria o parâmetro passado para a função
        data = get_data_for_category('producao')

        # Retorne a resposta no formato esperado pelo Vercel
        return {
            "statusCode": 200,
            "body": data
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Erro ao processar o arquivo: {str(e)}"
        }
