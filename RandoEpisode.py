import random

Random_List = [1,2,3,4,5,6,7,8]

#Check to see what the user considers canon
print "Do you want to include TAS? (y/n)"
TASprompt = raw_input()
if TASprompt != 'y' and TASprompt != 'n':
    print "I only accept \"y\" or \"n\" as options. Restart the program and try again!"
    quit()
print "Do you want to include the core movies? (y/n)"
MOVprompt = raw_input()
if MOVprompt != 'y' and MOVprompt != 'n':
    print "I only accept \"y\" or \"n\" as options. Restart the program and try again!"
    quit()
print "Do you want to include the Kelvin timeline? (y/n)"
Kelvinprompt = raw_input()
if Kelvinprompt != 'y' and Kelvinprompt != 'n':
    print "I only accept \"y\" or \"n\" as options. Restart the program and try again!"
    quit()

#next 3 lines are just for testing
#MOVprompt = 'n'
#TASprompt = 'y'
#Kelvinprompt = 'n'

#include all options    
if MOVprompt == 'y' and TASprompt == 'y' and Kelvinprompt == 'y':
    number = random.choice(Random_List)
    
#exclude some options
if MOVprompt == 'n':
    Random_List.remove(7)
if TASprompt == 'n':
    Random_List.remove(2)
if Kelvinprompt == 'n':
    Random_List.remove(8)
   
   
number = random.choice(Random_List)
    


    

