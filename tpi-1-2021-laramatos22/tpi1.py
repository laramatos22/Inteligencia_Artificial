# Lara Catarina da Silva Matos, nmec 95228

# Discuti os exercicios com os colegas:
# 93250 - Joao Eduardo da Silva Figueiredo
# 93418 - Beatriz Agante de Almeida
# 93183 - Joao Ferreira Martins
# 98392 - Mariana Barbara Silva
# 93196 - Pedro Costa Jorge Dias Pereira
# 93389 - Tiago Miguel Joaquim Pedrosa

from tree_search import *
from cidades import *

class MyNode(SearchNode):
    def __init__(self,state,parent,cost=None,heuristic=None,eval=None):
        super().__init__(state,parent)
        self.cost = cost
        self.heuristic = heuristic
        self.eval = eval
        self.children = []
        self.state = state

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',seed=0): 
        super().__init__(problem,strategy,seed)
        root = MyNode(problem.initial,None)
        root.heuristic = self.problem.domain.heuristic(problem.initial, self.problem.goal)
        self.solution_tree = None
        self.used_shortcuts = []
        root.cost = 0
        self.all_nodes = [root]
        root.eval = root.cost + root.heuristic
        self.state = None
        self.solution = None

        #self.nodes_visitados = []

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        self.open_nodes = sorted(self.open_nodes+lnewnodes, key=lambda n: self.all_nodes[n].cost + self.all_nodes[n].heuristic)
        #pass

    def propagate_eval_upwards(self,node):
        #IMPLEMENT HERE
        #Após discussão com a Beatriz

        if node.parent == None:
            return 

        for x in node.children:
            child_eval = self.all_nodes[x].eval
            c_eval = child_eval.sort(key = lambda eval: eval)
            x.eval = child_eval.pop(0)
            self.propagate_eval_upwards(x)

        #pass

    def search2(self,atmostonce=False):
        #IMPLEMENT HERE
        #após discutir com a Beatriz, o Pedro o João Matins, o João Figueiredo e o Pedro

        if atmostonce:
            visited = []        # guarda os nodes visitados

        while self.open_nodes != []:
            nodeID = self.open_nodes.pop(0)
            node = self.all_nodes[nodeID]
            node_eval = -1

            if atmostonce:
                if node.state is visited:
                    continue
                visited.append(node.state)

            if self.problem.goal_test(node.state):
                self.solution = node
                self.terminals = len(self.open_nodes) + 1
                self.cost = self.solution.cost
                return self.get_path(node)

            lnewnodes = []
            self.non_terminals += 1

            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)

                if atmostonce and newstate is visited:
                    continue

                if newstate not in self.get_path(node):
                    newnode = MyNode(newstate, nodeID)
                    #newnode = MyNode(newstate, nodeID, newnode.cost , self.problem.domain.heuristic(newstate, self.problem.goal))
                    newnodeID = len(self.all_nodes)
                    node.children.append(newnodeID)

                    newnode.cost = self.problem.domain.cost(node.state, a) + node.cost
                    newnode.heuristic = self.problem.domain.heuristic(newstate, self.problem.goal)
                    
                    newnode.eval = newnode.cost + newnode.heuristic
                    node.children.append(len(self.all_nodes))
                    self.all_nodes.append(newnode)
                    self.propagate_eval_upwards(newnode)
                    
                    lnewnodes.append(newnodeID)

                    if (node_eval == -1 or node.eval > newnode.eval):
                        node_eval = newnode.eval

            self.add_to_open(lnewnodes)

            if len(lnewnodes) != 0:
                node.eval = node_eval
                #pass
        return None


    def repeated_random_depth(self,numattempts=3,atmostonce=False):
        #IMPLEMENT HERE
        # depois de discutir com o Pedro e a Beatriz

        index = 0

        while index < numattempts:
            searchTree = MyTree(self.problem,strategy='rand_depth',seed=index)
            solucao = searchTree.search2()
            if (self.solution_tree == None) or searchTree.solution.cost < self.solution_tree.solution.cost:
                self.solution_tree = searchTree
                minimum_cost_solution = solucao
            index += 1
        
        return minimum_cost_solution

        #pass

    def make_shortcuts(self):
        #IMPLEMENT HERE
        # apos discutir o exercicio com a Beatriz e o Joao Martins

        sc_list = []
        index = 0
        
        if len(sc_list) == 1:
            return [sc_list[0]]

        neighbours = []
        for C1,C2,D in self.problem.domain.connections:
            if (C1 == self.state):
                neighbours.append(C2)
            if (C2 == self.state):
                neighbours.append(C1)
        #neighbours = sc_list[0]

        further = None
        for i in sc_list:
            if further == None:
                further = i
            if i in neighbours:
                further = i

        if further == None:
            index = 1
        else:
            index = list.index(further)

        if index > 1:
            self.used_shortcuts.append((sc_list[0],further))

        #return [sc_list[0]] + self.make_shortcuts(sc_list[index:])

        #pass

class MyCities(Cidades):

    def maximum_tree_size(self,depth):   # assuming there is no loop prevention
        #IMPLEMENT HERE
        # após discutir com o Joao Martins e a Beatriz
        if depth == 0:
            return 1

        cidades = set()
        num_total_vizinhos = 0
        sum = 0 # soma dos nodes
        
        for (C1,C2,D) in self.connections:
            cidades.add(C1)
            cidades.add(C2)
            num_total_vizinhos += 2

        #use the average number of neighbors per state as an estimate for
        #average branching factor
        avg_branching = num_total_vizinhos/len(cidades)

        while (depth > 0):
            temp = pow(avg_branching,depth)
            sum += temp
            depth -= 1
        
        sum += 1
        return sum

        #pass

    


