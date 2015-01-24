﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define c = Character('Cubicle Guy', color="#c8ffc8")
define b = Character('Receptionist', color="#c8ffc8")
define g = Character('Goggles', color="#c8ffc8")
define ka = Character('Kitchen Goer A', color="#c8ffc8")
define kb = Character('Kitchen Goer B', color="#c8ffc8")
image bg mydesk = "mydesk.jpg"
image bg officedesk = "officedesk.jpg"
image bg cubicle = "cubicle.jpg"
image bg kitchen = "kitchen.jpg"
image bg bossroom = "bossroom.jpg"
image bg reception = "reception.jpg"
image cubicleguy neutral = "cubicleguy.png"
image test = "test.jpg"
image nick = "nick.png"
image beyonce = "beyonce.png"


# The game starts here.
init python:
    import youtube

# The game starts here.
label start:
    $ cubicleguy_talked = False
    $ kitchen_happy = False
    $ kitchen_sad = False
    $ desk_searched = False
    $ bossroom_searched = False
    $ reception_visited = False
    scene bg mydesk

    menu:
        "There is a youtube video URL in my clipboard":
            jump video

label video:
    $ video = youtube.paste()
    "THIS [video.title] VIDEO IS THE WORST [video.duration] I HAVE EVER SPENT AND [video.dislikes] PEOPLE AGREE WITH ME"
    "THIS [video.likes] PEOPLE DISAGREE AND ARE IDIOTS AND [video.views] PEOPLE HAVE SHARED THIS TERRIBLE EXPERIENCE"

#How about a pop-up of the phone and some vibration noises?
    
    "Ungh..."
    "..."
    
#How about another pop-up of the phone, some vibration noises and some bleepy bloops?

    "You remove the phone from your pocket, and through bleary eyes, try to make out the information on the screen."
    
