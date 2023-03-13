import random

class SlotMachine:
    def __init__(self):
        self.numbers = ["1", "2", "3", "4", "5", "6"]
        self.balance = 0
        self.bet = 0

    def play(self):
        if self.balance <= 0:
            return "Nice play! You have lost everything! Try again!"


        while self.balance > 0:
            user_input = input(f"Your balance is: {self.balance} leva. Place your bet: ")

            if user_input == "Stop":
                print("Bye, looooserrrr!!!")
                print(f"You have miserable: {self.balance} leva!")
                new_input = input("Do you wnat to withraw it?")
                if new_input == "yes":
                    print("Off you go now!")
                    self.balance = 0
                    continue
                else:
                    continue

            else:
                if user_input.isdigit():
                    self.bet = int(user_input)
                else:
                    print("Invalid input! What are you trying to bet moron?! Letters?!")
                    print()
                    continue

            if self.bet > self.balance:
                print("You can't bet more than you have!")
                continue

            reels = [random.choice(self.numbers) for _ in range(3)]
            print()
            print("-".join(reels))

            if reels[0] == reels[1] == reels[2]:
                winnings = self.bet * 10
                print(f"JACKPOT!!! You just won {winnings} leva!!!")

            elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
                winnings = self.bet * 2
                print(f"Nice!!! You just doubled your bet! You won: {winnings}")

            else:
                winnings = 0
                print("You suck!!! Try to win something!!!")

            self.balance += winnings - self.bet
            if self.balance <= 0:
                print("You have lost everything! Looser!")



    def add_money(self, amount):
            self.balance += amount
            print(f"You added {amount} leva and now your {self.balance} is leva!")

    # def withraw_money(self, amount):
    #     if self.amount <= self.balance:
    #         self.balance -= amount
    #         print(f"You withrew {amount} leva, and now your balance is {self.balance} leva.")
    #     else:
    #         print(f"You have only {self.balance} leva IDIOT!!!")

machine = SlotMachine()
money_amount = int(input("How much do you want to start with:"))
print()
machine.add_money(money_amount)
print("------Welcome to the Greatest Casino of the World! Now you will be be f*cked!------")
print()
while machine.balance > 0:
    machine.play()

