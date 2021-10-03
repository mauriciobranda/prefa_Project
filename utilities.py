import requests

tipoRemuneracao = 'mensal'
paramUrlLimit = '/?limit=1&offset=' #limite de 1 registro
paramOffset = 0 #o ideal seria capturar o total de registros no records

def periodo(paramMonth, paramYear):
    if paramMonth < 10:
        paramMonthStr = str (paramMonth)
        paramMonthStr = paramMonthStr.zfill (2) #completa com zero
    else:
        paramMonthStr = str (paramMonth)

    return paramMonthStr

#funcao para remover os brackets 
def removebrack(valor):
   var_rem = (str(valor).replace('[','').replace(']',''))
   return var_rem

def totalFuncionarios (paramMonth, paramYear):
    
    URL = 'https://remuneracoes.caxias.rs.gov.br/api/'+str(paramYear)+'/'+periodo(paramMonth, paramYear)+'/01/'+str(tipoRemuneracao)+str(paramUrlLimit)+str(paramOffset)

    people1 = requests.get(URL)
    people_json1  = people1.json()
    totalFuncionarios = people_json1['response']['total']

    return totalFuncionarios