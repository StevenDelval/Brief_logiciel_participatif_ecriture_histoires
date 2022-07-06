def function_vote(last_Paragraph):
    """
    fonction pour voter la supprition de paragraph
    :parametre derniere paragraphe
    :return vote
    """
    print(last_Paragraph)
    a=bool(int(input("votez oui ou non pour supprimer\n0 = Non\n1 = Oui\n")))

    return a



def start_poll(last_Paragraph):
    """
    fonction lancer le vote
    :parametre le derniere paragraph
    :return true or false
    """
    print(last_Paragraph)
    a=bool(int(input("votez oui ou non pour lancer vote\n0 = Non\n1 = Oui\n")))

    return a