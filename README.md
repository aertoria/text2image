# text2image

[![Join the chat at https://gitter.im/aertoria/text2image](https://badges.gitter.im/aertoria/text2image.svg)](https://gitter.im/aertoria/text2image?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/aertoria/text2image.svg?branch=master)](https://travis-ci.org/aertoria/text2image)


![alt tag](https://github.com/aertoria/text2image/blob/master/text2image/doc/example/1.jpg?raw=true)


text2image is a python program that allow you to convert any text to a word-image like 'read me' above.
This let you to better comment when you programming, writing documentation.

To use it is very simple:

Example 1:
 python ./text2image.py "hello world"
Output:
![alt tag](https://github.com/aertoria/text2image/blob/master/text2image/doc/example/2.jpg?raw=true)



Example 2:
 python ./text2image.py "SPARK V2.0_1"
Output:
![alt tag](https://github.com/aertoria/text2image/blob/master/text2image/doc/example/3.jpg?raw=true)
It's an opensource program. You are free to use, re-distribtue etc. Welcome to jump in and contribute.



To use it as a library:
from Text2image import Text2image
instance=Text2image.Text2image()
print instance.get_image("HelloWorld")

VERSION:  Code Initial Release    2015-11-13
This is a project based on an project I created at 2010. Was on MIT license. Now put on Apache License.
Copyright 2015 aertoria
https://github.com/aertoria

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
