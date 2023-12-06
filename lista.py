continuar = 1
boletim = {'Nome':[], 'tel_aluno' : [], 'email': [], 'endereco': [], 'resultado': []}
boletims = []
while continuar == 1:
    #for i in range (2):
        boletim['Nome'] = input ("digite o nome do alunos")
        boletim['tel_aluno'] = [input ("digite o telefone do alunos")]
        boletim['email'] = [input ("digite o email do alunos")]
        boletim['endereco'] = [input ("digite o endereço do alunos")]

        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        nota4 = float(input('Digite a quarta nota: '))

        resultado = (nota1 + nota2 + nota3 + nota4) / 4
        boletim['resultado'] = (nota1 + nota2 + nota3 + nota4) / 4          
        print(f"o resultado da média é",{resultado})

        boletims.append  (boletim)

        print(boletims)  

        sair = input("deseja cadastrar mais um aluno? S/N")

        if sair.upper == ('N'):
            exit()
            continuar = 111

        elif sair.upper == ('S'):
                continuar == 1
                


        
