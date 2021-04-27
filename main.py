"""
Run the perceptron learning tasks and the learning problems.
"""

from perceptron import Perceptron
from utils import process_iris_data

def learning_problems(weights, data):
	"""
	Acomplish the three learning tasks as outlined in Task 2.

	Tasks
	--------------------------------------------------------------------
		LP 1: iris setosa (+1) versus not iris setosa (-1)
		LP 2: iris versicolor (+1) versus not iris versicolor (-1)
		LP 3: iris virginica (+1) versus not iris virginica (-1)
	
	Arguments
	--------------------------------------------------------------------
		weights : [] : list of weights to use for learning problems 
			(different learning problems specify different weights)
		data : {} : the iris data to use for learning problems
			(different learning problems specify different shufflings)
	"""

	pass

def task4():
	"""
	Setup learning environment as specified for task 4.
	"""
	
	pass

def task3():
	"""
	Setup learning environment as specified for task 3.
	"""
	
	pass

def task2():
	"""
	Setup learning environment as specified for task 2.
	"""
	with open('iris.data', 'r') as sampleData:
		data = sampleData.readlines()
	#created 3 arrays of data for petals 
	#cannot implement further until function declarations of perceptrons are created
	iris_setosa = data[1:50]
	iris_versicolor = data[50:100]
	iris_virginica = data[100:150]

	pass

def main():
	"""
	
	""" 
	pass

if __name__ == "__main__":
	main()