from random import choice

class Answer():
    def __init__(self, args):
        self.args = args
    
    def get(self, args):
      if istanceof(args, list):
        return choice(args)
      if instanceof(args, Answer):
        return args.get()
