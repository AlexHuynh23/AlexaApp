def testing(prompt):
    print("Testing %s..." % prompt)

class Question():
    def __init__(self, prompt, posAnswers):
        self.prompt = prompt
        self.posAnswers = posAnswers
        self.answerCount = {}
        for answers in posAnswers:
            self.answerCount[answers] = 0

    def __str__(self):
        s = "Prompt: %s"
        i = 1
        for answers in self.posAnswers:
            s += "\nAnswer %d: %s" % (i, answers)
        return s 
    
    def getAnswers(self):
        pass

    def getPosAnswers(self):
        return self.posAnswers

    def getPrompt(self):
        return self.prompt
    
if __name__ == "__main__":
    testing("getPrompt")
    



