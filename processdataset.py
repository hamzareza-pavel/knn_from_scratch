#author: Hamza Reza Pavel
# This file has utility methods to preprocess the dataset. To eliminate outliers, duplicates, and convert string data to numerical data.
import pandas as pd


def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())


def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup


def isfloat(x):
	if x.find(".") == -1:
		return False
	else:
		try:
			a = float(x)
		except ValueError:
			return False
		else:
			return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def process_data_set(dataset):
	attributemap = list()
	for i in range(len(dataset[0])):
		if isfloat(dataset[0][i]):
			str_column_to_float(dataset, i)
		else:
			lookup = str_column_to_int(dataset,i)
			attributemap.append((lookup, i))
	df = pd.DataFrame(dataset)
	return attributemap, df