#More bloopy bleeps

    "Looks like the boss has scheduled an urgent meeting. Nothing like a bit of notice when it comes to these things."
    "..."
    m "What... what the hell?"
    "You see, there's not much that tops an unexpected urgent meeting that takes place as soon as five minutes time, but this..."
    "This is right up there."
    m "Who... am I?"
    "Fortunately for you, there is at least some time to collect your thoughts and figure out who you are. Amnesia doesn't have to be the end of your career, you know."
    "."
    ".."
    "..."
    "Well don't just stand there you fool, go and figure out who you are!"
    
    label pre_meeting_options:
        scene bg officedesk
        with fade
    
    menu:
        "Search through your things.":
            jump search
        
        "Talk to the guy in the cubicle over there.":
            jump cubicle
            
        "Head to the kitchen and try to overhear people.":
            jump kitchen
            
        "Sneak into your boss' room.":
            jump bossroom
        
        "Ask the cheerful-looking person on the reception desk.":
            jump reception
            
    label search:
        scene bg mydesk
        with fade
    
    if desk_searched:
        m "I've already searched the important stuff. I should go elsewhere."
        m "..."
        m "I'm already talking to myself. God help me."
        jump pre_meeting_options
    
    "A messy desk for a messy person."
    "I mean, you might not remember anything, but I'm pretty sure this is your desk."
    "I can tell by just looking at you."
    "No offense."
    jump searchmenu
    
    label searchmenu:
        scene bg mydesk
        with fade
    
    menu:
        "Mess about aimlessly on the computer.":
            jump computer
        
        "Look in the drawers.":
            jump drawers
        
        "Check the stack of sheets with all the numbers on them.":
            jump numbersheets
        
    label computer:
    "You stare at the computer screen, eyes drawn to the password field."
    "If this was a movie, you could probably guess what the password is."
    "Unfortunately you're not nearly as important, so there will be no miracles here."
    "Sorry about that."
    jump searchmenu
    
    label drawers:
    "You face a tough decision."
    "For the sake of saving face, you commit yourself to going through with it."
    "{i}It's so gross though oh my goooood.{/i}"
    "Ah whatever, it's your hand."
    "And fingers."
    "Hang on a second I'm going to vomit."
    "."
    ".."
    "..."
    "My apologies."
    "That wasn't very professional of me."
    "You gingerly extend your hand out in front of you and rummage around the drawers."
    "These have definitely been worn before."
    jump searchmenu
       
    label numbersheets:
    $ desk_searched = True
    "There's a stack of sheets on your desk."
    "Perhaps it's because you were busy with something."
    "Perhaps it's because you were trying to {i}look{/i} busy with something."
    "Whatever the case, it may prove useful in figuring out just what you're meant to be doing here."
    "The numbers are clearly statistics. Lots of talk about 'hits'."
    "That's a pretty awful website you're running if that's what it is, because these figures are diabolical."
    "You're not going to be in this company longer when your hits are typically fourty or less."
    "Looking at another sheet, the hits seem to skyrocket."
    "Millions? Hundreds of millions? This seems to be something else but I can't make heads or tails of it."
    "But whatever, that's your problem not mine. I believe in you."
    "But seriously if you're running a website I think you're soon to be replaced.."
    jump pre_meeting_options
    
    label cubicle:
        scene bg cubicle
        with fade
        show nick at left
    
    if cubicleguy_talked:
        c "Dude, you should hurry along to that meeting. You don't want to piss off the boss."
        jump pre_meeting_options
    
    c "Oh hey there, Steve. How's it hanging?"
    "See? It isn't that difficult. You should remember that though. Just in case."
    
    menu:
        "It's hanging just fine, thanks. And yours?":
            jump banana
        
        "I'm alright, thanks. Yourself?":
            jump banana2
            
    label banana:
    
    c "Swinging low, man. Swinging low."
    jump banana3
        
    label banana2:
    
    c "Not bad at all, thanks for asking."
    jump banana3
        
    label banana3:
    
    c "So was there something you were after?"
    
    menu:
        "I've lost all of my memories and I've got an important meeting shortly. Give a bro a hand.":
            jump banana4
        
        "Do you know anything about the meeting that's in a few minutes?":
            jump banana5
            
    label banana4:
    
    $ cubicleguy_talked = True
    c "No offense bro, but you're not the kind of guy to crack jokes and it shows. Maybe don't do that in your meeting."
    m "S-sorry. I'll leave now."
    jump pre_meeting_options
            
    label banana5:
    
    $ cubicleguy_talked = True
    c "Ah, sorry bud, I'm not in that meeting. Too high level and important for a character like me."
    c "I think I heard some people talking about it over in the kitchen, though."
    m "Thanks."
    jump pre_meeting_options
    
    label kitchen:
        scene bg kitchen
        with fade
        show cubicleguy neutral at left
    
    if kitchen_happy:
        ka "You should prepare for the meeting."
        kb "Yeah, prepare for the meeting."
        ka "Stop it."
        jump pre_meeting_options
        
    if kitchen_sad:
        ka "We don't talk to eavesdroppers."
        kb "Except for Cheryl from accounting."
        ka "Yeah, except for Cheryl."
        jump pre_meeting_options
        
    ka "...wait, he did? With what?"
    kb "A pneumatic drill and a second hand trombone."
    ka "That's disgusting! He has a family to look out for!"
    kb "Yeah, well, he should have thought about that beforehand. Now he'll never get the chance."
    ka "Honestly, some people. They'll never let him keep pets again."
    kb "Music to my ears. Speaking of which, are you going to be in the meeting?"
    ka "No, not today. It's far too important for someone like me. Like, job-on-the-line levels of important."
    
    label kitchendialogue:
        scene bg kitchen
        with fade
        show cubicleguy neutral at left
    
    menu:
        "Good morning.":
            jump kitchen2
            
        "Hey, uh, fancy meeting you here.":
            jump kitchen8
        
        "So what's this meeting about, anyway?":
            jump kitchen7
        
        "I am 99%% certain that I'm a cliché amnesia character, help me.":
            jump kitchen9
        
    label kitchen2:
    
    ka "Good morning?"
    kb "2pm is a bit late for a good morning."
    ka "Actually, it's morning somewhere in the world."
    kb "Oh, how informative and original. Thanks for that."
    m "...good afternoon."
    ka "Good afternoon."
    kb "Good afternoon."
    
    menu:
        "Are either of you going to be in the meeting?":
            jump kitchen3
        
        "Why are you not invited to the meeting?":
            jump kitchen7
            
    label kitchen3:
        
    ka "No, not us."
    kb "We're not high enough up the food chain."
    ka "It's for the best."
    kb "Yes, for the best."
    
    menu:
        "It's for the best?":
            jump kitchen4
            
    label kitchen4:
    
    ka "Of course it's for the best."
    kb "It's definitely for the best."
    ka "It's for the best."
    
    menu:
        "Why is it for the best?":
            jump kitchen5
    
    label kitchen5:
        
    ka "Because the boss is going to be in the meeting."
    kb "And the boss knows best."
    ka "Always knows best."
    kb "So it's for the best."
    m "..."
    ka "..."
    kb "..."
    ka "It's for th-"
    
    menu:
        "It's for the best, yes, I know that. But seriously, this repetitiveness is really grinding my gears and it's an obvious attempt to waste down the timer in an office sparsely packed with people to talk to. Hell, even I'm talking nonsense in an attempt to fill in the dead air here. But please, I'm pulling a blank and would love it if you could perhaps tell me why this meeting is so important. It's been a rough day.":
            jump kitchen6
    
    label kitchen6:
    $ kitchen_happy = True
    
    ka "Oh, well why didn't you say?"
    kb "Yeah, why didn't you say?"
    ka "Alright come on, enough of that."
    kb "Fair dos."
    ka "The meeting is important because they are compiling the list today."
    kb "It's that time of the year again. It always goes so quickly."
    ka "I hope you're prepared, though. They're not going to be able to collate everything into an album without you being on top form."
    m "Thank you. Sorry for the outburst."
    ka "Don't worry."
    kb "We're used to it."
    jump pre_meeting_options
    
    label kitchen7:
    $ kitchen_sad = True
    
    ka "You were eavesdropping on us?"
    kb "What do you think this is, a game?"
    ka "Get out of our sight."
    jump pre_meeting_options
    
    label kitchen8:
    
    ka "Uhh..."
    kb "Do we know you?"
    ka "I don't know you."
    kb "Neither do I."
    m "I don't know you."
    ka "Weird."
    jump kitchendialogue
    
    label kitchen9:
    
    ka "You what mate?"
    kb "It's at least imaginative."
    ka "There is that."
    kb "Makes a change."
    m "I'm sorry."
    ka "It's okay."
    jump kitchendialogue
    
    label bossroom:
        scene bg bossroom
        with fade
        show cubicleguy neutral at right
    
    if bossroom_searched:
        "You don't have the time to hide in here and spin around in the chair."
        "But now that I've said it that does sound kind of fun."
        "Now I'm disappointed."
        jump pre_meeting_options
        
    "Well, this is it. We've become desperate enough to put the job on the line. Whatever it is."
    "Fortunately for you, the boss insists on arriving to meetings early. They've already booted out the people who should currently be in the meeting room."
    "Perks of being the boss, I suppose."
    "But it gives you free reign of the boss' room. You'd hope that there would be something here that would tell you what's up."
    "{i}You'd hope.{/i}"
    
    label inbossroom:
        scene bg bossroom
        with fade
        show cubicleguy neutral at left
    
    menu:
        "Search under the desk.":
            jump boss1
            
        "Look at the paperwork on the desk.":
            jump boss2
        
        "Look inside the book marked 'Bossing for Dummies'.":
            jump boss3
        
    label boss1:
    
    "It's an interesting approach to take, that much is for sure."
    "I mean, we have paperwork all over the desk and various doodads around the room."
    "But you opt for looking under the desk."
    "I'm starting to wonder exactly how seriously you're taking this."
    "I hope you're not panicking over the time limit."
    "This is totally your fault. Like seriously, what were you expecting?"
    "Oh hey actually, hold up. We've got something here."
    "Never mind. It's just dust."
    jump inbossroom
    
    label boss2:
    $ bossroom_searched = True
    "Here it is. The true nature of the boss, finally revealed!"
    "This paperwork, while certainly interesting, isn't going to be much help with you."
    "That is unless you find doodles of moustached individuals helpful."
    "Underneath the top layer of doodles is a list of popular singers. I guess they're pop musicians, anyway. I've heard of them so they must be pretty famous."
    "Beyoncé? Sure, why not. Not so sure about the obsession with Kanye though."
    "He was great in that one Twitter simulation, though."
    "Nothing important, apparently. Just what appears to be notes on the boss' latest mix tape."
    "Glad to see the boss can get the hard work done when it really matters."
    jump pre_meeting_options
    
    label boss3:
    
    "They sure do make these books for the dumbest subjects, huh."
    "Fingers crossed this isn't how the boss got their job. Realistically? Roll a dice, I guess."
    "Hold the phone, this book is annotated. There might be something interesting here."
    "Hmm, looks like a few passages are highlighted. 'How to negotiate with business partners' and 'Budgeting 101' are quite vigorously circled."
    "Let's just be happy knowing that they are at least trying to better themselves, one way or another."
    jump inbossroom
    
    label reception:
        scene bg reception
        with fade
    
    if reception_visited:
        "You don't have the time to hide in here and spin around in the chair."
        "But now that I've said it that does sound kind of fun."
        "Now I'm disappointed."
        jump pre_meeting_options
        
    "Nothing like a friendly receptionist to lighten the mood."
    "I mean, I can't really see what they'll be able to do about your meeting predicament, but I guess it's worth a shot?"
    "If we hang around long enough we might get some free coffee."
    
    label atreception:
        scene bg reception
        with fade
        show beyonce
    
    menu:
        "Ask about the meeting.":
            jump reception1
            
        "Ask about the weather.":
            jump reception2
            
        "Ask about how common it is for people to lose memories in the office.":
            jump reception3
            
    label reception1:
    
    b "The meeting? I'm sorry, I'm afraid you're going to have to be more specific."
    b "There's just far too much going on here that it's difficult to keep track of."
    b "Well, difficult is perhaps a stretch. It's just no fun."
    jump atreception
    
    label reception2: 
    b "The weather? Hang on, let me ask my Personal Assistant™ about that."
    b "Okay Goggles, tell me what the weather is like outside."
    g "ｄｉａｌｌｉｎｇ　ｇｒｅｇｏｒｙ"
    b "It's raining."
    jump atreception
    
    label reception3: 
    b "Well, I'm not sure about"
    b "Okay Goggles, tell me what the weather is like outside."
    b "ｄｉａｌｌｉｎｇ　ｇｒｅｇｏｒｙ"
    b "It's raining."
    jump pre_meeting_options
                                                        
    return
