# Making-of-Journal 
## Twitter bot for practising 
### and if succeed for botting henry hub gas price and so on

### 27.4.2022 
- Upgraded twitter account one level for api in hand

### Automatic follower
- Found RealPython.com's Tweepy code and practising with it. Some time have passed from article but found solutions for old code. 
- Added checking that if there is no followers, pauses for one day
- Found [*pause*](https://pypi.org/project/pause/) to use. Should be better than sleep. Could not find it from conda, so piped it.  

### 12.5.2022
- Found new code to study and to get things forward for favandretweet - just could not refactor RP's code. Now working: followfolloers and favretweet (#henryhub). Code is not in Docker yet, but no hurry here. Have to learn some basics first ;)
- So this is kind of forked code and so on

### 14.5.2022
- added to Dockerfikle and dockerised. Favretweet and follow should be working
- Now retewwting #henryhub -posts
- No actual new information still, but because it's important feature to learn, we will rock you. 

### 16.5.2022
- Found solution for multiple search terms
- Modified codes outputs
- Thinking about tweeking things. I have ingreased bots acting times from 60 sec to 480 sec. Is it good or bad? Best week is maeby if I put just filter that it only process current days tweets?
- Yes, can not say if Follower part works in docker. Should I separate scripts or use shell script? I do not like to separate.  

### 19.5 2022
- Now follow followers works also (via start.sh). Next thinking what is relevant or essential info and how to show that. Thinking that some information can be in profile? Maeby in pinned tweet?  

### 28.5.2022
- Hmm. Ok, scrpit -version for "dualbooting" just dont work, so have to fix that.

### TODOS
P = Partial, X= Done
-[P] Check time so not retweeting old news <- actually it is allready limited to 7 days, but it can be expanded to check that it favs tweets only written in same day. No need now.  
- [X] Use env for secrets
- [X] Put to run inside docker (maeby after impelementing more parts)
- [P] Actual action: henry hub -information
- [P] More energy things
- [] Maeby more elegant solution for todos is using github's Issues.
- [x] Fix Follow2Follow to work in Docker.
- [] Information from outer data source to bot. Thats kind of crusial.   

[https://twitter.com/MyGasAndEnergy1](https://twitter.com/MyGasAndEnergy1)

## 25.4.2023
- Twitter have been made so much changes for their accounts so this approah I think do not work anymore. So Archiving.
