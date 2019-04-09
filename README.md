# Itermark
Extension for iterable data types; adds boundwise bookmark iteration, enabling active item
tracking/setting (type allowing)

Ideal for 'paging' through iterables

## Installation
```
pip install itermark
```

## Using Itermark
 ```python
>>> from itermark import Itermark
>>> iterlist = Itermark(['zero', 'one', 'two', 'three'])
>>> iterlist.active
'zero'
>>> iterlist.mark += 2
>>> iterlist.active
'two'
>>> iterlist.mark = 5   # Would put mark outside active index
>>> iterlist.active
'three'                 # Defaults to highest upper bound
>>> iterlist.active = 'new three'
>>> iterlist.active
'new three'
```
The Itermark extension adds two properties (three for dicts), and two functions to it's objects.
Note that all itermark attributes are disabled if underlying iterable is empty  

##### `mark` 
Acts as a bookmark index, and can be assigned a value directly (`iterlist.mark = 2`) or by operator assignment
(`iterlist.mark += 1`, `iterlist.mark -= 1`)

##### `active` 
Retrieves nth item from iterable where self.mark = n. Dictionary Itermarks return nth value 

##### `activekey` 
Dict specific, retrieves nth key from dictonary type where self.mark = n. 
Note that itermark was made post 3.6's insertion ordered dicts. While itermark properties still work
pre 3.6, collections.OrderedDict is recommended and supported

##### `markend()`
Set mark to end value. Mark will never go above upper bound, but without calling len() user may not
know what that upper bound is. Use .markend() to reliably set mark to upper bound

## Supported types

##### `list`
Original implementation, full mark and active usage

##### `tuple
No active assignment
`
##### `dict`
Uses iterator gen for mark and active properties. `active` calls and sets values, 
`activekey` calls immutable keys

##### `OrderedDict`
Same features as a regular dict, but for pre 3.6 implementation

##### `string`
Sure, strings are just a list of characters

##### `set`
Look, I don't know who'd want bookmark iteration through a set but here ya go
