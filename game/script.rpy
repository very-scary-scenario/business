# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define c = Character('Cubicle Guy', color="#c8ffc8")
define r = Character('Receptionist', color="#c8ffc8")
define g = Character('Goggles', color="#c8ffc8")
define s = Character('Sam', color="#c8ffc8")
define ka = Character('Kitchen Goer A', color="#c8ffc8")
define kb = Character('Kitchen Goer B', color="#c8ffc8")
define b = Character('Boss', color="#c8ffc8")
define d = Character('David', color="#c8ffc8")
define h = Character('Harold', color="#c8ffc8")
define f = Character('Fiona', color="#c8ffc8")
define mi = Character('Mia', color="#c8ffc8")
define l = Character('Leslie', color="#c8ffc8")
define ge = Character('George', color="#c8ffc8")
define sub = Character('Subordinate', color="#c8ffc8")
define tut = Character('Hint', color="#c8ffc8")
define ddd = Character('3D Boss', color="#c8ffc8")
image bg mydesk = "mydesk.jpg"
image bg officedesk = "officedesk.jpg"
image bg cubicle = "cubicle.jpg"
image bg kitchen = "kitchen.jpg"
image bg bossroom = "bossroom.jpg"
image bg reception = "reception.jpg"
image bg premeeting = "premeeting.jpg"
image bg meeting = "meeting.jpg"
image bg george = "trenchfoot.jpg"
image bg war = "dream.png"
image bg toilet = "toilet.jpg"
image bg certificate = im.Scale("certificate.gif", 800, 600)
image beyonce = "beyonce.png"
image barbara = "barbara.png"
image bdb = "bdb.png"
image harold = "harold.png"
image leslie = "leslie.png"
image mia = "mia.png"
image boss = "boss.png"
image dave = "dave.png"
image fiona = "fiona.png"
image phone = "phone.png"
image david = "david.png"
image dddboss = "3dboss.png"

init:
    $ meeting_timer_set = None
    python:
        style.default.font = FontGroup().add('Lato-Regular.ttf', 0x0020, 0x2fff).add("batang.ttf", 0x0000, 0xffff)
        import youtube
        playlist = youtube.Playlist()
        timers = []
        seconds_in_a_minute = 60.0

        def make_notifier(count):
            return lambda: renpy.notify(count)

        def start_meeting_timer():
            ui.layer("screens")
            renpy.notify('five minutes remaining')

            for count, name in [
                (1, 'four minutes remaining'),
                (2, 'three minutes remaining'),
                (3, 'two minutes remaining'),
                (4, 'one minute remaining'),
            ]:
                timers.append(ui.timer(count * seconds_in_a_minute, action=make_notifier(name)))

            timers.append(ui.timer(5 * seconds_in_a_minute, action=ui.jumps("timesup")))
            ui.close()

        def kill_meeting_timer():
            ui.layer("screens")
            for timer in timers:
                ui.remove(timer)
            ui.close()
            
        hands_washed_times = 0
        

label start:
    scene bg war

    sub "Commander! Sir! Wake Up!"
    m "..."
    sub "Sir!"
    m "Ungh..."
    m "Wait, what's with all the tanks?"
    sub "We've been caught in a meeting engagement with a German mechanised company, sir!"
    m "What!? Again?"
    sub "We've come into contact with the lead units of the enemy formation on the crossroads to Kelberg!"
    m "{i}What's going on here?{/i}"
    sub "Enemy forces are reported to consist of three infantry squads, a single Sd. Kfz. 234 IFV, and a single Panzer IV."
    sub "The Germans have managed to take advantage of the situation by seizing the nearby hill and firing down upon our forces."
    sub "Our lead platoon is taking a beating. Lt. Hawkings has taken heavy casualties and is in desperate need of reinforcements!"
    sub "If we don't turn this around, the cohesion of the company and the whole damn battalion's advance is in jeopardy."
    sub "Thank God you convinced Lt. Col. Jefferson to give us that extra attachment of an armoured platoon."
    sub "Their firepower and manoeuvrability will allow us to regain the initiative and force the Germans to disengage."
    tut "{color=#3366CC}Tutorial Start.{/color}"
    tut "{color=#3366CC}Click on one of the tanks to select it.{/color}"
    
    hide text with dissolve
    $ renpy.pause()
    scene black with dissolve

    jump awaken
    
