import spacy
from nltk.stem.snowball import SnowballStemmer as SBS

def conv_txt(fname):
    nlp = spacy.load("en_core_web_sm")
    normal_sub = ""
    with open(fname,'r') as subs:
        normal_sub = subs.read()
    doc = nlp(normal_sub)
    normal_sub = normal_sub.title()
    new_sub = ""
    print("Input Text: ",normal_sub)
    for token in doc:
        if token.pos_ == "CONJ":
            new_sub += '. '
        elif token.pos_ == "PUNCT" and token.text != '.':
            new_sub += ''
        elif token.pos_ == "SYM" or token.pos_ == "X" or token.pos_ == "DET" or token.pos_ == "CCONJ" or token.tag_ == "IN":
            new_sub += ''
        elif token.text == 'I' or token.text == 'i':
            new_sub += ' me'
        else:
            new_add = token.lemma_
            new_sub += " "+new_add
    doc = nlp(new_sub[1:])
    sbs = SBS(language='english')
    for token in doc:
        if(token.text == 'me'):
            continue
        check_token = nlp(token.lemma_)[0]
        if(check_token.pos_ == "VERB" and check_token.tag_ not in ['VBP','VBZ','VB']):
            new_sub = new_sub.replace(" "+token.text+" ", " "+sbs.stem(check_token.text)+" ")
        elif(check_token.text != token.text):
            new_sub = new_sub.replace(token.text,check_token.text)

    nlp = spacy.load("en_core_web_sm")
    txt = new_sub
    doc = nlp(txt)
    text = []
    done = {}
    for i in txt:
        text.append("")
    for token in doc:
        ancestors = [t.pos_ for t in token.ancestors]
        children = [t for t in token.children]
#     temp= []
        try:
            if(done[token.i]):
                pass
        except:
            done[token.i] = token.i
        if(token.pos_ == "VERB"):
    #         temp += token.text
            text.insert(done[token.i],token.text)
            if(token.dep_ == "root"):
                for child in children:
                    if child.pos_ == "VERB":
                        text.insert(done[token.i]+1,child.text)
                        done[child.i] = done[token.i]+1
    #                     del 
            for child in children:                    
                if child.pos_ == "AUX" and child.dep_ == "aux":
                    text.insert(done[token.i]-1,child.text)
    #                 temp = child.text + temp
                    done[child.i] = done[token.i]-1
                if child.pos_ == "ADV" and child.dep_ == "advmod":
                    text.insert(done[token.i]+1,child.text)
    #                 temp += child.text 
                    done[child.i] = done[token.i]+1
            if(token.dep_ == "root"):
                for child in children:
                    if child.pos_ == "NOUN" and child.dep_[-3:] == "obj":
                        text.insert(done[token.i]-1,child.text)
                        done[child.i] = done[token.i]-1
        if(token.pos_ == "NOUN"):
            text.insert(done[token.i],token.text)
            for child in children:
                if((child.pos_,child.dep_) not in [("ADJ","amod"),("NOUN","nummod")]):
                    text.insert(done[token.i]+1,child.text)
    #                 temp += child.text 
                    done[child.i] = done[token.i]+1
                if(child.pos_ == "ADJ" and child.dep_ == "amod"):
                    text.insert(done[token.i]+1,child.text)
    #                 temp += child.text 
                    done[child.i] = done[token.i]+1
                if(child.pos_ == "NUM" and child.dep_ == "nummod"):
                    text.insert(done[token.i]+1,child.text)
    #                 temp += child.text 
                    done[child.i] = done[token.i]+1
        if(token.pos_ not in ["VERB","NOUN"] and token.text not in text and "NOUN" not in ancestors and "VERB" not in ancestors):
            text.insert(done[token.i],token.text)

        if(token.dep_[-4:] == "subj"):
            text.insert(done[token.i],token.text)

    #     text[done[token.i]] = temp

    text = list(set(text))
    sent = " ".join(text)
    sent = sent.lower()
    print("Output Text",sent)
    return sent

if __name__ == "__main__":
    # conv_txt("I really used to love eating three tasty apples")
    # conv_txt("I go to school")
    pred=conv_txt("input_01.txt")
    with open('input_01.txt', 'w') as file:
            file.write(pred)
