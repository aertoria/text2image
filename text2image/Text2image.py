#!/usr/bin/python
'''
VERSION:  Code Initial Release    2015-11-13 
Copyright 2015@aertoria
ethanwang.dev@gmail.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from Library_ewst1311 import Library_ewst1311
import sys

class Text2image(Library_ewst1311):
	def __init__(self):
		super(Text2image,self).__init__()

	#public. To generate the image and return the result
	"""usage: output =instanceGenrator.generate_image('hello world')"""
	def get_image(self,s_input):
		L_input=list(s_input.upper())
		if not self.__check(L_input):
			return "Error During Processing. Only allow character, space, dash and dot"
		return self.__generate(L_input)

	#Check to see if input not containing other charecter	
	def __check(self, L_input):
		for word in L_input:
			if word not in self.dict.keys():
				return False
		return True

	#Given list of valid characters, return result as a string
	def __generate(self, L_input):
		resultImage=''
		for i in range(6):
			result = ''
			for letter_index in range(len(L_input)):
				result+=self.dict[L_input[letter_index]][i]
			resultImage+=result+'\n'
		return resultImage.strip('\n')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		instance=Text2image()
		print instance.get_image(sys.argv[1])
	else:
		print 'Invalid input. Sample: python generate.py "hello world"'