label awaken:
    $ cubicleguy_talked = False
    $ kitchen_happy = False
    $ kitchen_sad = False
    $ desk_searched = False
    $ bossroom_searched = False
    $ bossroom_poetry = False
    $ reception_visited = False
    scene bg mydesk
    play music "shitty vn music.ogg"

    #How about a pop-up of the phone and some vibration noises?

    show phone at right

    $ start_meeting_timer()

    "Ungh..."

    hide phone

    "..."

    show phone at right

    #How about another pop-up of the phone, some vibration noises and some bleepy bloops?

    "You remove the phone from your pocket, and through bleary eyes, try to make out the information on the screen."

    #More bloopy bleeps

    "Looks like the boss has scheduled an urgent meeting. Nothing like a bit of notice when it comes to these things."
    "..."

    hide phone

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
            
        "Go for a poo.":
            jump toilet

        "Waltz into the meeting. You've got this.":
            jump meeting

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
    "Or perhaps it's because you were trying to {i}look{/i} busy with something."
    "Whatever the case, it may prove useful in figuring out just what you're meant to be doing here."
    "The numbers are clearly statistics. Lots of talk about 'hits'."
    "That's a pretty awful website you're running if that's what it is, because these figures are diabolical."
    "You're not going to be in this company longer when your hits are typically forty or less."
    "Looking at another sheet, the hits seem to skyrocket."
    "Millions? Hundreds of millions? This seems to be something else but I can't make heads or tails of it."
    "But whatever, that's your problem not mine. I believe in you."
    "But seriously if you're running a website I think you're soon to be replaced.."
    jump pre_meeting_options

label cubicle:
    scene bg cubicle
    with fade
    show bdb

    if cubicleguy_talked:
        c "Dude, you should hurry along to that meeting. You don't want to piss off the boss."
        jump pre_meeting_options
    "These office cubicles are the worst."
    "It's like seeing battery hens, only with humans and in an office."
    "The smell is about the same, though."
    c "Oh, hey there."
    "Oh no, he's locked eyes with you. You won't be able to escape until after the battle."
    c "How's it hanging?"
    
    menu:
        "It's hanging just fine, thanks. And yours?":
            jump banana
            
        "I'm hanging just fine, thanks. And you?":
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
        "I've lost all of my memories and I've got an important meeting shortly. I would appreciate some assistance.":
            jump banana4

        "Do you know anything about the meeting that's in a few minutes?":
            jump banana5

label banana4:
    $ cubicleguy_talked = True
    c "No offense, but cracking awful jokes doesn't really suit you. Don't quit the day job."
    m "S-sorry. I'll leave now."
    jump pre_meeting_options

label banana5:
    $ cubicleguy_talked = True
    c "Ah, sorry, I'm not in that meeting."
    c "I'm far too busy shouting down phones at people demanding our 'final lists'."
    c "Damn prank callers."
    c "I think I heard some people talking about it over in the kitchen, though."
    m "Thanks."
    jump pre_meeting_options

label kitchen:
    scene bg kitchen
    with fade
    show barbara at left
    show dave at right

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
    show barbara at left
    show dave at right

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

    if bossroom_searched:
        "You don't have the time to hide in here and spin around in the chair."
        "But now that I've said it that does sound kind of fun."
        "Now I'm disappointed."
        jump pre_meeting_options

    "Well, this is it. You've become desperate enough to put the job on the line. Whatever it is."
    "Fortunately for you, the boss doesn't appear to be here. They've already booted out the people who should currently be in the meeting room."
    "Perks of being the boss, I suppose."
    "But it gives you free reign of the boss' room. You'd hope that there would be something here that would tell you what's up."
    "{i}You'd hope.{/i}"

label inbossroom:
    scene bg bossroom
    with fade
    $ bossroom_entered = True

    menu:
        "Search under the desk.":
            jump boss1

        "Look at the paperwork on the desk.":
            jump boss2

        "Look inside the book marked 'Bossing for Dummies'.":
            jump boss3
            
        "Flip through the boss' notepad.":
            jump boss4

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
    
