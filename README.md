                                               # SCOPES & CLOSURES

The part of the code where the name(or binding) is defined is called the lexical scope

Each scope has it's namespace.

## Global Scope:

    It can also be called module scope.It spans a single file(eg main.py).

Built-in objects like True, False, None, print etc are an exception and can be used anywhere and in any function.

Modules are nested inside a built-in scope.


## Local Scope:

    A new scope is created whenever a function is called. Local scopes are nested in the Module scope which is nested in Built-in scope.

The following is the ascending order of scopes.

Local ......> Non Local ........> Global .......> Built-in

For loops and conditional statements don't have their own scope in Python.


## Nonlocal Scope:
    This is neither global nor local scope. Functions defined inside another function can access the nonlocal variables.

## Closures:
    A closure is like a function with an extended scope containing free variables.


                                                  # Assignment



## Task 1
In this task we need to create a function to check each function has doc string and doc string should be of 50 character each. here we create doc string_check function which takes the function who has to be checked as a parameter. here we have defined min_count which is the minimum character count. Then we have defined another function mycount which is a closure which takes in min count as non local parameter and then checks its length by fetching the docstring of the function. It returns a True if doc string is more than 50 characters else returns false

## Task 2
In this Task we need a function to calculate the next Fibonacci number, here we define first and second number as free variables i.e. will be used by generate_my_next_number closure and that closure will add these numbers and then will update the value of these numbers and then will return the added result

## Task 3
In this task we need to calculate how many times a function is being called, so to do that we define a my counter function with count as free variable. Then we defined inner function which updates the count value and returns it.

## Task 4
This task is slight addition to the previous task, here we define 4 functions i.e. add, mul, sub, and div. in this task we keep a global dictionary my-dict to have a check on how many times each operation is being called. so here we define a function my counter_with_global_dict which takes in function as a parameter, the free variable count is the value obtained from the key of the global dictionary as function name. Here we define a closure called inner which takes in a and b as parameters, which are the numbers over which each operation will be performed. The function updated the global dictionary and returns the count

## Task 5
This task is and upgraded version of task 4, The only difference is that instead of updating in global variable we pass a dictionary as a parameter and that gets updated.