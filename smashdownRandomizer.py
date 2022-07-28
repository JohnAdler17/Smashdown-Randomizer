#author: John Adler

from simplegraphics import *
#from threading import Thread
import random
import time
import sys

# 2 or more players

def main():
    closeApp = False
    characterRoster = [
        ["Mario", 'mario.png'],
        ["Donkey Kong", "dk.png"],
        ["Link", "link.png"],
        ["Samus", "samus.png"],
        ["Yoshi", "yoshi.png"],
        ["Kirby", "kirby.png"],
        ["Fox", "fox.png"],
        ["Pikachu", "pikachu.png"],
        ["Luigi", "luigi.png"],
        ["Ness", "ness.png"],
        ["Captain Falcon", "cptfalcon.png"],
        ["Jigglypuff", "jigglypuff.png"],
        ["Peach", "peach.png"],
        ["Bowser", "bowser.png"],
        ["Ice Climbers", "iceclimbers.png"],
        ["Sheik", "sheik.png"],
        ["Zelda", "zelda.png"],
        ["Dr. Mario", "drmario.png"],
        ["Pichu", "pichu.png"],
        ["Falco", "falco.png"],
        ["Marth", "marth.png"],
        ["Young Link", "younglink.png"],
        ["Ganondorf", "ganondorf.png"],
        ["Mewtwo", "mewtwo.png"],
        ["Roy", "roy.png"],
        ["Mr. Game & Watch", "gamewatch.png"],
        ["Meta Knight", "metaknight.png"],
        ["Pit", "pit.png"],
        ["Zero Suit Samus", "zerosuit.png"],
        ["Wario", "wario.png"],
        ["Snake", "snake.png"],
        ["Ike", "ike.png"],
        ["Pokemon Trainer", "trainer.png"],
        ["Diddy Kong", "diddykong.png"],
        ["Lucas", "lucas.png"],
        ["Sonic", "sonic.png"],
        ["King Dedede", "dedede.png"],
        ["Olimar", "olimar.png"],
        ["Lucario", "lucario.png"],
        ["R.O.B.", "rob.png"],
        ["Toon Link", "toonlink.png"],
        ["Wolf", "wolf.png"],
        ["Villager", "villager.png"],
        ["Mega Man", "megaman.png"],
        ["Wii Fit Trainer", "wiifit.png"],
        ["Rosalina & Luma", "rosalina.png"],
        ["Little Mac", "littlemac.png"],
        ["Greninja", "greninja.png"],
        ["Mii Brawler", "brawler.png"],
        ["Mii Swordfighter", "swordfighter.png"],
        ["Mii Gunner", "gunner.png"],
        ["Palutena", "palutena.png"],
        ["Pac-man", "pacman.png"],
        ["Robin", "robin.png"],
        ["Shulk", "shulk.png"],
        ["Bowser Jr.", "bowserjr.png"],
        ["Duck Hunt", "duckhunt.png"],
        ["Ryu", "ryu.png"],
        ["Cloud", "cloud.png"],
        ["Corrin", "corrin.png"],
        ["Bayonetta", "bayonetta.png"],
        ["Inkling", "inkling.png"],
        ["Ridley", "ridley.png"],
        ["Simon", "simon.png"],
        ["King K. Rool", "kkrool.png"],
        ["Isabelle", "isabelle.png"],
        ["Incineroar", "peach.png"],
        ["Piranha Plant", "piranha.png"],
        ["Joker", "joker.png"],
        ["Hero", "hero.png"],
        ["Banjo & Kazooie", "banjo.png"],
        ["Terry", "terry.png"],
        ["Byleth", "byleth.png"],
        ["Min Min", "minmin.png"],
        ["Steve", "steve.png"],
        ["Sephiroth", "sephiroth.png"],
        ["Pyra/Mythra", "pythra.png"],
        ["Kazuya", "kazuya.png"],
        ["Sora", "sora.png"],
        ["Dark Samus", "darksamus.png"],
        ["Daisy", "daisy.png"],
        ["Lucina", "lucina.png"],
        ["Chrom", "chrom.png"],
        ["Dark Pit", "darkpit.png"],
        ["Ken", "ken.png"],
        ["Richter", "richter.png"]
    ]

    #identical copy of characterRoster to be copied to characterRoster when restart is clicked
    backupRoster = [
        ["Mario", 'mario.png'],
        ["Donkey Kong", "dk.png"],
        ["Link", "link.png"],
        ["Samus", "samus.png"],
        ["Yoshi", "yoshi.png"],
        ["Kirby", "kirby.png"],
        ["Fox", "fox.png"],
        ["Pikachu", "pikachu.png"],
        ["Luigi", "luigi.png"],
        ["Ness", "ness.png"],
        ["Captain Falcon", "cptfalcon.png"],
        ["Jigglypuff", "jigglypuff.png"],
        ["Peach", "peach.png"],
        ["Bowser", "bowser.png"],
        ["Ice Climbers", "iceclimbers.png"],
        ["Sheik", "sheik.png"],
        ["Zelda", "zelda.png"],
        ["Dr. Mario", "drmario.png"],
        ["Pichu", "pichu.png"],
        ["Falco", "falco.png"],
        ["Marth", "marth.png"],
        ["Young Link", "younglink.png"],
        ["Ganondorf", "ganondorf.png"],
        ["Mewtwo", "mewtwo.png"],
        ["Roy", "roy.png"],
        ["Mr. Game & Watch", "gamewatch.png"],
        ["Meta Knight", "metaknight.png"],
        ["Pit", "pit.png"],
        ["Zero Suit Samus", "zerosuit.png"],
        ["Wario", "wario.png"],
        ["Snake", "snake.png"],
        ["Ike", "ike.png"],
        ["Pokemon Trainer", "trainer.png"],
        ["Diddy Kong", "diddykong.png"],
        ["Lucas", "lucas.png"],
        ["Sonic", "sonic.png"],
        ["King Dedede", "dedede.png"],
        ["Olimar", "olimar.png"],
        ["Lucario", "lucario.png"],
        ["R.O.B.", "rob.png"],
        ["Toon Link", "toonlink.png"],
        ["Wolf", "wolf.png"],
        ["Villager", "villager.png"],
        ["Mega Man", "megaman.png"],
        ["Wii Fit Trainer", "wiifit.png"],
        ["Rosalina & Luma", "rosalina.png"],
        ["Little Mac", "littlemac.png"],
        ["Greninja", "greninja.png"],
        ["Mii Brawler", "brawler.png"],
        ["Mii Swordfighter", "swordfighter.png"],
        ["Mii Gunner", "gunner.png"],
        ["Palutena", "palutena.png"],
        ["Pac-man", "pacman.png"],
        ["Robin", "robin.png"],
        ["Shulk", "shulk.png"],
        ["Bowser Jr.", "bowserjr.png"],
        ["Duck Hunt", "duckhunt.png"],
        ["Ryu", "ryu.png"],
        ["Cloud", "cloud.png"],
        ["Corrin", "corrin.png"],
        ["Bayonetta", "bayonetta.png"],
        ["Inkling", "inkling.png"],
        ["Ridley", "ridley.png"],
        ["Simon", "simon.png"],
        ["King K. Rool", "kkrool.png"],
        ["Isabelle", "isabelle.png"],
        ["Incineroar", "peach.png"],
        ["Piranha Plant", "piranha.png"],
        ["Joker", "joker.png"],
        ["Hero", "hero.png"],
        ["Banjo & Kazooie", "banjo.png"],
        ["Terry", "terry.png"],
        ["Byleth", "byleth.png"],
        ["Min Min", "minmin.png"],
        ["Steve", "steve.png"],
        ["Sephiroth", "sephiroth.png"],
        ["Pyra/Mythra", "pythra.png"],
        ["Kazuya", "kazuya.png"],
        ["Sora", "sora.png"],
        ["Dark Samus", "darksamus.png"],
        ["Daisy", "daisy.png"],
        ["Lucina", "lucina.png"],
        ["Chrom", "chrom.png"],
        ["Dark Pit", "darkpit.png"],
        ["Ken", "ken.png"],
        ["Richter", "richter.png"]
    ]

    draw_canvas()
    #This outer while loop is to make the back button function
    while closeApp == False:
        draw_player_number_selection()

        numPlayers = player_number_selection()
        
        draw_game_selection()
        game = game_selection()

        charsLeft = set_character_number(game)

        draw_canvas_elements(numPlayers)

        #inner while loop runs the game loop
        while closeApp == False:
            if charsLeft == 0:
                #write no characters left, returning to player selection
                draw_string("No characters left, return to player selection screen on click", 300, 75, 16)
                wait_for_click()
                clear_canvas()
                break
            if numPlayers == "1 Player":
                status = one_player_screen(characterRoster, charsLeft, backupRoster)
                if status == "Restart":
                    characterRoster = backupRoster
                    charsLeft = set_character_number(game)
                    
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)
                    continue
                elif status == "Back":
                    break
                else:
                    charsLeft -= 1
                    #draws circle and number of characters left in roster
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)

                    
            elif numPlayers == "2 Player":
                if status == "Restart":
                    characterRoster = backupRoster
                    charsLeft = set_character_number(game)
                    
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)
                    continue
                elif status == "Back":
                    break
                else:
                    charsLeft -= 1
                    #draws circle and number of characters left in roster
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)

                    
            elif numPlayers == "3 Player":
                if status == "Restart":
                    characterRoster = backupRoster
                    charsLeft = set_character_number(game)
                    
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)
                    continue
                elif status == "Back":
                    break
                else:
                    charsLeft -= 1
                    #draws circle and number of characters left in roster
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)

                    
            elif numPlayers == "4 Player":
                if status == "Restart":
                    characterRoster = backupRoster
                    charsLeft = set_character_number(game)
                    
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)
                    continue
                elif status == "Back":
                    break
                else:
                    charsLeft -= 1
                    #draws circle and number of characters left in roster
                    set_color("white")
                    draw_filled_rect(230, 10, 40, 30)
                    set_color("black")
                    draw_string(str(charsLeft), 250, 25, 25)
            
        #if back button is pressed, inner while loop is broken and outer while loop is continued to redraw the starting screen
        continue


