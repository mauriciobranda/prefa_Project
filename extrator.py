import requests, csv
from datetime import datetime

#Qual o mes que voce quer ?
paramMonth = 5
#e de qual ano ?
paramYear = 2021

if paramMonth < 10:
    paramMonthStr = str (paramMonth)
    paramMonthStr = paramMonthStr.zfill (2) #completa com zero
else:
    paramMonthStr = str (paramMonth)


tipoRemuneracao = 'mensal'
paramUrlLimit = '/?limit=1&offset=' #limite de 1 registro
paramOffset = 0 #o ideal seria capturar o total de registros no records

#capturar o numero de registros atual
URL = 'https://remuneracoes.caxias.rs.gov.br/api/'+str(paramYear)+'/'+str(paramMonthStr)+'/01/'+str(tipoRemuneracao)+str(paramUrlLimit)+str(paramOffset)
print (URL)

people1 = requests.get(URL)
people_json1  = people1.json()
totalFuncionarios = people_json1['response']['total']

paramOffsetLoop = totalFuncionarios
#agora que eu já tenho o total de registros da remuneração do mes, começo o loop

#funcao para remover os brackets 
def removebrack(valor):
   var_rem = (str(valor).replace('[','').replace(']',''))
   return var_rem

#export to csv
with open('/Users/mauriciobrandalise/Projects/prefa/files_remunera/remunera_'+str (paramYear) + str (paramMonthStr)+'.csv', 'w') as f:
#with open('D:/workspace/personal/dev/prefeitura_caxiasdosul/remunera_'+str (paramYear) + str (paramMonthStr)+'_parte2.csv', 'w') as f:
    theWriter = csv.writer(f)
    theWriter.writerow(['tipoRemuneracao','paramYear','paramMonthStr','periodoWorked','countFunc','id','nome','admissao','cargo','padrao_cargo','funcao_gratificada',
        'total_bruto','auxilio_alimentacao','auxilio_creche','antecipacao_ferias','indenizacoes_diversas','licenca_premio_compensada','descontos','redutor','total_liquido'])


    countFunc = 0
    while countFunc < totalFuncionarios:
        # capturar o numero de registros atual
        URL_loop = 'https://remuneracoes.caxias.rs.gov.br/api/' + str (paramYear) + '/' + str (paramMonthStr) + '/01/' + str (
            tipoRemuneracao) + str (paramUrlLimit) + str (countFunc)
        people1 = requests.get (URL_loop)
        people_json1 = people1.json ()

        #declaro a lista que vai receber todos os registros vindos do endpoint
        my_list = []

        #To print the names of people and folha com o total bruto
        for i in people_json1['response']['records']:
            my_list.append(tipoRemuneracao)
            my_list.append (paramYear)
            my_list.append (paramMonthStr)
            my_list.append ("10"+"/"+paramMonthStr+"/"+str(paramYear)) #primeiro dia do mes trabalhado
            my_list.append(countFunc)
            my_list.append (i['id'])
            my_list.append (i['nome'])

            admissao = [i['admissao']]
            my_list.append (admissao[:9])


            my_list.append (i['cargo'])
            my_list.append (i['padrao_cargo'])
            my_list.append (i['funcao_gratificada'])
            #my_list.append (i['tempo_servico'])
            total_bruto = [i['folha']['total_bruto']]

            my_list.append (removebrack(total_bruto))

            auxilio_alimentacao = [i['folha']['auxilio_alimentacao']]
            my_list.append (removebrack(auxilio_alimentacao))

            auxilio_creche = [i['folha']['auxilio_creche']]
            my_list.append (removebrack(auxilio_creche))

            antecipacao_ferias = [i['folha']['antecipacao_ferias']]
            my_list.append (removebrack(antecipacao_ferias))

            indenizacoes_diversas = [i['folha']['indenizacoes_diversas']]
            my_list.append (removebrack(indenizacoes_diversas))

            licenca_premio_compensada = [i['folha']['licenca_premio_compensada']]
            my_list.append (removebrack(licenca_premio_compensada))

            descontos = [i['folha']['descontos']]
            my_list.append (removebrack(descontos))
          
            redutor = [i['folha']['redutor']]
            my_list.append (removebrack(redutor))

            total_liquido = [i['folha']['total_liquido']]
            my_list.append (removebrack(total_liquido))

            theWriter.writerow(my_list)
            print ("---------------------")
            print (countFunc)
            print ("---------------------")

        #decrease registros
            countFunc = countFunc + 1

        #hora de sair do loop, pois acabaram os registros ! '''