def spam():
  # In this function, eggs refers to the global variable,
  # so don't make a local variable called 'eggs'
  
  # So we are modifying the global variable 'eggs'
  global eggs
  eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
  
  