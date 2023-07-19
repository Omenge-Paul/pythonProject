shuffled_cards = {
    'card 2' : 2,
    'card 3' : 3,
    'card 4' : 4,
    'card 5' : 5,
    'card 6' : 6,
    'card 7' : 7,
    'card 8' : 8,
    'card 9' : 9,
    'card 10': 10,
    'ace1' : 1 ,
    'ace2' : 10,
    'king': 10,
    'queen' : 10,
    'jack' : 10
}
def  tupule_to_dict(tupule):
    key = tupule[0]
    value = tupule[1]
    dictionary = {key:value}
    return dictionary
shuffled_52cards = [(key, value) for key,value in shuffled_cards.items()]
list_of_dictionaries = []
for tuple_in_list in shuffled_52cards:
    tuple_changed_to_dictionary = tupule_to_dict(tuple_in_list)   
    list_of_dictionaries.append(tuple_changed_to_dictionary)
len_list_of_dictionaries = len(list_of_dictionaries)
len_of_dictionaries_quotient = len_list_of_dictionaries // 2
def deal_player_cards(list):
    card_dealt = list[len_of_dictionaries_quotient]
    return card_dealt
def get_card_key(card):
    for dealt_card1 in card:
        real_dealt_card1 = dealt_card1
        return real_dealt_card1
def get_dealt_card_value(card,card_key):
    dealt_card_value = card[f'{card_key}']
    return dealt_card_value
while len_list_of_dictionaries > 7:
    if input('Welcome to Blackjack. \nI hope you are familiar with the rules.\nTo start please enter \'play\'.\nTo continue playing subsequent rounds just still enter \'play\':  ').lower() == 'play':
        player_card1 = deal_player_cards(list_of_dictionaries)
        player_card1_key = get_card_key(player_card1)
        player_card1_value = get_dealt_card_value(player_card1,player_card1_key)
        list_of_dictionaries.remove(player_card1)
        player_card2 = deal_player_cards(list_of_dictionaries)
        player_card2_key = get_card_key(player_card2)
        player_card2_value = get_dealt_card_value(player_card2,player_card2_key)
        list_of_dictionaries.remove(player_card2)
        combined_player_cards_value = (player_card1_value + player_card2_value)
        dealer_card1 = deal_player_cards(list_of_dictionaries)
        dealer_card1_key = get_card_key(dealer_card1)
        dealer_card1_value = get_dealt_card_value(dealer_card1,dealer_card1_key)
        list_of_dictionaries.remove(dealer_card1)
        dealer_card2 = deal_player_cards(list_of_dictionaries)
        dealer_card2_key = get_card_key(dealer_card2)
        dealer_card2_value = get_dealt_card_value(dealer_card2,dealer_card2_key)
        list_of_dictionaries.remove(dealer_card2)
        combined_dealer_cards_value = dealer_card1_value + dealer_card2_value
        print(f'You have been dealt two cards these are: {player_card1_key} and {player_card2_key}')
        print(f'Dealer was dealt {dealer_card1} as his first card')
        does_player_want_more_cards = input(f'If you want more cards Kindly enter \'hit\'. If you don\'t want more cards just enter \'stay\': ')
        while does_player_want_more_cards.lower() == 'hit':
            added_card_to_player = deal_player_cards(list_of_dictionaries)
            added_card_to_player_key = get_card_key(added_card_to_player)
            added_card_to_player_value = get_dealt_card_value(added_card_to_player,added_card_to_player_key)
            combined_player_cards_value += added_card_to_player_value
            list_of_dictionaries.remove(added_card_to_player)
            print(f'You have been added card {added_card_to_player_key}. your combined card value is {combined_player_cards_value}. If you still want another card you can enter \'hit\' on the prompt below. If you do not want more cards just enter \'stay\'')
            if does_player_want_more_cards.lower() == 'stay':
             break
        while combined_dealer_cards_value <= 16:
            added_card_to_dealer = deal_player_cards(list_of_dictionaries)
            added_card_to_dealer_key = get_card_key(added_card_to_dealer)
            added_card_to_dealer_value = get_dealt_card_value(added_card_to_dealer,added_card_to_dealer_key)
            combined_dealer_cards_value += added_card_to_dealer_value
            print(f"Dealer was dealt two cards whose values were {dealer_card1_key} and {dealer_card2_key}\n this brings the combined dealer card value to {combined_dealer_cards_value}\n This is less than 16 or 16 as the case may be \n Dealer therefore has picked another card which is {added_card_to_dealer_key}")
            list_of_dictionaries.remove(added_card_to_dealer)
        if 16 < combined_dealer_cards_value <= 21:
            print(f'Dealer has been dealt two cards which are {dealer_card1_key} and {dealer_card2_key} whose combined value is {combined_dealer_cards_value}')
            if combined_dealer_cards_value > 21:
                print(f'Dealer busted. His cards totalled {combined_dealer_cards_value}. This is above 21.You have won this round. 👏')
            if combined_player_cards_value > 21:
                print(f'You\'re busted. Your cards totalled {combined_player_cards_value}. Dealer wins. You have lost this round')
            if combined_player_cards_value > combined_dealer_cards_value:
                print(f'Congrats you beat the dealer. Your cards combined value was {combined_player_cards_value} against dealer\'s {combined_dealer_cards_value}.')
            if combined_dealer_cards_value > combined_player_cards_value:
                print(f'sorry you lost. Dealer Beat you. His cards total led  {combined_dealer_cards_value} against yours whose value was {combined_player_cards_value}')
            if combined_player_cards_value ==combined_dealer_cards_value:
                print('It\'s a tie neither you nor the dealer won.')



















#print(list_of_dictionaries)
#print(list_of_dictionaries[1]['card 3'])
#list_of_dictionaries.pass













