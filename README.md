# Itermark
Bookmark extension for iterable data types; adds bounds aware bookmark
 enabling active item read/write (type allowing)

Ideal for 'paging' through lists/dicts/tuples

## Installation
```
pip install itermark
```

## Usage
 ```python
from itermark import Itermark as im
itermark_list = im(['one', 'two'])
itermark_list
# [<class 'itermark.ItermarkIndicator'>, 'one', 'two']

next(itermark_list)
# 'one'
next(itermark_list)
# 'two'
next(itermark_list)
# StopIteration: End of itermark iteration. set mark to -1 or reset to 1

itermark_list.mark = -1
itermark_list.active
# 'two'

itermark_list.mark += 2
# IndexError: Mark [4] out of bounds [1-2]
# 'four'

itermark_list.mark
# 2

itermark_list.active = 'TWO'
print(itermark_list)
# [<class 'itermark.ItermarkIndicator'>, 'one', 'TWO']
```
The Itermark extension adds properties `.mark` and `.active` (and `.activekey`/
 `.activeval` for dicts) as a bookmark/active item reference. 
 
Immutable obj `ItermarkIndicator` is inserted at `[0]` to track lower
 bounds. `.mark` and `.active` return None if only entry in iterable is
  `ItermarkIndicator`

## Types
```python
from itermark import Itermark as im
from collections import OrderedDict

_sample_list = [1, 2, 3]
_sample_dict = {1: 'one', 2: 'two', 3: 'three'}
_sample_ordr = OrderedDict(_sample_dict)        # for pre 3.6 implementation
_sample_tupl = (1, 2, 3)

im(_sample_list)
# [<class 'itermark.ItermarkIndicator'>, 1, 2, 3]

im(_sample_dict)
# {0: <class 'itermark.ItermarkIndicator'>, 1: 'one', 2: 'two', 3: 'three'}

im(_sample_ordr)
# ItermarkOrDict([
#     (0, <class 'itermark.ItermarkIndicator'>), 
#     (1, 'one'), (2, 'two'), (3, 'three')
# ])

im(_sample_tupl)
# (<class 'itermark.ItermarkIndicator'>, 1, 2, 3)
```

## Properties

### `mark` 
Bookmark index, can be assigned a value directly (`itermarklist.mark = 2`) or
 by 
 operator assignment (`itermarklist.mark += 1`)

### `active` 
Retrieves item based on current mark. `itermarklist[mark]`. On dicts/OrderedDicts
 returns `{.activekey: .activeval}` 

### `activekey` 
Dict specific, retrieves nth key from dictonary type where self.mark = n
 Note that itermark was made post 3.6's insertion ordered dicts. While
  itermark properties still work pre 3.6, collections.OrderedDict is
   recommended

### `activeval`
Dict specific, retrieved value based on current .activekey 

### `next()`
Emulation of an iterable's `__next__` functionality. Iterates from current
 `.mark` to end, and throws StopIteration at end while preserving obj. (Not
  meant to be as fast as actual iteration obj)

## Supported types

### `list`
Original implementation, full mark and active usage

#### Default functions with Itermark support
##### `clear()`
##### `remove()`
##### `pop()`
##### `reverse()`
`
##### `dict`
Uses iterator gen for mark and active properties. `activekey` calls immutable
 key, `activeval` calls and sets activekey's value

##### `OrderedDict`
Same features as a regular dict, but for pre 3.6 implementation

##### `tuple
No active assignment 

## Bugs
Unintended side effect: OrderedDicts show up as `ItermarkOrDict`. While it
 looks nice, it does not assist in tracking lower bounds. Development is not
  seeking to replicate among default types at this time
  
Itermark extendsdefault types, however some default types will naturally not 
 play well with Itermark, esp in regards to ItermarkIndicator.  If a builtin 
  function moves or removes ItermarkIndicator, itermark can no longer
   track lower bound and when decrementing will loop from 0 to -1. Work in 
    progress on extending default functions with itermark support on each type