def draw_canvas():
    canvas_size = 500
    open_canvas(canvas_size + 100, canvas_size)

def draw_canvas_elements(numPlayers):
    if numPlayers == "1 Player":
        draw_string("Characters Left:", 125, 25, 25)

        set_color("white")
        draw_filled_circle(250, 250, 128)

        draw_button(200, 400, 100, 40, "Restart", 20, "white")
        draw_button(350, 400, 100, 40, "Random", 20, "white")
        draw_button(50, 400, 100, 40, "Close", 20, "white")
        draw_button(10, 450, 80, 32, "Back", 20, "white")
        
    elif numPlayers == "2 Players":
        draw_string("Characters Left:", 125, 25, 25)

        set_color("white")
        draw_filled_circle(250, 250, 128)

        draw_button(200, 400, 100, 40, "Restart", 20, "white")
        draw_button(350, 400, 100, 40, "Random", 20, "white")
        draw_button(50, 400, 100, 40, "Close", 20, "white")
        draw_button(10, 450, 80, 32, "Back", 20, "white")

    elif numPlayers == "3 Players":
        draw_string("Characters Left:", 125, 25, 25)

        set_color("white")
        draw_filled_circle(250, 250, 128)

        draw_button(200, 400, 100, 40, "Restart", 20, "white")
        draw_button(350, 400, 100, 40, "Random", 20, "white")
        draw_button(50, 400, 100, 40, "Close", 20, "white")
        draw_button(10, 450, 80, 32, "Back", 20, "white")

    elif numPlayers == "4 Players":
        draw_string("Characters Left:", 125, 25, 25)

        set_color("white")
        draw_filled_circle(250, 250, 128)

        draw_button(200, 400, 100, 40, "Restart", 20, "white")
        draw_button(350, 400, 100, 40, "Random", 20, "white")
        draw_button(50, 400, 100, 40, "Close", 20, "white")
        draw_button(10, 450, 80, 32, "Back", 20, "white")