def TOS():
    season_number = random.randrange(1, 4)
    if season_number is 1:
        episode_number = random.randrange(1, 31)
        if episode_number is 1:
            sea_ep_code = 'TOS, s1e1'
            title = 'The Cage'
        if episode_number is 2:
            sea_ep_code = 'TOS, s1e2'
            title = 'The Man Trap'
        if episode_number is 3:
            sea_ep_code = 'TOS, s1e3'
            title = 'Charlie X'
        if episode_number is 4:
            sea_ep_code = 'TOS, s1e4'
            title = 'Where No Man Has Gone Before'
        if episode_number is 5:
            sea_ep_code = 'TOS, s1e5'
            title = 'The Naked Time'
        if episode_number is 6:
            sea_ep_code = 'TOS, s1e6'
            title = 'The Enemy Within'
        if episode_number is 7:
            sea_ep_code = 'TOS, s1e7'
            title = 'Mudd\'s Women'
        if episode_number is 8:
            sea_ep_code = 'TOS, s1e8'
            title = 'What Are Little Girls Made Of?'
        if episode_number is 9:
            sea_ep_code = 'TOS, s1e9'
            title = 'Miri'
        if episode_number is 10:
            sea_ep_code = 'TOS, s1e10'
            title = 'Dagger of the Mind'
        if episode_number is 11:
            sea_ep_code = 'TOS, s1e11'
            title = 'The Corbomite Maneuver'
        if episode_number is 12:
            sea_ep_code = 'TOS, s1e12'
            title = 'The Menagerie: Part I'
        if episode_number is 13:
            sea_ep_code = 'TOS, s1e13'
            title = 'The Menagerie: Part II'
        if episode_number is 14:
            sea_ep_code = 'TOS, s1e14'
            title = 'The Conscience of the King'
        if episode_number is 15:
            sea_ep_code = 'TOS, s1e15'
            title = 'Balance of Terror'
        if episode_number is 16:
            sea_ep_code = 'TOS, s1e16'
            title = 'Shore Leave'
        if episode_number is 17:
            sea_ep_code = 'TOS, s1e17'
            title = 'The Galileo Seven'
        if episode_number is 18:
            sea_ep_code = 'TOS, s1e18'
            title = 'The Squire of Gothos'
        if episode_number is 19:
            sea_ep_code = 'TOS, s1e19'
            title = 'Arena'
        if episode_number is 20:
            sea_ep_code = 'TOS, s1e20'
            title = 'Tomorrow = Yesterday'
        if episode_number is 21:
            sea_ep_code = 'TOS, s1e21'
            title = 'Court Martial'
        if episode_number is 22:
            sea_ep_code = 'TOS, s1e22'
            title = 'The Return of the Archons'
        if episode_number is 23:
            sea_ep_code = 'TOS, s1e23'
            title = 'Space Seed'
        if episode_number is 24:
            sea_ep_code = 'TOS, s1e24'
            title = 'A Taste of Armageddon'
        if episode_number is 25:
            sea_ep_code = 'TOS, s1e25'
            title = 'This Side of Paradise'
        if episode_number is 26:
            sea_ep_code = 'TOS, s1e26'
            title = 'The Devil in the Dark'
        if episode_number is 27:
            sea_ep_code = 'TOS, s1e27'
            title = 'Errand of Mercy'
        if episode_number is 28:
            sea_ep_code = 'TOS, s1e28'
            title = 'The Alternative Factor'
        if episode_number is 29:
            sea_ep_code = 'TOS, s1e29'
            title = 'The City on the Edge of Forever'
        if episode_number is 30:
            sea_ep_code = 'TOS, s1e30'
            title = 'Operation -- Annihilate!'
    if season_number is 2:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'TOS, s2e1'
            title = 'Amok Time'
        if episode_number is 2:
            sea_ep_code = 'TOS, s2e2'
            title = 'Who Mourns for Adonais?'
        if episode_number is 3:
            sea_ep_code = 'TOS, s2e3'
            title = 'The Changeling'
        if episode_number is 4:
            sea_ep_code = 'TOS, s2e4'
            title = 'Mirror, Mirror'
        if episode_number is 5:
            sea_ep_code = 'TOS, s2e5'
            title = 'The Apple'
        if episode_number is 6:
            sea_ep_code = 'TOS, s2e6'
            title = 'The Doomsday Machine'
        if episode_number is 7:
            sea_ep_code = 'TOS, s2e7'
            title = 'Catspaw'
        if episode_number is 8:
            sea_ep_code = 'TOS, s2e8'
            title = 'I, Mudd'
        if episode_number is 9:
            sea_ep_code = 'TOS, s2e9'
            title = 'Metamorphosis'
        if episode_number is 10:
            sea_ep_code = 'TOS, s2e10'
            title = 'Journey to Babel'
        if episode_number is 11:
            sea_ep_code = 'TOS, s2e11'
            title = 'Friday\'s Child'
        if episode_number is 12:
            sea_ep_code = 'TOS, s2e12'
            title = 'The Deadly Years'
        if episode_number is 13:
            sea_ep_code = 'TOS, s2e13'
            title = 'Obsession'
        if episode_number is 14:
            sea_ep_code = 'TOS, s2e14'
            title = 'Wolf in the Fold'
        if episode_number is 15:
            sea_ep_code = 'TOS, s2e15'
            title = 'The Trouble with Tribbles'
        if episode_number is 16:
            sea_ep_code = 'TOS, s2e16'
            title = 'The Gamesters of Triskelion'
        if episode_number is 17:
            sea_ep_code = 'TOS, s2e17'
            title = 'A Piece of the Action'
        if episode_number is 18:
            sea_ep_code = 'TOS, s2e18'
            title = 'The Immunity Syndrome'
        if episode_number is 19:
            sea_ep_code = 'TOS, s2e19'
            title = 'A Private Little War'
        if episode_number is 20:
            sea_ep_code = 'TOS, s2e20'
            title = 'Return to Tomorrow'
        if episode_number is 21:
            sea_ep_code = 'TOS, s2e21'
            title = 'Patterns of Force'
        if episode_number is 22:
            sea_ep_code = 'TOS, s2e22'
            title = 'By Any Other Name'
        if episode_number is 23:
            sea_ep_code = 'TOS, s2e23'
            title = 'The Omega Glory'
        if episode_number is 24:
            sea_ep_code = 'TOS, s2e24'
            title = 'The Ultimate Computer'
        if episode_number is 25:
            sea_ep_code = 'TOS, s2e25'
            title = 'Bread and Circuses'
        if episode_number is 26:
            sea_ep_code = 'TOS, s2e26'
            title = 'Assignment: Earth'
    if season_number is 3:
        episode_number = random.randrange(1, 25)
        if episode_number is 1:
            sea_ep_code = 'TOS, s3e1'
            title = 'Spock\'s Brain'
        if episode_number is 2:
            sea_ep_code = 'TOS, s3e2'
            title = 'The Enterprise Incident'
        if episode_number is 3:
            sea_ep_code = 'TOS, s3e3'
            title = 'The Paradise Syndrome'
        if episode_number is 4:
            sea_ep_code = 'TOS, s3e4'
            title = 'And the Children Shall Lead'
        if episode_number is 5:
            sea_ep_code = 'TOS, s3e5'
            title = '= There in Truth No Beauty?'
        if episode_number is 6:
            sea_ep_code = 'TOS, s3e6'
            title = 'Spectre of the Gun'
        if episode_number is 7:
            sea_ep_code = 'TOS, s3e7'
            title = 'Day of the Dove'
        if episode_number is 8:
            sea_ep_code = 'TOS, s3e8'
            title = 'For the World is Hollow and I Have Touched the Sky'
        if episode_number is 9:
            sea_ep_code = 'TOS, s3e9'
            title = 'The Tholian Web'
        if episode_number is 10:
            sea_ep_code = 'TOS, s3e10'
            title = 'Plato\'s Stepchildren'
        if episode_number is 11:
            sea_ep_code = 'TOS, s3e11'
            title = 'Wink of an Eye'
        if episode_number is 12:
            sea_ep_code = 'TOS, s3e12'
            title = 'The Empath'
        if episode_number is 13:
            sea_ep_code = 'TOS, s3e13'
            title = 'Elaan of Troyius'
        if episode_number is 14:
            sea_ep_code = 'TOS, s3e14'
            title = 'Whom Gods Destroy'
        if episode_number is 15:
            sea_ep_code = 'TOS, s3e15'
            title = 'Let That Be Your Last Battlefield'
        if episode_number is 16:
            sea_ep_code = 'TOS, s3e16'
            title = 'The Mark of Gideon'
        if episode_number is 17:
            sea_ep_code = 'TOS, s3e17'
            title = 'That Which Survives'
        if episode_number is 18:
            sea_ep_code = 'TOS, s3e18'
            title = 'The Lights of Zetar'
        if episode_number is 19:
            sea_ep_code = 'TOS, s3e19'
            title = 'Requiem for Methuselah'
        if episode_number is 20:
            sea_ep_code = 'TOS, s3e20'
            title = 'The Way to Eden'
        if episode_number is 21:
            sea_ep_code = 'TOS, s3e21'
            title = 'The Cloud Minders'
        if episode_number is 22:
            sea_ep_code = 'TOS, s3e22'
            title = 'The Savage Curtain'
        if episode_number is 23:
            sea_ep_code = 'TOS, s3e23'
            title = 'All Our Yesterdays'
        if episode_number is 24:
            sea_ep_code = 'TOS, s3e24'
            title = 'Turnabout Intruder'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def TAS():
    season_number = random.randrange(1, 3)
    if season_number is 1:
        episode_number = random.randrange(1,17)
        if episode_number is 1:
            sea_ep_code = 'TAS, s1e1'
            title = 'Beyond the Farthest Star'
        if episode_number is 2:
            sea_ep_code = 'TAS, s1e2'
            title = 'Yesteryear'
        if episode_number is 3:
            sea_ep_code = 'TAS, s1e3'
            title = 'One of Our Planets is Missing'
        if episode_number is 4:
            sea_ep_code = 'TAS, s1e4'
            title = 'The Lorelei Signal'
        if episode_number is 5:
            sea_ep_code = 'TAS, s1e5'
            title = 'More Tribbles, More Troubles'
        if episode_number is 6:
            sea_ep_code = 'TAS, s1e6'
            title = 'The Survivor'
        if episode_number is 7:
            sea_ep_code = 'TAS, s1e7'
            title = 'The Infinite Vulcan'
        if episode_number is 8:
            sea_ep_code = 'TAS, s1e8'
            title = 'The Magicks of Megas-Tu'
        if episode_number is 9:
            sea_ep_code = 'TAS, s1e9'
            title = 'Once Upon a Planet'
        if episode_number is 10:
            sea_ep_code = 'TAS, s1e10'
            title = 'Mudd\'s Passion'
        if episode_number is 11:
            sea_ep_code = 'TAS, s1e11'
            title = 'The Terratin Incident'
        if episode_number is 12:
            sea_ep_code = 'TAS, s1e12'
            title = 'The Time Trap'
        if episode_number is 13:
            sea_ep_code = 'TAS, s1e13'
            title = 'The Ambergris Element'
        if episode_number is 14:
            sea_ep_code = 'TAS, s1e14'
            title = 'The Slaver Weapon'
        if episode_number is 15:
            sea_ep_code = 'TAS, s1e15'
            title = 'The Eye of the Beholder'
        if episode_number is 16:
            sea_ep_code = 'TAS, s1e16'
            title = 'The Jihad'
    if season_number is 2:
        episode_number = random.randrange(1,7)
        if episode_number is 1:
            sea_ep_code = 'TAS, s2e1'
            title = 'The Pirates of Orion'
        if episode_number is 2:
            sea_ep_code = 'TAS, s2e2'
            title = 'Bem'
        if episode_number is 3:
            sea_ep_code = 'TAS, s2e3'
            title = 'The Practical Joker'
        if episode_number is 4:
            sea_ep_code = 'TAS, s2e4'
            title = 'Albatross'
        if episode_number is 5:
            sea_ep_code = 'TAS, s2e5'
            title = 'How Sharper Than a Serpent\'s Tooth'
        if episode_number is 6:
            sea_ep_code = 'TAS, s2e6'
            title = 'The Counter-Clock Incident'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def VOY():
    season_number = random.randrange(1, 8)
    if season_number is 1:
        episode_number = random.randrange(1, 16)
        if episode_number is 1:
            sea_ep_code = 'VOY, s1e1'
            title = 'Caretaker'
        if episode_number is 2:
            sea_ep_code = 'VOY, s1e2'
            title = 'Parallax'
        if episode_number is 3:
            sea_ep_code = 'VOY, s1e3'
            title = 'Time and Again'
        if episode_number is 4:
            sea_ep_code = 'VOY, s1e4'
            title = 'Phage'
        if episode_number is 5:
            sea_ep_code = 'VOY, s1e5'
            title = 'The Cloud'
        if episode_number is 6:
            sea_ep_code = 'VOY, s1e6'
            title = 'Eye of the Needle'
        if episode_number is 7:
            sea_ep_code = 'VOY, s1e7'
            title = 'Ex Post Facto'
        if episode_number is 8:
            sea_ep_code = 'VOY, s1e8'
            title = 'Emanations'
        if episode_number is 9:
            sea_ep_code = 'VOY, s1e9'
            title = 'Prime Factors'
        if episode_number is 10:
            sea_ep_code = 'VOY, s1e10'
            title = 'State of Flux'
        if episode_number is 11:
            sea_ep_code = 'VOY, s1e11'
            title = 'Heroes and Demons'
        if episode_number is 12:
            sea_ep_code = 'VOY, s1e12'
            title = 'Cathexis'
        if episode_number is 13:
            sea_ep_code = 'VOY, s1e13'
            title = 'Faces'
        if episode_number is 14:
            sea_ep_code = 'VOY, s1e14'
            title = 'Jetrel'
        if episode_number is 15:
            sea_ep_code = 'VOY, s1e15'
            title = 'Learning Curve'
    if season_number is 2:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'VOY, s2e1'
            title = 'The 37\'s'
        if episode_number is 2:
            sea_ep_code = 'VOY, s2e2'
            title = 'Initiations'
        if episode_number is 3:
            sea_ep_code = 'VOY, s2e3'
            title = 'Projections'
        if episode_number is 4:
            sea_ep_code = 'VOY, s2e4'
            title = 'Elogium'
        if episode_number is 5:
            sea_ep_code = 'VOY, s2e5'
            title = 'Non Sequitur'
        if episode_number is 6:
            sea_ep_code = 'VOY, s2e6'
            title = 'Tw=ted'
        if episode_number is 7:
            sea_ep_code = 'VOY, s2e7'
            title = 'Parturition'
        if episode_number is 8:
            sea_ep_code = 'VOY, s2e8'
            title = 'Persistence of Vision'
        if episode_number is 9:
            sea_ep_code = 'VOY, s2e9'
            title = 'Tattoo'
        if episode_number is 10:
            sea_ep_code = 'VOY, s2e10'
            title = 'Cold Fire'
        if episode_number is 11:
            sea_ep_code = 'VOY, s2e11'
            title = 'Maneuvers'
        if episode_number is 12:
            sea_ep_code = 'VOY, s2e12'
            title = 'Res=tance'
        if episode_number is 13:
            sea_ep_code = 'VOY, s2e13'
            title = 'Prototype'
        if episode_number is 14:
            sea_ep_code = 'VOY, s2e14'
            title = 'Alliances'
        if episode_number is 15:
            sea_ep_code = 'VOY, s2e15'
            title = 'Threshold'
        if episode_number is 16:
            sea_ep_code = 'VOY, s2e16'
            title = 'Meld'
        if episode_number is 17:
            sea_ep_code = 'VOY, s2e17'
            title = 'Dreadnought'
        if episode_number is 18:
            sea_ep_code = 'VOY, s2e18'
            title = 'Death Wish'
        if episode_number is 19:
            sea_ep_code = 'VOY, s2e19'
            title = 'Lifesigns'
        if episode_number is 20:
            sea_ep_code = 'VOY, s2e20'
            title = 'Investigations'
        if episode_number is 21:
            sea_ep_code = 'VOY, s2e21'
            title = 'Deadlock'
        if episode_number is 22:
            sea_ep_code = 'VOY, s2e22'
            title = 'Innocence'
        if episode_number is 23:
            sea_ep_code = 'VOY, s2e23'
            title = 'The Thaw'
        if episode_number is 24:
            sea_ep_code = 'VOY, s2e24'
            title = 'Tuvix'
        if episode_number is 25:
            sea_ep_code = 'VOY, s2e25'
            title = 'Resolutions'
        if episode_number is 26:
            sea_ep_code = 'VOY, s2e26'
            title = 'Basics: Part 1'
    if season_number is 3:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'VOY, s3e1'
            title = 'Basics: Part 2'
        if episode_number is 2:
            sea_ep_code = 'VOY, s3e2'
            title = 'Flashback'
        if episode_number is 3:
            sea_ep_code = 'VOY, s3e3'
            title = 'The Chute'
        if episode_number is 4:
            sea_ep_code = 'VOY, s3e4'
            title = 'The Swarm'
        if episode_number is 5:
            sea_ep_code = 'VOY, s3e5'
            title = 'False Profits'
        if episode_number is 6:
            sea_ep_code = 'VOY, s3e6'
            title = 'Remember'
        if episode_number is 7:
            sea_ep_code = 'VOY, s3e7'
            title = 'Sacred Ground'
        if episode_number is 8:
            sea_ep_code = 'VOY, s3e8'
            title = 'Future\'s End: Part 1'
        if episode_number is 9:
            sea_ep_code = 'VOY, s3e9'
            title = 'Future\'s End: Part 2'
        if episode_number is 10:
            sea_ep_code = 'VOY, s3e10'
            title = 'Warlord'
        if episode_number is 11:
            sea_ep_code = 'VOY, s3e11'
            title = 'The Q and the Grey'
        if episode_number is 12:
            sea_ep_code = 'VOY, s3e12'
            title = 'Macrocosm'
        if episode_number is 13:
            sea_ep_code = 'VOY, s3e13'
            title = 'Fair Trade'
        if episode_number is 14:
            sea_ep_code = 'VOY, s3e14'
            title = 'Alter Ego'
        if episode_number is 15:
            sea_ep_code = 'VOY, s3e15'
            title = 'Coda'
        if episode_number is 16:
            sea_ep_code = 'VOY, s3e16'
            title = 'Blood Fever'
        if episode_number is 17:
            sea_ep_code = 'VOY, s3e17'
            title = 'Unity'
        if episode_number is 18:
            sea_ep_code = 'VOY, s3e18'
            title = 'Darkling'
        if episode_number is 19:
            sea_ep_code = 'VOY, s3e19'
            title = 'Rise'
        if episode_number is 20:
            sea_ep_code = 'VOY, s3e20'
            title = 'Favorite Son'
        if episode_number is 21:
            sea_ep_code = 'VOY, s3e21'
            title = 'Before and After'
        if episode_number is 22:
            sea_ep_code = 'VOY, s3e22'
            title = 'Real Life'
        if episode_number is 23:
            sea_ep_code = 'VOY, s3e23'
            title = 'Distant Origin'
        if episode_number is 24:
            sea_ep_code = 'VOY, s3e24'
            title = 'Displaced'
        if episode_number is 25:
            sea_ep_code = 'VOY, s3e25'
            title = 'Worst Case Scenario'
        if episode_number is 26:
            sea_ep_code = 'VOY, s3e26'
            title = 'Scorpion: Part 1'
    if season_number is 4:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'VOY, s4e1'
            title = 'Scorpion: Part 2'
        if episode_number is 2:
            sea_ep_code = 'VOY, s4e2'
            title = 'The Gift'
        if episode_number is 3:
            sea_ep_code = 'VOY, s4e3'
            title = 'Day of Honor'
        if episode_number is 4:
            sea_ep_code = 'VOY, s4e4'
            title = 'Nemesis'
        if episode_number is 5:
            sea_ep_code = 'VOY, s4e5'
            title = 'Revulsion'
        if episode_number is 6:
            sea_ep_code = 'VOY, s4e6'
            title = 'The Raven'
        if episode_number is 7:
            sea_ep_code = 'VOY, s4e7'
            title = 'Scientific Method'
        if episode_number is 8:
            sea_ep_code = 'VOY, s4e8'
            title = 'Year of Hell: Part 1'
        if episode_number is 9:
            sea_ep_code = 'VOY, s4e9'
            title = 'Year of Hell: Part 2'
        if episode_number is 10:
            sea_ep_code = 'VOY, s4e10'
            title = 'Random Thoughts'
        if episode_number is 11:
            sea_ep_code = 'VOY, s4e11'
            title = 'Concerning Flight'
        if episode_number is 12:
            sea_ep_code = 'VOY, s4e12'
            title = 'Mortal Coil'
        if episode_number is 13:
            sea_ep_code = 'VOY, s4e13'
            title = 'Waking Moments'
        if episode_number is 14:
            sea_ep_code = 'VOY, s4e14'
            title = 'Message in a Bottle'
        if episode_number is 15:
            sea_ep_code = 'VOY, s4e15'
            title = 'Hunters'
        if episode_number is 16:
            sea_ep_code = 'VOY, s4e16'
            title = 'Prey'
        if episode_number is 17:
            sea_ep_code = 'VOY, s4e17'
            title = 'Retrospect'
        if episode_number is 18:
            sea_ep_code = 'VOY, s4e18'
            title = 'The Killing Game: Part 1'
        if episode_number is 19:
            sea_ep_code = 'VOY, s4e19'
            title = 'The Killing Game: Part 2'
        if episode_number is 20:
            sea_ep_code = 'VOY, s4e20'
            title = 'Vis A Vis'
        if episode_number is 21:
            sea_ep_code = 'VOY, s4e21'
            title = 'The Omega Directive'
        if episode_number is 22:
            sea_ep_code = 'VOY, s4e22'
            title = 'Unforgettable'
        if episode_number is 23:
            sea_ep_code = 'VOY, s4e23'
            title = 'Living Witness'
        if episode_number is 24:
            sea_ep_code = 'VOY, s4e24'
            title = 'Demon'
        if episode_number is 25:
            sea_ep_code = 'VOY, s4e25'
            title = 'Hope and Fear'
        if episode_number is 26:
            sea_ep_code = 'VOY, s4e26'
            title = 'Hope and Fear'
    if season_number is 5:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'VOY, s5e1'
            title = 'Night'
        if episode_number is 2:
            sea_ep_code = 'VOY, s5e2'
            title = 'Drone'
        if episode_number is 3:
            sea_ep_code = 'VOY, s5e3'
            title = 'Extreme Risk'
        if episode_number is 4:
            sea_ep_code = 'VOY, s5e4'
            title = 'In the Flesh'
        if episode_number is 5:
            sea_ep_code = 'VOY, s5e5'
            title = 'Once Upon a Time'
        if episode_number is 6:
            sea_ep_code = 'VOY, s5e6'
            title = 'Timeless'
        if episode_number is 7:
            sea_ep_code = 'VOY, s5e7'
            title = 'Infinite Regress'
        if episode_number is 8:
            sea_ep_code = 'VOY, s5e8'
            title = 'Nothing Human'
        if episode_number is 9:
            sea_ep_code = 'VOY, s5e9'
            title = 'Thirty Days'
        if episode_number is 10:
            sea_ep_code = 'VOY, s5e10'
            title = 'Counterpoint'
        if episode_number is 11:
            sea_ep_code = 'VOY, s5e11'
            title = 'Latent Image'
        if episode_number is 12:
            sea_ep_code = 'VOY, s5e12'
            title = 'Bride of Chaotica!'
        if episode_number is 13:
            sea_ep_code = 'VOY, s5e13'
            title = 'Gravity'
        if episode_number is 14:
            sea_ep_code = 'VOY, s5e14'
            title = 'Bliss'
        if episode_number is 15:
            sea_ep_code = 'VOY, s5e15'
            title = 'Dark Frontier: Part 1'
        if episode_number is 16:
            sea_ep_code = 'VOY, s5e16'
            title = 'Dark Frontier: Part 2'
        if episode_number is 17:
            sea_ep_code = 'VOY, s5e17'
            title = 'The Disease'
        if episode_number is 18:
            sea_ep_code = 'VOY, s5e18'
            title = 'Course: Oblivion'
        if episode_number is 19:
            sea_ep_code = 'VOY, s5e19'
            title = 'The Fight'
        if episode_number is 20:
            sea_ep_code = 'VOY, s5e20'
            title = 'Think Tank'
        if episode_number is 21:
            sea_ep_code = 'VOY, s5e21'
            title = 'Juggernaut'
        if episode_number is 22:
            sea_ep_code = 'VOY, s5e22'
            title = 'Someone to Watch Over Me'
        if episode_number is 23:
            sea_ep_code = 'VOY, s5e23'
            title = '11:59'
        if episode_number is 24:
            sea_ep_code = 'VOY, s5e24'
            title = 'Relativity'
        if episode_number is 25:
            sea_ep_code = 'VOY, s5e25'
            title = 'Warhead'
        if episode_number is 26:
            sea_ep_code = 'VOY, s5e26'
            title = 'Equinox: Part 1'
    if season_number is 6:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'VOY, s6e1'
            title = 'Equinox: Part 2'
        if episode_number is 2:
            sea_ep_code = 'VOY, s6e2'
            title = 'Survival Instinct'
        if episode_number is 3:
            sea_ep_code = 'VOY, s6e3'
            title = 'Barge of the Dead'
        if episode_number is 4:
            sea_ep_code = 'VOY, s6e4'
            title = 'Tinker Tenor Doctor Spy'
        if episode_number is 5:
            sea_ep_code = 'VOY, s6e5'
            title = 'Alice'
        if episode_number is 6:
            sea_ep_code = 'VOY, s6e6'
            title = 'Riddles'
        if episode_number is 7:
            sea_ep_code = 'VOY, s6e7'
            title = 'Dragon\'s Teeth'
        if episode_number is 8:
            sea_ep_code = 'VOY, s6e8'
            title = 'One Small Step'
        if episode_number is 9:
            sea_ep_code = 'VOY, s6e9'
            title = 'The Voyager Conspiracy'
        if episode_number is 10:
            sea_ep_code = 'VOY, s6e10'
            title = 'Pathfinder'
        if episode_number is 11:
            sea_ep_code = 'VOY, s6e11'
            title = 'Fair Haven'
        if episode_number is 12:
            sea_ep_code = 'VOY, s6e12'
            title = 'Blink of an Eye'
        if episode_number is 13:
            sea_ep_code = 'VOY, s6e13'
            title = 'Virtuoso'
        if episode_number is 14:
            sea_ep_code = 'VOY, s6e14'
            title = 'Memorial'
        if episode_number is 15:
            sea_ep_code = 'VOY, s6e15'
            title = 'Tsunkatse'
        if episode_number is 16:
            sea_ep_code = 'VOY, s6e16'
            title = 'Collective'
        if episode_number is 17:
            sea_ep_code = 'VOY, s6e17'
            title = 'Spirit Folk'
        if episode_number is 18:
            sea_ep_code = 'VOY, s6e18'
            title = 'Ashes to Ashes'
        if episode_number is 19:
            sea_ep_code = 'VOY, s6e19'
            title = 'Child\'s Play'
        if episode_number is 20:
            sea_ep_code = 'VOY, s6e20'
            title = 'Good Shepherd'
        if episode_number is 21:
            sea_ep_code = 'VOY, s6e21'
            title = 'Live Fast and Prosper'
        if episode_number is 22:
            sea_ep_code = 'VOY, s6e22'
            title = 'Muse'
        if episode_number is 23:
            sea_ep_code = 'VOY, s6e23'
            title = 'Fury'
        if episode_number is 24:
            sea_ep_code = 'VOY, s6e24'
            title = 'Life Line'
        if episode_number is 25:
            sea_ep_code = 'VOY, s6e25'
            title = 'The Haunting of Deck Twelve'
        if episode_number is 26:
            sea_ep_code = 'VOY, s6e26'
            title = 'Unimatrix Zero: Part 1'
    if season_number is 7:
        episode_number = random.randrange(1, 26)
        if episode_number is 1:
            sea_ep_code = 'VOY, s7e1'
            title = 'Unimatrix Zero: Part 2'
        if episode_number is 2:
            sea_ep_code = 'VOY, s7e2'
            title = 'Imperfection'
        if episode_number is 3:
            sea_ep_code = 'VOY, s7e3'
            title = 'Drive'
        if episode_number is 4:
            sea_ep_code = 'VOY, s7e4'
            title = 'Repression'
        if episode_number is 5:
            sea_ep_code = 'VOY, s7e5'
            title = 'Critical Care'
        if episode_number is 6:
            sea_ep_code = 'VOY, s7e6'
            title = 'Inside Man'
        if episode_number is 7:
            sea_ep_code = 'VOY, s7e7'
            title = 'Body and Soul'
        if episode_number is 8:
            sea_ep_code = 'VOY, s7e8'
            title = 'Nightingale'
        if episode_number is 9:
            sea_ep_code = 'VOY, s7e9'
            title = 'Flesh and Blood'
        if episode_number is 10:
            sea_ep_code = 'VOY, s7e10'
            title = 'Flesh and Blood: Part 2'
        if episode_number is 11:
            sea_ep_code = 'VOY, s7e11'
            title = 'Shattered'
        if episode_number is 12:
            sea_ep_code = 'VOY, s7e12'
            title = 'Lineage'
        if episode_number is 13:
            sea_ep_code = 'VOY, s7e13'
            title = 'Repentance'
        if episode_number is 14:
            sea_ep_code = 'VOY, s7e14'
            title = 'Prophecy'
        if episode_number is 15:
            sea_ep_code = 'VOY, s7e15'
            title = 'The Void'
        if episode_number is 16:
            sea_ep_code = 'VOY, s7e16'
            title = 'Workforce: Part 1'
        if episode_number is 17:
            sea_ep_code = 'VOY, s7e17'
            title = 'Workforce: Part 2'
        if episode_number is 18:
            sea_ep_code = 'VOY, s7e18'
            title = 'Human Error'
        if episode_number is 19:
            sea_ep_code = 'VOY, s7e19'
            title = 'Q2'
        if episode_number is 20:
            sea_ep_code = 'VOY, s7e20'
            title = 'Author, Author'
        if episode_number is 21:
            sea_ep_code = 'VOY, s7e21'
            title = 'Friendship One'
        if episode_number is 22:
            sea_ep_code = 'VOY, s7e22'
            title = 'Natural Law'
        if episode_number is 23:
            sea_ep_code = 'VOY, s7e23'
            title = 'Homestead'
        if episode_number is 24:
            sea_ep_code = 'VOY, s7e24'
            title = 'Renaissance Man'
        if episode_number is 25:
            sea_ep_code = 'VOY, s7e25'
            title = 'Endgame'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def DS9():
    season_number = random.randrange(1, 8)
    if season_number is 1:
        episode_number = random.randrange(1, 20)
        if episode_number is 1:
            sea_ep_code = 'DS9, s1e1'
            title = 'Em=sary'
        if episode_number is 2:
            sea_ep_code = 'DS9, s1e2'
            title = 'Past Prologue'
        if episode_number is 3:
            sea_ep_code = 'DS9, s1e3'
            title = 'A Man Alone'
        if episode_number is 4:
            sea_ep_code = 'DS9, s1e4'
            title = 'Babel'
        if episode_number is 5:
            sea_ep_code = 'DS9, s1e5'
            title = 'Captive Pursuit'
        if episode_number is 6:
            sea_ep_code = 'DS9, s1e6'
            title = 'Q-Less'
        if episode_number is 7:
            sea_ep_code = 'DS9, s1e7'
            title = 'Dax'
        if episode_number is 8:
            sea_ep_code = 'DS9, s1e8'
            title = 'The Passenger'
        if episode_number is 9:
            sea_ep_code = 'DS9, s1e9'
            title = 'Move Along Home'
        if episode_number is 10:
            sea_ep_code = 'DS9, s1e10'
            title = 'The Nagus'
        if episode_number is 11:
            sea_ep_code = 'DS9, s1e11'
            title = 'Vortex'
        if episode_number is 12:
            sea_ep_code = 'DS9, s1e12'
            title = 'Battle Lines'
        if episode_number is 13:
            sea_ep_code = 'DS9, s1e13'
            title = 'The Storyteller'
        if episode_number is 14:
            sea_ep_code = 'DS9, s1e14'
            title = 'Progress'
        if episode_number is 15:
            sea_ep_code = 'DS9, s1e15'
            title = 'If W=hes Were Horses'
        if episode_number is 16:
            sea_ep_code = 'DS9, s1e16'
            title = 'The Forsaken'
        if episode_number is 17:
            sea_ep_code = 'DS9, s1e17'
            title = 'Dramatis Personae'
        if episode_number is 18:
            sea_ep_code = 'DS9, s1e18'
            title = 'Duet'
        if episode_number is 19:
            sea_ep_code = 'DS9, s1e19'
            title = 'In the Hands of the Prophets'
    if season_number is 2:
        episode_number = random.randrange(1,27)
        if episode_number is 1:
            sea_ep_code = 'DS9, s2e1'
            title = 'The Homecoming'
        if episode_number is 2:
            sea_ep_code = 'DS9, s2e2'
            title = 'The Circle'
        if episode_number is 3:
            sea_ep_code = 'DS9, s2e3'
            title = 'The Siege'
        if episode_number is 4:
            sea_ep_code = 'DS9, s2e4'
            title = 'Invasive Procedures'
        if episode_number is 5:
            sea_ep_code = 'DS9, s2e5'
            title = 'Cardassians'
        if episode_number is 6:
            sea_ep_code = 'DS9, s2e6'
            title = 'Melora'
        if episode_number is 7:
            sea_ep_code = 'DS9, s2e7'
            title = 'Rules of Acquisition'
        if episode_number is 8:
            sea_ep_code = 'DS9, s2e8'
            title = 'Necessary Evil'
        if episode_number is 9:
            sea_ep_code = 'DS9, s2e9'
            title = 'Second Sight'
        if episode_number is 10:
            sea_ep_code = 'DS9, s2e10'
            title = 'Sanctuary'
        if episode_number is 11:
            sea_ep_code = 'DS9, s2e11'
            title = 'Rivals'
        if episode_number is 12:
            sea_ep_code = 'DS9, s2e12'
            title = 'The Alternate'
        if episode_number is 13:
            sea_ep_code = 'DS9, s2e13'
            title = 'Armageddon Game'
        if episode_number is 14:
            sea_ep_code = 'DS9, s2e14'
            title = 'Whispers'
        if episode_number is 15:
            sea_ep_code = 'DS9, s2e15'
            title = 'Paradise'
        if episode_number is 16:
            sea_ep_code = 'DS9, s2e16'
            title = 'Shadowplay'
        if episode_number is 17:
            sea_ep_code = 'DS9, s2e17'
            title = 'Playing God'
        if episode_number is 18:
            sea_ep_code = 'DS9, s2e18'
            title = 'Profit and Loss'
        if episode_number is 19:
            sea_ep_code = 'DS9, s2e19'
            title = 'Blood Oath'
        if episode_number is 20:
            sea_ep_code = 'DS9, s2e20'
            title = 'The Maquis: Part 1'
        if episode_number is 21:
            sea_ep_code = 'DS9, s2e21'
            title = 'The Maquis: Part 2'
        if episode_number is 22:
            sea_ep_code = 'DS9, s2e22'
            title = 'The Wire'
        if episode_number is 23:
            sea_ep_code = 'DS9, s2e23'
            title = 'Crossover'
        if episode_number is 24:
            sea_ep_code = 'DS9, s2e24'
            title = 'The Collaborator'
        if episode_number is 25:
            sea_ep_code = 'DS9, s2e25'
            title = 'Tribunal'
        if episode_number is 26:
            sea_ep_code = 'DS9, s2e26'
            title = 'The Jem\'Hadar'
    if season_number is 3:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'DS9, s3e1'
            title = 'The Search: Part 1'
        if episode_number is 2:
            sea_ep_code = 'DS9, s3e2'
            title = 'The Search: Part 2'
        if episode_number is 3:
            sea_ep_code = 'DS9, s3e3'
            title = 'The House of Quark'
        if episode_number is 4:
            sea_ep_code = 'DS9, s3e4'
            title = 'Equilibrium'
        if episode_number is 5:
            sea_ep_code = 'DS9, s3e5'
            title = 'Second Skin'
        if episode_number is 6:
            sea_ep_code = 'DS9, s3e6'
            title = 'The Abandoned'
        if episode_number is 7:
            sea_ep_code = 'DS9, s3e7'
            title = 'Civil Defense'
        if episode_number is 8:
            sea_ep_code = 'DS9, s3e8'
            title = 'Meridian'
        if episode_number is 9:
            sea_ep_code = 'DS9, s3e9'
            title = 'Defiant'
        if episode_number is 10:
            sea_ep_code = 'DS9, s3e10'
            title = 'Fascination'
        if episode_number is 11:
            sea_ep_code = 'DS9, s3e11'
            title = 'Past Tense: Part 1'
        if episode_number is 12:
            sea_ep_code = 'DS9, s3e12'
            title = 'Past Tense: Part 2'
        if episode_number is 13:
            sea_ep_code = 'DS9, s3e13'
            title = 'Life Support'
        if episode_number is 14:
            sea_ep_code = 'DS9, s3e14'
            title = 'Heart of Stone'
        if episode_number is 15:
            sea_ep_code = 'DS9, s3e15'
            title = 'Destiny'
        if episode_number is 16:
            sea_ep_code = 'DS9, s3e16'
            title = 'Prophet Motive'
        if episode_number is 17:
            sea_ep_code = 'DS9, s3e17'
            title = 'Visionary'
        if episode_number is 18:
            sea_ep_code = 'DS9, s3e18'
            title = 'Distant Voices'
        if episode_number is 19:
            sea_ep_code = 'DS9, s3e19'
            title = 'Through the Looking Glass'
        if episode_number is 20:
            sea_ep_code = 'DS9, s3e20'
            title = 'Improbable Cause'
        if episode_number is 21:
            sea_ep_code = 'DS9, s3e21'
            title = 'The Die Is Cast'
        if episode_number is 22:
            sea_ep_code = 'DS9, s3e22'
            title = 'Explorers'
        if episode_number is 23:
            sea_ep_code = 'DS9, s3e23'
            title = 'Family Business'
        if episode_number is 24:
            sea_ep_code = 'DS9, s3e24'
            title = 'Shakaar'
        if episode_number is 25:
            sea_ep_code = 'DS9, s3e25'
            title = 'Facets'
        if episode_number is 26:
            sea_ep_code = 'DS9, s3e26'
            title = 'The Adversary'
    if season_number is 4:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'DS9, s4e1'
            title = 'The Way of the Warrior'
        if episode_number is 2:
            sea_ep_code = 'DS9, s4e2'
            title = 'The Visitor'
        if episode_number is 3:
            sea_ep_code = 'DS9, s4e3'
            title = 'Hippocratic Oath'
        if episode_number is 4:
            sea_ep_code = 'DS9, s4e4'
            title = 'Indiscretion'
        if episode_number is 5:
            sea_ep_code = 'DS9, s4e5'
            title = 'Rejoined'
        if episode_number is 6:
            sea_ep_code = 'DS9, s4e6'
            title = 'Starship Down'
        if episode_number is 7:
            sea_ep_code = 'DS9, s4e7'
            title = 'Little Green Men'
        if episode_number is 8:
            sea_ep_code = 'DS9, s4e8'
            title = 'The Sword of Kahless'
        if episode_number is 9:
            sea_ep_code = 'DS9, s4e9'
            title = 'Our Man Bashir'
        if episode_number is 10:
            sea_ep_code = 'DS9, s4e10'
            title = 'Homefront'
        if episode_number is 11:
            sea_ep_code = 'DS9, s4e11'
            title = 'Paradise Lost'
        if episode_number is 12:
            sea_ep_code = 'DS9, s4e12'
            title = 'Crossfire'
        if episode_number is 13:
            sea_ep_code = 'DS9, s4e13'
            title = 'Return to Grace'
        if episode_number is 14:
            sea_ep_code = 'DS9, s4e14'
            title = 'Sons of Mogh'
        if episode_number is 15:
            sea_ep_code = 'DS9, s4e15'
            title = 'Bar Association'
        if episode_number is 16:
            sea_ep_code = 'DS9, s4e16'
            title = 'Accession'
        if episode_number is 17:
            sea_ep_code = 'DS9, s4e17'
            title = 'Rules of Engagement'
        if episode_number is 18:
            sea_ep_code = 'DS9, s4e18'
            title = 'Hard Time'
        if episode_number is 19:
            sea_ep_code = 'DS9, s4e19'
            title = 'Shattered Mirror'
        if episode_number is 20:
            sea_ep_code = 'DS9, s4e20'
            title = 'The Muse'
        if episode_number is 21:
            sea_ep_code = 'DS9, s4e21'
            title = 'For the Cause'
        if episode_number is 22:
            sea_ep_code = 'DS9, s4e22'
            title = 'To the Death'
        if episode_number is 23:
            sea_ep_code = 'DS9, s4e23'
            title = 'The Quickening'
        if episode_number is 24:
            sea_ep_code = 'DS9, s4e24'
            title = 'Body Parts'
        if episode_number is 25:
            sea_ep_code = 'DS9, s4e25'
            title = 'Broken Link'
    if season_number is 5:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'DS9, s5e1'
            title = 'Apocalypse Rising'
        if episode_number is 2:
            sea_ep_code = 'DS9, s5e2'
            title = 'The Ship'
        if episode_number is 3:
            sea_ep_code = 'DS9, s5e3'
            title = 'Looking for par\'Mach in All the Wrong Places'
        if episode_number is 4:
            sea_ep_code = 'DS9, s5e4'
            title = '...Nor the Battle to the Strong'
        if episode_number is 5:
            sea_ep_code = 'DS9, s5e5'
            title = 'The Assignment'
        if episode_number is 6:
            sea_ep_code = 'DS9, s5e6'
            title = 'Trials and Tribble-ations'
        if episode_number is 7:
            sea_ep_code = 'DS9, s5e7'
            title = 'Let He Who Is Without Sin...'
        if episode_number is 8:
            sea_ep_code = 'DS9, s5e8'
            title = 'Things Past'
        if episode_number is 9:
            sea_ep_code = 'DS9, s5e9'
            title = 'The Ascent'
        if episode_number is 10:
            sea_ep_code = 'DS9, s5e10'
            title = 'Rapture'
        if episode_number is 11:
            sea_ep_code = 'DS9, s5e11'
            title = 'The Darkness and the Light'
        if episode_number is 12:
            sea_ep_code = 'DS9, s5e12'
            title = 'The Begotten'
        if episode_number is 13:
            sea_ep_code = 'DS9, s5e13'
            title = 'For the Uniform'
        if episode_number is 14:
            sea_ep_code = 'DS9, s5e14'
            title = 'In Purgatory\'s Shadow'
        if episode_number is 15:
            sea_ep_code = 'DS9, s5e15'
            title = 'By Inferno\'s Light'
        if episode_number is 16:
            sea_ep_code = 'DS9, s5e16'
            title = 'Doctor Bashir, I Presume?'
        if episode_number is 17:
            sea_ep_code = 'DS9, s5e17'
            title = 'A Simple Investigation'
        if episode_number is 18:
            sea_ep_code = 'DS9, s5e18'
            title = 'Business as Usual'
        if episode_number is 19:
            sea_ep_code = 'DS9, s5e19'
            title = 'Ties of Blood and Water'
        if episode_number is 20:
            sea_ep_code = 'DS9, s5e20'
            title = 'Ferengi Love Songs'
        if episode_number is 21:
            sea_ep_code = 'DS9, s5e21'
            title = 'Soldiers of the Empire'
        if episode_number is 22:
            sea_ep_code = 'DS9, s5e22'
            title = 'Children of Time'
        if episode_number is 23:
            sea_ep_code = 'DS9, s5e23'
            title = 'Blaze of Glory'
        if episode_number is 24:
            sea_ep_code = 'DS9, s5e24'
            title = 'Empok Nor'
        if episode_number is 25:
            sea_ep_code = 'DS9, s5e25'
            title = 'In the Cards'
        if episode_number is 26:
            sea_ep_code = 'DS9, s5e26'
            title = 'Call to Arms'
    if season_number is 6:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'DS9, s6e1'
            title = 'A Time to Stand'
        if episode_number is 2:
            sea_ep_code = 'DS9, s6e2'
            title = 'Rocks and Shoals'
        if episode_number is 3:
            sea_ep_code = 'DS9, s6e3'
            title = 'Sons and Daughters'
        if episode_number is 4:
            sea_ep_code = 'DS9, s6e4'
            title = 'Behind the Lines'
        if episode_number is 5:
            sea_ep_code = 'DS9, s6e5'
            title = 'Favor the Bold'
        if episode_number is 6:
            sea_ep_code = 'DS9, s6e6'
            title = 'Sacrifice of Angels'
        if episode_number is 7:
            sea_ep_code = 'DS9, s6e7'
            title = 'You Are Cordially Invited...'
        if episode_number is 8:
            sea_ep_code = 'DS9, s6e8'
            title = 'Resurrection'
        if episode_number is 9:
            sea_ep_code = 'DS9, s6e9'
            title = 'Statistical Probabilities'
        if episode_number is 10:
            sea_ep_code = 'DS9, s6e10'
            title = 'The Magnificent Ferengi'
        if episode_number is 11:
            sea_ep_code = 'DS9, s6e11'
            title = 'Waltz'
        if episode_number is 12:
            sea_ep_code = 'DS9, s6e12'
            title = 'Who Mourns for Morn?'
        if episode_number is 13:
            sea_ep_code = 'DS9, s6e13'
            title = 'Far Beyond the Stars'
        if episode_number is 14:
            sea_ep_code = 'DS9, s6e14'
            title = 'One Little Ship'
        if episode_number is 15:
            sea_ep_code = 'DS9, s6e15'
            title = 'Honor Among Thieves'
        if episode_number is 16:
            sea_ep_code = 'DS9, s6e16'
            title = 'Change of Heart'
        if episode_number is 17:
            sea_ep_code = 'DS9, s6e17'
            title = 'Wrongs Darker Than Death or Night'
        if episode_number is 18:
            sea_ep_code = 'DS9, s6e18'
            title = 'Inquisition'
        if episode_number is 19:
            sea_ep_code = 'DS9, s6e19'
            title = 'In the Pale Moonlight'
        if episode_number is 20:
            sea_ep_code = 'DS9, s6e20'
            title = 'His Way'
        if episode_number is 21:
            sea_ep_code = 'DS9, s6e21'
            title = 'The Reckoning'
        if episode_number is 22:
            sea_ep_code = 'DS9, s6e22'
            title = 'Valiant'
        if episode_number is 23:
            sea_ep_code = 'DS9, s6e23'
            title = 'Profit and Lace'
        if episode_number is 24:
            sea_ep_code = 'DS9, s6e24'
            title = 'Time\'s Orphan'
        if episode_number is 25:
            sea_ep_code = 'DS9, s6e25'
            title = 'The Sound of Her Voice'
        if episode_number is 26:
            sea_ep_code = 'DS9, s6e26'
            title = 'Tears of the Prophets'
    if season_number is 7:
        episode_number = random.randrange(1, 26)
        if episode_number is 1:
            sea_ep_code = 'DS9, s7e1'
            title = 'Image in the Sand'
        if episode_number is 2:
            sea_ep_code = 'DS9, s7e2'
            title = 'Shadows and Symbols'
        if episode_number is 3:
            sea_ep_code = 'DS9, s7e3'
            title = 'Afterimage'
        if episode_number is 4:
            sea_ep_code = 'DS9, s7e4'
            title = 'Take Me Out to the Holosuite'
        if episode_number is 5:
            sea_ep_code = 'DS9, s7e5'
            title = 'Chrysalis'
        if episode_number is 6:
            sea_ep_code = 'DS9, s7e6'
            title = 'Treachery, Faith, and the Great River'
        if episode_number is 7:
            sea_ep_code = 'DS9, s7e7'
            title = 'Once More Unto the Breach'
        if episode_number is 8:
            sea_ep_code = 'DS9, s7e8'
            title = 'The Siege of AR-558'
        if episode_number is 9:
            sea_ep_code = 'DS9, s7e9'
            title = 'Covenant'
        if episode_number is 10:
            sea_ep_code = 'DS9, s7e10'
            title = 'It\'s Only a Paper Moon'
        if episode_number is 11:
            sea_ep_code = 'DS9, s7e11'
            title = 'Prodigal Daughter'
        if episode_number is 12:
            sea_ep_code = 'DS9, s7e12'
            title = 'The Emperor\'s New Cloak'
        if episode_number is 13:
            sea_ep_code = 'DS9, s7e13'
            title = 'Field of Fire'
        if episode_number is 14:
            sea_ep_code = 'DS9, s7e14'
            title = 'Chimera'
        if episode_number is 15:
            sea_ep_code = 'DS9, s7e15'
            title = 'Badda-Bing, Badda-Bang'
        if episode_number is 16:
            sea_ep_code = 'DS9, s7e16'
            title = 'Inter Arma Enim Silent Leges'
        if episode_number is 17:
            sea_ep_code = 'DS9, s7e17'
            title = 'Penumbra'
        if episode_number is 18:
            sea_ep_code = 'DS9, s7e18'
            title = '\'Til Death Do Us Part'
        if episode_number is 19:
            sea_ep_code = 'DS9, s7e19'
            title = 'Strange Bedfellows'
        if episode_number is 20:
            sea_ep_code = 'DS9, s7e20'
            title = 'The Changing Face of Evil'
        if episode_number is 21:
            sea_ep_code = 'DS9, s7e21'
            title = 'When It Rains...'
        if episode_number is 22:
            sea_ep_code = 'DS9, s7e22'
            title = 'Tacking Into the Wind'
        if episode_number is 23:
            sea_ep_code = 'DS9, s7e23'
            title = 'Extreme Measures'
        if episode_number is 24:
            sea_ep_code = 'DS9, s7e24'
            title = 'The Dogs of War'
        if episode_number is 25:
            sea_ep_code = 'DS9, s7e25'
            title = 'What You Leave Behind'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def TNG():
    season_number = random.randrange(1, 8)
    if season_number is 1:
        episode_number = random.randrange(1, 26)
        if episode_number is 1:
            sea_ep_code = 'TNG, s1e1'
            title = 'Encounter at Farpoint'
        if episode_number is 2:
            sea_ep_code = 'TNG, s1e2'
            title = 'The Naked Now'
        if episode_number is 3:
            sea_ep_code = 'TNG, s1e3'
            title = 'Code of Honor'
        if episode_number is 4:
            sea_ep_code = 'TNG, s1e4'
            title = 'The Last Outpost'
        if episode_number is 5:
            sea_ep_code = 'TNG, s1e5'
            title = 'Where No One Has Gone Before'
        if episode_number is 6:
            sea_ep_code = 'TNG, s1e6'
            title = 'Lonely Among Us'
        if episode_number is 7:
            sea_ep_code = 'TNG, s1e7'
            title = 'Justice'
        if episode_number is 8:
            sea_ep_code = 'TNG, s1e8'
            title = 'The Battle'
        if episode_number is 9:
            sea_ep_code = 'TNG, s1e9'
            title = 'Hide and Q'
        if episode_number is 10:
            sea_ep_code = 'TNG, s1e10'
            title = 'Haven'
        if episode_number is 11:
            sea_ep_code = 'TNG, s1e11'
            title = 'The Big Goodbye'
        if episode_number is 12:
            sea_ep_code = 'TNG, s1e12'
            title = 'Datalore'
        if episode_number is 13:
            sea_ep_code = 'TNG, s1e13'
            title = 'Angel One'
        if episode_number is 14:
            sea_ep_code = 'TNG, s1e14'
            title = '11001001'
        if episode_number is 15:
            sea_ep_code = 'TNG, s1e15'
            title = 'Too Short a Season'
        if episode_number is 16:
            sea_ep_code = 'TNG, s1e16'
            title = 'When the Bough Breaks'
        if episode_number is 17:
            sea_ep_code = 'TNG, s1e17'
            title = 'Home Soil'
        if episode_number is 18:
            sea_ep_code = 'TNG, s1e18'
            title = 'Coming of Age'
        if episode_number is 19:
            sea_ep_code = 'TNG, s1e19'
            title = 'Heart of Glory'
        if episode_number is 20:
            sea_ep_code = 'TNG, s1e20'
            title = 'The Arsenal of Freedom'
        if episode_number is 21:
            sea_ep_code = 'TNG, s1e21'
            title = 'Symbios='
        if episode_number is 22:
            sea_ep_code = 'TNG, s1e22'
            title = 'Skin of Evil'
        if episode_number is 23:
            sea_ep_code = 'TNG, s1e23'
            title = 'We\'ll Always Have Paris'
        if episode_number is 24:
            sea_ep_code = 'TNG, s1e24'
            title = 'Conspiracy'
        if episode_number is 25:
            sea_ep_code = 'TNG, s1e25'
            title = 'The Neutral Zone'
    if season_number is 2:
        episode_number = random.randrange(1, 23)
        if episode_number is 1:
            sea_ep_code = 'TNG, s2e1'
            title = 'The Child'
        if episode_number is 2:
            sea_ep_code = 'TNG, s2e2'
            title = 'Where Silence Has Lease'
        if episode_number is 3:
            sea_ep_code = 'TNG, s2e3'
            title = 'Elementary, Dear Data'
        if episode_number is 4:
            sea_ep_code = 'TNG, s2e4'
            title = 'The Outrageous Okona'
        if episode_number is 5:
            sea_ep_code = 'TNG, s2e5'
            title = 'Loud as a Whisper'
        if episode_number is 6:
            sea_ep_code = 'TNG, s2e6'
            title = 'The Schizoid Man'
        if episode_number is 7:
            sea_ep_code = 'TNG, s2e7'
            title = 'Unnatural Selection'
        if episode_number is 8:
            sea_ep_code = 'TNG, s2e8'
            title = 'A Matter of Honor'
        if episode_number is 9:
            sea_ep_code = 'TNG, s2e9'
            title = 'The Measure of a Man'
        if episode_number is 10:
            sea_ep_code = 'TNG, s2e10'
            title = 'The Dauphin'
        if episode_number is 11:
            sea_ep_code = 'TNG, s2e11'
            title = 'Contagion'
        if episode_number is 12:
            sea_ep_code = 'TNG, s2e12'
            title = 'The Royale'
        if episode_number is 13:
            sea_ep_code = 'TNG, s2e13'
            title = 'Time Squared'
        if episode_number is 14:
            sea_ep_code = 'TNG, s2e14'
            title = 'The Icarus Factor'
        if episode_number is 15:
            sea_ep_code = 'TNG, s2e15'
            title = 'Pen Pals'
        if episode_number is 16:
            sea_ep_code = 'TNG, s2e16'
            title = 'Q Who?'
        if episode_number is 17:
            sea_ep_code = 'TNG, s2e17'
            title = 'Samaritan Snare'
        if episode_number is 18:
            sea_ep_code = 'TNG, s2e18'
            title = 'Up the Long Ladder'
        if episode_number is 19:
            sea_ep_code = 'TNG, s2e19'
            title = 'Manhunt'
        if episode_number is 20:
            sea_ep_code = 'TNG, s2e20'
            title = 'The Emissary'
        if episode_number is 21:
            sea_ep_code = 'TNG, s2e21'
            title = 'Peak Performance'
        if episode_number is 22:
            sea_ep_code = 'TNG, s2e22'
            title = 'Shades of Gray'
    if season_number is 3:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'TNG, s3e1'
            title = 'Evolution'
        if episode_number is 2:
            sea_ep_code = 'TNG, s3e2'
            title = 'The Ensigns of Command'
        if episode_number is 3:
            sea_ep_code = 'TNG, s3e3'
            title = 'The Survivors'
        if episode_number is 4:
            sea_ep_code = 'TNG, s3e4'
            title = 'Who Watches the Watchers'
        if episode_number is 5:
            sea_ep_code = 'TNG, s3e5'
            title = 'The Bonding'
        if episode_number is 6:
            sea_ep_code = 'TNG, s3e6'
            title = 'Booby Trap'
        if episode_number is 7:
            sea_ep_code = 'TNG, s3e7'
            title = 'The Enemy'
        if episode_number is 8:
            sea_ep_code = 'TNG, s3e8'
            title = 'The Price'
        if episode_number is 9:
            sea_ep_code = 'TNG, s3e9'
            title = 'The Vengeance Factor'
        if episode_number is 10:
            sea_ep_code = 'TNG, s3e10'
            title = 'The Defector'
        if episode_number is 11:
            sea_ep_code = 'TNG, s3e11'
            title = 'The Hunted'
        if episode_number is 12:
            sea_ep_code = 'TNG, s3e12'
            title = 'The High Ground'
        if episode_number is 13:
            sea_ep_code = 'TNG, s3e13'
            title = 'Deja Q'
        if episode_number is 14:
            sea_ep_code = 'TNG, s3e14'
            title = 'A Matter of Perspective'
        if episode_number is 15:
            sea_ep_code = 'TNG, s3e15'
            title = 'Yesterday\'s Enterprise'
        if episode_number is 16:
            sea_ep_code = 'TNG, s3e16'
            title = 'The Offspring'
        if episode_number is 17:
            sea_ep_code = 'TNG, s3e17'
            title = 'Sins of the Father'
        if episode_number is 18:
            sea_ep_code = 'TNG, s3e18'
            title = 'Allegiance'
        if episode_number is 19:
            sea_ep_code = 'TNG, s3e19'
            title = 'Captain\'s Holiday'
        if episode_number is 20:
            sea_ep_code = 'TNG, s3e20'
            title = 'Tin Man'
        if episode_number is 21:
            sea_ep_code = 'TNG, s3e20'
            title = 'Hollow Pursuits'
        if episode_number is 22:
            sea_ep_code = 'TNG, s3e22'
            title = 'The Most Toys'
        if episode_number is 23:
            sea_ep_code = 'TNG, s3e23'
            title = 'Sarek'
        if episode_number is 24:
            sea_ep_code = 'TNG, s3e24'
            title = 'Menage a Troi'
        if episode_number is 25:
            sea_ep_code = 'TNG, s3e25'
            title = 'Transfigurations'
        if episode_number is 26:
            sea_ep_code = 'TNG, s3e26'
            title = 'The Best of Both Worlds: Part 1'
    if season_number is 4:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'TNG, s4e1'
            title = 'The Best of Both Worlds: Part 2'
        if episode_number is 2:
            sea_ep_code = 'TNG, s4e2'
            title = 'Family'
        if episode_number is 3:
            sea_ep_code = 'TNG, s4e3'
            title = 'Brothers'
        if episode_number is 4:
            sea_ep_code = 'TNG, s4e4'
            title = 'Suddenly Human'
        if episode_number is 5:
            sea_ep_code = 'TNG, s4e5'
            title = 'Remember Me'
        if episode_number is 6:
            sea_ep_code = 'TNG, s4e6'
            title = 'Legacy'
        if episode_number is 7:
            sea_ep_code = 'TNG, s4e7'
            title = 'Reunion'
        if episode_number is 8:
            sea_ep_code = 'TNG, s4e8'
            title = 'Future Imperfect'
        if episode_number is 9:
            sea_ep_code = 'TNG, s4e9'
            title = 'Final Mission'
        if episode_number is 10:
            sea_ep_code = 'TNG, s4e10'
            title = 'The Loss'
        if episode_number is 11:
            sea_ep_code = 'TNG, s4e11'
            title = 'Data\'s Day'
        if episode_number is 12:
            sea_ep_code = 'TNG, s4e12'
            title = 'The Wounded'
        if episode_number is 13:
            sea_ep_code = 'TNG, s4e13'
            title = 'Devil\'s Due'
        if episode_number is 14:
            sea_ep_code = 'TNG, s4e14'
            title = 'Clues'
        if episode_number is 15:
            sea_ep_code = 'TNG, s4e15'
            title = 'First Contact'
        if episode_number is 16:
            sea_ep_code = 'TNG, s4e16'
            title = 'Galaxy\'s Child'
        if episode_number is 17:
            sea_ep_code = 'TNG, s4e17'
            title = 'Night Terrors'
        if episode_number is 18:
            sea_ep_code = 'TNG, s4e18'
            title = 'Identity Crisis'
        if episode_number is 19:
            sea_ep_code = 'TNG, s4e19'
            title = 'The Nth Degree'
        if episode_number is 20:
            sea_ep_code = 'TNG, s4e20'
            title = 'Qpid'
        if episode_number is 21:
            sea_ep_code = 'TNG, s4e21'
            title = 'The Drumhead'
        if episode_number is 22:
            sea_ep_code = 'TNG, s4e22'
            title = 'Half a Life'
        if episode_number is 23:
            sea_ep_code = 'TNG, s4e23'
            title = 'The Host'
        if episode_number is 24:
            sea_ep_code = 'TNG, s4e24'
            title = 'The Mind\'s Eye'
        if episode_number is 25:
            sea_ep_code = 'TNG, s4e25'
            title = 'In Theory'
        if episode_number is 26:
            sea_ep_code = 'TNG, s4e26'
            title = 'Redemption'
    if season_number is 5:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'TNG, s5e1'
            title = 'Redemption II'
        if episode_number is 2:
            sea_ep_code = 'TNG, s5e2'
            title = 'Darmok'
        if episode_number is 3:
            sea_ep_code = 'TNG, s5e3'
            title = 'Ensign Ro'
        if episode_number is 4:
            sea_ep_code = 'TNG, s5e4'
            title = 'Silicon Avatar'
        if episode_number is 5:
            sea_ep_code = 'TNG, s5e5'
            title = 'Disaster'
        if episode_number is 6:
            sea_ep_code = 'TNG, s5e6'
            title = 'The Game'
        if episode_number is 7:
            sea_ep_code = 'TNG, s5e7'
            title = 'Unification I'
        if episode_number is 8:
            sea_ep_code = 'TNG, s5e8'
            title = 'Unification II'
        if episode_number is 9:
            sea_ep_code = 'TNG, s5e9'
            title = 'A Matter of Time'
        if episode_number is 10:
            sea_ep_code = 'TNG, s5e10'
            title = 'New Ground'
        if episode_number is 11:
            sea_ep_code = 'TNG, s5e11'
            title = 'Hero Worship'
        if episode_number is 12:
            sea_ep_code = 'TNG, s5e12'
            title = 'Violations'
        if episode_number is 13:
            sea_ep_code = 'TNG, s5e13'
            title = 'The Masterpiece Society'
        if episode_number is 14:
            sea_ep_code = 'TNG, s5e14'
            title = 'Conundrum'
        if episode_number is 15:
            sea_ep_code = 'TNG, s5e15'
            title = 'Power Play'
        if episode_number is 16:
            sea_ep_code = 'TNG, s5e16'
            title = 'Ethics'
        if episode_number is 17:
            sea_ep_code = 'TNG, s5e17'
            title = 'The Outcast'
        if episode_number is 18:
            sea_ep_code = 'TNG, s5e18'
            title = 'Cause and Effect'
        if episode_number is 19:
            sea_ep_code = 'TNG, s5e19'
            title = 'The First Duty'
        if episode_number is 20:
            sea_ep_code = 'TNG, s5e20'
            title = 'Cost of Living'
        if episode_number is 21:
            sea_ep_code = 'TNG, s5e21'
            title = 'The Perfect Mate'
        if episode_number is 22:
            sea_ep_code = 'TNG, s5e22'
            title = 'Imaginary Friend'
        if episode_number is 23:
            sea_ep_code = 'TNG, s5e23'
            title = 'I Borg'
        if episode_number is 24:
            sea_ep_code = 'TNG, s5e24'
            title = 'The Next Phase'
        if episode_number is 25:
            sea_ep_code = 'TNG, s5e25'
            title = 'The Inner Light'
        if episode_number is 26:
            sea_ep_code = 'TNG, s5e26'
            title = 'Time\'s Arrow: Part 1'
    if season_number is 6:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'TNG, s6e1'
            title = 'Time\'s Arrow: Part 2'
        if episode_number is 2:
            sea_ep_code = 'TNG, s6e2'
            title = 'Realm of Fear'
        if episode_number is 3:
            sea_ep_code = 'TNG, s6e3'
            title = 'Man of the People'
        if episode_number is 4:
            sea_ep_code = 'TNG, s6e4'
            title = 'Relics'
        if episode_number is 5:
            sea_ep_code = 'TNG, s6e5'
            title = 'Schisms'
        if episode_number is 6:
            sea_ep_code = 'TNG, s6e6'
            title = 'True Q'
        if episode_number is 7:
            sea_ep_code = 'TNG, s6e7'
            title = 'Rascals'
        if episode_number is 8:
            sea_ep_code = 'TNG, s6e8'
            title = 'A Fistful of Datas'
        if episode_number is 9:
            sea_ep_code = 'TNG, s6e9'
            title = 'The Quality of Life'
        if episode_number is 10:
            sea_ep_code = 'TNG, s6e10'
            title = 'Chain of Command: Part 1'
        if episode_number is 11:
            sea_ep_code = 'TNG, s6e11'
            title = 'Chain of Command: Part 2'
        if episode_number is 12:
            sea_ep_code = 'TNG, s6e12'
            title = 'Ship in a Bottle'
        if episode_number is 13:
            sea_ep_code = 'TNG, s6e13'
            title = 'Aquiel'
        if episode_number is 14:
            sea_ep_code = 'TNG, s6e14'
            title = 'Face of the Enemy'
        if episode_number is 15:
            sea_ep_code = 'TNG, s6e15'
            title = 'Tapestry'
        if episode_number is 16:
            sea_ep_code = 'TNG, s6e16'
            title = 'Birthright: Part 1'
        if episode_number is 17:
            sea_ep_code = 'TNG, s6e17'
            title = 'Birthright: Part 2'
        if episode_number is 18:
            sea_ep_code = 'TNG, s6e18'
            title = 'Starship Mine'
        if episode_number is 19:
            sea_ep_code = 'TNG, s6e19'
            title = 'Lessons'
        if episode_number is 20:
            sea_ep_code = 'TNG, s6e20'
            title = 'The Chase'
        if episode_number is 21:
            sea_ep_code = 'TNG, s6e21'
            title = 'Frame of Mind'
        if episode_number is 22:
            sea_ep_code = 'TNG, s6e22'
            title = 'Suspicions'
        if episode_number is 23:
            sea_ep_code = 'TNG, s6e23'
            title = 'Rightful Heir'
        if episode_number is 24:
            sea_ep_code = 'TNG, s6e24'
            title = 'Second Chances'
        if episode_number is 25:
            sea_ep_code = 'TNG, s6e25'
            title = 'Timescape'
        if episode_number is 26:
            sea_ep_code = 'TNG, s6e26'
            title = 'Descent: Part 1'
    if season_number is 7:
        episode_number = random.randrange(1, 26)
        if episode_number is 1:
            sea_ep_code = 'TNG, s7e1'
            title = 'Descent: Part 2'
        if episode_number is 2:
            sea_ep_code = 'TNG, s7e2'
            title = 'Liaisons'
        if episode_number is 3:
            sea_ep_code = 'TNG, s7e3'
            title = 'Interface'
        if episode_number is 4:
            sea_ep_code = 'TNG, s7e4'
            title = 'Gambit: Part 1'
        if episode_number is 5:
            sea_ep_code = 'TNG, s7e5'
            title = 'Gambit: Part 2'
        if episode_number is 6:
            sea_ep_code = 'TNG, s7e6'
            title = 'Phantasms'
        if episode_number is 7:
            sea_ep_code = 'TNG, s7e7'
            title = 'Dark Page'
        if episode_number is 8:
            sea_ep_code = 'TNG, s7e8'
            title = 'Attached'
        if episode_number is 9:
            sea_ep_code = 'TNG, s7e9'
            title = 'Force of Nature'
        if episode_number is 10:
            sea_ep_code = 'TNG, s7e10'
            title = 'Inheritance'
        if episode_number is 11:
            sea_ep_code = 'TNG, s7e11'
            title = 'Parallels'
        if episode_number is 12:
            sea_ep_code = 'TNG, s7e12'
            title = 'The Pegasus'
        if episode_number is 13:
            sea_ep_code = 'TNG, s7e13'
            title = 'Homeward'
        if episode_number is 14:
            sea_ep_code = 'TNG, s7e14'
            title = 'Sub Rosa'
        if episode_number is 15:
            sea_ep_code = 'TNG, s7e15'
            title = 'Lower Decks'
        if episode_number is 16:
            sea_ep_code = 'TNG, s7e16'
            title = 'Thine Own Self'
        if episode_number is 17:
            sea_ep_code = 'TNG, s7e17'
            title = 'Masks'
        if episode_number is 18:
            sea_ep_code = 'TNG, s7e18'
            title = 'Eye of the Beholder'
        if episode_number is 19:
            sea_ep_code = 'TNG, s7e19'
            title = 'Genes='
        if episode_number is 20:
            sea_ep_code = 'TNG, s7e20'
            title = 'Journey\'s End'
        if episode_number is 21:
            sea_ep_code = 'TNG, s7e21'
            title = 'Firstborn'
        if episode_number is 22:
            sea_ep_code = 'TNG, s7e22'
            title = 'Bloodlines'
        if episode_number is 23:
            sea_ep_code = 'TNG, s7e23'
            title = 'Emergence'
        if episode_number is 24:
            sea_ep_code = 'TNG, s7e24'
            title = 'Preemptive Strike'
        if episode_number is 25:
            sea_ep_code = 'TNG, s7e25'
            title = 'All Good Things...'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def ENT():
    season_number = random.randrange(1, 5)
    if season_number is 1:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'ENT, s1e1'
            title = 'Broken Bow: Part 1'
        if episode_number is 2:
            sea_ep_code = 'ENT, s1e2'
            title = 'Broken Bow: Part 2'
        if episode_number is 3:
            sea_ep_code = 'ENT, s1e3'
            title = 'Fight or Flight'
        if episode_number is 4:
            sea_ep_code = 'ENT, s1e4'
            title = 'Strange New World'
        if episode_number is 5:
            sea_ep_code = 'ENT, s1e5'
            title = 'Unexpected'
        if episode_number is 6:
            sea_ep_code = 'ENT, s1e6'
            title = 'Terra Nova'
        if episode_number is 7:
            sea_ep_code = 'ENT, s1e7'
            title = 'The Andorian Incident'
        if episode_number is 8:
            sea_ep_code = 'ENT, s1e8'
            title = 'Breaking the Ice'
        if episode_number is 9:
            sea_ep_code = 'ENT, s1e9'
            title = 'Civilization'
        if episode_number is 10:
            sea_ep_code = 'ENT, s1e10'
            title = 'Fortunate Son'
        if episode_number is 11:
            sea_ep_code = 'ENT, s1e11'
            title = 'Cold Front'
        if episode_number is 12:
            sea_ep_code = 'ENT, s1e12'
            title = 'Silent Enemy'
        if episode_number is 13:
            sea_ep_code = 'ENT, s1e13'
            title = 'Dear Doctor'
        if episode_number is 14:
            sea_ep_code = 'ENT, s1e14'
            title = 'Sleeping Dogs'
        if episode_number is 15:
            sea_ep_code = 'ENT, s1e15'
            title = 'Shadows of P\'Jem'
        if episode_number is 16:
            sea_ep_code = 'ENT, s1e16'
            title = 'Shuttlepod One'
        if episode_number is 17:
            sea_ep_code = 'ENT, s1e17'
            title = 'Fusion'
        if episode_number is 18:
            sea_ep_code = 'ENT, s1e18'
            title = 'Rogue Planet'
        if episode_number is 19:
            sea_ep_code = 'ENT, s1e19'
            title = 'Acquisition'
        if episode_number is 20:
            sea_ep_code = 'ENT, s1e20'
            title = 'Oasis'
        if episode_number is 21:
            sea_ep_code = 'ENT, s1e21'
            title = 'Detained'
        if episode_number is 22:
            sea_ep_code = 'ENT, s1e22'
            title = 'Vox Sola'
        if episode_number is 23:
            sea_ep_code = 'ENT, s1e23'
            title = 'Fallen Hero'
        if episode_number is 24:
            sea_ep_code = 'ENT, s1e24'
            title = 'Desert Crossing'
        if episode_number is 25:
            sea_ep_code = 'ENT, s1e25'
            title = 'Two Days and Two Nights'
        if episode_number is 26:
            sea_ep_code = 'ENT, s1e26'
            title = 'Shockwave: Part 1'
    if season_number is 2:
        episode_number = random.randrange(1, 27)
        if episode_number is 1:
            sea_ep_code = 'ENT, s2e1'
            title = 'Shockwave: Part 2'
        if episode_number is 2:
            sea_ep_code = 'ENT, s2e2'
            title = 'Carbon Creek'
        if episode_number is 3:
            sea_ep_code = 'ENT, s2e3'
            title = 'Minefield'
        if episode_number is 4:
            sea_ep_code = 'ENT, s2e4'
            title = 'Dead Stop'
        if episode_number is 5:
            sea_ep_code = 'ENT, s2e5'
            title = 'A Night in Sickbay'
        if episode_number is 6:
            sea_ep_code = 'ENT, s2e6'
            title = 'Marauders'
        if episode_number is 7:
            sea_ep_code = 'ENT, s2e7'
            title = 'The Seventh'
        if episode_number is 8:
            sea_ep_code = 'ENT, s2e8'
            title = 'The Communicator'
        if episode_number is 9:
            sea_ep_code = 'ENT, s2e9'
            title = 'Singularity'
        if episode_number is 10:
            sea_ep_code = 'ENT, s2e10'
            title = 'Vanishing Point'
        if episode_number is 11:
            sea_ep_code = 'ENT, s2e11'
            title = 'Precious Cargo'
        if episode_number is 12:
            sea_ep_code = 'ENT, s2e12'
            title = 'The Catwalk'
        if episode_number is 13:
            sea_ep_code = 'ENT, s2e13'
            title = 'Dawn'
        if episode_number is 14:
            sea_ep_code = 'ENT, s2e14'
            title = 'Stigma'
        if episode_number is 15:
            sea_ep_code = 'ENT, s2e15'
            title = 'Cease Fire'
        if episode_number is 16:
            sea_ep_code = 'ENT, s2e16'
            title = 'Future Tense'
        if episode_number is 17:
            sea_ep_code = 'ENT, s2e17'
            title = 'Canamar'
        if episode_number is 18:
            sea_ep_code = 'ENT, s2e18'
            title = 'The Crossing'
        if episode_number is 19:
            sea_ep_code = 'ENT, s2e19'
            title = 'Judgment'
        if episode_number is 20:
            sea_ep_code = 'ENT, s2e20'
            title = 'Horizon'
        if episode_number is 21:
            sea_ep_code = 'ENT, s2e21'
            title = 'The Breach'
        if episode_number is 22:
            sea_ep_code = 'ENT, s2e22'
            title = 'Cogenitor'
        if episode_number is 23:
            sea_ep_code = 'ENT, s2e23'
            title = 'Regeneration'
        if episode_number is 24:
            sea_ep_code = 'ENT, s2e24'
            title = 'First Flight'
        if episode_number is 25:
            sea_ep_code = 'ENT, s2e25'
            title = 'Bounty'
        if episode_number is 26:
            sea_ep_code = 'ENT, s2e26'
            title = 'The Expanse'
    if season_number is 3:
        episode_number = random.randrange(1, 25)
        if episode_number is 1:
            sea_ep_code = 'ENT, s3e1'
            title = 'The Xindi'
        if episode_number is 2:
            sea_ep_code = 'ENT, s3e2'
            title = 'Anomaly'
        if episode_number is 3:
            sea_ep_code = 'ENT, s3e3'
            title = 'Extinction'
        if episode_number is 4:
            sea_ep_code = 'ENT, s3e4'
            title = 'Rajiin'
        if episode_number is 5:
            sea_ep_code = 'ENT, s3e5'
            title = 'Impulse'
        if episode_number is 6:
            sea_ep_code = 'ENT, s3e6'
            title = 'Exile'
        if episode_number is 7:
            sea_ep_code = 'ENT, s3e7'
            title = 'The Shipment'
        if episode_number is 8:
            sea_ep_code = 'ENT, s3e8'
            title = 'Twilight'
        if episode_number is 9:
            sea_ep_code = 'ENT, s3e9'
            title = 'North Star'
        if episode_number is 10:
            sea_ep_code = 'ENT, s3e10'
            title = 'Similitude'
        if episode_number is 11:
            sea_ep_code = 'ENT, s3e11'
            title = 'Carpenter Street'
        if episode_number is 12:
            sea_ep_code = 'ENT, s3e12'
            title = 'Chosen Realm'
        if episode_number is 13:
            sea_ep_code = 'ENT, s3e13'
            title = 'Proving Ground'
        if episode_number is 14:
            sea_ep_code = 'ENT, s3e14'
            title = 'Stratagem'
        if episode_number is 15:
            sea_ep_code = 'ENT, s3e15'
            title = 'Harbinger'
        if episode_number is 16:
            sea_ep_code = 'ENT, s3e16'
            title = 'Doctor\'s Orders'
        if episode_number is 17:
            sea_ep_code = 'ENT, s3e17'
            title = 'Hatchery'
        if episode_number is 18:
            sea_ep_code = 'ENT, s3e18'
            title = 'Azati Prime'
        if episode_number is 19:
            sea_ep_code = 'ENT, s3e19'
            title = 'Damage'
        if episode_number is 20:
            sea_ep_code = 'ENT, s3e20'
            title = 'The Forgotten'
        if episode_number is 21:
            sea_ep_code = 'ENT, s3e21'
            title = 'E^2'
        if episode_number is 22:
            sea_ep_code = 'ENT, s3e22'
            title = 'The Council'
        if episode_number is 23:
            sea_ep_code = 'ENT, s3e23'
            title = 'Countdown'        
        if episode_number is 24:
            sea_ep_code = 'ENT, s3e24'
            title = 'Zero Hour'
    if season_number is 4:
        episode_number = random.randrange(1, 22)
        if episode_number is 1:
            sea_ep_code = 'ENT, s4e1'
            title = 'Storm Front: Part 1'
        if episode_number is 2:
            sea_ep_code = 'ENT, s4e2'
            title = 'Storm Front: Part 2'
        if episode_number is 3:
            sea_ep_code = 'ENT, s4e3'
            title = 'Borderland'
        if episode_number is 4:
            sea_ep_code = 'ENT, s4e4'
            title = 'Cold Station 12'
        if episode_number is 5:
            sea_ep_code = 'ENT, s4e5'
            title = 'The Augments'
        if episode_number is 6:
            sea_ep_code = 'ENT, s4e6'
            title = 'The Forge'
        if episode_number is 7:
            sea_ep_code = 'ENT, s4e7'
            title = 'Awakening'
        if episode_number is 8:
            sea_ep_code = 'ENT, s4e8'
            title = 'Kir\'Shara'
        if episode_number is 9:
            sea_ep_code = 'ENT, s4e9'
            title = 'Daedalus'
        if episode_number is 10:
            sea_ep_code = 'ENT, s4e10'
            title = 'Observer Effect'
        if episode_number is 11:
            sea_ep_code = 'ENT, s4e11'
            title = 'Babel One'
        if episode_number is 12:
            sea_ep_code = 'ENT, s4e12'
            title = 'United'
        if episode_number is 13:
            sea_ep_code = 'ENT, s4e13'
            title = 'The Aenar'
        if episode_number is 14:
            sea_ep_code = 'ENT, s4e14'
            title = 'Affliction'
        if episode_number is 15:
            sea_ep_code = 'ENT, s4e15'
            title = 'Divergence'
        if episode_number is 16:
            sea_ep_code = 'ENT, s4e16'
            title = 'Bound'
        if episode_number is 17:
            sea_ep_code = 'ENT, s4e17'
            title = 'In a Mirror, Darkly: Part 1'
        if episode_number is 18:
            sea_ep_code = 'ENT, s4e18'
            title = 'In a Mirror, Darkly: Part 2'
        if episode_number is 19:
            sea_ep_code = 'ENT, s4e19'
            title = 'Demons'
        if episode_number is 20:
            sea_ep_code = 'ENT, s4e20'
            title = 'Terra Prime'
        if episode_number is 21:
            sea_ep_code = 'ENT, s4e21'
            title = 'These Are the Voyages...'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def MOV():
    episode_number = random.randrange(1, 11)
    if episode_number is 1:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek: The Motion Picture'
    if episode_number is 2:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek II: The Wrath of Khan'    
    if episode_number is 3:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek III: The Search for Spock'    
    if episode_number is 4:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek IV: The Voyage Home'    
    if episode_number is 5:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek V: The Final Frontier'    
    if episode_number is 6:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek VI: The Undiscovered Country'    
    if episode_number is 7:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek Generations'    
    if episode_number is 8:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek: First Contact'    
    if episode_number is 9:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek: Insurrection'   
    if episode_number is 10:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek: Nemesis'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
def NUTREK():
    episode_number = random.randrange(1,4)
    if episode_number is 1:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek (2009)'
    if episode_number is 2:
        sea_ep_code = 'MOVIE'
        title = 'Stark Trek: Into Darkness'
    if episode_number is 3:
        sea_ep_code = 'MOVIE'
        title = 'Star Trek: Beyond'
    sea_ep_code = str(sea_ep_code)
    title = str(title)
    print "You'll be watching "+sea_ep_code+": "+title
    
    
#select series based on first random number
if number == 1:
    TOS()
if number == 2:
    TAS()
if number == 3:
    TNG()
if number == 4:
    DS9()
if number == 5:
    VOY()
if number == 6:
    ENT()
if number == 7:
    MOV()
if number == 8:
    NUTREK()