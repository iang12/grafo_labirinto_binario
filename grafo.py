from random import *
matriz_grafo      = []
matriz_visitas    = []
lista_de_posicoes = []
posicao_inicial   = []
posicao_final     = []
lista_de_passos   = []
passo = 1
#matriz de visitas

#print(matriz_visitas)

f = open("entrada.txt", "r")
dim = f.readline().replace("\n","").split(" ")
n = int(dim[0]) #numero de linhas
m = int(dim[1]) #numero de colunas
cont = 1
matrix = []
for i in range(n):
    matrix.append(f.readline().replace("\n","").split(" "))
begin = f.readline().replace("\n","").split(" ")
end = f.readline().replace("\n","").split(" ")

matriz_visitas = [ [ 0 for i in range(m) ] for j in range(n) ] 


print(matrix)    
print(begin)
print(end)
# print(lista_de_posicoes)
       
class Point:
    def __init__(self,x=0,y=0,dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.dist)+')'



def isValid(row, col):
    # return true if row number and  
    # column number is in range 
    return (row >= 0) and (row < n) and (col >= 0) and (col < m); 




p = Point(x=int(begin[0]),y=int(begin[1]))
lista = []
lista.append(p)
matriz_visitas[p.x][p.y] = 1

find = False
while lista:
    q = lista.pop(0)
    print(q)
    if(q.x==int(end[0]) and q.y==int(end[1])):
        print("Caminho mais curto: "+str(q.dist))
        find = True
        break
    
    #cima
    if(isValid(q.x-1,q.y)):
        if(matrix[q.x-1][q.y]=='1' and (not matriz_visitas[q.x-1][q.y])):
            lista.append(Point(x=q.x-1,y=q.y,dist=q.dist+1))
            matriz_visitas[q.x-1][q.y] = 1
          
    #baixo
    if(isValid(q.x+1,q.y)):
        if(matrix[q.x+1][q.y]=='1' and (not matriz_visitas[q.x+1][q.y])):
            lista.append(Point(x=q.x+1,y=q.y,dist=q.dist+1))
            matriz_visitas[q.x+1][q.y] = 1
            # print("não testou")

    #esquerda
    if(isValid(q.x,q.y-1)):
        if(matrix[q.x][q.y-1]=='1' and (not matriz_visitas[q.x][q.y-1])):
            lista.append(Point(x=q.x,y=q.y-1,dist=q.dist+1))
            matriz_visitas[q.x][q.y-1] = 1
            # print('esquerda')

    #direita
    if(isValid(q.x,q.y+1)):
        if(matrix[q.x][q.y+1]=='1' and (not matriz_visitas[q.x][q.y+1])):
            lista.append(Point(x=q.x,y=q.y+1,dist=q.dist+1))
            matriz_visitas[q.x][q.y+1] = 1
            # print('direita')
    #print(matriz_visitas)

if(not find):
    print("Não tem caminho!")

#print(p.x,p.y,p.dist)
#Positions = []
#Positions.append([p.x,p.y,p.dist]) 
#print(Positions)
