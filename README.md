# By-The-People
- Special mention of Seoul Editors Lab 31 March 2017 - 01 April 2017
- Real-time Debate Fact Checking System By Crowd
- This is only prototype

## Description
The media is full of bias and faked news. The truth is hidden, yet reachable.

For this presidential election, we suggest a real time fact checking solution.

Our solution maximizes the power of collective intelligence to find facts in the candidates’ speeches. Whenever the candidates are on debate, our website will provide the real time live video and structured subtitles. The users can drag the subtitles to question a statement, or upload evidences to prove/disprove the statement. The critical evidences will be shown on the top, the user who finds it will be awarded with special badges like the ‘watchman’. Aside from the badges, the users will be classified by tiers(bronze, silver, gold...) on their precision. The user has to find true or false statements from candidates’ speech, and when the opinion meets adequate evidences thus acknowledged by the administrator to be solidly true or false, the user gains EXP. To add more gamification to the solution, we offer a scoreboard that reflects the percentage of facts and fakes from each candidate’s speech. The scoreboard from each debate session will pile up in our database, which will work as an index to find out who is a frequent liar. The competitive system is designed to draw more users’ participation, ultimately leading to better decisions.

This election, the truth will win By the People.

![demo1](https://raw.githubusercontent.com/todoaskit/realtime-fact-checker/master/img/demo1.png)

![demo2](https://raw.githubusercontent.com/todoaskit/realtime-fact-checker/master/img/demo2.png)

![demo3](https://raw.githubusercontent.com/todoaskit/realtime-fact-checker/master/img/demo3.png)

![demo4](https://raw.githubusercontent.com/todoaskit/realtime-fact-checker/master/img/demo4.png)


## Technologies used for this project
Our system needs two significant module: ‘Speech to Structured Text’, ‘Fact Check By Crowd’. Since we were running out of time, we implemented only latter one, but we will explain how to implement the former one.
- [Fact Check By Crowd] Because it is based on web, we use HTML5, CSS3, Javascript to build the front-end. Here is the list of front-end library that we used: Jquery, meterializecss, typedjs, medium-editor.js, YouTube iframe api. Back-end is implemented with Django.
- [Speech to Structured Text] To make dialogue with text and speaker from YouTube video, we need Google Cloud streaming speech api(audio to text), Microsoft speaker identification api(speaker identification by audio), Google Cloud vision api(speaker identification by captured image).

## Applicants
- Dongkwan Kim(Developer), Seyun Parklee(Designer), Taehyeon Kim(Planner)

## Links
- [GEN Community Project](http://community.globaleditorsnetwork.org/content/bythepeople-0)
- [Presentation](https://docs.google.com/viewerng/viewer?url=http://community.globaleditorsnetwork.org/sites/default/files/gen_hackathon.pdf)