def draw_player_number_selection():
    set_background_color("maroon")
    draw_string("Select Number of Players:", 300, 30, 27)
    draw_button(100, 100, 100, 100, "1 Player", 20, "orange")
    draw_button(250, 100, 100, 100, "2 Players", 20, "red")
    draw_button(400, 100, 100, 100, "3 Players", 20, "light blue")
    draw_button(100, 250, 100, 100, "4 Players", 20, "gold")
    draw_button(50, 400, 100, 40, "Close", 20, "white")

def player_number_selection():
    #get click
    while True:
        wait_for_click()
        clickX = get_last_click_x()
        clickY = get_last_click_y()

        if clickX >= 100 and clickX <= 200 and clickY >= 100 and clickY <= 200:
            #button click graphic
            draw_button(100, 100, 100, 100, "1 Player", 20, "grey")
            time.sleep(0.1)
            draw_button(100, 100, 100, 100, "1 Player", 20, "orange")
        
            clear_canvas()
            return "1 Player"

        if clickX >= 250 and clickX <= 350 and clickY >= 100 and clickY <= 200:
            #button click graphic
            draw_button(250, 100, 100, 100, "2 Player", 20, "grey")
            time.sleep(0.1)
            draw_button(250, 100, 100, 100, "2 Player", 20, "red")
        
            clear_canvas()
            return "2 Player"

        if clickX >= 400 and clickX <=500 and clickY >= 100 and clickY <= 200:
            #button click graphic
            draw_button(400, 100, 100, 100, "3 Player", 20, "grey")
            time.sleep(0.1)
            draw_button(400, 100, 100, 100, "3 Player", 20, "light blue")
            clear_canvas()
            return "3 Player"

        if clickX >= 100 and clickX <= 200 and clickY >= 250 and clickY <= 350:
            #button click graphic
            draw_button(100, 250, 100, 100, "4 Player", 20, "grey")
            time.sleep(0.1)
            draw_button(100, 250, 100, 100, "4 Player", 20, "gold")
        
            clear_canvas()
            return "4 Player"
    
        if clickX >= 50 and clickX <= 150 and clickY >= 400 and clickY <= 440:
            #button click graphic
            draw_button(50, 400, 100, 40, "Close", 20, "grey")
            time.sleep(0.01)
            draw_button(50, 400, 100, 40, "Close", 20, "white")
        
            close_canvas()
            sys.exit()

