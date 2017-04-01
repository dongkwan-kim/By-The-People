from django.shortcuts import render
from django.http import HttpResponse
import opinion.register as rg
from opinion.models import Mention, Sentence, Comment

import opinion.ownhash as oh
import json

def fc_main(request):
    mall = Mention.objects.all()
    mention = []
    for m in mall:
        sid = m.md_sentence.all()[0].hash_id
        sentence = m.md_sentence.all()[0].text
        speaker = m.speaker.all()[0]
        mention.append({
            "sid": sid,
            "sentence": sentence,
            "speaker": speaker,
        })
    context = {"mention": mention}

    return render(request, "factcheck.html", context)

def save_comment(request):
    uid = request.GET["uid"]
    text = request.GET["comment"]
    assert_kind = request.GET["assert_kind"]

    new_comment = Comment(
        hash_id=oh.sha_t(uid),
        uid=uid,
        crowd_id="assert",
        text=text,
        assert_kind=assert_kind,
    )
    new_comment.save()

    return HttpResponse("good~")

def res_comment(request):
    uid = request.GET["uid"]
    co_list = [
        {
            "uid": c.uid,
            "hash_id": c.hash_id,
            "text": c.text,
            "vote_up": c.vote_up,
            "vote_down": c.vote_down,
            "assert_kind": c.assert_kind,
        }
        for c in Comment.objects.filter(uid=uid)
    ]

    return HttpResponse(json.dumps(co_list))

def v_update(request):
    hash_id = request.GET["hash_id"]
    update_vote = request.GET["update_vote"]
    c = Comment.objects.filter(hash_id=hash_id)[0]
    c.vote_up = update_vote
    c.save()

    return HttpResponse("success~")

def register(request):
    rg.register_ms()
    return HttpResponse("done")
