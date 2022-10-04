def nota_correta(nota1, nota2):
    nota_correta = 0
    media = 0
    if nota1 >= 0 and nota1 <=10:
        nota_correta = nota_correta + 1
        media = media + nota1
    if nota2 >= 0 and nota2 <=10:
        nota_correta = nota_correta + 1
        media = media + nota2
    if nota_correta < 2: 
        return "Uma das notas está errada"
    else:
        return media/2

        