def draw_game_selection():
    set_background_color("light blue")
    draw_string("Smashdown Randomizer", 300, 30, 30)
    draw_string("Select the Super Smash Bros. Game", 300, 75, 18)
    draw_button(100, 100, 100, 100, "Smash64", 20, "light green")
    draw_button(250, 100, 100, 100, "Melee", 20, "green")
    draw_button(400, 100, 100, 100, "Brawl", 20, "purple")
    draw_button(100, 250, 100, 100, "Sm4sh", 20, "azure")
    draw_button(250, 250, 100, 100, "Ultimate", 20, "pink")
    draw_button(50, 400, 100, 40, "Close", 20, "white")


def game_selection():
    #get click
    while True:
        wait_for_click()
        clickX = get_last_click_x()
        clickY = get_last_click_y()

        if clickX >= 100 and clickX <= 200 and clickY >= 100 and clickY <= 200:
            #Smash64
            #button click graphic
            draw_button(100, 100, 100, 100, "Smash64", 20, "grey")
            time.sleep(0.1)
            draw_button(100, 100, 100, 100, "Smash64", 20, "light green")
        
            clear_canvas()
            return "Smash64"

        if clickX >= 250 and clickX <= 350 and clickY >= 100 and clickY <= 200:
            #Melee
            #button click graphic
            draw_button(250, 100, 100, 100, "Melee", 20, "grey")
            time.sleep(0.1)
            draw_button(250, 100, 100, 100, "Melee", 20, "green")
        
            clear_canvas()
            return "Melee"

        if clickX >= 400 and clickX <=500 and clickY >= 100 and clickY <= 200:
            #Brawl
            #button click graphic
            draw_button(400, 100, 100, 100, "Brawl", 20, "grey")
            time.sleep(0.1)
            draw_button(400, 100, 100, 100, "Brawl", 20, "purple")
            clear_canvas()
            return "Brawl"

        if clickX >= 100 and clickX <= 200 and clickY >= 250 and clickY <= 350:
            #Sm4sh
            #button click graphic
            draw_button(100, 250, 100, 100, "Sm4sh", 20, "grey")
            time.sleep(0.1)
            draw_button(100, 250, 100, 100, "Sm4sh", 20, "azure")
        
            clear_canvas()
            return "Sm4sh"

        if clickX >= 250 and clickX <= 350 and clickY >= 250 and clickY <= 350:
            #Ultimate
            #button click graphic
            draw_button(250, 250, 100, 100, "Ultimate", 20, "grey")
            time.sleep(0.1)
            draw_button(250, 250, 100, 100, "Ultimate", 20, "pink")
        
            clear_canvas()
            return "Ultimate"
    
        if clickX >= 50 and clickX <= 150 and clickY >= 400 and clickY <= 440:
            #button click graphic
            draw_button(50, 400, 100, 40, "Close", 20, "grey")
            time.sleep(0.01)
            draw_button(50, 400, 100, 40, "Close", 20, "white")
        
            close_canvas()
            sys.exit()
        

