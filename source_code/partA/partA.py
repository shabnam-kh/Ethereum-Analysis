

"""Lab 1. Basic wordcount
"""
from mrjob.job import MRJob
import re
from datetime import datetime

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class Lab1, which extends the MRJob format.
class Lab1(MRJob):

# this class will define two additional methods: the mapper method goes here
	def mapper(self, _, line):
		fields = line.split(',')
		tran_timestamp = fields[6]
		if tran_timestamp == "block_timestamp":
			pass
		else:
			dt_object = datetime.fromtimestamp(int(tran_timestamp))
			yield((str(dt_object.month),str(dt_object.year)),1)

#and the reducer method goes after this line
	def reducer(self, key, values):
		yield (key, sum(values))

#this part of the python script tells to actually run the defined MapReduce job. Note that Lab1 is the name of the class
if __name__ == '__main__':
	Lab1.run()

