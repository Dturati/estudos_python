b = 2
def f1(a):
  print(a)
  print(b)

# f1(1)

def f2(a):
  global b
  print(a)
  print(b)
  b = 3

# f2(1)

class Averager:
  def __init__(self) -> None:
      self.series = []

  def __call__(self, new_value):
    self.series.append(new_value)
    total = sum(self.series)
    return total/len(self.series)

def make_averager():
  series = []

  def averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total/len(series)
  return averager

def make_averager2():
  count = 0
  total = 0

  def averager(new_value):
    nonlocal count, total
    count += 1
    total += new_value
    return total / count
  return averager

avg = make_averager2()
print(avg(1))