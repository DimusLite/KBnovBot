import re
inputMsg = """Неактуальная версия конф. 1С!
№7360 (ул. Восстания, 3/1, Старая Русса)(9.448 от 04.07.19)
№8247 (ул. Попова, 4, кор. 1, Великий Новгород)(9.448 от 04.07.19)
№10196 (ул. Псковская, 13, Великий Новгород)(9.448 от 04.07.19)"""

/*======================================================*/    
#inputMsg = message.text
OLD_VER_LIST_KEY = "Неактуальная версия конф. 1С!"

def MakeNumBold(msg):
    numsList = re.findall(r'№\d+', msg)
    for num in numsList:
        msg = re.sub(num, '*' + num + '*', msg)
    return msg

if OLD_VER_LIST_KEY in inputMsg:
    replyText = MakeNumBold(inputMsg)

/*======================================================*/    
    
    print(replyText)
