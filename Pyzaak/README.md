# Pyzaak
A GUI-based card game similar to blackjack. Originally found in the Bioware game Star Wars: Knights of the Old Republic.
This sub-project is focused on an implementation with Python rather than C#.

# Game rules:
Pazaak plays like balckjack; each player is attemptimg to score as close to a value as they can without going over. In blackjack, the target score is 21, while in Pazaak, the target score is 20.
Pazaak also adds a hand of cards for each player that can adjust their score value. These cards can add or remove points from a players score to help that player acheive the target of 20 points.
## Setup:
The game is played with a "table deck" which contains cards numbered from 1 to 10 (typically four of each number, but technically there is no limit to the table deck size).
Each player selects ten cards to create their own "side deck". From these ten cards, four are randomly drawn at the start of a game to create the player's hand.
At the start of a game, each player draws a card from the table deck. The player that draws the highest number takes the first turn in each round. Ties are resolved with a redraw.
## Gameplay:
Each game consist of rounds where the players draw and play cards to acquire 20 points without going any higher.
Each round, players alternate turns taking the following actions:
- Draw a card from the table deck, placing it face-up on the table and adding the number to their score.
- Either
    - Play a card from their hand, placing it face-up on the table and adding (or subtracting, based on the card) the number to their score.
    - End their turn to pass to the other player.
    - "Stand" to lock in their score and play no more cards for the round.
Turns continue alternating until a player has won the round. Ties are not counted for either player. Rounds continue until a player has won three rounds.
A player may only play one card from their hand per turn. Cards played from a player's hand are not replaced in that game.
## Victory:
A player wins a round by
- Outscoring; a player reaches 20 while their opponent reaches a lower score.
- Busting; a player wins by default when their opponent scores higher than 20.
A player wins a game when they have won three rounds.

[Game and rules source](https://starwars.fandom.com/wiki/Pazaak/Legends)