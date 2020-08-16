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
The Itermark extension adds properties `.mark` and `.active` (and `.activekey`/
 `.activeval` for dicts) as a bookmark/active item reference. Immutable obj 
 `ItermarkIndicator` is inserted at `[0]` to track lower bounds. `.mark` and 
 `.active` return None if only entry in iterable is `ItermarkIndicator`
  
### `mark` 
Bookmark index, can be assigned a value directly (`itermarklist.mark = 2`) or
 by 
 operator assignment (`itermarklist.mark += 1`)

### `active` 
Retrieves item based on current mark. `itermarklist[mark]`. On dicts/OrderedDicts
 returns a tuple of `(.activekey, .activeval)` 

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

## Types' modified default functions

Below types' default functions have been modified to ignore ItermarkIndicator

### `list`
##### `clear()` 
##### `remove()`
##### `pop()`
##### `reverse()`

### `dict` \ `OrderedDict`
##### `keys()`
##### `values()`


## Bugs
Unintended side effect: OrderedDicts show up as `ItermarkOrDict`. While it
 looks nice, it does not assist in tracking lower bounds. Development is not
  seeking to replicate among default types at this time
