def isValid(text):
    text = text.lower()
    if 'was' in text and 'antwort' in text:
        return True
    if 'warum' in text:
        return True
    else:
        return False

def handle(text, tiane, profile):
    if 'antwort' in text.lower():
        tiane.say('42')
    elif 'warum' in text.lower():
        tiane.say('Weil Baum')
