# -*- coding: utf-8 -*-
from opinion.models import Mention, Sentence, Speaker
import datetime
import opinion.ownhash as oh

def register_ms():

    Speaker.objects.all().delete()
    Mention.objects.all().delete()
    Sentence.objects.all().delete()

    for line in open("speaker.txt"):
        [name, profile] = line.split(",")
        s = Speaker(name=name, profile=profile)
        s.save()

    for line in open("dialogue.txt"):
        if "=" in line:
            [cand, text] = [x.strip() for x in line.split("=")]
            speaker = Speaker.objects.get(name=cand)
            new_mention = Mention(
                hash_id=oh.sha_t(cand),
                date_time=datetime.datetime.now(),
            )
            new_mention.save()
            new_mention.speaker.add(speaker)

            new_sentence = Sentence(
                hash_id=oh.sha_t(text.strip()),
                text=text.strip(),
            )
            new_sentence.save()
            new_mention.md_sentence.add(new_sentence)

if __name__ == "__main__":
    register()
