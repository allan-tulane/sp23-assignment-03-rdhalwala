# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING


def iterate(f, x, a):
  # done. do not change me.
  if len(a) == 0:
    return x
  else:
    return iterate(f, f(x, a[0]), a[1:])


def reduce(f, id_, a):
  # done. do not change me.
  if len(a) == 0:
    return id_
  elif len(a) == 1:
    return a[0]
  else:
    # can call these in parallel
    res = f(reduce(f, id_, a[:len(a) // 2]), reduce(f, id_, a[len(a) // 2:]))
    return res


#### Iterative solution
def parens_match_iterative(mylist):
  result = iterate(parens_update, 0, mylist)
  if result == 0:
    return True
  else:
    return False
  """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
  ### TODO


def parens_update(current_output, next_input):
  if next_input == '(':
    return current_output + 1
  elif next_input == ')':
    return current_output - 1
  else:
    return current_output
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    ###TODO


def test_parens_match_iterative():
  assert parens_match_iterative(['(', ')']) == True
  print(parens_match_iterative(['(', ')']) == True)
  assert parens_match_iterative(['(']) == False
  assert parens_match_iterative([')']) == False


#### Scan solution


def parens_match_scan(mylist):
  mapped_result = list(map(paren_map, mylist))
  final_value = scan(lambda x, y: min_f(x, y), 0, mapped_result)
  if final_value == 0:
    return True
  else:
    return False
  """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
  ###TODO


def scan(f, id_, a):
  """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
  return ([reduce(f, id_, a[:i + 1])
           for i in range(len(a))], reduce(f, id_, a))


def paren_map(x):
  """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
  if x == '(':
    return 1
  elif x == ')':
    return -1
  else:
    return 0


def min_f(x, y):
  """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
  if x < y:
    return x
  return y


def test_parens_match_scan():
  assert parens_match_scan(['(', ')']) == True
  assert parens_match_scan(['(']) == False
  assert parens_match_scan([')']) == False


#### Divide and conquer solution


def parens_match_dc(mylist):
  """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
  # done.
  n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
  return n_unmatched_left == 0 and n_unmatched_right == 0


def parens_match_dc_helper(mylist):
  if len(mylist) == 1:
    if mylist[0] == ')':
        return (1, 0)
    elif mylist[0] == '(':
      return (0, 1)

  middle = len(mylist) // 2
  left = parens_match_dc_helper(mylist[:middle])
  right = parens_match_dc_helper(mylist[middle:])
  
  R = 0
  L = 0

  if right[1] > 0:
    L += right[1] 
    
  if left[0] > 0:
    R += left[0]

  if left[1] > 0 and right[0] > 0:
    match = min(left[1], right[0])
    R += right[0] - match
    L += left[1] - match

  return (R, L)
  
  """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """


def test_parens_match_dc():
  assert parens_match_dc(['(', ')']) == True
  print(parens_match_dc(['(', ')']) == True)
  assert parens_match_dc(['(']) == False
  assert parens_match_dc([')']) == False

test_parens_match_dc()