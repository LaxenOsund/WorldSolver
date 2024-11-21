import tkinter as tk
import pyautogui
from tkinter import messagebox

class WordleGUI:
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic
        self.board_region = None

        # Button to mark game board
        mark_button = tk.Button(root, text="Mark Game Board", command=self.mark_gameboard)
        mark_button.pack(pady=20)

        # Button to process game board and suggest the next guess
        process_button = tk.Button(root, text="Process Game Board", command=self.process_gameboard)
        process_button.pack(pady=20)

    def mark_gameboard(self):
        messagebox.showinfo("Info", "Move your cursor to the top-left corner of the game board and press Enter.")
        x1, y1 = pyautogui.position()
        messagebox.showinfo("Info", "Now move your cursor to the bottom-right corner of the game board and press Enter.")
        x2, y2 = pyautogui.position()

        # Save the marked region coordinates
        self.board_region = (x1, y1, x2 - x1, y2 - y1)
        messagebox.showinfo("Success", "Game board marked! Now process it.")
    
    def process_gameboard(self):
        if self.board_region:
            # Use logic.py to process the board and detect tile colors
            tiles = self.logic.divide_and_detect_tiles(self.board_region)
            print("Tiles processed. Now use the solver logic.")
            # Here you would use solver logic to provide the next guess
        else:
            messagebox.showerror("Error", "You need to mark the game board first.")

# Run GUI
if __name__ == "__main__":
    from logic import WordleLogic  # Import logic from the core logic file

    root = tk.Tk()
    root.title("Wordle Solver")
    logic = WordleLogic()
    app = WordleGUI(root, logic)
    root.mainloop()
