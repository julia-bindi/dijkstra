from typing import List, Dict
from functools import total_ordering
from heap import MinHeap
class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho:"Vertice", peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

@total_ordering
class DistanciaVerticeOrigem:
	def __init__(self, vertice:Vertice, distancia:int):
		self.vertice = vertice 
		self.distancia = distancia
		
	def __eq__(self, outro:"DistanciaVerticeOrigem") ->bool:
		return self.vertice == outro.vertice and self.distancia == outro.distancia
	
	def __lt__(self,  outro:"DistanciaVerticeOrigem") -> bool:
		return self.distancia < outro.distancia

	def __str__(self):
		return f"Dist. até {self.vertice.valor}: {self.distancia}"
	
	def __repr__(self):
		return str(self)


class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		#importante pois podem haver vertices que não tem arestas
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice

	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)

	def obtem_vertice(self, valor_vertice) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None

	def dijkstra_relax(self, fila_min_heap:MinHeap,vertice_u: Vertice, vertice_v:Vertice, distancia:Dict[Vertice, DistanciaVerticeOrigem], pai:Dict[Vertice,Vertice]):
		p = None
		anterior = None
		atual = None
		dist = 0
		for v in pai.keys():
			if pai[v] is None:
				p = v
				anterior = p
			else:
				atual = v
				ad = anterior.adjacencias
				dist = dist + ad[v]
				anterior = v
		if distancia[vertice_v].distancia > dist:
			distancia[vertice_v].distancia = dist
			pai[vertice_v ]= vertice_u
			fila_min_heap.insere(distancia[vertice_v])

	def dijkstra(self, valor_vertice_origem) -> (Dict[Vertice,DistanciaVerticeOrigem], Dict[Vertice,Vertice]):
		distancia = {}
		pai = {}
		vertice_origem = self.obtem_vertice(valor_vertice_origem)
		if not vertice_origem:
			return None

		fila_min_heap = MinHeap()
		#inicialização 
		for vertice in self.vertices.values():
			pass
		
		#print(f"HEAP: {fila_min_heap}")
		#print(f"Vertice Origem: {vertice_origem.valor}")

		#escreva o código abaixo para preencher as veriaveis distancia e pai adequadamente

		return distancia, pai