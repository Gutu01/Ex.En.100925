nome = input("Digite seu nome:")
disciplina = input("Nome da disciplina:")
nota1 = float(input("Nota 1º prova:"))
nota2 = float(input("Nota 2º prova:"))
nota3 = float(input("Nota 3º prova:"))

media = (nota1+nota2+nota3)/3

print("\nNome:", nome)
print("Disciplina:", disciplina)
print("1º nota:", nota1)
print("2º nota:", nota2)
print("3º nota:", nota3)
print("Média:", media)

if media >= 6:
    print("\nAluno aprovado!")
else:
    print("\nAluno reprovado!")