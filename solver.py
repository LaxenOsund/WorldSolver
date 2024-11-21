class WordleSolver:
    def __init__(self, word_list):
        self.word_list = word_list

    def suggest_next_guess(self, feedback):
        # Filter the word list based on feedback (green, yellow, gray tiles)
        filtered_words = self.word_list  # Apply your filtering logic here
        
        # Suggest the best word based on remaining possibilities
        return filtered_words[0]  # Placeholder: replace with actual guess logic
