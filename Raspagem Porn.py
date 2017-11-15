    #Andressa Flávia Ribeiro de Oliveira 1° ADS B
    #Raspagem com propósito de coletar títulos de cunho sexual impróprio


print ('    Olá! Este é um programa raspa títulos de pornôs com o intuito de criar um ranking dos videos e possivelmente identificar quais possuem cunho sexual impróprios que ferem éticas humanas.')
print ('    É importante ressaltar que todos os dados são brasileiros!')
idade = int(input('    Para seguirmos adiante, responda sua idade em números:'))
print ('\n')

if idade<=17:
    print ('    Você não pode verificar o programa devido a menor idade.')

else:
    rodar = True

    while(rodar):
        opcao = int(input("QUAL A OPÇÃO DESEJADA?\n"+
                      "1-Videos mais vistos\n"+
                      "2-Raspagem dos Títulos com cunho sexual imprório\n"+ 
                      "3-Categorias - Mais vistas e quantidade de videos(HETERO)\n"+
                      "4-Categorias - Mais vistas e quantidade de videos (GAY)\n"+
                      "5-Informações do Desenvolvedor e Curiosidades da Raspagem\n"+
                      "6-Sair\n" ))    

        if opcao == 1:
            import requests
            from bs4 import BeautifulSoup

            url = 'https://pt.pornhub.com/video?o=mv&t=y' 
            counter = 1

            for n in range(1,13):
                pagina = url+'&page='+str(n)
                html = requests.get(pagina)
                bs = BeautifulSoup(html.content, 'html.parser')
                valores = bs.find('ul', {'class':'nf-videos videos search-video-thumbs'})
                valores = valores.findAll("span",{'class':'title'})
                for palavra in valores: 
                    print(str(counter)+'º lugar:' + palavra.getText())
                    counter +=1
                    print("\n")

                

        elif opcao == 2:
            import requests
            from bs4 import BeautifulSoup

            url = 'https://pt.pornhub.com/video?o=mv&t=y' 
            counter = 1


            for n in range(1,13):
                pagina = url+'&page='+str(n)
                html = requests.get(pagina)
                bs = BeautifulSoup(html.content, 'html.parser')
                valores = bs.find('ul', {'class':'nf-videos videos search-video-thumbs'})
                valores = valores.findAll("span",{'class':'title'})
                for palavra in valores:
                    t = (str(counter)+'º lugar:' + palavra.getText())
                    counter +=1
                    doentio = ["irma","irmã","pai","mae","mãe","madrasta","padrasto","primo","prima","adolescente","teen","mother","sister","father","brother","abuse"]
                    lista = []
                    lista.append(t)

                    improprios = []
                    for frase in lista:
                        for palavra in doentio:
                           if palavra in frase:
                                print (frase)

        elif opcao == 3:
            import requests
            from bs4 import BeautifulSoup

            url = 'https://pt.pornhub.com/categories'
            counter = 1


            html = requests.get(url)
            bs = BeautifulSoup(html.content, 'html.parser')
            valores = bs.findAll('h5')
            for palavra in valores: 
                print(str(counter)+'º lugar:' + palavra.getText())
                counter +=1


        elif opcao == 4:
            import requests
            from bs4 import BeautifulSoup

            url = 'https://pt.pornhub.com/gay/categories'
            counter = 1


            pagina = url
            html = requests.get(pagina)
            bs = BeautifulSoup(html.content, 'html.parser')
            valores = bs.findAll('h5')
            for palavra in valores: 
                print(str(counter)+'º lugar:' + palavra.getText())
                counter +=1
                print("\n")

        elif opcao == 5: #arrumar espaçamento
            print ('\n')
            print('Desenvolvido por Andressa Flávia Ribeiro Oliveira\n'+
                  'Curiosidade nº1: Uma das categorias mais vistas pelo público\n'+
                  'HÉTERO, é a categoria travesti, o que não faz sentido já que\n'+
                  '90% do público pôrno são homens, que por sua vez nesse grupo, se dizem héteros.\n'+
                  'Curiosidade nº2: Quando analisada a categoria Gay, não há vi\n'+
                  'deos de mulheres homossexuais, isso reforça que sites pornôs\n'+
                  'não são destinados a mulheres, e que a categoria "lésbica" só\n'+
                  'serve em pró do publico masculino (na visão dos sites)\n'+
                  'Curiosidade nº3: 3/4 dos títulos violam o correto, isso\n'+
                  'reforça o desejo pelo proíbido/incorreto.')
            print ('\n')

         
        elif opcao == 6:
            print("Espero que as informações tenham sido úteis. Até mais!")
            rodar = False

        else:
            print("numero invalido\n")
