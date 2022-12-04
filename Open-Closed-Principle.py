
class Question:
    def __init__(self, type, description, choices = []):
        self.type = type
        self.description = description
        self.choices = choices



class QuestionLogger:


    def logQuestion(questions):
        for question in questions:
            print(question.description)
            match question.type:
                case 'boolean':
                    print("1, True")
                    print("2, False")
                    break
                case 'multipleChoice':
                    for i, choice in enumerate(question.choices):
                        print(i + 1, choice)
                    break  
            print('')



# QuestionLogger violates the Open-Closed-Principle.
# If we wanted to add a new type of question we would have to extend the switch statement even further which will make it look much worse.




class IQuestion():
    def printQuestionChoices():
        raise NotImplementedError
        


class BooleanQuestion(IQuestion):
    
    def __init__(self, choices ,description):
        self.choices = choices
        self.description = description

    def printQuestionChoices():
        print("1, True")
        print("2, False")
     

class MultipleChoiceQuestions(IQuestion):
    
    def __init__(self, choices, description):
        self.choices = choices
        self.description = description

    def printQuestionChoices(self):
        for i, choice in enumerate(self.choices):
            print(i, choice)

        

class QuestionLogger:
    def logQuestion(questions):
        for question in questions:
            print(question.description)
            print(question.printQuestionChoices())
            print('')
    


# Now if we wanted to add a new type of Question we would have to create a new class that implements the methods of the Interface IQuestion.
# Without having to extend the switch statment which caused a main issue.