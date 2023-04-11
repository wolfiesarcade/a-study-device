import random
class study:
    def __init__(self):
        self.no_of_questions=input("enter the amount of questions you'd like to be asked: ")
        self.filename=input("enter the file name: ")
    def file_opener(self):
        file = open(self.filename, 'r')
        title = file.readline().split(',')
        index_questions= title.index('"Questions"')
        index_answers = title.index('"Answers"')
        data=file.readlines()
        self.questions1=[]
        self.answers1=[]
        # self.answers2 = []
        # self.answers3 = []
        # self.correctanswers = []

        for lines in data:
            parsed = lines.split(',')
            self.questions1.append(parsed[index_questions])
            self.answers1.append(parsed[index_answers])
            # self.answers2.append(parsed[index_answers+1])
            # self.answers3.append(parsed[index_answers+2])
            # self.correctanswers.append(int(parsed[index_answers+3]))
    def randomizer(self):
        random_index= random.randint(0, len(self.questions1)-1)
        print(random_questions=self.questions1[random_index])
        random_answers = self.answers1[random_index]
        self.questions1.pop(random_index)
        self.answers1.pop(random_index)

    def displaystudy(self):
        print(self.no_of_questions)
        print(self.filename)

study1= study()


#study1.fileopener()