label boss4:
    $ bossroom_poetry = True
    "We just hit a goldmine. It's a notebook labelled 'Haikus by Boss'."
    "Flick to the end, I want to see what the latest entry is."
    "Bear at the river \nStomach growling with hunger \nNext applicant, please."
    "...the boss continues to impress."
    jump inbossroom

label reception:
    scene bg reception
    with fade

    if reception_visited:
        r "I appreciate you coming to visit me again, but I'm not going to make you a coffee."
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
    r "The meeting? I'm sorry, I'm afraid you're going to have to be more specific."
    r "There's just far too much going on here that it's difficult to keep track of."
    r "Well, difficult is perhaps a stretch. It's just no fun."
    jump atreception

label reception2:
    r "The weather? Hang on, let me ask my Personal Assistant™ about that."
    r "Okay Goggles, tell me what the weather is like outside."
    g "ｄｉａｌｌｉｎｇ　ｇｒｅｇｏｒｙ"
    r "It's raining."
    jump atreception

label reception3:
    $ reception_visited = True
    r "Well, I'm not sure about people losing their memories, but people sure seem to be forgetful about things. The boss specifically."
    r "I've had this prototype disc for the longest time and no one seems to be that bothered about it."
    r "Between you and me, I'm also not in a rush to hand it back. It's got some great tunes on it."
    r "I'm rather partial to Mrs Knowles."
    jump pre_meeting_options
    
label toilet:
    scene bg toilet
    with fade

    "Welcome to the smelliest, coldest and possibly cleanest area of the office; the toilets."
    "I like to call it the Dank Stank."
    "If you've genuinely come to look for clues, you might leave disappointed."
    "Actually, you're right to keep an open mind. You might be a cleaner and you could find your work permit inside a cistern."
    "You could just hide here. For five minutes, anyway."

label attoilet:
    scene bg toilet
    with fade

    menu:
        "Flush all of your hopes and dreams down the toilet.":
            jump toilet1

        "Wash your hands.":
            jump toilet2

        "Have a bit of a sit down.":
            jump toilet3

label toilet1:
    "*FLUSH*"
    "Well, there they go..."
    jump attoilet

label toilet2:
    $ hands_washed_times += 1
    "*SLOSH*"
    if hands_washed_times == 1:
        "You have washed your hands once."
    else:
        "You have washed your hands [hands_washed_times] times."
    if hands_washed_times >= 5:
        "You've used used up the last of the soap, but you continue to wash your hands anyway."
    jump attoilet

label toilet3:
    "As much as you might like to, you can't just spend five minutes in the toilets."
    "People might need them."
    "For poopin'."
    "There are a couple of magazines here, though."
    "Man, these are gross. This one is even stained."
    
label toilet3b:
    menu:
        "Pick-up Smash Hits.":
            "Looks like someone has taken a pen to this magazine."
            "Some musicians seem to be circled. Others have had scars and eyepatches drawn on them."
            "Productivity at its finest."
            jump pre_meeting_options

        "Pick-up Adventure Fishing.":
            "ARE YOU LOOKING FOR FISHING?"
            "ARE YOU ALSO LOOKING FOR AN ADVENTURE?"
            "HOLY SHIT COULD YOU ALSO BE LOOKING FOR ADVENTURE FISHING?"
            "Because, like, this magazine is way too damp to even open so I guess you're out of luck."
            jump toilet3b
            
        "Pick-up TIME Magazine.":
            "Is this a legitimate copy of Time?"
            "It's got a picture of a strange looking guy in a monkey suit on the front."
            "I bet he won't be able to get a job any time soon."
            jump toilet3b

label timesup:
    show leslie
    s "Hey, you're going to be late for the meeting!"
    s "Get moving or it's your head on the block!"
    hide leslie
    jump meeting

label meeting:
    $ kill_meeting_timer()
    scene bg premeeting
    with fade

    "I sure hope you're ready for this. I personally have no idea what you're getting into."
    "What really matters is that you tried. Or not."
    "It's actually more about my own personal enjoyment of watching you flail about in a dire attempt to fumble your way through this meeting."
    "But no hard feelings, okay?"
    "Go get 'em, soldier."

