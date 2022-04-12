import discord
import os
import random
import typing
from replit import db
from keep_alive import keep_alive

client = discord.Client()

###############################################
##   TAR Mina Mina (This Time For Africa)    ##
##            Friday Bot Codes               ##
###############################################

# List of Teams
teams = [
    "TEST", 
    "BARDAGASCAR", 
    "BORA BOYS", 
    "BREWHAHA", 
    "DELTA NU SLUTS",
    "GLITTER AND BE GAY", 
    "HAKUNA MATATA", 
    "LOOSE HOLES", 
    "PIATTOS",
    "RED CARABAO", 
    "SAFARI BESTIES", 
    "TEAM BUKTU", 
    "TOTE BAG", 
    "VOUGH RATT"
]

# LEG 07 Wordle Words
wordleRange = 20
wordleTryLimit = 4
wordleWinCondition = 3
wordleBoothVisitLimit = 8
wordleWords = [
  "RAVEN",
  "COAST",
  "LUNGE",
  "POWER",
  "CLOUT",
  "SALTY",
  "SHOAL",
  "MOUND",
  "HAREM",
  "LATCH",
  "BLACK",
  "GRACE",
  "SHARK",
  "GAUZE",
  "EARTH",
  "PORCH",
  "BASIC",
  "ARSON",
  "UNDER",
  "ISLET"
]

# LEG 05 List of allowed ingredients
ingredients = [
    "CACAO",
    "CINNAMON",
    "LAVENDER",
    "MILK",
    "BUTTER",
    "VANILLA"
]

# LEG 05 Rolas Island Map 5x5 Rows
mapRows = ["S", "A", "B", "C", "D", "E"]

# LEG 05 Coordinates of Unwelcome Islands
unwelcomeVinylList = [
  {"set": "TEST", "coordinates": ["E1", "E5", "D2", "D5", "C1", "C4", "C5", "B3", "B4", "B5", "A2", "A3"]},
  {"set": "BARDAGASCAR", "coordinates": ["E1", "E5", "D2", "D5", "C1", "C4", "C5", "B3", "B4", "B5", "A2", "A3"]}, #yellow
  {"set": "DELTA NU SLUTS", "coordinates": ["E1", "E5", "D2", "D4", "C1", "C2", "C3", "B1", "B2", "B5", "A3", "A4"]}, #pink
  {"set": "GLITTER AND BE GAY", "coordinates": ["E1", "E5", "D3", "D4", "C1", "C2", "C4", "B1", "B3", "B5", "A1", "A4"]}, #darkblue
  {"set": "HAKUNA MATATA", "coordinates": ["E1", "E5", "D1", "D3", "C3", "C4", "C5", "B2", "B3", "B4", "A2", "A5"]}, #green
  {"set": "LOOSE HOLES", "coordinates": ["E1", "E5", "D3", "D5", "C2", "C3", "C4", "B1", "B2", "B4", "A2", "A4"]}, #orange
  {"set": "RED CARABAO", "coordinates": ["E1", "E5", "D2", "D3", "C1", "C4", "C5", "B1", "B2", "B5", "A1", "A5"]}, #red
  {"set": "TEAM BUKTU", "coordinates": ["E1", "E5", "D2", "D5", "C1", "C3", "C4", "B1", "B2", "B3", "A3", "A5"]}, #lightblue
  {"set": "VOUGH RATT", "coordinates": ["E1", "E5", "D1", "D4", "C2", "C3", "C5", "B2", "B4", "B5", "A1", "A3"]} #gray
]

