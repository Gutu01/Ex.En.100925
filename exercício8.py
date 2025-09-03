distacio = float(input("Distacia total (Km):"))
consumo = float(input("Consumo do carro (Km/l):"))
preco = float(input("Preço do combustível (Litros): R$"))

custo = (distacio/consumo)*preco

print("\nCusto estimado da viagem: R$", custo)