label inmeeting:
    scene bg meeting
    with fade
    show boss

    b "Welcome, everyone. We'll start shortly, but let's give the stragglers a few more minutes to arrive before we do."

    hide boss

    "."
    ".."
    "..."
    "...."
    "....."
    "......"

    show boss

    b "I-is there anyone on the call?"

    hide boss
    scene bg george

    ge "Hey, it's George!"
    "~Morning George~"
    ge "I'm dialing in from my car so the call quality might be hit and miss."
    show boss at left
    b "Sorry George, just a second."
    b "Would someone turn off this god awful music?"
    show david at right
    d "Boss, I'm pretty sure that's coming from your phone."
    b "...oh."
    stop music
    b "Please continue, George."
    hide boss
    hide david
    ge "I was finished talking. Sorry boss."
    m "Wait, I thought that music was playing all over the office?"
    show boss
    b "I've seen {i}everything{/i}."
    
    if bossroom_poetry:
    
        b "Speaking of which, I've scheduled you in for a three hour meeting after this, I hope you don't mind."
        b "You seem to have an interest in poetry so I'd like to bounce some ideas off you."
    
    scene bg meeting

    b "In that case we're just waiting on Mia."

    hide boss
    show boss at left
    show fiona at right

    f "Oh she's definitely in the office. I've seen her."

    hide fiona
    hide boss
    show boss

    b "Okay. Well, in the interests of time, let's kick off the meeting."
    b "As there are a lot of unfamiliar faces here in the room, I'd like us all to introduce ourselves."
    b "Well, you all know who I am, so let's go clockwise from me."

    hide boss
    show david
    with fade
    
    d "Hi, I'm David. You might remember me from the Christmas party. I work in sales."
    
    hide david
    show harold
    with fade
    
    h "I'm Harold. I work as part of the marketing team."
    
    hide harold
    show fiona
    with fade
    
    f "My name's Fiona. I'm with the sales and marketing team."
    
    hide fiona
    scene bg george
    
    ge "Hey, it's George!"
    "~Morning George~"
    ge "I'm in the retail team."
    
    scene bg meeting
    with fade
    
    $ name = renpy.input("Looks like you're up. Give them your name!")
    
    m "Hello, my name is [name], I'm uhh..."
    
    show boss
    with fade
    
    b "Don't worry, we all know who you are."
    b "Right, at this point we should get down to business-"
    
    hide boss
    scene bg george
    show mia
    
    mi "S-sorry I'm late! Good heavens, I'm not normally this late. I'm so, so sorry!"
    
    hide mia 
    scene bg meeting
    show boss at left
    show mia at right
    
    b "Don't worry, Mia, it happens to the best of us."
    mi "Thank you, boss!"
    b "We'll talk about this later. Bring your things."
    mi "O-okay..."
    
    if hands_washed_times >= 5:
        b "What... what is that smell?"
        mi "I'm sorry boss, someone used up all of the soap in the ladies bathroom."
        b "I'm... sorry I asked."
    
    hide mia
    hide boss
    scene bg meeting
    with fade
    show boss
    
    b "As I was saying, I'm now going to hand the meeting over to [name]. It was you who suggested we hold this meeting, anyway."
    m "R-right. Yes. I did say that, huh."
    b "You do remember what we're here to talk about, right?"
    
    hide boss
    
label meeting_dec_one:
    scene bg meeting
    with fade
    
    menu:
        "Yes. We're here to discuss the downright terrifying levels of body odour in the office.":
            jump meetingd1o1

        "We're here to discuss the business strategy running through FY15.":
            jump meetingd1o2

        "I wanted us to debate theories and phenomena that would cause a grown human to lose their memories.":
            jump meetingd1o3
            
        "We need to urgently discuss the feature tracks for our latest compilation.":
            jump meetingd1o4
        
        "I have three proposals to share regarding our next big client.":
            jump meetingd1o5
            
label meetingd1o1:
    show boss
    b "[name], it's unlike you to be making jokes. Is something the matter?"
    b "It's basically common knowledge that we're not having that meeting until Monday when everyone is in the office."
    hide boss
    jump meeting_dec_one
    
label meetingd1o2:
    show harold at left
    h "Business strategy?"
    show mia at right
    mi "Have we ever had a business strategy?"
    show boss
    b "I have a dartboard."
    hide boss
    hide mia
    hide harold
    jump meeting_dec_one
    
