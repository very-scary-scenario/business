# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define c = Character('Cubicle Guy', color="#c8ffc8")
define ka = Character('Kitchen Goer A', color="#c8ffc8")
define kb = Character('Kitchen Goer B', color="#c8ffc8")
image bg mydesk = "mydesk.jpg"
image bg officedesk = "officedesk.jpg"
image bg cubicle = "cubicle.jpg"
image bg kitchen = "kitchen.jpg"
image cubicleguy neutral = "cubicleguy.png"

init python:
    import youtube

# The game starts here.
label start:
    $ cubicleguy_talked = False
    $ kitchen_happy = False
    $ kitchen_sad = False
    $ desk_searched = False
    scene bg mydesk

    $ title = youtube.Video.from_url(renpy.input('give us a url')).title
    "THIS [title] VIDEO IS TERRIBLE"
    
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
            
        "Sneak into boss' room.":
            jump boss_room
        
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
    
    label cubicle:
        scene bg cubicle
        with fade
        show cubicleguy neutral
    
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
    
    return