#draws a button with a black outline at a position and size with specified text and button color
def draw_button(x, y, width, height, buttonText, textSize, buttonColor):
    set_color(buttonColor)
    draw_filled_rect(x, y, width, height)

    set_line_thickness(3)
    set_color("black")
    draw_line(x, y, x + width, y)
    draw_line(x, y + height, x + width, y + height)
    draw_line(x, y, x, y + height)
    draw_line(x + width, y, x + width, y + height)

    draw_string(buttonText, x + width/2, y + height/2, textSize)

#return a random integer depending on the game selected
#the less characters in the game, the less range the random function has
def random_character(maxCharacters):
    randInd = random.randint(0, maxCharacters)
    return randInd

def random_button_clicked(characterRoster, charsLeft):
    draw_button(350, 400, 100, 40, "Random", 20, "grey")
    time.sleep(0.08)
    draw_button(350, 400, 100, 40, "Random", 20, "white")
            
    randomCharacter = random_character(charsLeft)

    #print("Random Button Clicked")
    set_color("white")
    draw_filled_circle(250, 250, 128)
            
    set_color("black")
    draw_string(characterRoster[randomCharacter][0], 250, 325, 20)
           
    draw_image(characterRoster[randomCharacter][1], 250, 250)

    time.sleep(0.15)

    randomCharacter = random_character(charsLeft)

    set_color("white")
    draw_filled_circle(250, 250, 128)
            
    set_color("black")
    draw_string(characterRoster[randomCharacter][0], 250, 325, 20)
            
    draw_image(characterRoster[randomCharacter][1], 250, 250)

    time.sleep(0.18)

    randomCharacter = random_character(charsLeft)

    set_color("white")
    draw_filled_circle(250, 250, 128)
            
    set_color("black")
    draw_string(characterRoster[randomCharacter][0], 250, 325, 20)
            
    draw_image(characterRoster[randomCharacter][1], 250, 250)

    time.sleep(0.2)

    randomCharacter = random_character(charsLeft)

    set_color("white")
    draw_filled_circle(250, 250, 128)
            
    set_color("black")
    draw_string(characterRoster[randomCharacter][0], 250, 325, 20)
            
    draw_image(characterRoster[randomCharacter][1], 250, 250)

    time.sleep(0.4)

    randomCharacter = random_character(charsLeft)

    set_color("white")
    draw_filled_circle(250, 250, 128)
            
    set_color("black")
    draw_string(characterRoster[randomCharacter][0], 250, 325, 20)
            
    draw_image(characterRoster[randomCharacter][1], 250, 250)
    
    del characterRoster[randomCharacter]

    return "Random"

def set_character_number(game):
    if game == "Smash64":
            set_background_color("light green")
            return 12
    elif game == "Melee":
            set_background_color("green")
            return 26
    elif game == "Brawl":
            set_background_color("purple")
            return 42
    elif game == "Sm4sh":
            set_background_color("azure")
            return 61
    else:
            set_background_color("pink")
            return 85

def one_player_screen(characterRoster, charsLeft, backupRoster):
    #draws circle and number of characters left in roster
    set_color("white")
    draw_filled_rect(230, 10, 40, 30)
    set_color("black")
    draw_string(str(charsLeft), 250, 25, 25)

    #waits for click
    wait_for_click()
    clickX = get_last_click_x()
    clickY = get_last_click_y()
                
    #tests to see if click hit a button

    #restart button
    if clickX >= 200 and clickX <= 300 and clickY >= 400 and clickY <= 440:
        #print("Restart Button Clicked")
        draw_button(200, 400, 100, 40, "Restart", 20, "grey")
        time.sleep(0.1)
        draw_button(200, 400, 100, 40, "Restart", 20, "white")

        set_color("white")
        draw_filled_circle(250, 250, 128)
            
        return "Restart"

    #random button
    if clickX >= 350 and clickX <= 450 and clickY >= 400 and clickY <= 440:

        random_button_clicked(characterRoster, charsLeft)
            
    #close button 
    if clickX >= 50 and clickX <= 150 and clickY >= 400 and clickY <= 440:
        #button click graphic
        draw_button(50, 400, 100, 40, "Close", 20, "grey")
        time.sleep(0.01)
        draw_button(50, 400, 100, 40, "Close", 20, "white")
                
        close_canvas()
        sys.exit()

    #back button
    if clickX >= 10 and clickX <= 90 and clickY >= 450 and clickY <= 482:
        clear_canvas()
        return "Back"

main()
