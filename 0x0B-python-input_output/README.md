JSON JaveScript Object Notation is data representation format, light and easy to read, used in many config files and APIs and easy interable in languages.
to create a JSON file we just use .json at the end of the filename. exp: text.json
it is similar to dictionaries in Python
here is an example of a JSON object, last example is to show all type can be in values but only string in keys:
{
	"employees": [
		{
			"firstName": "John",
			"lastName": "Doe",
			"age": 30
		},
		{
			"firstName": "Anna",
			"lastName": "Smith",
			"age": [16,
				null,
				18,
				"no longer underage xD",
			]
		}
	]
}
JSON differs from dict by having only string as keys can be repeated, values can be called json[key] or json.key

JSON: https://www.geeksforgeeks.org/difference-between-json-and-dictionary-in-python/

----------------------------------

now for input output with python

f = open('filename', mode, encoding="uft-8")
the mode can be r for read or 'w' or 'a' for append or 'r+' for read and write. the mode is optionnal and is set to r by default.
appending b to the mode opens the file with binary encoding like 'rb' or 'rb+', encoding variable is not specified in this case
if we open a binary in textmode the \r\n will be converted to \n, this will corrupt files like JPEG...
to avoid f.close each time we will use the with block that ensures the closure of the file, otherwise se need to f.close:
with open(...) as f:
	statements

f.read(n)
to read n elements from	actual cursor position. if n is negative or ommited, the entire file is read.

f.readline()
read chars until \n is encountered
we can also use
for line in f:
	# to itterate inside the file

f.write(string) to write

f.tell() to return the current position of the cursor in the map

f.seek(offset, whence) whence is 0: beginning of the file, 1: current position and 2: end of file
if the file is opened in binary mode seek don't behave correctly, see the end of 7.2.1 Methods of File Objects

