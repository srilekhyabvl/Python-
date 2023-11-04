import re
import long_response as long
import speech_recognition as s


def msg_probability(user_msg,recognised_words,single_response=False,required_words=[]):
    msg_certainty=0
    has_req_words=True 

    # Count how many words are present in each pre-defined msg
    for word in user_msg:
        if word in recognised_words:
            msg_certainty+=1
    
    # Calculate the percent of recognised words in a user_msg
    percentage=float(msg_certainty) / float(len(recognised_words))

    # Check the required words in the string
    for word in required_words:
        if word not in user_msg:
            has_req_words=False
            break
    
    if has_req_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_msg(msg):
    high_prob={}

    # adding items to dictionary 
    def response(bot_res,list_words,single_response=False,required_words=[]):
        nonlocal high_prob
        high_prob[bot_res]=msg_probability(msg,list_words,single_response,required_words)
    
    # Bot's response
    response('Hello',['hello','hi','hey','heyo'],single_response=True)
    response('I am doing fine, and you?',['how','are','you','doing'],required_words=['how'])
    response('Thank You',['your','code','is','good'],required_words=['your','code','good'])
    response('Sorry, I do not have feelings',['i','like','you'],required_words=['like','you'])
    response(long.r_eat,['what','you','eat'],required_words=['eat','you'])
    
    
    # checking the highest probability response
    best_match=max(high_prob,key=high_prob.get)
    # print(high_prob)

    return long.unknown() if high_prob[best_match]<1 else best_match



def get_response(user_input):
    split_msg=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_msg(split_msg)
    return response

# Taking input in the form of audio and convert it into string
while True:
    # print("Bot: "+get_response(input("You: ")))
    # object 
    sr=s.Recognizer()
    text=" "
    print("Bot is listening: ")
    with s.Microphone(device_index=1) as m:
        audio=sr.listen(m)
        try:
            text=sr.recognize_google(audio)
        except:
            print("Not working")
        print("You: "+ text)
        print("Bot: "+ get_response(text))
    
    