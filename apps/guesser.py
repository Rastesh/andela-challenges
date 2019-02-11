class Guesser:
  def _init_(self, number, lives):
    self.number = number
    self.lives = lives
  def guess(self, n):
    if self.lives < 1: raise "Too many guesses!"
    if self.number == n: return True
    self.lives -= 1
    return False

print(Guesser)