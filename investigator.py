class Investigator:
  name: str


  def  __init__(self, name):
    self.name = name
    pass

  def hello(self):
    print("Hello, I am " + self.name)