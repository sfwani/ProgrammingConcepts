'''
This code defines a function get_questions() which returns a list of 10 Question objects. Each Question object has a question string, four possible answer options, and an integer representing the correct answer option. The questions cover a range of topics including space, animals, dinosaurs, and children's stories. This function is meant to provide the questions for a trivia game. The Question class is imported from the questions module.
'''

from questions import Question

def get_questions():
    return [
        Question("How many days are in a lunar year?", "354", "365", "243", "379", 1),
        Question("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2),
        Question("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4),
        Question("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3),
        Question("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2),
        Question("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4),
        Question("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1),
        Question("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3),
        Question("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2),
        Question("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 1)
    ]