label meetingd1o3:
    show david
    d "Amnesia is a deficit in memory caused by brain damage, disease, or psychological trauma."
    d "Amnesia can also be caused temporarily by the use of various sedatives and hypnotic drugs."
    d "Essentially, amnesia is loss of memory. The memory can be either wholly or partially lost due to the extent of damage that was caused."
    d "There are two main types of amnesia:"
    hide david
    show david at left
    show boss at right
    b "David?"
    d "Retrograde amnesia and anterograde amnesia."
    b "David!"
    d "Yes?"
    b "You're doing it again."
    d "Sorry boss."
    hide david
    hide boss
    jump meeting_dec_one
    
label meetingd1o4:
    show david at left
    show harold at right
    d "Hey, that's not a bad idea."
    h "Not bad at all! That's definitely at least an idea!"
    hide david
    hide harold
    jump meetingpart2
    
label meetingd1o5:
    show boss
    b "Three proposals?"
    m "Yes sir."
    b "Three fully written proposals?"
    m "Yes sir."
    b "Can I see them?"
    m "No sir."
    b "We don't write proposals here."
    m "No sir."
    b "We ARE the law."
    m "Yes sir."
    hide boss
    jump meeting_dec_one
    
label meetingpart2:
    show boss
    b "Order! Order in the room!"
    b "Now, we've made it past what it said on the meeting invite I sent to your phones."
    show mia at left
    mi "It said that?"
    show fiona at right
    f "Yeah, you just had to scroll down a bit."
    hide mia
    hide fiona
    b "Anyway, that's all well and good, but there's so much that goes on here that it's hard to keep track of what album we're talking about."
    b "[name], care to fill us in?"
    hide boss
    
label meeting_dec_two:
    scene bg meeting
    with fade
    
    menu:
        "Sure. This is regarding the classical music compilation we're currently working on.":
            jump meetingd2o1

        "This is for the sweet summer jams mixtape I'm working on.":
            jump meetingd2o2

        "No problem, it's for the latest Beyoncé album.":
            jump meetingd2o3
            
        "The company photo album. We need some backing music for the official presentation.":
            jump meetingd2o4
        
        "It's for our yearly offering of the latest and greatest pop sensations.":
            jump meetingd2o5

label meetingd2o1:
    scene bg george
    ge "Classical music?"
    show bg meeting
    show fiona
    f "What counts as classical? Like, early Bieber?"
    hide fiona
    show fiona at left
    show boss at right
    b "What? No, of course not! Idiot!"
    b "We're talking {i}at least{/i} 1994."
    hide boss
    hide fiona
    jump meeting_dec_two
    
label meetingd2o2:
    show david
    d "Ah, the healing properties of the summer jam."
    d "A frankly understated pleasure."
    d "The highlight of many a caravan trip."
    d "Bliss."
    hide david
    show boss
    b "It wasn't a summer jam mixtape."
    b "Sorry."
    hide boss
    jump meeting_dec_two
    
label meetingd2o3:
    show mia
    mi "OH MY GOD."
    hide mia
    show mia at left
    mi "OH."
    hide mia
    show mia at right
    mi "MY."
    hide mia
    show mia
    mi "GOD."
    mi "A NEW BEYONCÉ ALBUM!"
    "{i}incomprehensible screaming.{/i}"
    mi "As Field Marshall of the Beyontourage, I must leave the meeting and prepare the daily newsletter!"
    hide mia
    show mia at right
    show boss at left
    b "[name], it wasn't funny the last time you did this."
    hide mia
    hide boss
    show mia at right
    show boss
    show leslie at left
    l "DID SOMEONE SAY NEW BEYONCÉ ALBUM?"
    b "Who are you?"
    mi "NEW BEYONCÉ ALBUM!"
    "{i}incomprehensible screaming: the reckoning{/i}."
    m "Sorry boss."
    b "You'd better be."
    hide mia
    hide boss
    hide leslie
    jump meeting_dec_two
    
label meetingd2o4:
    show boss
    b "Ooh, an employee photo album? That's kind of cool!"
    b "We could make it like those American graduation books and have witty comments beneath our pictures."
    b "I could be wearing my Batman onesie, throwing a batarang and the comment would read 'The Dark Boss Rises'."
    b "We'll sort it out. We have some money that we're meant to use for employee bonuses that isn't getting used."
    b "Thanks for the idea, but let's get back on topic."
    hide boss
    jump meeting_dec_two
    
