# Itermark
Bookmark extension for iterable data types; adds bounds aware bookmark
 enabling active item read/write (type allowing)

Ideal for 'paging' through iterables

## Installation
```
pip install itermark
```

## Using Itermark
 ```python
>>> from itermark import Itermark
>>> iterlist = Itermark(['one', 'two', 'three', 'four'])
>>> next(iterlist)
'one'
>>> iterlist.active
2
>>> iterlist.mark += 2
>>> iterlist.active
'four'
>>> iterlist.mark = 6   # Would put mark outside active index
IndexError: Given mark [6] outside index range 1-5 
>>> iterlist.active = 'FOUR'
>>> print(iterlist)
['one', 'two', 'three', 'four']
```
The Itermark extension adds properties .mark and .active (and .activekey/
 .activeval for dicts), and an IteratorIndicator object inserted at the
  beginning of the iterable. Itermark properties are disabled if underlying
   iterable is empty  

##### `mark` 
Acts as a bookmark index, and can be assigned a value directly (`iterlist.mark
 = 2`) or by operator assignment (`iterlist.mark += 1`, `iterlist.mark -= 1`)

##### `active` 
Retrieves item based on current mark. `list[mark]`

##### `activekey` 
Dict specific, retrieves nth key from dictonary type where self.mark = n
 Note that itermark was made post 3.6's insertion ordered dicts. While
  itermark properties still work pre 3.6, collections.OrderedDict is
   recommended and supported

##### `activeval`
Dict specific, retrieved value based on current .activekey 

## Supported types

##### `list`
Original implementation, full mark and active usage

##### `tuple
No active assignment
`
##### `dict`
Uses iterator gen for mark and active properties. `activekey` calls immutable
 key, `activeval` calls and sets activekey's value

##### `OrderedDict`
Same features as a regular dict, but for pre 3.6 implementation

##### `string`
Sure, strings are just a list of characters

##### `set`
Read only use, similar to list. To preserve quick read/ref of a Set, 

## Notes
Itermark Indicator is enforced to ensure desired outcome of IndexError when
 trying to decrement below lowest given entry. Without Indicator, itermark
  loops from 0 to final entry, and loses lower bound awareness
 