# LEG 05 Weather Event Masterlist
# EventType: (0)ADJUST or (1)COMPARE
# If (0)ADJUST, increase/decrease canoe strength.
# If (1)COMPARE, check if canoe strength is enough.
weatherEvents = [
  {"id": 1, "name": "Lightning Barrage", "effectType": 1, "value": 50, "description": "A powerful lightning barrage wrecks and burns the canoe. You were thrown back to the shores, barely alive."},

{"id": 2, "name": "Maelstrom", "effectType": 1, "value": 25, "description": "A violent, rogue maelstrom threatens your canoe! The wooden hull is creeking! If your canoe strength is 24 or less, your boat will be destroyed."},

{"id": 3, "name": "Tsunami", "effectType": 1, "value": 24, "description": "The tsunami warning has been triggered! You have been warned. The boat is in the line of danger. Any canoe with strength of 23 or less, will be destroyed."},

{"id": 4, "name": "Whirlpool", "effectType": 1, "value": 23, "description": "The current of the whirlpool is pulling your boat in. You desperately paddle to avoid being sucked in. If your canoe strength is 22 or less, your boat will be destroyed."},

{"id": 5, "name": "Storm", "effectType": 1, "value": 22, "description": "You are expected to be in the eye of the storm. You can manage to dodge it by staying within, but all canoes with a strength of 21 or less will not be able to survive."},

{"id": 6, "name": "Hail", "effectType": 1, "value": 21, "description": "A relentless hail storm pours boulders all over the sky. If your canoe is strong and swift, it can dodge. However, canoes with a strength of 20 or less will have no shot at surviving."},

{"id": 7, "name": "Solar Flare", "effectType": 1, "value": 20, "description": "As you near the equator, the direct rays of the sun are piercing. In fact, the sun has reached its solar maxima and has released a solar flare. If your boat is poorly built with a strength of 19 or less, the sun will melt your canoe away."},

{"id": 8, "name": "Eclipse", "effectType": 1, "value": 19, "description": "An eclipse happens pulling the water a little harder. The tides are relentless and pelts your canoe. However, a good canoe can withstand this beating. Those with strength of 18 or less will say goodbye to their canoe."},

{"id": 9, "name": "Storm Surge", "effectType": 1, "value": 18, "description": "Storm surge is predicted by fishing vessels and are getting away. However, it’s easy to survive if your canoe is strong. Those with strength of 17 or less will not live to tell the tale."},

{"id": 10, "name": "Underwater Volcano", "effectType": 1, "value": 19, "description": "An underwater volcano exploded beneath the surface of the ocean sector you’re in! Poorly-made canoes would stand no chance, if your strength is 18 or less."},

{"id": 11, "name": "Thick Fog", "effectType": 1, "value": 17, "description": "Thick fog is covering the surrounding area, as gaseous compounds start to infiltrate the canoe’s body. If there are holes and leaks from poor construction with strength of 16 or less, the canoe would melt in acid."},

{"id": 12, "name": "Ashfall", "effectType": 1, "value": 16, "description": "Ashfall rains down from an island volcano eruption. Superheated rocks are hurled like projectiles all over your ocean sector. If your canoe has a strength of 15 or less, the canoe will tear away."},

{"id": 13, "name": "Shark Attack", "effectType": 0, "value": -3, "description": "A great white shark appears out of nowhere and bites a huge chunk off of your canoe. Your canoe strength went from [N] to [N-3]."},

{"id": 14, "name": "Woodpeckers", "effectType": 0, "value": -1, "description": "Migratory birds start circling around your canoe - and these bands of woodpeckers drill holes to your canoe. Its strength went from [N] to [N-1]."},

{"id": 15, "name": "Close Shave", "effectType": 0, "value": -2, "description": "You have a close shave with a fishing vessel, tearing away chunks of wood and metalworks in your canoe. Its strength went from [N] to [N-2]."},

{"id": 16, "name": "Rodents", "effectType": 0, "value": -2, "description": "Having forgotten to clean the canoe bottom, those rodents managed to tear away chunks of it piece by piece and causing your canoe to have holes on the bottom. The strength went from [N] to [N-2]."},

{"id": 17, "name": "Pirates", "effectType": 0, "value": -4, "description": "A pirate ship chases you to the ends of the ocean. The pirates, drunk, mad, and angry, using their cutlass, severely damages your boat, takes out the metalworks, and laughs at you. The strength went from [N] to [N-4]."},

{"id": 18, "name": "In Heat", "effectType": 0, "value": -1, "description": "Because you are alone and in heat, you had passionate SEX with your teammate. However, you went so hard that you destroyed one of the wooden encasement of the canoe. The canoe strength went from  [N] to [N-1]."},

{"id": 19, "name": "Rocky Outcrop", "effectType": 0, "value": -3, "description": "You were busy sightseeing when you collided hard with a rocky outcrop. Your teammate is mad at you because the canoe strength went from [N] to [N-3]."},

{"id": 20, "name": "Dents and Gaps", "effectType": 0, "value": -2, "description": "Untreated dents and gaps in the wooden construction of the canoe proved to weaken the canoe little by little. The canoe strength went from [N] to [N-2]."},

{"id": 21, "name": "Cameramen Sabotage", "effectType": 0, "value": -3, "description": "The camera crew hates your team and thus they decided to sabotage your canoe, so they can hopefully see you eliminated. The canoe strength went from [N] to [N-3]."},

{"id": 22, "name": "Waka Waka", "effectType": 0, "value": -1, "description": "You practiced dancing the theme song of the race,  “Waka Waka (This Time For Africa)”. You did not know that each time you jumped or grooved, the canoe strength went from [N] to [N-1]."},

{"id": 23, "name": "Mermaid", "effectType": 0, "value": -2, "description": "A poor mermaid purposely lured you into her cove to take away precious metalwork. You were gullible because she is beautiful and your canoe which had the strength of [N] is now just [N-2]."},

{"id": 24, "name": "Ballistic Missile", "effectType": 0, "value": -4, "description": "A Russian ballistic missile misfires and hits your canoe straight on. You got away with just bruises and second-degree burns. The canoe strength went from [N] to [N-4]."},

{"id": 25, "name": "Compliance Check", "effectType": 0, "value": 2, "description": "A compliance check from the marines for COVID-19 inadvertently pointed out an error in your woodworking and corrected it. Your canoe strength went from [N] to [N+2]."},

{"id": 26, "name": "Production Favorite", "effectType": 0, "value": 3, "description": "Secretly, production really loves your team. They secretly repair and strengthened your canoe without you seeing. You are the favorite. Your canoe strength went from [N] to [N+3]."},

{"id": 27, "name": "Irritating Teammate", "effectType": 0, "value": 2, "description": "You are so irritated with your teammate. All your team mate does is complain and magpabuhat. So tinali mo siya tight para di makagalaw. This pays off as your canoe is sturdier and more stable as the strength went from [N] to [N+2]."},

{"id": 28, "name": "Oil Spill", "effectType": 0, "value": 3, "description": "An oil spill shockingly happened before your eyes. Taking advantage of the situation, you scooped up the oil and poured it onto the metal bearings. Your canoe strength went from [N] to [N+3]."},

{"id": 29, "name": "Algae", "effectType": 0, "value": 1, "description": "You passed through a part of the ocean filled with algae. Because of that, the waterlogged part of your canoe became stronger. The strength went from [N] to [N+1]."},

{"id": 30, "name": "Lone Fisherman", "effectType": 0, "value": 2, "description": "A lone fisherman helped you with canoe-stabilizing techniques. You thank him for his efforts as your canoe strength went from [N] to [N+2]."},

{"id": 31, "name": "Spiritual Connection", "effectType": 0, "value": 3, "description": "In the middle of the ocean, everything felt right, and you feel the spiritual connection with God. You pray that the canoe can make it through this treacherous waters. God answered your prayers as the strength went from [N] to [N+3]."},

{"id": 32, "name": "Shakira Cruise", "effectType": 0, "value": 2, "description": "You meet Shakira by chance as she takes a cruise promoting her new album. She called up her shipwrights to fix your canoe up! The strength went from [N] to [N+2]"},

{"id": 33, "name": "Ocean Garbage Patch", "effectType": 0, "value": 1, "description": "You passed by an ocean garbage patch and recycled the PET bottles to have more stability in your canoe. The strength went from [N] to [N+1]."},

{"id": 34, "name": "Tequila Shots", "effectType": 0, "value": 1, "description": "You and your partner stripped NAKED and took tequila body shots on one another. The spilled tequila’s acidity was enough to harden the canoe layer. The canoe strength went from [N] to [N+1]."},

{"id": 35, "name": "Shore Advice", "effectType": 0, "value": 1, "description": "You and your partner took advice from the head shipwright at the shore - that’s why you can do maintenance yourselves. The canoe strength went from [N] to [N+1]."},

{"id": 36, "name": "We Love Ellis", "effectType": 0, "value": 0, "description": "You declare your love for host Ellis Medrano for bringing the world with the best lumpia across Africa and the world. Truly a culinary treasure, and a friend to count on in the toughest of times"},

{"id": 37, "name": "We Hate Carl", "effectType": 0, "value": 0, "description": "You declare your hatred for host Carl Dayandante who you are jealous of because he lives in a first-class elite executive village in Laguna, has a high-paying job, a fantastic work ethic, work-life balance that would put yours to shame."},

{"id": 38, "name": "Unzipped", "effectType": 0, "value": 0, "description": "It was a hot, sweltering day. Your partner’s sweat makes you thirst for more. So you unzipped both of your pants and the rest was history."},

{"id": 39, "name": "Toto", "effectType": 0, "value": 0, "description": "You listened to Toto’s Africa song. It was like the best song you have ever heard and perfectly encapsulated the race feeling."},

{"id": 40, "name": "Friendzoned", "effectType": 0, "value": 0, "description": "You confessed to your partner that you liked them before... and you love them now. And your partner friend zoned you. That’s sad, but the race moves forward."},

{"id": 41, "name": "Susan Africa", "effectType": 0, "value": 0, "description": "You saw a seaplane zooming in and discovers the legendary actress, Susan Africa, waving at you."},

{"id": 42, "name": "Dream", "effectType": 0, "value": 0, "description": "You dreamed about winning TAR MINA MINA and had a sudden realization that you can actually do that."},

{"id": 43, "name": "Laplap", "effectType": 0, "value": 0, "description": "Nag-smack kayo ng partner mo. Then, dinalaan ka sa leeg. Tapos nag-momol kayo. Buong kaluluwa. Laplap. Sarap."},

{"id": 44, "name": "We Love Arvin", "effectType": 0, "value": 0, "description": "You declare your love for host Arvin Gonzales who is so hot as hell, handsome, fucking cute, has an infectious smile, an aura of mystery and sex appeal. Truly, the best in the hosting team. "},

{"id": 45, "name": "We Love Friday", "effectType": 0, "value": 0, "description": "You declare your love for the genius that is Francis Bien Viernes who is ever relatable, always caring, reliable, organized, and truly innovative."}
]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

