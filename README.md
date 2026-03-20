# ♠️ Texas Hold’em Poker Engine (Python)

A command-line Texas Hold’em poker engine built in Python using object-oriented programming. This project simulates core poker mechanics including dealing, community cards, and hand evaluation from a 7-card pool.

---

## 🚀 Features

- 52-card deck with suits and ranks  
- Random deck shuffling  
- Player vs Dealer setup  
- Flop, Turn, and River simulation  
- Interactive dealing system (`type "deal"` to continue)  

### 🃏 Hand Detection
- Pair  
- Two Pair  
- Three of a Kind  
- Four of a Kind  
- Full House  
- Straight  
- Flush  
- Straight Flush  
- Royal Flush  

---

## 🏗️ Project Structure

- **Player class**  
  Handles player cards, dealing, and display  

- **River class (inherits Player)**  
  Manages community cards (flop, turn, river)  

- **Game class**  
  Controls game flow and evaluates hands  

- **Deck**  
  Represented as a list of strings (e.g., `"A(heart)"`)  

---

## ⚙️ How to Run

1. Make sure Python 3 is installed  
2. Download or clone the repository  
3. Run the file:

```bash
python betterPoker.py