label meetingd2o5:
    show boss
    b "The latest {b}and{/b} greatest! I like that!"
    b "Bit of a lie, but hey, it's part of the business."
    b "It's like... our own personal autotune."
    b "We hide the truth with ａｇｇｒｅｓｓｉｖｅ　ａｕｄｉｏ　ｔｒｅａｔｍｅｎｔ　ａｎｄ　ｔｈｅ　ｌａｔｅｓｔ　ｉｎ　ｖｏｃａｌ　ｔｅｃｈｎｏｌｏｇｉｅｓ．"
    show fiona at left
    f "That's deep."
    hide fiona
    b "Yes. Yes it is."
    hide boss
    jump meetingpart3
    
label meetingpart3:
    show bg meeting
    show boss
    b "We are here to finalise the track list for this year's Now album, which as you all know is titled:"
    b "Now That's What I Call a Collection of Songs from Various Artists Arranged into a Seemingly Arbitrary Order but Actually Not Quite Because we Made Sure that The Best Ones were Near the Top! 137."
    b "For the most part, we've finalised the necessary deals for 95%% of the music, but we still need something with a bit more pizzazz."
    b "Something a bit more rambunctious."
    b "Ostentatious! Exorbitant! Profligate!"
    b "c-r-a-z-y."
    b "Does anyone have any ideas?"
    scene bg george
    show david at left
    show harold at left
    show fiona at right
    show mia at right
    show leslie 
    "OIFOIJREWOJOIHWEFOIHEORGFPOIHJOIFDGPOPWROIHWEOIHTOIHEHGFHOIH"
    h "There's this one track from Sweden that I think will go great-"
    mi "We DEFINITELY need another Beyoncé track-"
    l "DID SOMEONE SAY BEYONCÉ?"
    b "Who {i}are{/i} you?"
    g "Can someone play the Cliff Richard song for [name] so he knows-"
    mi "Pass me your laptop I want to play you a song."
    b "No way, I'm first."
    l "No! Give it {i}back{/i}."
    $ youtube.open_youtube()
    b "As your boss, I must apologise for that."
    b "You have final say in all of this. We just need to hear the songs you'd like to feature."
    b "Make sure you have each YouTube URL copied. I'm a simple man and I'm easily confused, so that's the best way for us to do this."
    scene bg meeting
    hide david
    hide harold
    hide fiona
    hide mia
    hide leslie 
    jump new_video

label new_video:
    if playlist.is_complete():
        g "ｔｈａｎｋ　ｙｏｕ　ｆｏｒ　ｙｏｕｒ　ｃｏｏｐｅｒａｔｉｏｎ"
        jump endgame

    if playlist:
        "Okay so we have:\n[playlist.formatted]"

        if playlist.remaining == 5:
            b "So for starters, let's have something a bit effervescent:"
        if playlist.remaining == 4:
            d "Anything that isn't Beyoncé:"
        if playlist.remaining == 3:
            f "Something that isn't the same old shit:"
        if playlist.remaining == 2:
            h "Something foreign. For example, something Swedish. I like Sweden:"
        if playlist.remaining == 1:
            ge "Last track? Please pick something by Cliff Richard."

    menu:
        "I have the correct YouTube URL copied already.":
            jump paste

label paste:
    $ video = youtube.paste()
    if video:
        if video.is_already_in_playlist(playlist):
            b "Hey now, you've played this one already (and I didn't think it was that good, anyway)."
            jump new_video

        $ playlist = playlist.with_video(video)

        if video.is_the_trailer():
            jump trailer
        if video.was_already_suggested():
            jump was_already_suggested
        if video.is_3d():
            jump is_3d
        if video.is_trending_hard():
            jump trending_hard
        if video.is_gangnam_style():
            jump gangnam_style_video
        if video.is_psy():
            jump psy_video
        if video.is_bass_boost():
            jump bass_boost_video
        if video.is_really_short():
            jump really_short_video
        if video.is_hardly_watched_at_all():
            jump dead_video
        if video.is_really_long():
            jump really_long_video
        if video.is_not_watched_a_lot():
            jump obscure_video
        if video.is_short():
            jump short_video
        if video.is_long():
            jump long_video
        
        else:
            jump nothing_special_video
    else:
        b "You, uhh, might want to try that again. Something broke and I'm too lazy to move from my seat and find out why."
        jump new_video

