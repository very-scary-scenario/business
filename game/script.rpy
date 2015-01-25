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
image bg mydesk = "mydesk.jpg"
image bg officedesk = "officedesk.jpg"
image bg cubicle = "cubicle.jpg"
image bg kitchen = "kitchen.jpg"
image bg bossroom = "bossroom.jpg"
image bg reception = "reception.jpg"
image bg premeeting = "premeeting.jpg"
image bg meeting = "meeting.jpg"
image bg george = "trenchfoot.jpg"
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

label start:
    jump new_video  # XXX should be the dream sequence (or at least awaken)

label awaken:
    $ cubicleguy_talked = False
    $ kitchen_happy = False
    $ kitchen_sad = False
    $ desk_searched = False
    $ bossroom_searched = False
    $ reception_visited = False
    scene bg mydesk

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

    "Well, this is it. We've become desperate enough to put the job on the line. Whatever it is."
    "Fortunately for you, the boss insists on arriving to meetings early. They've already booted out the people who should currently be in the meeting room."
    "Perks of being the boss, I suppose."
    "But it gives you free reign of the boss' room. You'd hope that there would be something here that would tell you what's up."
    "{i}You'd hope.{/i}"

label inbossroom:
    scene bg bossroom
    with fade

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

    scene bg meeting
    show boss

    b "In that case we're just waiting on Fiona."

    hide boss
    show boss at left
    show mia at right

    mi "Oh she's definitely in the office. I've seen her."

    hide mia
    hide boss
    show boss

    b "Okay. Well, in the interests of time, let's kick off the meeting."
    b "As there are a lot of unfamilar faces here in the room, I'd like us all to introduce ourselves."
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
            
label meetingd101:
    show boss
    b "[name], it's unlike you to be making jokes. Is something the matter?"
    b "It's basically common knowledge that we're not having that meeting until Monday when everyone is in the office."
    hide boss
    jump meeting_dec_one
    
label meetingd101:
    show harold left
    h "Business strategy?"
    show mia right
    mi "Have we ever had a business strategy?"
    hide harold
    show boss left
    b "I have a dartboard."
    hide boss
    hide mia
    jump meeting_dec_one
    

    
    
    # guff below

    $ video = youtube.paste()
    if video:
        "THIS [video.title] VIDEO IS THE WORST [video.duration] I HAVE EVER SPENT AND [video.dislikes] PEOPLE AGREE WITH ME"
        "THIS [video.likes] PEOPLE DISAGREE AND ARE IDIOTS AND [video.views] PEOPLE HAVE SHARED THIS TERRIBLE EXPERIENCE"
    else:
        "i dunno maybe our internet is broken that didn't work"

    jump new_video

label new_video:
    $ youtube.open_youtube()
    if playlist.is_complete():
        "WE ARE DONE HERE"
        jump endgame

    if playlist:
        "Okay so we have:\n[playlist.formatted]"

        if playlist.remaining != 1:
            "We need [playlist.remaining] more tracks."
        else:
            "Only one left!"

    menu:
        "There is a youtube video URL in my clipboard":
            jump paste

label paste:
    $ video = youtube.paste()
    if video:
        if video.is_already_in_playlist(playlist):
            "YOU SHIT WE HAVE THAT LLAREJIOAJREAEADY"
            jump new_video

        $ playlist = playlist.with_video(video)

        if video.is_gangnam_style():
            jump gangnam_style_video
        if video.is_psy():
            jump psy_video
        if video.is_short():
            jump short_video
        else:
            jump nothing_special_video
    else:
        "i dunno maybe our internet is broken that didn't work"
        jump new_video

label gangnam_style_video:
    "oh just fuck off"
    jump new_video

label psy_video:
    "look i know you think you're a proper hipster"
    "but that shit just doesn't fly here, we all hear this shit all god damn day on the fucking radio one radio show"
    jump new_video

label short_video:
    "FUCK MAN THAT IS WAY TOO SHORT"
    jump new_video

label nothing_special_video:
    "there is nothing special about this"
    jump new_video

label endgame:
    "many combolations elizagerth"