def displayWordleLetters(data):
  for index in range(0, 5):
    if data[index] == "*":
      data[index] = ":green_square:"
    elif data[index] == "-":
      data[index] = ":orange_square:"
    else:
      data[index] = ":white_large_square:"
  return ' '.join(data)

def find_all_char_positions(word: str, char: str) -> typing.List[int]:
    """Given a word and a character, find all the indices of that character."""
    positions = []
    pos = word.find(char)
    while pos != -1:
        positions.append(pos)
        pos = word.find(char, pos + 1)
    return positions

# test cases for find_all_char_positions
# find_all_char_positions("steer", "e") => [2, 3]
# find_all_char_positions("steer", "t") => [1]
# find_all_char_positions("steer", "q") => []

def compare(expected: str, guess: str) -> typing.List[str]:
    """Compare the guess with the expected word and return the output parse."""
    # the output is assumed to be incorrect to start,
    # and as we progress through the checking, update
    # each position in our output list
    output = ["_"] * len(expected)
    counted_pos = set()

    # first we check for correct words in the correct positions
    # and update the output accordingly
    for index, (expected_char, guess_char) in enumerate(zip(expected, guess)):
        if expected_char == guess_char:
            # a correct character in the correct position
            output[index] = "*"
            counted_pos.add(index)

    # now we check for the remaining letters that are in incorrect
    # positions. in this case, we need to make sure that if the
    # character that this is correct for was already
    # counted as a correct character, we do NOT display
    # this in the double case. e.g. if the correct word
    # is "steer" but we guess "stirs", the second "S"
    # should display "_" and not "-", since the "S" where
    # it belongs was already displayed correctly
    # likewise, if the guess word has two letters in incorrect
    # places, only the first letter is displayed as a "-".
    # e.g. if the guess is "floss" but the game word is "steer"
    # then the output should be "_ _ _ - _"; the second "s" in "floss"
    # is not displayed.
    for index, guess_char in enumerate(guess):
        # if the guessed character is in the correct word,
        # we need to check the other conditions. the easiest
        # one is that if we have not already guessed that
        # letter in the correct place. if we have, don't
        # double-count
        if guess_char in expected and \
                output[index] != "*":
            # first, what are all the positions the guessed
            # character is present in
            positions = find_all_char_positions(word=expected, char=guess_char)
            # have we accounted for all the positions
            for pos in positions:
                # if we have not accounted for the correct
                # position of this letter yet
                if pos not in counted_pos:
                    output[index] = "-"
                    counted_pos.add(pos)
                    # we only count the "correct letter" once,
                    # so we break out of the "for pos in positions" loop
                    break
    # return the list of parses
    return output

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  # TEST COMMAND ONLY
  if msg.startswith("$hellofriday"):
    await message.channel.send("Waka Waka, Eh Eh!")

  # ******************************
  # LEG 07: Lake Chad
  # Wordle
  #
  # [wordle-words]: list of wordle of words available to all
  # [team-wordle-words-taken]: list of wordle words owned by a team
  # [team-wordle-words-wrong]: list of wordle words owned by a team
  # [team-wordle-words-curr]: current wordle word team is solving
  # [team-wordle-words-try]: current wordle word attempt number
  # [team-wordle-guess]: TRUE if guessing, otherwise FALSE if selecting a booth
  # [team-wordle-visited]: number of visited stations.
  # ******************************

  if msg.startswith("$wordle-"):
    cmd = msg.split("$wordle-", 1)[1]
    print(cmd)

    # resets and initializes all team data
    if cmd == "reset-teams":
      for team in teams:
        db[team + "-wordle-words-taken"] = []
        db[team + "-wordle-words-wrong"] = []
        db[team + "-wordle-words-curr"] = 0
        db[team + "-wordle-words-try"] = 0
        db[team + "-wordle-guess"] = False
        db[team + "-wordle-visited"] = 0
        db["wordle-words"] = wordleWords
      await message.channel.send("Reset complete.")

    if cmd == "stats":
      embedVar = discord.Embed(title=":canoe: **WORDLE STATS** :canoe:",description="",color=0x0F0000)
      
      for team in teams:
        outputMsg = ""
        #currBoothNo = db[team + "-wordle-words-curr"]
        #currTryNo = db[team + "-wordle-words-try"]
        #guessStatus = db[team + "-wordle-guess"]
        solvedWords = db[team + "-wordle-words-taken"]
        bannedWords = db[team + "-wordle-words-wrong"]
        visitedBoothNo = db[team + "-wordle-visited"]

        #outputMsg = outputMsg + "Current booth: " + str(currBoothNo) + "\n"
        outputMsg = outputMsg + "Visited booths: " + str(visitedBoothNo) + "\n"
        outputMsg = outputMsg + "Banned booths: "
        bannedMsg = ""
        for word in bannedWords:
          bannedMsg = bannedMsg + str(word) + " "
        outputMsg = outputMsg + bannedMsg + "\n"
        outputMsg = outputMsg + "Guessed words:\n"
        for word in solvedWords:
          outputMsg = outputMsg + word + "\n"

        teamName = team + " (" + str(len(solvedWords)) + ")"
        
        embedVar.add_field(name=teamName, value=outputMsg, inline=False)
        
      await message.channel.send(embed=embedVar)

    if cmd.startswith("select-booth "):
      author = message.author.display_name
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          team = role.name
      if team == "":
        await message.channel.send(":warning: **" + author + "**, you do not have permissions to join. Sorry.")
        return

      if db[team + "-wordle-guess"] == True:
        await message.channel.send(":warning: **" + author + "**, you solve your current word before switching!")
        return

      if db[team + "-wordle-visited"] > wordleBoothVisitLimit - 1 or len(db[team + "-wordle-words-taken"]) >= wordleWinCondition:
        await message.channel.send(":warning: **" + author + "**, game over for your team!")
        return
      
      boothNo = msg.split("select-booth ", 1)[1]
      if boothNo.isnumeric() == False or int(boothNo) < 1 or int(boothNo) > wordleRange:
        await message.channel.send(":warning: **" + author + "**, invalid input.")
        return

      boothNo = int(boothNo)
      wordleWordAnswer = db["wordle-words"][boothNo - 1]

      if boothNo in db[team + "-wordle-words-wrong"]:
        await message.channel.send(":warning: **" + author + "**, you are not allowed in this booth. Choose another.")
        return

      if wordleWordAnswer == "":
        await message.channel.send(":warning: **" + author + "**, this booth is already won by another team! Choose another booth.")
        return

      db[team + "-wordle-words-curr"] = boothNo
      db[team + "-wordle-words-try"] = wordleTryLimit
      db[team + "-wordle-visited"] = db[team + "-wordle-visited"] + 1
      db[team + "-wordle-guess"] = True
      await message.channel.send("**" + author + "**, you selected word Booth #" + str(boothNo) + ". Your team may now start solving.")
      return

    if cmd.startswith("solve "):
      author = message.author.display_name
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          team = role.name
      if team == "":
        await message.channel.send(":warning: **" + author + "**, you do not have permissions to join. Sorry.")
        return

      if db[team + "-wordle-guess"] == False:
        await message.channel.send(":warning: **" + author + "**, you must first select a booth!")
        return

      currWordleBoothNo = db[team + "-wordle-words-curr"]
      currWordleTryNo = db[team + "-wordle-words-try"]
      
      print("Booth No: " + str(currWordleBoothNo))
      print("Try No: " + str(currWordleTryNo))

      wordGuess = msg.split("solve ", 1)[1].upper()
      wordCorrect = db["wordle-words"][currWordleBoothNo - 1]

      if wordCorrect == "":
        db[team + "-wordle-words-curr"] = 0
        db[team + "-wordle-words-try"] = 4
        await message.channel.send(":warning: **" + author + "**, this word is taken. Choose another booth.")
        db[team + "-wordle-guess"] = False
        return

      if len(wordGuess) != 5 or wordGuess.isalpha() == False:
        await message.channel.send(":warning: **" + author + "**, invalid input.")
        return
      
      # Correct input, let us check
      guessList = compare(wordCorrect, wordGuess)
      win = guessList.count("*") == 5

      currWordleTryNo = currWordleTryNo - 1
      db[team + "-wordle-words-try"] = currWordleTryNo
      outputMsg = "**" + author + "**, you guessed **" + wordGuess + "**:\n"
      outputMsg = outputMsg + displayWordleLetters(guessList) + "\n"

      if win == True:
        db["wordle-words"][currWordleBoothNo - 1] = ""
        correctWords = db[team + "-wordle-words-taken"]
        correctWords.append(str(currWordleBoothNo) + " - " +  wordCorrect)
        db[team + "-wordle-words-taken"] = correctWords
        db[team + "-wordle-guess"] = False
        if (len(correctWords) < wordleWinCondition):
          outputMsg = outputMsg + "Congratulations! Go to the next booth!\n"
        else:
          outputMsg = outputMsg + "Congratulations, **" + team + "**! You have guessed three words correctly! Screenshot this message and send to your Team GC to get your next clue!\n"
        outputMsg = outputMsg + "# of Correct Words: " + str(len(correctWords)) + " out of " + str(wordleWinCondition) + "\n"
        outputMsg = outputMsg + "# of Visited Booths: " + str(db[team + "-wordle-visited"]) + " out of " + str(wordleBoothVisitLimit)
      else:
        if currWordleTryNo <= 0:
          wrongWords = db[team + "-wordle-words-wrong"]
          wrongWords.append(currWordleBoothNo)
          db[team + "-wordle-words-wrong"] = wrongWords
          db[team + "-wordle-guess"] = False
          visitedBooths = db[team + "-wordle-visited"]
          if visitedBooths + 1 > wordleBoothVisitLimit:
            outputMsg = outputMsg + "**" + author + "**, game over! You have reached the specified limit of booths to visit! Screenshot this message and send to your Team GC to get your next instructions!"
          else:
            outputMsg = outputMsg + "**" + author + "**, you have reached the try limit for this word! Find another station!\n"
          outputMsg = outputMsg + "# of Correct Words: " + str(len(db[team + "-wordle-words-taken"])) + " out of " + str(wordleWinCondition) + "\n"
          outputMsg = outputMsg + "# of Visited Booths: " + str(db[team + "-wordle-visited"]) + " out of " + str(wordleBoothVisitLimit)
        else:
          outputMsg = outputMsg + "Attempts left: **" + str(currWordleTryNo) + "**"
    
      await message.channel.send(outputMsg)
      
  # ******************************
  # LEG 05: Sao Tome and Principe
  # Rolas Island Sailing
  #
  # [team-canoe-strength]: boat strength
  # [team-canoe-rolls]: last three rolls
  # [team-sail-row]: A-E location, S if SHORE
  # [team-sail-col]: 1-5 location, 0 if SHORE
  # [team-canoe-lock]: true / false
  # ******************************
  if msg.startswith("$canoe-"):
    cmd = msg.split("$canoe-", 1)[1]
    print(cmd)

    # resets and initializes all team data
    if cmd == "reset-teams":
      for team in teams:
        db[team + "-canoe-rolls"] = []
        db[team + "-canoe-strength"] = 0
        db[team + "-sail-row"] = "S"
        db[team + "-sail-col"] = 0
        db[team + "-canoe-lock"] = False
      await message.channel.send("All boats into shore. Data reset complete.")

    if cmd == "stats":
      embedVar = discord.Embed(title=":canoe: **ROLES ISLAND CANOE STATS** :canoe:",description="",color=0x0F0000)
      
      for team in teams:
        outputMsg = ""
        canoeHistoryList = db[team + "-canoe-rolls"]
        canoeStrength = db[team + "-canoe-strength"]
        canoeIsLocked = db[team + "-canoe-lock"]
        sailLocCol = db[team + "-sail-col"]
        sailLocRow = db[team + "-sail-row"]
        
        outputMsg = outputMsg + "Canoe Strength: " + ' '.join(map(str, canoeHistoryList)) + " = " + str(canoeStrength) + "\n"
        if canoeIsLocked == False:
          canoeStatus = ":hammer_pick: Building..."
        else:
          coor = "SHORE"
          if sailLocRow != "S" and sailLocRow != "E":
            coor = sailLocRow + str(sailLocCol)
          canoeStatus = ":sailboat: Sailing at " + coor
          if sailLocRow == "E":
            canoeStatus = ":white_check_mark: Reached Pitstop!"
  
        teamName = team + " - " + canoeStatus + ""
        
        embedVar.add_field(name=teamName, value=outputMsg, inline=False)
        
      await message.channel.send(embed=embedVar)

    if cmd == "build":
      author = message.author.display_name
      teamPosition = ""
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          team = role.name
        if role.name == "LEFT" or role.name == "RIGHT":
          teamPosition = role.name
      if team == "" or teamPosition == "":
        await message.channel.send(":warning: **" + author + "**, you do not have permissions to join. Sorry.")
        return
      
      canoeLock = db[team + "-canoe-lock"]
      if canoeLock == True:
        await message.channel.send(":warning: **" + author + "**, your team is already sailing!")
        return

      if teamPosition == "RIGHT":
        await message.channel.send(":warning: **" + author + "**, only your partner can build!")
        return

      roll10 = random.randint(1, 10)
      
      canoeHistoryList = db[team + "-canoe-rolls"]
      if len(canoeHistoryList) > 2:
        canoeHistoryList.pop(0)
      
      canoeHistoryList.append(roll10)
      
      db[team + "-canoe-rolls"] = canoeHistoryList
      outputMsg = ":hammer_pick:** BUILDING... **:hammer_pick:\n**" + author + "** :game_die: rolled a **" + str(roll10) + "**!\n"
      outputMsg = outputMsg + "Your :canoe: canoe's current strength is: **" + str(sum(canoeHistoryList)) + "**"
      await message.channel.send(outputMsg)

    if cmd == "lock":
      author = message.author.display_name
      teamPosition = ""
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          team = role.name
        if role.name == "LEFT" or role.name == "RIGHT":
          teamPosition = role.name
      if team == "" or teamPosition == "":
        await message.channel.send(":warning: **" + author + "**, you do not have permissions to join. Sorry.")
        return

      canoeLock = db[team + "-canoe-lock"]
      if canoeLock == True:
        await message.channel.send(":warning: **" + author + "**, your team is already sailing!")
        return

      if teamPosition == "RIGHT":
        await message.channel.send(":warning: **" + author + "**, only your partner can lock!")
        return

      db[team + "-canoe-lock"] = True
      canoeHistoryList = db[team + "-canoe-rolls"]
      db[team + "-canoe-strength"] = sum(canoeHistoryList)
      await message.channel.send(":lock:** LOCKING... **:lock:\n**" + author + "**, success! Your team is ready to sail! Your :canoe: canoe strength is: **" + str(sum(canoeHistoryList)) + "**")

    if cmd.startswith("sail "):
      author = message.author.display_name
      teamPosition = ""
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          team = role.name
        if role.name == "LEFT" or role.name == "RIGHT":
          teamPosition = role.name
      if team == "" or teamPosition == "":
        await message.channel.send(":warning: **" + author + "**, you do not have permissions to join. Sorry.")
        return

      if db[team + "-canoe-lock"] == False:
        await message.channel.send(":warning: **" + author + "**, your :canoe: canoe must be locked first!")
        return

      if teamPosition == "LEFT":
        await message.channel.send(":warning: **" + author + "**, only your partner can sail!")
        return
        
      loc = msg.split("sail ", 1)[1]
      nextRow = loc[0]
      nextCol = loc[1]

      currRow = db[team + "-sail-row"]
      currCol = db[team + "-sail-col"]
      if nextRow.isalpha() == False or nextCol.isnumeric() == False or nextRow not in mapRows or mapRows.index(currRow) + 1 != mapRows.index(nextRow):
        await message.channel.send(":warning: **" + author + "**, invalid coordinates! Try again.")
        return

      #Perform weather event here
      weatherRandId = random.randint(1, 45)
      weatherDetails = list(filter(lambda x:x["id"] == weatherRandId, weatherEvents))
      weatherName = weatherDetails[0]["name"]
      weatherValue = weatherDetails[0]["value"]
      weatherEffectType = weatherDetails[0]["effectType"]
      weatherDesc = weatherDetails[0]["description"]

      canoeStr = db[team + "-canoe-strength"]

      embedVar = discord.Embed(title=":canoe: ** " + team + "'s CANOE IS SAILING! :sailboat: ** :canoe:",description="",color=0x0F0000)
      
      #One part for coordinates
      if currRow == "S":
        currCoor = "Shore"
      else:
        currCoor = currRow + str(currCol)
      movementValue = author + ", you moved from " + currCoor + " to " + nextRow + str(nextCol)
      movementValue = movementValue + "\n Current Canoe Strength: **" + str(canoeStr) + "**"
      embedVar.add_field(name=":sailboat: MOVEMENT :sailboat:", value=movementValue, inline=False)

      #One part for weather
      weatherUpdate = "**" + weatherName + "**\n" + weatherDesc + "\n"
      embedVar.add_field(name=":cloud::sunny: WEATHER :cloud::sunny:", value=weatherUpdate, inline=False)

      origCanoeStr = canoeStr
      
      canoeSunk = False
      if weatherEffectType == 0:
        canoeStr = canoeStr + weatherValue
        if canoeStr <= 0:
          canoeSunk = True
      else:
        if canoeStr < weatherValue:
          canoeSunk = True

      #One part for canoe's destruction
      if canoeSunk == True:
        db[team + "-sail-row"] = "S"
        db[team + "-sail-col"] = 0
        db[team + "-canoe-rolls"] = []
        db[team + "-canoe-strength"] = 0
        db[team + "-canoe-lock"] = False
        valueWeather = "Oh no! You did not survive the weather! **" + author + "** (**" + team + "**), go back to shore and build your canoe!\n"
        valueWeather = valueWeather + currCoor + " :arrow_right: Shore"
        embedVar.add_field(name=":warning: EVENT :warning:", value=valueWeather, inline=False)
        await message.channel.send(embed=embedVar)
        return

      #One part for canoe's adjusted values
      canoeValue = str(origCanoeStr) + ' :arrow_right: ' + str(canoeStr)
      embedVar.add_field(name=":canoe: CANOE STATS :canoe:", value=canoeValue, inline=False)

      #Checking of unwelcome islands
      invalidList = list(filter(lambda x:x["set"] == team, unwelcomeVinylList))
      invalidListCoor = invalidList[0]["coordinates"]
      if loc in invalidListCoor:
        db[team + "-sail-row"] = "S"
        db[team + "-sail-col"] = 0
        db[team + "-canoe-rolls"] = []
        db[team + "-canoe-strength"] = 0
        db[team + "-canoe-lock"] = False
        unwelcomeValue = "You have landed in an unwelcome island! **" + author + "** (**" + team + "**) Get out of here! Go back to shore and build your destroyed canoe again!\n"
        unwelcomeValue = unwelcomeValue + currCoor + " :arrow_right: Shore"
        embedVar.add_field(name=":warning: EVENT :warning:", value=unwelcomeValue, inline=False)
        await message.channel.send(embed=embedVar)
        return

      db[team + "-sail-row"] = nextRow
      db[team + "-sail-col"] = nextCol
      db[team + "-canoe-strength"] = canoeStr

      if nextRow == "E":
        pitstopValue = "Congratulations, you have reached **ROLAS ISLAND**. The next instructions are posted on your Team GC!"
        embedVar.add_field(name=":white_check_mark: EVENT :white_check_mark:", value=pitstopValue, inline=False)
      else:
        movementValue = "You have reached the island on " + nextRow + str(nextCol) + ". Keep on sailing!"
        embedVar.add_field(name=":island: CURRENT ISLAND :island:", value=movementValue, inline=False)
        
      await message.channel.send(embed=embedVar)

  # ******************************
  # LEG 05: Sao Tome and Principe
  # Cacao Roadblock
  # ******************************
  if msg.startswith("$choco-"):
    cmd = msg.split("$choco-", 1)[1]
    print(cmd)

    if cmd == "reset-ingredients":
      db["choco-active"] = False
      for team in teams:
        db[team + "-choco-ingredients"] = []
      await message.channel.send("All teams' ingredients list has been reset")

    if cmd == "reset-round":
      db["choco-active-ingredients"] = {}
      db["choco-recap-list"] = []
      db["choco-active"] = False
      await message.channel.send("Round has been reset.")

    if cmd == "list":
      embedVar = discord.Embed(title=":chocolate_bar: **CHOCOLATE INGREDIENT LIST** :chocolate_bar:",description="",color=0x0F0000)
      
      for team in teams:
        chocoIngredientList = db[team + "-choco-ingredients"]
        chocoIngredientCtr = len(chocoIngredientList)
        chocoIngredientMsg = ""
        
        if chocoIngredientCtr == 0:
          chocoIngredientMsg = "None.\n\n"
  
        for chocoIngredient in chocoIngredientList:
          chocoIngredientMsg = chocoIngredientMsg + chocoIngredient + " "
  
        teamName = team + " (" + str(chocoIngredientCtr) + ")"
        if chocoIngredientCtr >= 6:
          teamName = ":white_check_mark: " + teamName
        
        embedVar.add_field(name=teamName, value=chocoIngredientMsg, inline=False)
        
      await message.channel.send(embed=embedVar)

    if cmd == "set":
      #automatically generate a list of ingredients
      ingredientCtr = random.randint(3, 6)
      validIngredientsList = []
      db["choco-recap-list"] = []
      outputMsg = "No. of Ingredients: " + str(ingredientCtr) + "\n\n**Added ingredients**:\n"
      while ingredientCtr > 0:
        pickedIngredient = random.choice(ingredients)
        outputMsg = outputMsg + pickedIngredient + "\n"
        validIngredientsList.append(pickedIngredient)
        ingredientCtr = ingredientCtr - 1

      db["choco-active"] = True
      db["choco-active-ingredients"] = validIngredientsList
      await message.channel.send(outputMsg)

    if cmd.startswith("set-ingredients"):
      chocoIngredients = msg.split("$choco-set-ingredients ", 1)[1]
      ingredientsList = chocoIngredients.split(" ")
      validIngredientsList = []
      outputMsg = ""
      for ingredient in ingredientsList:
        if ingredient in ingredients:
          validIngredientsList.append(ingredient)
          outputMsg = outputMsg + ingredient + "\n"
      db["choco-active-ingredients"] = validIngredientsList
      db["choco-recap-list"] = []
      db["choco-active"] = True
      outputMsg = "**Added ingredients:**\n" + outputMsg
      await message.channel.send(outputMsg)

    if cmd.startswith("claim "):
      print(db["choco-active-ingredients"])
      outputMsg = ""
      val = msg.split("claim ", 1)[1]
      author = message.author.display_name

      if db["choco-active"] == False:
        await message.channel.send("You are not allowed to do that at the moment. Please wait for the hosts' cue.")
        return

      if val not in ingredients:
        return

      rolePermitted = False
      team = ""
      for role in message.author.roles:
        if role.name in teams:
          rolePermitted = True
          team = role.name
          break
      if rolePermitted == False:
        await message.channel.send(author + ", you are not permitted to join. Sorry.")
        return
        
      print(len(db["choco-active-ingredients"]))
      if len(db["choco-active-ingredients"]) == 0:
        outputMsg = "No more ingredients left!\n"
        for recap in db["choco-recap-list"]:
          outputMsg = outputMsg + recap + "\n"
        db["choco-active"] = False
        return

      if (val in db[team + "-choco-ingredients"]):
        await message.channel.send(author + ", you already have " + val)
        return
 
      if val in db["choco-active-ingredients"]:
        newChocoIngredientList = db["choco-active-ingredients"]
        newChocoIngredientList.remove(val)
        outputMsg = "**" + author + "** has claimed **" + val + "**!"
        newTeamList = db[team + "-choco-ingredients"]
        newTeamList.append(val)
        db[team + "-choco-ingredients"] = newTeamList
        newRecapList = db["choco-recap-list"]
        newRecapList.append(outputMsg)
        db["choco-recap-list"] = newRecapList
        
        if len(db["choco-active-ingredients"]) == 0:
          outputMsg = outputMsg + "\n\nNo more ingredients left!\n"
          for recap in db["choco-recap-list"]:
            outputMsg = outputMsg + recap + "\n"
          db["choco-active"] = False
      
      await message.channel.send(outputMsg)

    if cmd == "recap":
      outputMsg = "Recap:"
      for recap in db["choco-recap-list"]:
        outputMsg = outputMsg + recap + "\n"
      
      await message.channel.send(outputMsg)

keep_alive()
client.run(os.getenv("TOKEN"))
