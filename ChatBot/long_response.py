import random

r_eat="I am a bot so I do not eat anything!"
def unknown():
    response=['Could you please re-phrase that?',".....",'Sounds right','What does that mean?','Sorry, I did not understand that!'][random.randrange(5)]
    return response