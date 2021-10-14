def deco(func):
  def inner():
    print("Running inner")
  return inner

@deco
def init():
  pass

init()