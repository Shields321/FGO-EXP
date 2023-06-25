import PySimpleGUI as sg

# CONSTANTS
SCEB = 1.20 # Same Card EXP Bonus 
BASE_EXP_5 = 81000
BASE_EXP_4 = 27000
BASE_EXP_3 = 9000
LV_100_MAX = 20311500
LV_120_MAX = 426541500

# Function to check for negative values in the input
def has_negative(cards):
    for card in cards:
        if(card['5'] < 0 or card['4'] < 0 or card['3'] < 0):
            return True;

    return False;

#getting the 5 star card exp 

# Add some color
# to the window
sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys

layout = [
	[sg.Text('Please select the servant class you want to level up with 5 star EXP cards')],
    [sg.DropDown(["Saber", "Archer", "Lancer", "Rider", "Caster", "Assassin", "Berserker", "Extra"], size=(25, 1), default_value="Saber")],
    [sg.Text('EXP Class Card', size=(15, 1)), sg.Text('5⭐', size=(15, 1)),sg.Text('4⭐', size=(15, 1)), sg.Text('3⭐', size=(15, 1))],
	[sg.Text('Saber', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Archer', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Lancer', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Rider', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Caster', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Assassin', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('Berserker', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text('All', size =(15, 1)), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0"), sg.InputText(size=(15, 1), default_text="0")],
    [sg.Text(size=(60,1), key='-ERROR-', background_color="red", text_color="white", visible=False)],
	[sg.Submit(), sg.Quit()],
    [sg.Text(size=(60,1), key='-OUTPUT_100-')],
    [sg.Text(size=(60,2), key='-OUTPUT_100_SAME-')],
    [sg.Text(size=(60,1), key='-OUTPUT_120-')],
    [sg.Text(size=(60,2), key='-OUTPUT_120_SAME-')]
]

window = sg.Window('FGO EXP calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    try:
        character = values[0].lower()

        SaberExp = {
            'type': "saber",
            '5': int(values[1]),
            '4': int(values[2]),
            '3': int(values[3])
        }

        ArcherExp = {
            'type': "archer",
            '5': int(values[4]),
            '4': int(values[5]),
            '3': int(values[6])
        }

        LancerExp = {
            'type': "lancer",
            '5': int(values[7]),
            '4': int(values[8]),
            '3': int(values[9])
        }

        RiderExp = {
            'type': "rider",
            '5': int(values[10]),
            '4': int(values[11]),
            '3': int(values[12])
        }

        CasterExp = {
            'type': "caster",
            '5': int(values[13]),
            '4': int(values[14]),
            '3': int(values[15])
        }

        AssassinExp = {
            'type': "assassin",
            '5': int(values[16]),
            '4': int(values[17]),
            '3': int(values[18])
        }

        BerserkerExp = {
            'type': "berserker",
            '5': int(values[19]),
            '4': int(values[20]),
            '3': int(values[21])
        }

        ExtraExp = {
            'type': "extra",
            '5': int(values[22]),
            '4': int(values[23]),
            '3': int(values[24])
        }

        cards = [SaberExp, ArcherExp, LancerExp, RiderExp, CasterExp, AssassinExp, BerserkerExp, ExtraExp]

        if(has_negative(cards)): raise ValueError()

        total_5exp = sum([card['5'] * BASE_EXP_5 if card['type'] != character else card['5'] * (BASE_EXP_5 * SCEB) for card in cards ])
        total_4exp = sum([card['4'] * BASE_EXP_4 if card['type'] != character else card['4'] * (BASE_EXP_4 * SCEB) for card in cards ])
        total_3exp = sum([card['3'] * BASE_EXP_3 if card['type'] != character else card['3'] * (BASE_EXP_3 * SCEB) for card in cards ])

        #print the values for the amount of exp and how much exp is needed left to get different lvls
        #amount needed for lvl 100
        # --------------------------------------------------------------------------- #

        total_exp = total_5exp + total_4exp + total_3exp
        print("Total exp gained from cards is")
        print(total_exp)

        print("amount needed to get servant lvl 100")
        final_total_100 = LV_100_MAX - total_exp

        if final_total_100<=0:
            final_total_100 = 0

        print(final_total_100)

        # --------------------------------------------------------------------------- #

        cards_left_100 = final_total_100 / BASE_EXP_5

        if cards_left_100 < 0:
            cards_left_100 = 0

        print("Amount of 5 star exp cards needed left to lv 100")
        print(cards_left_100)

        # --------------------------------------------------------------------------- #

        cards_left_100_same = final_total_100 / (BASE_EXP_5 * SCEB);

        if cards_left_100_same < 0:
            cards_left_100_same = 0

        print("Amount of 5 star exp cards of same class needed left to lv 100")
        print(cards_left_100_same)

        # --------------------------------------------------------------------------- #

        #amount for lvl 120

        print("amount needed to get servant lvl 120")
        final_total_120 = LV_120_MAX - total_exp

        if final_total_120<=0:
            final_total_120 = 0

        print(final_total_120)

        # --------------------------------------------------------------------------- #

        cards_left_120 = final_total_120 / BASE_EXP_5

        if cards_left_120 < 0:
            cards_left_120 = 0

        print("Amount of 5 star exp cards needed left to lv 120")
        print(cards_left_120)

        # --------------------------------------------------------------------------- #

        cards_left_120_same = final_total_120 / (BASE_EXP_5 * SCEB)

        if cards_left_120_same < 0:
            cards_left_120_same = 0

        print("Amount of 5 star exp cards of same class needed left to lv 120")
        print(cards_left_120_same)

        # --------------------------------------------------------------------------- #

        window['-OUTPUT_100-'].update(f"{round(cards_left_100)} <5⭐> EXP cards left to reach LV 100", text_color='green')
        window['-OUTPUT_100_SAME-'].update(f"{round(cards_left_100_same)} <5⭐> EXP cards left of the same class to reach LV 100", text_color='green', background_color="yellow")

        window['-OUTPUT_120-'].update(f"{round(cards_left_120)} <5⭐> EXP cards left to reach LV 120", text_color='green')
        window['-OUTPUT_120_SAME-'].update(f"{round(cards_left_120_same)} <5⭐> EXP cards left of the same class to reach LV 120", text_color='green', background_color="yellow")
       
    except ValueError as ve:
        window['-ERROR-'].update("Please enter only positive numbers for the amount of exp cards", visible=True)
    except IndexError as ie:
        window['-ERROR-'].update("Index Out of bounds. No clue how this happended", visible=True)
    except:
        window['-ERROR-'].update("Some unknown error happened", visible=True)

window.close()



