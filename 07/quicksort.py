def quicksort(elements):
  if elements == []:
    return []
  else:
    pivot = elements[0]

    less = []
    great = []

    for item in elements[1:]:
      if item < pivot:
        less.append(item)
      else:
        great.append(item)
        
    less = quicksort(less)
    great = quicksort(great)
    return less + [pivot] + great

print(quicksort([10, 23, 1, 17, 93, 10]))