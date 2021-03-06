
import random


class Numbergame:

    def __init__(self):
        print("New Run")
        self.num = random.randint(0, 101)
        self.correct = False
        self.choice = False
        while True:
            self.process()
            self.choice = input("Do you want to try again? y/n ")
            if self.choice == "y":
                self.__init__()
            if self.choice == "n":
                break
            else:
                print("Insufficient command !")
            self.get_parameters()

    def process(self):
        while not self.correct:
            guess = int(input("what's your guess: "))
            if guess > self.num:
                print("You guessed to high!")
            elif guess < self.num:
                print("You guessed to low!")
            elif guess == self.num:
                print('Correct!')
                self.correct = True

    def get_parameters(self):
        self.num = random.randint(0, 101)
        self.correct = False
        self.choice = False


class MachinesTry:

    def __init__(self):
        self.highest = 100
        self.corridor = [0, self.highest]
        self.rightanswer = False
        self.pasttries = []
        self.highlow = [0]
        self.track = []
        print("Choose a number in the range from 0 to", self.highest)
        print("Got a number?")
        input("Enter any key to start: ")
        self.guessalgorithm()

    def guessalgorithm(self):
        self.firstguess()
        while not self.rightanswer:
            if bool(self.highlow[0]) == True:
                self.make_a_guess_low()
                self.track.append(0)
            elif bool(self.highlow[0]) == False:
                self.make_a_guess_high()
            print(self.pasttries[-1])
            feedback = input("That's my guess. "
                             "Am I right? Or to high or to low y/h/l: ")
            if feedback == "y":
                    break
            if feedback == "h":
                self.corridor[1] = self.pasttries[-1]
                self.highlow[0] = 1
            if feedback == "l":
                self.corridor[0] = self.pasttries[-1]
                self.highlow[0] = 0
        print("I knew it :)")

    def firstguess(self):
        guess = round((self.highest * 0.7), 0)
        self.pasttries.append(guess)

    def make_a_guess_high(self):
        guess = round(((self.corridor[1] - self.corridor[0]) * 0.7 + self.corridor[0]), 0)
        self.pasttries.append(guess)

    def make_a_guess_low(self):
        guess = round(((self.corridor[1] - self.corridor[0]) * 0.3 + self.corridor[0]), 0)
        self.pasttries.append(guess)


class Start(Numbergame, MachinesTry):

    def __init__(self):
        print("You like numbers eh? ")
        self.choosing()

    def choosing(self):
        x = True
        while x:
            self.wahl = input("Do want to guess or is it the machines try? (i/m) "
                              "Or press Enter to end ")

            if self.wahl == "i":
                Numbergame()

            elif self.wahl == "m":
                MachinesTry()

            elif self.wahl == "":
                break


Start()