label gangnam_style_video:
    show boss
    b "OPPA GANGNAM FUCK YOU."
    hide boss
    jump new_video
    
label bass_boost_video:
    show dave at left
    kb "Damn son! Where'd you find this!?"
    hide dave
    jump new_video

label psy_video:
    show boss
    b "I'm sorry if you were being serious, but please don't play that around here any more."
    b "No one plays PSY around here and lives to tell the tale."
    hide boss
    jump new_video
    
label really_short_video:
    show boss
    b "Did anything even play just then? Did I blink and miss it?"
    b "Actually, that sounds rather edgy. Like you're making a statement. I like that."
    hide boss
    jump new_video

label short_video:
    show boss
    b "That song is a bit short, isn't it? People will feel robbed if we put that on the compilation."
    b "Well... more so."
    hide boss
    jump new_video

label long_video:
    show david
    d "A masterpiece. An epic."
    d "A song that goes on far too long."
    d "Where am I?"
    hide david
    jump new_video

label really_long_video:
    show boss
    b "It's been a while since I've heard music that just goes on and on and on and on."
    hide boss
    show mia
    mi "And on and on and on and on."
    hide mia
    show david
    d "And on and on and on."
    hide david
    scene bg george
    ge "And on and on."
    scene bg meeting
    show boss
    b "And on."
    hide boss
    jump new_video
    
label obscure_video:
    scene bg george
    ge "Everyone knows that the more views a video has, the better the music is."
    scene bg meeting
    show fiona
    f "So this just isn't any good."
    hide fiona
    jump new_video

label dead_video:
    show harold
    h "Either this video just got uploaded, or it's one of your videos."
    h "Because no one seems to care about it."
    h "You didn't even view it more than a few times yourself?"
    hide harold
    jump new_video
    
label trailer:
    show boss
    b "A game trailer, eh? What a terrible looking game."
    b "Why would you want this on the compilation?"
    b "The characters look like they were made in MS Paint and were held up on a laptop."
    b "You have awful taste in games. Good music though. Everyone loves dubstep."
    hide boss
    jump new_video
    
label was_already_suggested:
    show boss
    b "Didn't we hear this earlier when all that noise blared out of your laptop?"
    b "I didn't like it then and I don't like it now."
    b "I'm personally going to fire whoever it was in this room that put it into your laptop."
    hide boss
    jump new_video
    
label is_3d:
    show dddboss
    ddd "This is in 3D!"
    ddd "This is stupid, nobody likes 3D."
    ddd "I would never be seen dead watching something in 3D."
    ddd "I'll let you add the track though."
    hide dddboss
    jump new_video
    
label trending_hard:
    show fiona
    f "Got your finger on the pulse, eh?"
    f "Ehhhhh?"
    f "You better not have found this in the trending videos on YouTube."
    f "You cheat."
    hide fiona
    jump new_video
        
label normal5:
    show fiona
    f "Eh, I've heard better."
    hide fiona
    jump new_video
    
label normal4:
    show harold
    h "This doesn't sound Swedish."
    hide harold
    jump new_video
    
label normal3:
    show mia
    mi "This reminds me of that time we all got drunk at morning meeting."
    hide mia
    jump new_video
    
label normal2:
    scene bg george
    ge "This makes me feel insecure."
    scene bg meeting
    jump new_video
    
label normal1:
    show boss
    b "Thank you, [name]."
    hide boss
    jump new_video

label nothing_special_video:
    $ ui.jumps(["normal1", "normal2", "normal3", "normal4", "normal5"][playlist.remaining])()

label endgame:
    scene bg certificate
    with fade

    $ centered(u"{color=#000000}{size=+10}~CONGRATULATIONS~{/size}\nYou and your team assembled a collection of soulless music and it brought no relief to the short, meaningless existences of anyone who heard it.\n\nGaze upon your creation and weep.\n\n[playlist.certificate_text]{/color}")
    $ centered(u"{color=#000000}[playlist.stats]{/color}")
