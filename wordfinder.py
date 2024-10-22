import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filename="randomwords.txt"):
        """Initializes WordFinder with a list of words from the given file."""
        self.words = self.read_file(filename)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        """Show representation."""

        word = random.choice(self.words)

        return f"<WordFinder Word is: {word}>"

    def read_file(self, filename):
        """Reads the file and returns a list of words without newlines."""

        with open(filename, 'r') as file:
            return [word.strip() for word in file if word.strip()]
        
    def random(self):
        """Returns a random word from the list."""

        return random.choice(self.words)

    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that ignores blank lines/comments."""

    def read_file(self, filename):
        """Reads the file and returns a list of words, ignoring blank lines and comments."""

        with open(filename, 'r') as file:
            return [word.strip() for word in file if word.strip() and not word.startswith('#')]
        
    def __repr__(self):
        return super().__repr__()