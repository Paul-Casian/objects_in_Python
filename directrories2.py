tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}

spread["past"] = tarot.pop(13,"This card does not exist")
spread["present"] = tarot.pop(22,"This card does not exist")
spread["future"] = tarot.pop(10,"This card does not exist")

for key,value in spread.items():
    print("Your {0} is the {1} card.".format(key,value))
