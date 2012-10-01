About
---------------
This is a very simple tool for generating random text from patterns.

Usage
-----

	import randomtext
	
	randomtext.generate("(Code|Documenaton) of {project} (rocks|sucks)!", {'project': 'randomtext'})

Where `(...|...|...)` is list of words separated by `|` symbol. Pattern can be nested. So something like
`((Test1|Test2)|(Test3|Test4))` will work.

Where `{project}` is key of element in `data` dict.
The second argument should be a python `dict`.