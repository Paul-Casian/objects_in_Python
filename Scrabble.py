letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

### Creating a object for letters and points
letters_to_points = {key:value for key,value in zip(letters,points)}
#print(letters_to_points)
letters_to_points[" "] = 0
#print(letters_to_points)

### Functin to get a word points
def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letters_to_points.keys():
            point_total += letters_to_points[letter]
    return point_total
###
players_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
players_to_point = {}
for player,words in players_to_words.items():
    player_points = 0
    for word in words:
        player_points = player_points + score_word(word)
    players_to_point[player] = [player_points]
print(players_to_point)