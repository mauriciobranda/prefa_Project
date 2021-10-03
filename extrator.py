import requests, csv
from datetime import datetime
import utilities

paramMonth = 5
paramYear = 2021

#export to csv
with open('/Users/mauriciobrandalise/Projects/prefa/files_remunera/remunera_'+str (paramYear) + str(utilities.periodo(paramMonth, paramYear))+'.csv', 'w') as f:
#with open('D:/workspace/personal/dev/prefeitura_caxiasdosul/remunera_'+str (paramYear) + str (paramMonthStr)+'_parte2.csv', 'w') as f:
    theWriter = csv.writer(f)
    theWriter.writerow(['tipoRemuneracao','paramYear','paramMonthStr','periodoWorked','countFunc','id','nome','admissao','cargo','padrao_cargo','funcao_gratificada',
        'total_bruto','auxilio_alimentacao','auxilio_creche','antecipacao_ferias','indenizacoes_diversas','licenca_premio_compensada','descontos','redutor','total_liquido'])

    countFunc = 0
    while countFunc < utilities.totalFuncionarios(paramMonth, paramYear):
        # capturar o numero de registros atual
        URL_loop = 'https://remuneracoes.caxias.rs.gov.br/api/' + str (paramYear) + '/' + str(utilities.periodo(paramMonth, paramYear)) + '/01/' + str (
            utilities.tipoRemuneracao) + str (utilities.paramUrlLimit) + str (countFunc)
        people1 = requests.get (URL_loop)
        people_json1 = people1.json ()

        #declaro a lista que vai receber todos os registros vindos do endpoint
        lista_func = []

        #To print the names of people and folha com o total bruto
        for i in people_json1['response']['records']:
            lista_func.append(utilities.tipoRemuneracao)
            lista_func.append (paramYear)
            lista_func.append (str(utilities.periodo(paramMonth, paramYear)))
            lista_func.append ("10"+"/"+str(utilities.periodo(paramMonth, paramYear)+"/"+str(paramYear))) #primeiro dia do mes trabalhado
            lista_func.append (countFunc)
            lista_func.append (i['id'])
            lista_func.append (i['nome'])

            admissao = [i['admissao']]
            lista_func.append (admissao[:9])


            lista_func.append (i['cargo'])
            lista_func.append (i['padrao_cargo'])
            lista_func.append (i['funcao_gratificada'])
            #lista_func.append (i['tempo_servico'])
            total_bruto = [i['folha']['total_bruto']]

            lista_func.append (utilities.removebrack(total_bruto))

            auxilio_alimentacao = [i['folha']['auxilio_alimentacao']]
            lista_func.append (utilities.removebrack(auxilio_alimentacao))

            auxilio_creche = [i['folha']['auxilio_creche']]
            lista_func.append (utilities.removebrack(auxilio_creche))

            antecipacao_ferias = [i['folha']['antecipacao_ferias']]
            lista_func.append (utilities.removebrack(antecipacao_ferias))

            indenizacoes_diversas = [i['folha']['indenizacoes_diversas']]
            lista_func.append (utilities.removebrack(indenizacoes_diversas))

            licenca_premio_compensada = [i['folha']['licenca_premio_compensada']]
            lista_func.append (utilities.removebrack(licenca_premio_compensada))

            descontos = [i['folha']['descontos']]
            lista_func.append (utilities.removebrack(descontos))
          
            redutor = [i['folha']['redutor']]
            lista_func.append (utilities.removebrack(redutor))

            total_liquido = [i['folha']['total_liquido']]
            lista_func.append (utilities.removebrack(total_liquido))

            theWriter.writerow(lista_func)
            print (i['id']+" "+str(i['nome']))
            print ("---------------------")

        #decrease registros
            countFunc = countFunc + 1