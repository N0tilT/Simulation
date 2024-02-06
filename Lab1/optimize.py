from pulp import LpVariable, LpProblem, LpMaximize, value
from cvxopt.modeling import variable, op
import time

def pulp_solve():
    print("PULP SOLUTION\n_____________")
    start = time.time()
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    x4 = LpVariable("x4", lowBound=0)
    problem = LpProblem('0', LpMaximize)
    problem += 9*x1 + 6*x2 + 4*x3 + 7*x4, "Функция цели"
    problem += 1*x1 + 0*x2 + 2* x3 + 1*x4 <= 180, "1"
    problem += 0*x1 + 1*x2 + 3* x3 + 2*x4 <= 210, "2"
    problem += 4*x1 + 2*x2 + 0*x3 + 4*x4 <= 800, "3"
    problem.solve()
    print("Результат:")
    for variable in problem.variables():
        print (variable.name, "=", variable.varValue)
    print("Прибыль:")
    print(value(problem.objective))
    stop = time.time()
    print ("Время :")
    print(stop - start)
    return variable

def cvxopt_solve():
    print("CVXOPT SOLUTION\n_____________")
    start = time.time()
    x = variable(4, 'x')
    z=-(9*x[0] +6*x[1] + 4*x[2] + 7*x[3]) #Функция цели
    mass1 = (1*x[0] + 0*x[1] + 2*x[2] + 1*x[3] <= 180) #"1"
    mass2 = (0*x[0] + 1*x[1] + 3*x[2] + 2*x[3] <= 210 ) # "2"
    mass3 = (4*x[0] + 2*x[1] + 0*x[2] + 4*x[3]  <= 800) #"3"
    x_non_negative = (x >= 0) #"4"    
    problem =op(z,[mass1,mass2,mass3, x_non_negative])
    problem.solve(solver='glpk')  
    problem.status

    print ("Прибыль:")
    print(abs(problem.objective.value()[0]))
    print ("Результат:")
    print(x.value)
    stop = time.time()
    print ("Время :")
    print(stop - start)

pulp_solve()
cvxopt_solve()