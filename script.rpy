

define mr = Character("Mozzy", color = "#c7a600")
define mr_thought = Character("Mozzy", what_italic=True, color = "#ffd919")
define mt  = Character("Mira", color = "#603000")
define pc = Character("Pitaya", color = "#c22640")
define hd = Character("Honey", color = "#018e01")
define ss = Character("Stirling", color = "#ff70ba")
define jp = Character("Jazz", color = "#ff1919")
define sp = Character("Smith", color = "#82f046")
define int_box = Character(None, what_xalign=0.5, what_text_align=0.5)
default twin_int = False
default ss_int = False
default hd_int = False
default pc_int = False
default pc_testimony = False
default twin_testimony = False
default successful_gaydar = False
default failed_gaydar = False
default hat = False
default gem = False
default honey_doll = False
default hd_hospital = False
default ss_hospital = False
default pitaya_guilt = False
default twin_guilt = False
default stirling_guilt = False


label start:
    "Hi."
    "This game is made for the 2026 NZ schools game jam."
    "But apparently, our teacher doesn't want to go through 30 minutes of dialogue."
    "I mean, fair enough, I guess."
    "So I'm adding an option where you can skip the dialogue and get to the juicy gameplay."
    menu:
        "So, which will it be?"
        "I just want to try the minigames":
            "Alright."
            "Off we go!"
            jump hidden_object
        "I'd like to play the story too":
            "Alright."
            "Off we go!"
            jump story

label story:
    scene bg bus
    with dissolve

    show mira default at right
    show mozzy curious at left 

    mr "I just don't get it, Mira!"
    mt  "Hm?"
    mr "I mean, I know I'm an ace detective and all, but why are WE on our way to investigate a robbery here?"
    mr "It's the richest neighbourhood as well! Shouldn't someone a bit more higher-up take the case?"
    show mira hide
    mt  "..."
    show mira default
    mt  "This isn't actually an official case yet."
    mr "..."
    show mozzy shock
    mr "h-hUH?!" with hpunch
    show mira smile
    mt  "A dear friend of mine asked me to help investigate before there is a scandal."
    mt  "And, well, you haven't had a case in a while either, so I decided to bring you along."
    show mira default
    show mozzy curious
    mt  "Speaking of which, let's run over how to do investigations and interrogations."
    mt  "You'll notice that I haven't told you which house we're heading to."
    mt  "Your goal is to try and pull information out of me. Then, when we arrive at our stop, you'll use the information you received to find the correct house."
    menu:
        mr  "Do I interrogate Mira?"
        "Yeah, we need information!":
            jump interrogate_tut
        "No, I feel like I've done this before.":
            jump skip_tut
    
label interrogate_tut:
    show mozzy excited
    mr "Alright!"
    mr "Bring it on!"
    hide mozzy excited
    show mira smile at right
    show mira smile at default
    with move
    int_box "INTERROGATE: Mira Tisu"
    menu: 
        mt  "Well, Mozzy? Ask away."
        "What colour is the house?":
            jump house_colour
        "What is the address?": 
            jump house_address
        "Who is the owner of the house?":
            jump house_owner

    label house_colour:
        mt  "Well, my dear friend adores the colour pink."
        mt  "That's why the house is a sort of reddish pink colour."
        mt  "The roof, however, is covered in black shingles."
        jump question_list

    label house_address:
        show mira default
        mt  "That's a good question."
        show mira smile
        mt  "But where's the fun in just telling you the answer?"
        mr_thought "Mira, quit trolling me...!"
        jump question_list
        
    label house_owner:
        show mira default
        mt  "The owner of the house...? Odd question to ask in this scenario."
        mt  "Well, it is none other than my dear friend, Stirling Strawberry."
        mt  "But that really doesn't seem like a question that will help you."
        mr "Huh? O-oh!"
        mr_thought "Dang...she's right!"
        mt  "It's quite alright, but just remember that others aren't so forgiving as I am when you ask irrelevant questions."
        jump question_list

    label question_list:
        menu:
            mt  "Any other questions?"
            "What colour is the house?":
                jump house_colour
            "What is the address?": 
                jump house_address
            "Who is the owner of the house?":
                jump house_owner
            "No, no more questions.":
                jump tutorial_end

label skip_tut:
    mr "Mira, you know I usually would, but..."
    show mozzy default
    mr "I'm getting a lot of deja vu. I think I can find the house without any help."
    mt  "I will never understand your strange sixth sense."
    mr_thought "(We talked about some of our coworkers for the rest of the bus ride.)"
    jump tutorial_end

label tutorial_end:
    scene bg bus
    show mozzy default at left
    show mira default at right
    mr "Right...I think that's all the information need."
    mt  "Hm, and just in time too."
    mt  "This is where we get off."
    mr_thought "Mira and I thanked the bus driver and jumped off the bus."
    scene bg rich street
    with dissolve
    show mozzy default at left
    show mira default at right
    mt  "Alright Mozzy, time to put the clues you gathered to good use."
    mt  "Can you find the house now?"
    show mozzy excited
    mr "Of course!"
    show mozzy curious
    mr "But, uh, Mira...?"
    show mira default #curious, but we don't have the time for that as of now
    mt  "?"
    mr "How much time do I have?"
    show mira surprise
    mt  "!"
    show mira smile
    mt  "That's what you're worried about? Don't worry, take all the time you need. We're in no hurry."
    show mozzy excited
    mr "Phew! Thanks, Mira!"
    label hidden_object_tut:
        call screen richstreet
    
    label Found:
        mr "There it is!"
        jump continue_story1

screen richstreet():
    add "bg rich street"
    modal True

   
    imagebutton auto "houseST_%s.jpg":
        focus_mask True
        hovered SetVariable("screen_tooltip", "houseST_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Found")

label continue_story1:
    scene bg gates
    with dissolve 
    show mozzy excited at left
    show mira smile at right
    mr "Okay! Made it!"
    mt  "That was quick. Well done."
    mr "Of course! It was a piece of pie for the Great Detective Mozzy Rella!"
    mt  "Hm...of course."
    mr "Well, what are we waiting for? Let's go!"
    show mira surprise
    mt  "Mozzy, wait-!"
    show mozzy shock 
    mr "...!"
    mr "The gates...are locked!"
    mt  "Of course they are! Stirling kept them locked so that the thief couldn't get out."
    show mozzy damage
    mr_thought "Can't a thief just climb over the gates though?"
    show mira default
    show mozzy default
    mt  "I'll let Stirling know that we're here."
    "{i}(insert ringtone){/i}"
    mt  "..."
    mt  "Hey Stirling. My partner and I are outside your gates. Do you mind letting us in?"
    mt  "..."
    mt  "Investigative partner, Stirling. I'm not dating anyone at the moment. I still don't have time for that. Besides, he's far too young-"
    show mozzy damage
    mr "Hey! I'm 23!, I can definitely vote....legally."
    mr_thought "Mira simply ignored me."
    show mozzy default
    show mira hide
    mt  "..."
    show mira serious
    mt  "Stirling Strawberry, you will let us in right this moment or I will tell those cousins of yours that you ate the last cookie." with hpunch
    show mozzy shock
    mr "Eep!"
    mr_thought "Mira can be so scary sometimes..."
    mt  "..."
    show mira smile
    mt  "Thanks. I'll see you soon."
    show mira default
    mt  "..."
    show mira sadly
    mt  "Sorry, did I scare you?"
    show mozzy excited
    mr "Um...I don't know what you're talking about! A great detective is never scared!"
    show mira default
    mr_thought "For some reason, Mira doesn't seem to believe that."
    mt  "...If you insist."
    show mozzy default
    mr "..."
    mt  "..."
    mr "Your friend is taking a while."
    scene bg gates open
    show mozzy default at left
    show mira default at right
    mr_thought "Lo and behold, just as I said those words, the gates opened."
    show mozzy damage
    mr "Are you kidding me?"
    show mira smile
    mt  "I must say Mozzy, you have impeccable timing at times."
    mr "Let's...let's just go in."
    scene bg garden
    mr_thought "I fixed up my hat, and we walked through the gates."
    mr_thought "There was a really cool garden there. The fences were wrapped in ivy and roses, and there was a glass gladiator dome. It was really well kept, clearly someone was obsessed with fighting the weeds."
    mr_thought "Suddenly, I heard a familiar voice shouting...a lot of things I won't repeat."
    show pitaya angry
    pc "That's it, you people deal with this yourself! I'm outta here!"
    mr "Pitaya!"
    show pitaya surprise
    pc "...?"
    show pitaya default
    pc "Mozzy! Hey, man!"
    mr_thought "Pitaya Crim, I was close with him during High school and college, acts like a big tough guy but he is really just a sweetheart, volunteering at nursing homes and what-not."
    mr_thought "...Okay, so MAYBE he was on trial for murder like a hundred times, but he's never actually committed any of them!"
    show pitaya disgust
    pc "Mozzy you're spacing out again."
    pc "Are you doing that thing where you introduce people in your head completely out of character?"
    mr_thought "Ack. Guilty."
    menu:
        mr_thought "Quick, Mozzy, deflect!"
        "Actually, I'm thinking about koalas.":
            jump koalas
        "No, I'm thinking about you.":
            jump gay

    label gay:
        show pitaya damage
        pc "W-W-What?!"
        mr_thought "Hehe, that always catches him off guard."
        jump enter_house

    label koalas:
        show pitaya surprise
        pc "...Koalas?"
        mr "Yeah! Did you know, a koala could frame someone for a crime!"
        pc "How would a koala-"
        mr "Koalas have fingerprints, just like us! So, if a koala commits a crime and leaves its fingerprints everywhere, you'd think a human did it!"
        show pitaya smile
        pc "Wow...so they do teach detectives something."
        mr "Oh, nah, I learnt this one myself."
        show pitaya surprise
        pc "...From where?"
        mr "So, there's this social media site called-"
        show pitaya deadpan
        pc "Nevermind, I got what you're saying."
        jump enter_house

label enter_house:
    mr "Anyways, time to get a move on people!, no time to waste!"
    show pitaya deadpan
    pc "oh my gosh you oblivious swiss cheese..."
    hide pitaya
    show mira surprise
    mt  "...my goodness."
    scene bg living room
    mr_thought "We went into the house. Somehow, it was both simpler and fancier than the garden."
    show mira surprise
    mt "Oh, Mozzy, take your shoes off. Stirling's half-Korean, so guests have to take their shoes off at the entrance."
    hide mira surprise
    mr_thought "We made our way to what I assume is the living room. The floor was made of wood, and a pink rug laid over one section."
    mr_thought "There were two couches near the TV, and a table in front of them. Under the table were...videogames?! Awesome! This Stirling person, whether they're a man or woman, has good taste!"
    show pitaya smile
    pc "Well people, we have our detective and everyone's favourite lawyer."
    show smith aloof at right
    with dissolve
    show pitaya damage
    "???" "...He looks like a dud."
    mr "how dare you!, you...you...gremlin?, sorry you're just extremely short."
    show jazz aloof at left 
    with dissolve
    "???" "And? We're literally fourteen."
    show jazz smug
    "???" "If anything, you're the short one."
    mr "HEY!!"
    hide pitaya damage
    show mira hide
    mt  "*sigh*"
    show mira default
    mt  "Jazz, Smith, meet Mozzy. I met him on one of my cases."
    mt  "Mozzy, these are the Pale twins, Jazz and Smith. Jazz is the red one, Smith is green."
    show jazz smug
    jp "We met her when Stirling introduced his \"girlfriend\" to his family."
    show smith smug
    sp "Which is just us."
    show mira smile
    mt  "Bold of you two to assume that Stirling can last a day dating me."
    jp "Fair point."
    sp "Yeah, you deserve better anyways."
    hide mira smile
    hide jazz smug
    hide smith smug
    show stirling grumpy
    "???" "Hey, I heard that!"
    hide stirling grumpy
    show jazz aloof
    jp "Oh, you're here? Whoops." 
    mr_thought "That was the most unsincere apology I have ever heard."
    mr_thought "And I went to school with Pitaya."
    hide jazz aloof
    show honey default
    "???" "Stirling, I would love to come to your defense, {w}" 
    show honey smile
    extend "but to be honest, I do think Mira deserves better."
    hide honey smile
    show stirling grumpy
    ss "So someone like you?"
    hide stirling grumpy
    show honey surprise
    "???" "..."
    show honey smile
    "???" "Oh, no. But certainly not you, you're too childish."
    hide honey smile
    show stirling angry
    ss "Too childish-it's called being optimistic!"
    hide stirling angry
    show honey smile
    "???" "My apologies, I was only teasing you, silly."
    hide honey smile
    show stirling grumpy
    ss "Why are you like thiiis?"
    hide stirling grumpy
    show honey default
    "???" "Well, someone has to be a responsible adult when dear Mira's not around."
    "???" "I can hardly compare with her, but I do my best!"
    mr_thought "Wow, these guys really like Mira, huh?"
    hide honey smile
    show mira smile
    mt  "Hi, honey."
    mr_thought "Mira using pet names? Is the world ending?"
    show mira serious
    mt  "I don't know what you're thinking, but cut it out."
    show mira default
    mt  "Honey, this is Mozzy. Mozzy, meet Honey Dew. I know her from university."
    hide mira default
    show honey smile
    hd "Pleasure to meet you."
    mr_thought "Oh, so Honey's her name, not a term of affection."
    mr_thought "Probably should have figured that out."
    hide honey smile
    show stirling smile
    ss "And I'm Stirling Strawberry, besties with Mira since we met in college ten years ago!"
    mr "I see."
    mr "..."
    mr "Wait Mira you went to college when you were 10?"
    hide stirling smile
    show mira default
    mt  "...How old do you think I am? "
    mr "...twenty, right?"
    show mira serious
    mt  "I'm thirty-two."
    mr "Oh."
    mr "Well, in any case, thank you, good madam!"
    hide mira serious
    show stirling shock
    ss "Huh? I-uh-I'm not-"
    mr "Huh? What's wrong?"
    hide stirling shock
    show pitaya nervous
    pc "Oh, man-"
    hide pitaya nervous
    show jazz default at left
    show smith default at right
    "Jazz and Smith" "And another one bites the dust!"
    hide jazz default
    hide smith default
    show mira sadly
    mt  "Mozzy..."
    hide mira sadly
    show stirling shock
    mt  "Stirling's a man."
    mr "GAH!"
    show stirling nervous
    mr "ajkfbldashfircids I am SO sorry!"
    ss "It-it's fine...it happens a lot..."
    show stirling awkward
    ss "Do I really look that much like a girl...?"
    hide stirling awkward
    show pitaya deadpan
    pc "Yup."
    show jazz aloof at left
    jp "You do."
    show smith aloof at right
    sp "You really look like a girl."
    show pitaya angry
    pc "Hey, YOU can't say anything! You and your sister look identical!"
    show jazz disgust
    jp "What part of \"identical twins\" do you not understand...?"
    show smith smug
    sp "It's only fair, I mean, she looked identical to me a few years ago, so now I'm identical to her."
    show pitaya deadpan
    pc "I know, I know, I was there when you guys announced the change to the family!"
    hide pitaya deadpan
    hide smith smug
    hide jazz aloof
    show honey surprise
    hd "..."
    show honey default
    hd "I personally don't think you look like a girl Stirling...{nw}{w=.5}"
    show honey smile
    extend "but I can see why people think so!"
    hide honey smile
    show stirling nervous
    ss "Well...I guess that's a me problem."
    hide stirling nervous
    show mira default
    mt  "Speaking of problems...I brought Mozzy here to help with yours."
    mr "Please hold your applause, I know I'm glamorous!"
    hide mira default
    show jazz disgust
    jp "Is he always like this?"
    mr "Hey, what's that supposed to mean?"
    hide jazz disgust
    show mira default
    mt  "So if we could start our investigation soon, that would be great."
    hide mira default
    show stirling default
    ss "Aww, come on, Mira! All the suspects are here, can't it wait?"
    hide stirling default
    show mira serious
    mt  "No. The faster we get this done, the less we have to worry about it."
    hide mira serious
    show pitaya deadpan
    pc "Man, lawyers are scarily efficient."
    hide pitaya deadpan
    show honey default
    hd "Alright."
    show honey sadly
    hd "Stirling called you because the Melon Baller was stolen!"
    mr "The what?"
    hide honey sadly
    show stirling determined
    ss "The Melon Baller. It's Honey's favourite necklace."
    hide stirling determined
    show jazz disgust
    jp "Favourite? She's only had it for the past week."
    hide jazz disgust
    show honey grumpy
    hd "Would it kill you kids to have some tact?"
    hd "Hmph. I'll show you my room. It's a bit of a mess since I was looking through everything, but you might be able to find some clues."

screen honeysroom():
    add "bg honey room"
    modal True
   
    imagebutton auto "Jewel_box_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Jewel_box_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Jewel")

    imagebutton auto "Mannequin_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Mannequin_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Mannequin")

    imagebutton auto "candle_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "candle_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Candle")
        
    imagebutton auto "mira_doll_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "mira_doll_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Doll")

    imagebutton auto "mira_picture_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "mira_picture_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Photo")

    imagebutton auto "pillow_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "pillow_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Pillow")

    imagebutton auto "door_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "door_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Leave")

label hidden_object:
    scene bg honey room
    show mozzy shock
    mr "W-wow! You weren't kidding when you said it was a mess!"
    hide mozzy shock
    show honey default
    hd "Yes, I practically turned it inside out."
    hd "You see, I first thought I misplaced it, but when I couldn't find it anywhere, I realised someone must have stolen it!"
    hide honey default
    show mira default
    mt  "Understood. Honey, could you step out and join everyone else? It's easier to investigate with just the two of us."
    hide mira default
    show honey grumpy
    hd "...Fine. If you say so."
    
    label honeys_room:
        call screen honeysroom
    
    label Jewel:
        scene bg honey room
        mr "This box is really neatly organised."
        mt  "Honey has a lot of jewellery, she likes to be able to see all of them and make sure they're there."
        mr "You'd think a thief would rummage through the jewellery box too."
        jump honeys_room
    
    label Candle:
        scene bg honey room
        mr "Ack...the watermelon scent is even stronger here."
        mt "Honey always loved her scented candles."
        jump honeys_room
        
    label Mannequin:
        scene bg honey room
        mt "This must have been where the Melon Baller was kept."
        mr "Weird, there's a feather missing from the hat."
        mt "Why, yes, that's true, but how could you tell?"
        mr "There's a random glue strip here between the feathers. "
        jump honeys_room

    label Doll:
        scene bg honey room
        mr "I didn't know you had merch Mira."
        mt "..."
        mr "..."
        mt "..."
        mr "...Mira?"
        mt "Let's...let's just ignore this."
        jump honeys_room
    
    label Pillow:
        scene bg honey room
        mr "Omigosh this is the softest pillow I have ever met."
        mt "Mozzy, for the love of god. Can you-what's the term these days-\"lock in\"?"
        mr "Mira, please never use slang ever again."
        jump honeys_room
    
    label Photo:
        scene bg honey room
        mr "A photo of Mira?"
        mt "Ah, I think this was after one of my first trials."
        mt "Why Honey has this though is beyond me."
        jump honeys_room

        
    label Leave:
        scene bg honey room
        menu:
            mt  "Are we done investigating?"
            "Yes":
                mr "Yeah, let's go."
                jump continue_story2
            "No, we still have stuff to find":
                jump honeys_room

label continue_story2:
    "As of 4/8/2026, 8:31pm, we don't have the full evidence list. So, here are the ones we don't have:"
    "Graduation banner, Brass knuckles, Stirling's smashed picture, Stirling's earring, Gem"
    scene bg hallway
    mr "Phew, we're finally done."
    show honey default
    hd "Ah, you're back, Mira! I hope the mess didn't trouble you too much."
    show honey default at left
    show mira default at right
    mt "Well-"
    mr "You have so much weird stuff in there, Ms Dew. Did you dig out that graduation banner from the trash?"
    show honey surprise
    show mira surprise
    hd "..."
    mt "..."
    mr "..."
    mr "Too weird?"
    show mira hide
    mt "A bit, yes."
    show honey grumpy
    hd "Well it wasn't in the trash when I retrieved it!"
    show mira serious
    mt "..."
    show stirling default
    ss "Hi! What did I miss?"
    show mira default
    show honey default
    mt "Nothing much."
    show stirling smile
    ss "Okay! Did you find who the thief is yet?"
    mt "No, not yet. We need more than just investigating to find the culprit."
    show stirling surprise
    ss "Oh."
    mr "You know what that means?"
    show mira smile
    show honey surprise
    show stirling default
    mt "We need to do what a lawyer does best!"
    "Mozzy and Mira" "IT'S INTERROGATION TIME!"
    scene bg living room
    with dissolve
    show pitaya smile
    pc "Heyo! Found anything?"
    mr "Yeah, loads! There was this-"
    hide pitaya smile
    show mira serious
    mt "We can discuss later. For now, we still have a job to do."
    mr "Oh, yeah. Ahem."
    mr "We're gonna interrogate all of y'all separately, okay? Just to make sure you guys don't interrupt each other while answering."
    hide mira default
    show jazz angry
    jp "You're not splitting us up."
    hide jazz angry
    show smith angry
    sp "Yeah! We're ride or die besties, got it?"
    mr "...Okay, fine. You guys can be interrogated together. But no one else!"
    hide smith guilty
    show honey default
    hd "That sounds fair."
    show honey smile
    hd "What do you think, Stirling?"
    hide honey smile
    show stirling smile
    ss "Let's do this!"
    hide stirling smile
    show mira smile
    mt "Then let's begin."
    hide mira smile
    menu:
        mr "Who should I interrogate first?"
        "Pitaya":
            jump int_pitaya
        "Honey Dew":
            jump int_honey
        "The Twins":
            jump int_twins
        "Stirling":
            jump int_stirling

label int_pitaya:
    $ pc_int = True
    show pitaya smile
    pc "Wazzup?"
    mr "Mr Crim-"
    show pitaya default
    pc "Ooh, we're doing this PROFESSIONALLY, okay, this oughta be good!"
    mr "Aw thanks! Anyways, please give us your version of the events-"
    show pitaya smile
    pc "Yeah, yeah, witness testimony, I got it."
    pc "Don't worry, I was the defendant for like half of Mira's cases, I know how this stuff works."
    mr "Wait, you guys knew each other before this?!"
    mt  "Yes, Stirling hired me as Pitaya's lawyer."
    mt  "But we're getting sidetracked. You two, lock in already."
    show pitaya deadpan
    pc "Mira, please, never use those words again."
    int_box "INTERROGATE: Pitaya Crim"
    label pc_ask:
        menu:
            mr "What to ask...?"
            "Testimony, please?":
                $ pc_testimony = True
                show pitaya default
                pc "I was just minding my own business, really!"
                show pitaya curious
                pc "We were expecting more people, but apparently there was a flight delay, so they couldn't come. But whatever, that's not important."
                pc "So yeah, I was just minding my own business, and waiting for dinner to be done. I was also checking out Stirling's videogames when Little Miss Drama Queen runs in screaming about how her necklace got stolen."
                show pitaya default
                pc "Yeah, that's all I can think of."
                show pitaya smile
                pc "By the way, I found the latest edition of that lawyer game you like so much in his collection, maybe we could play it together someday?"
                jump pc_ask
            "What is your alibi?":
                show pitaya curious
                pc "I mean, I was in the living room the whole time. Although, I don't know if anyone can confirm that."
                pc "I know for a fact that I saw the twins at one point, but they came from the corridor where the rooms are and went to the dining room right after, so they can't confirm my alibi."
                show pitaya default
                pc "But I swear on Old Mrs Frap, I did not go anywhere near Dew's room."
                pc "Seriously, she'd whup my butt if I lied to you!"
                jump pc_ask
            "What's on the crime agenda this year?":
                show pitaya default
                pc "Tax evasion."
                mr "...That's it?"
                show pitaya deadpan
                pc "What? It's a genuine crime."
                mr "Maybe, but it's also a normal thing for rich people to do."
                show pitaya curious
                pc "...Fair point."
                show pitaya smile
                pc "Oh well, I can change the annual crime in a few months anyways."
                show pitaya surprise
                mt  "What a thing to admit in front of your lawyer."
                jump pc_ask
            "That's all":
                show pitaya default
                mr "Okay...thank you Mr Crim."
    
    mr "That's all we need for interrogating Pitaya."
    menu:
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "Slaughter his defenses and put his castle under siege until he has to surrender!"
            show pitaya deadpan
            pc "Good lord, she's a lawyer again."
            show pitaya smile
            pc "Okay, go on. Cross examine me."
            jump pc_evidence
        "No?": 
            mt  "Well then, we should move on."
            jump interrogate
label pc_evidence:
    menu:
        mr "What evidence do I present?"
        "Brass knuckles":
            mr "Do you still wear Fuschia Breeze No.9?"
            show pitaya smile
            pc "What sort of question is that? Of course I do!"
            pc "It was a gift from you, after all."
            mr "Cool, cool. Do you know anyone who uses brass knuckles?"
            show pitaya curious
            pc "Brass knuckles...?"
            pc "Can't say for sure, but I heard Dew takes self-defense."
            pc "That surprised me, I mean, she's got the strength of a hundred men, what would she be trying to defend herself against?"
            mr "And you don't use brass knuckles?"
            show pitaya smile
            pc "Nah, haven't beaten anyone up since we graduated."
            show pitaya default
            pc "And besides, I liked the feeling of my oppenent's skull crushing beneath my fist."
            mt  "..."
            mr "..."
            pc "..."
            show pitaya deadpan
            pc "Too dark?"
            mt  "Pitaya, this is why people always think you're the murderer."
            show pitaya nervous
            pc "F-fair enough."
            jump pc_evidence
        "Broken picture":
            mr "Can I see your knuckles?"
            show pitaya deadpan
            pc "...Weird, but okay."
            mr "..."
            show pitaya smile
            mr "Okay, all done."
            pc "Great. Now, {w}"
            show pitaya nervous
            extend "WHAT THE HECK WAS THAT ALL ABOUT?!" with hpunch
            show pitaya curious
            mr "There was a broken picture in Honey's room, so I was checking to see if you broke it."
            mr "But your knuckles are clean, so, no worries."
            mr "Don't punch glass by the way, it's dangerous."
            show pitaya deadpan
            pc "Says the guy who ate an entire necklace of it."
            mr "Will you guys please let me forget that?"
            jump pc_evidence
        "Pillow":
            show pitaya curious
            mt  "...Mozzy, please don't tell me you actually put the pillow in as evidence."
            mr "It had feathers poking out of it like the hat!"
            mt  "...They're different colours?"
            mr "...Oh. They looked the same in the room."
            pc "Are those the feather pillows?"
            mr "Oh yeah, you have them in your room too, right?"
            show pitaya deadpan
            pc "I guess? I mean, sure, they're meant to be there, but I don't use them."
            show pitaya nervous
            pc "They're {i}too{/i} soft to be comfortable, if you get what I mean."
            jump pc_evidence
        "Pitaya's Testimony":
            mr "Why were you looking at the game collection?"
            show pitaya smile
            pc "What do you mean? I was bored, that's all."
            mr "That's the thing."
            mr "You don't like playing videogames. Not on your own, anyways."
            show pitaya surprise
            pc "!"
            mt  "That's right..."
            mt  "You only play if someone asks you to play with them, never on your own."
            mr "Yeah! So, my question to you, Mr Crim..."
            mr "...is why were  looking at Mr Strawberry's game collection on your own?"
            if failed_gaydar:
                mr "Could it be...that you are lying about your alibi?"
                pc "..."
                show pitaya nervous
                pc "Th-that's it?"
                mr "...Huh?"
                show pitaya smile
                pc "Man, I was worried...you were so confident too."
                mr "W-did I get it wrong?"
                show pitaya default
                pc "Nothing to worry about man, nothing to worry about!"
                show pitaya smile
                pc "I swear, on our friendship, my alibi is true."
                mr "Then...why were you looking through his videogames?"
                show pitaya embarrassed
                mr_thought "For some reason, Pitaya blushes and looks away."
                mt  "I think that is a question you should ask another time."
                jump pc_evidence
            else:
                if successful_gaydar:
                    mr "Could it be...that you were looking for someone else?"
                    pc "..."
                    show pitaya nervous
                    pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                    mr "NOT WHAT I MEANT!"
                    show pitaya surprise
                    mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                    mr "Someone like-"
                    mr "..."
                    mr "!"
                    mr "Wait, Pitaya-"
                    mr "Were you looking through the games...for me?"
                    show pitaya damage
                    pc "Gh-?!"
                    hide pitaya damage
                    with dissolve
                    with hpunch
                    mr "Y-yikes!"
                    mr_thought "Did he just fall to the floor?"
                    show pitaya embarrassed
                    with dissolve
                    pc "Y-yeah. Yeah, I was."
                    show pitaya smile
                    pc "That was...wow. That was impressive."
                    show pitaya nervous
                    pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                    show pitaya smile
                    pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                    show pitaya nervous
                    pc "So, yeah. Here I am. And for the record..."
                    show pitaya smile
                    pc "Playing those lawyer games with you are always fun. You're great at doing the voices!"
                    mr "Pitaya..."
                    mt  "As much as I don't want to interrupt this adorable moment..."
                    show pitaya surprise
                    mt  "The twins are glaring at you two. I think you need to start wrapping up."
                    mr "Dangit!"
                    pc "O-okay!"
                else:
                    menu:
                        mr "Could it be..."
                        "That you are lying about your alibi?":
                            $ failed_gaydar = True
                            pc "..."
                            show pitaya nervous
                            pc "Th-that's it?"
                            mr "...Huh?"
                            show pitaya smile
                            pc "Man, I was worried...you were so confident too."
                            mr "W-did I get it wrong?"
                            show pitaya default
                            pc "Nothing to worry about man, nothing to worry about!"
                            show pitaya smile
                            pc "I swear, on our friendship, my alibi is true."
                            mr "Then...why were you looking through his videogames?"
                            show pitaya embarrassed
                            mr_thought "For some reason, Pitaya blushes and looks away."
                            mt  "I think that is a question you should ask another time."
                            jump pc_evidence
                        "That you were looking for someone else?":
                            $ successful_gaydar = True
                            pc "..."
                            show pitaya nervous
                            pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                            mr "NOT WHAT I MEANT!"
                            show pitaya surprise
                            mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                            mr "Someone like-"
                            mr "..."
                            mr "!"
                            mr "Wait, Pitaya-"
                            mr "Were you looking through the games...for me?"
                            show pitaya damage
                            pc "Gh-?!"
                            hide pitaya damage
                            with dissolve
                            with hpunch
                            mr "Y-yikes!"
                            mr_thought "Did he just fall to the floor?"
                            show pitaya embarrassed
                            with dissolve
                            pc "Y-yeah. Yeah, I was."
                            show pitaya smile
                            pc "That was...wow. That was impressive."
                            show pitaya nervous
                            pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                            show pitaya smile
                            pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                            show pitaya nervous
                            pc "So, yeah. Here I am. And for the record..."
                            show pitaya smile
                            pc "Playing those lawyer games with you are always fun. You're great at doing the voices!"
                            mr "Pitaya..."
                            mt  "As much as I don't want to interrupt this adorable moment..."
                            show pitaya surprise
                            mt  "The twins are glaring at you two. I think you need to start wrapping up."
                            mr "Dangit!"
                            pc "O-okay!"
                            jump pc_evidence
        "Nevermind":
            show pitaya smile
            mr "I don't know what I was going to say."
            mt  "Then let's move on."
    
    jump interrogate

label int_honey:
    $ hd_int = True
    show honey smile
    hd "Hm? Can I help you?"
    mr "Ms Dew, we know that it was your necklace that was stolen, but can we still ask for your version of the events?"
    hd "My, my! You're talking so professionally! Mira taught you well."
    show honey surprise
    mt "Mozzy worked as a detective before meeting me."
    hd "...Oh. That's...a surprise."
    mr_thought "Is it?"
    show honey default
    int_box "INTERROGATE: Honey Dew"
    label hd_ask:
        menu:
            mr "What to ask...?"        
            "Testimony, please":
                show honey smile
                hd "Why, of course."
                hd "I showed everyone the Melon Baller during lunch. It is quite a beautiful necklace, and I got it for quite the steal!"
                show honey default
                hd "After lunch, I put it back on the mannequin in my room."
                show honey smile
                hd "You know, Mira, I'm glad Stirling gave the two of us permanent rooms in his house. Saves the hassle of packing unnecessary luggage!"
                hd "But anyways! I then went to the garden, and I spent about two hours reading my book."
                show honey surprise
                hd "Then I went back through the living room back to my room when I noticed that the Melon Baller wasn't on the mannequin."
                show honey sadly
                hd "I thought perhaps I put it somewhere else, so I searched through my room, but it still wasn't anywhere! My apologies for the mess, by the way, it must have been hard to investigate with everything thrown about. "
                show honey default
                hd "I ran back to the living room to let everyone else know of the theft, and..."
                show honey smile 
                hd "Now you're here, Mira."
                mr_thought "Did I just get ignored?"
                jump hd_ask
            "Alibi?":
                show honey grumpy
                hd "My alibi? Why do I need an alibi, it's my necklace that got stolen!"
                hd "You don't think I'm that much of an attention seeker, do you?"
                jump hd_ask
            "That's all":
                show honey default
                mr "Right! Thank you for your help, Ms Dew!"
    menu: 
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "But be careful. Honey has more bite than I do."
            show honey smile
            hd "Yes, I do."
            jump hd_evidence
        "No?":
            mt  "Well then, we should move on."
            jump interrogate
label hd_evidence:
    menu:
        mr "What evidence do I present?"
        "Hat":
            $ hat = True
            hd "Hm? Where did that come from?"
            mr "On the mannequin, where you said you kept the Melon Baller."
            mt  "Why is it named that anyways?"
            show honey surprise
            hd "I'm not sure. It was labelled that way when I bought it."
            show honey default
            hd "In any case, what do you want to know about the hat?"
            mr "Do you wear it often?"
            show honey smile
            hd "Of course! It's such a precious item, and I love it so much!"
            hd "It means so much to me, and it looks fabulous!"
            mt  "...I'm glad, Honey."
            mr "Cool!"
            show honey surprise
            mr "So where did you get such a cheap hat that looks so good?"
            mt "Ng-?!"
            hd "What?"
            mr "There's a feather missing from the hat, and I can see a glue strip here. But it also looks like it would be a really good quality hat."
            mr "My question is where did you get such a cheap hat?"
            mt  "Mozzy, the truth is that I-"
            show honey damage
            hd "Oh, YOU WANNA FIGHT, BOY?! YOU WANT TO FIGHT ME?!" with hpunch
            mt  "Aaand here we go again. Oh boy."
            hd "MIRA BOUGHT THAT FOR ME, OKAY?! YOU THINK IT'S CHEAP BEING A UNIVERSITY STUDENT?! STIRLING MAY BE A NEPO BABY, AND MY PARENTS MAY BE PRETTY WELL OFF, BUT MIRA WAS DOING THE BEST SHE COULD TO GET HER LAW DEGREE!"
            if gem:
                mr "Didn't we do this before?!"
            hd "The fact stands that despite ALL of that, she bought that hat as a gift for ME! ME! She got the best hat she could find within her budget, despite all her tight schedules, despite all her student loans! Got it? GOT IT?!"
            mt  "Yes, yes, we get it, Honey! Please, calm down!"
            hd "..."
            show honey smile
            hd "Oh, of course! I'm so sorry. Let's forget this, shall we?"
            jump hd_evidence
        "The twins' testimony":
            if twin_testimony:
                mr "The twins were also in the garden. Did you see them?"
                show honey surprise
                hd "They were? I'm afraid I didn't notice."
                show honey default
                hd "Though, I was reading a rather interesting book. Would you like to read it?"
                mr "...{i}Bejewelled Jaws{/i} by Constance Dew?"
                show honey smile
                hd "My sister wrote it. She's a botanist, you see. She specializes in carnivorous plants."
                mt  "Yes, I remember that."
                mt  "I didn't know Sun's name was actually Constance."
                show honey grumpy
                hd "Yes, well, our parents weren't the best at naming us. There's a reason I changed my name."
                mr "...Cool."
            else:
                show honey surprise
                hd "Oh, the heirs to the Pale family? What about them?"
                show honey smile
                mr "...That is a very good question."
                mt  "Mozzy, remember to get the testimony first before using it as evidence."
            jump hd_evidence
        "Mira plushie":
            $ honey_doll = True
            mr "Where did you get this?"
            mt  "Ng-!"
            show honey smile
            hd "Oh, that? I commissioned it myself!"
            hd "I can't see you these days because of how busy our schedules are! So I commissioned a plushie of you that I can talk to when I'm not with you!"
            mr "Ms Dew, have you considered maybe giving her a phone call like a normal person?"
            show honey surprise
            hd "But that's boring!"
            mt  "Can we please stop talking about this?!"
            jump hd_evidence
        "Gem":
            $ gem = True
            mr "What can you tell us about this gem?"
            show honey default
            hd "Ah, this must be from the Melon Baller. Where did you find it?"
            mr "On the bed. It's really neat, by the way. Why's that?"
            show honey smile
            hd "I like keeping my bed neat. And well, since it's so neat, I saw no reason to look through it as I'd be able to see if there's anything underneath anyways."
            menu: 
                mr_thought "Should I ask her why there's glue on this?"
                "Yes":
                    show honey surprise
                    hd "What."
                    mr "I was just curious, since you said you got this for a steal."
                    mr "Did you get scammed, by any chance?"
                    show honey grumpy
                    hd "I. Don't. Know. What. You're. Talking. About."
                    mr "I mean, getting it for a steal implies that you got a expensive thing for cheap."
                    mr "But the glue here suggests otherwise."
                    mt  "Mozzy, you really shouldn't-"
                    mr "So I was just wondering if you got scammed or if you were lying about how valuable it is."
                    mt  "Mozzy, I think you need to stop-"
                    show honey damage
                    hd "CURSE YOU!" with hpunch
                    mr "Gah!?"
                    hd "FIRST, you DARE interrupt my time with Mira. THEN, you ask for my alibi even though I'M THE VICTIM. And NOW, YOU JUDGE ME FOR BUYING CHEAP JEWELLERY?!"
                    if hat:
                        mr "Didn't we do this before?!"
                    mt  "Honey, please, calm down-"
                    hd "WHO CARES?! WHO CARES IF I BUY CHEAP JEWELLERY?! IT DOES ITS JOB SO LONG AS IT LOOKS PRETTY, NO?! WHO ARE YOU TO JUDGE ME?!"
                    hd "I HAVE BETTER THINGS TO SPEND MY MONEY ON THAN RIDICULOUSLY EXPENSIVE JEWELLERY."
                    mt  "Honey-"
                    hd "You know what? FINE!"
                    extend " I SAID IT WAS VALUABLE SO THOSE BRATS WOULDN'T MAKE FUN OF ME! OKAY?! SO SHUT THAT STUPID TRAP OF YOURS AND-" with hpunch
                    mt  "Honey Dew, calm down! Now!"
                    hd "..."
                    show honey smile
                    hd "Ah, sorry. My temper went out of hand there, didn't it?"
                    hd "This is embarrassing. I apologize."
                    show honey default
                    hd "Shall we move on?"
                    mt  "..."
                    mt  "Honey, we're going to talk about this later."
                    show honey smile
                    hd "Hm? Oh. Alright."
                    jump hd_evidence
                "No":
                    jump hd_evidence
        "Nevermind":
            mr "I don't know what I was going to say."
            mt  "Then let's move on."
        
    jump interrogate

label int_twins:
    $ twin_int = True
    show jazz aloof at left
    show smith disgust at right
    jp "What do you want?"
    mt  "Just a routine inspection, nothing more. We need all the information we can get if we want to solve this case, so would you be willing to cooperate?"
    show jazz guilty
    show smith guilty
    jp "..."
    sp "..."
    show smith disgust
    sp "Does...{i}he{/i} have to be here too?"
    mt  "Well, two heads are better than one."
    show jazz disgust
    jp "But he's so...blond. I don't see what help he could be."
    mr_thought "Aren't you guys also blond?"
    mt  "Jazz, what did I say about saying stuff like that?"
    show jazz guilty
    jp "...If you don't have anything nice to say, don't say anything at all."
    mt  "That's right."
    mt  "I know that you insult those close to you as a love language, but you do need to be mindful of what is banter and what is actually hurtful."
    mt  "That applies to you too, Smith. Do you understand?"
    show smith guilty
    sp "...Yeah."
    mt  "Great. Let's begin."
    show jazz default
    show smith default
    int_box "INTERROGATE: the Twins"
    label twin_ask:
        menu:
            mr "What to ask...?"
            "Testimony, please?":
                $ twin_testimony = True
                show jazz smug
                jp "Surely you don't think we were the ones who stole that tacky necklace."
                show smith smug
                sp "I mean, seriously, who wears a jewel THAT big?"
                mr_thought "After hearing that insults are their love language, I genuinely can't tell if they hate Honey or not."
                show jazz aloof
                jp "I personally wouldn't steal something like that, so you better go find someone with horrible taste."
                sp "Hey, maybe this \"detective\" stole it! He certainly fits the bill for horrible taste!"
                mr "Hey! I don't have horrible taste!"
                jump twin_ask
            "What is your alibi?":
                show jazz disgust
                show smith disgust
                jp "Seriously? You still think we did it? Ugh."
                show jazz aloof
                jp "But whatever. I was with Smith the whole time. I never even went near Dew's room."
                show smith smug
                sp "I can say the same...for obvious reasons." 
                sp "We were in the kitchen and the garden since lunch."
                show smith aloof
                sp "Besides, that watermelon scent is too strong for us. What reason would we have to go there?"
                show jazz smug
                jp "Is that all, you cretin?"
                jump twin_ask
            "That's all":
                show jazz aloof
                show smith aloof
                mr "Okay...thanks, guys."
                mr_thought "I guess."
    menu:
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "Leave no stone of their testimony unturned and unveil the truth for all to see!"
            show jazz disgust
            jp "Can we make fun of her for that?"
            show smith damage
            sp "Are you insane!? No!"
            show jazz aloof
            show smith smug
            jump twin_evidence
        "No?": 
            mt  "Well then, we should move on."
            jump interrogate
label twin_evidence:
    menu:
        mr "What evidence do I present?"
        "Stirling's earring":
            mr "Do either of you guys wear earrings?"
            show smith aloof
            sp "No."
            mr "..."
            mr "Does anyone else wear earrings?"
            show jazz disgust
            jp "Yeah, that punk loser named after a fruit does. So does Stirling."
            show smith smug
            sp "And he wonders why people mistake him for a her."
            jump twin_evidence
        "Pitaya's testimony":
            if pc_testimony:
                mr "Are you sure you were in the kitchen the whole time?"
                show jazz aloof
                jp "Didn't we literally say that we were also in the garden too?"
                mr "No! I mean, I have evidence that you went other places too!"
                mr "Mr Crim told us that he was in the living room, and at one point, you two walked in from the hallway."
                show jazz disgust
                show smith shock
                mr "The hallway...where the rooms are!"
                sp "What?! No way, we didn't see him-"
                show jazz angry
                jp "Shut up!"
                mt  "Too late."
                show jazz shock
                jp "M-Mira?"
                mt  "I'm sorry, I'm aware that I'm being a bit harsh on you. But I do have to do my job."
                mr "And it seems you two just admitted that you went to the living room!"
                show jazz nervous
                jp "W-you're forgetting something! We may have gone to the living room, but we didn't see that punk loser anywhere! "
                show smith nervous
                sp "Yeah! He's lying about seeing us come from the hallway!"
                mt  "That can also be explained."
                mt  "Pitaya was looking at the videogame collection."
                show jazz smug
                show smith smug
                jp "Aha! More proof! He hates videogames!"
                mt  "Indeed he does. I cannot explain why he was looking through the collection without speculation, but I do have proof that he was there. "
                mt  "Tell me, when did Pitaya arrive here?"
                show smith aloof
                sp "This morning. Why?"
                mt  "That's what I thought."
                mt  "You see, he mentioned a certain lawyer game. I know for a fact that the game he was referring to was only bought after his last visit to Stirling." 
                mt  "He wouldn't have had time to look through it this morning as he only just arrived. So the only way he could have known that Stirling bought that game..."
                show jazz shock
                show smith shock
                mr "...Is if his alibi is true!"
                mt  "Precisely. And if he was looking through the collection, he would probably be down on the ground, and anyone walking in wouldn't see him because he was covered by the couch."
                mr "But if you're behind the couch like this..."
                pc "What? Mozzy, what are you-"
                mr "You can still see the door to the hallway!"
                mr "What do you say to that?"
                show jazz damage with hpunch
                show smith damage with hpunch
                jp "Argh!"
                sp "Impossible...!"
                show jazz angry
                jp "You're telling us..."
                show smith angry
                sp "That you figured all of that out..."
                "Jazz and Smith" "Just by one man's word?!" with hpunch
                mr "That's Mira for you!"
                mt  "Well, to be honest, you also slipped up when you mentioned that the watermelon scent would be too strong for you."
                show jazz damage
                jp "...This is your fault."
                show smith damage with hpunch
                sp "My fault?! Why is it my fault?!"
                jp "You're the one that slipped up! Now they know that we were in that diva's room!"
                mt  "I mean, we didn't quite know that yet. Thank you for the confirmation."
                show jazz guilty
                jp "...Miercoles."
                show smith angry
                sp "See?! You messed up too!"
                show smith smug
                sp "Oh, and also, you said a naughty word!"
                show jazz angry
                jp "Nuh uh! I said \"Wednesday\"!"
                sp "Yuh huh!"
                jp "Nuh uh!"
                mr "Will you two stop so we can carry on our investigation?"
                show smith angry
                "Jazz and Smith" "CALLATE!" with hpunch
                mr "Yikes!"
                mt  "Jazz. Smith."
                show jazz guilty
                show smith guilty
                "Jazz and Smith" "Sorry."
                jump twin_evidence
            else:
                show jazz disgust
                show smith disgust
                mt  "What do you mean, Pitaya's testimony?"
                mr "What? My gut instinct tells me that this is important! And that's why-"
                mr "..."
                mr "I just remembered we haven't actually talked to him yet."
                jump twin_evidence
        "Candles":
            mr "You said you never went near Ms. Dew's room, correct?"
            show jazz aloof
            jp "Yeah...? I think I was pretty clear when I said that."
            mr "If that's the case...then how did you know it smelt like watermelon?"
            show jazz shock
            jp "Ngh!" with hpunch
            show smith damage
            sp "Gh?!" with hpunch
            show jazz nervous
            jp "I-well, isn't it obvious? The smell was so strong that we could smell it from outside the hallway!"
            show smith nervous
            sp "Y-yeah! It is quite strong, after all!"
            mr "Hm"
            mt  "I'll just let you know: the windows, as well as the door, were closed all day."
            show jazz guilty
            jp "Who-who said we smelt watermelons today? We're just talking about what we smelt on...Wednesday! Yeah!"
            mr_thought "... No way for me to disprove that, but that was such an obvious lie that even I can catch it."
            jump twin_evidence
        "Nevermind":
            mr "I don't know what I was going to say."
            mt  "Then, let's move on."

    
    jump interrogate

label int_stirling:
    $ ss_int = True
    show stirling default
    ss "Heyo!"
    mt "Alright, Stirling. You know the rules of an interrogation. Stick to facts as much as you can."
    show stirling smile
    ss "Yeah! Yeah, of course!"
    show stirling nervous
    ss "Hope I can help!"
    mr_thought "Why is he so nervous?"
    mt "..."
    mt "Are you sure you're alright, Stirling?"
    show stirling smile
    ss "What? Oh! Yeah, of course, why wouldn't I be? Let's just start the interrogation now, yeah?"
    int_box "INTERROGATE: Stirling Strawberry"
    label ss_ask:
        menu:
            mr "What to ask...?"
            "Testimony, please":
                show stirling nervous
                ss "I wanted to hold a big party, so I invited most people I know. Honey and Pitaya were the only ones who could show up though. And well, Jazz and Smith live here anyways."
                ss "Honey's been here since Thursday, and Pitaya arrived just this morning."
                ss "I made a strawberry cheesecake, so we had that for lunch. Although, I had a tiramisu, since I kinda need the caffeine diet right now. Pitaya just collapsed on the couch, so he skipped lunch."
                show stirling default
                ss "What else? Oh, Honey showed us the Melon Baller. She sounded really proud of it...I hope we find it soon. "
                show stirling nervous
                ss "Although, I did find it weird how she talked about how valuable it is...she doesn't like buying expensive jewellery. Probably not important though."
                ss "After lunch, I went to my room. I can't quite remember what I was doing, but I'm pretty sure I stayed there until Pitaya came to tell me that the Melon Baller was stolen."
                ss "I asked around, but nobody confessed, so I called you, and now the two of you are here."
                jump ss_ask
            "What is your alibi?":
                show stirling surprise
                ss "I'm sorry, I don't really have an alibi. I was in my room the whole time, but no one can confirm that."
                jump ss_ask
            "Why are you so nervous?":
                show stirling nervous
                ss "Whaat? Nervous? Who, me? Nah, I'm not nervous!"
                mr "..."
                mt "..."
                show stirling awkward
                ss "...Okay, maybe I'm a bit nervous. "
                menu:
                    "Keep pestering him":
                        menu:
                            "Why?":
                                show stirling nervous
                                ss "I don't know."
                                menu:
                                    "Why?":
                                        show stirling awkward
                                        ss "What did I just say? I don't know!"
                                        menu:
                                            "Why?":
                                                show stirling shuteye
                                                ss "I'm not saying anything."
                                                menu:
                                                    "Why?":
                                                        show stirling stress
                                                        ss "I-I just won't! Okay?"
                                                        menu:
                                                            "Why?":
                                                                show stirling sweat
                                                                ss "Ngh-do I have the right to silence?"
                                                                menu:
                                                                    "Why?":
                                                                        show stirling angry
                                                                        ss "I don't want to say it! Alright?"
                                                                        menu:
                                                                            "Why?":
                                                                                show stirling shuteye
                                                                                ss "Stop! Why are you like this?"
                                                                                menu:
                                                                                    "Why?":
                                                                                        show stirling grumpy
                                                                                        ss "Gh-"
                                                                                        menu:
                                                                                            "Why?":
                                                                                                show stirling shuteye
                                                                                                ss "BECAUSE THIS IS THE FIRST TIME I'VE EVER BEEN QUESTIONED AND MIRA'S SO SERIOUS IT'S KINDA SCARY OKAY?!" with hpunch
                                                                                                mt "..."
                                                                                                mr "..."
                                                                                                ss "..."
                                                                                                show stirling awkward
                                                                                                ss "Ack, didn't mean to say that."
                                                                                                mr "Well, that's an easy fix!"
                                                                                                mr "Just stop thinking of Mira as scary!"
                                                                                                ss "..."
                                                                                                mt "..."
                                                                                                show stirling nervous
                                                                                                ss "I don't think it works like that."
                                                                                                mt "Am I really that scary?"
                                                                                                mr "...So I think we should move on."
                                                                                                mt "Why does nobody ever answer that question?"
                                                                                                jump ss_ask
                                                                                            "Move on":
                                                                                                jump ss_ask
                                                                                    "Move on":
                                                                                        jump ss_ask
                                                                            "Move on":
                                                                                jump ss_ask
                                                                    "Move on":
                                                                        jump ss_ask
                                                            "Move on":
                                                                jump ss_ask
                                                    "Move on":
                                                        jump ss_ask
                                            "Move on":
                                                jump ss_ask
                                    "Move on":
                                        jump ss_ask
                            "Move on":
                                jump ss_ask
                    "Move on":
                        jump ss_ask
            "That's all":
                mr "Okay... Thank you, Mr Strawberry."
    menu:
        mt "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt "Well, then, go right ahead."
            mt "Dig out every hole in his statement, and may his tower crumble under your scrutinisation!"
            show stirling smile
            ss "Slay, queen!"
            jump ss_evidence
        "No?":
            mt "Well then, let's move on."
            jump interrogate
label ss_evidence:
    menu:
        mr "What evidence do I present?"
        "Stirling's earring":
            show stirling surprise
            ss "!"
            show stirling default
            ss "Where did you find that? I've been looking for it everywhere!"
            mr "...On the floor of Ms Dew's room."
            show stirling surprise
            ss "Huh? That doesn't make any - oh! I remember now!"
            show stirling nervous
            ss "I was cleaning Honey's room before she arrived - it must have fallen off then."
            show stirling smile
            ss "Well, in any case, thanks for finding it!"
            jump ss_evidence
        "Mira's plushie":
            show stirling surprise
            ss "I didn't know you had merch, Mira."
            mt "...I don't."
            show stirling awkward
            ss "...Oh. Then what's this?"
            if honey_doll:
                mr "Apparently Ms Dew commissioned it."
                show stirling default
                ss "Oh, yeah, it looks like she commissioned Enoki for it."
                mr "Who?"
                show stirling smile
                ss "Oh, she's the costume designer of Fruta Cabaret. She makes dolls as well."
                mr_thought "That answers nothing!"
                mt "Stirling, Mozzy doesn't know what Fruta Cabaret is."
                show stirling surprise
                ss "Oh! That's right. Fruta Cabaret is my theatre company. "
                show stirling default
                ss "Our production of Romeo and Juliet is on two months from now! Will you come?"
                menu:
                    "Sure?":
                        show stirling smile
                        ss "Great! Hope to see you there!"
                        mr "Are you playing Romeo?"
                        show stirling nervous
                        ss "Ah, no... I haven't really had many big roles. I guess I'm not cut out for it yet."
                        mt "Really? I always thought you were rather good."
                        show stirling smile
                        ss "Aw, thanks Mira!"
                        show stirling nervous
                        ss "Although, I don't think I would have wanted to be Romeo anyways."
                        show stirling sweat
                        ss "Hm. Or maybe I'm just having too much fun as Benvolio."
                        show stirling default
                        ss "Well, in any case, glad you're coming!"
                        jump ss_evidence
                    "Not interested":
                        show stirling damage 1 with hpunch
                        show stirling damage 2
                        ss "Gah!"
                        mr_thought "Why'd you react like you just got punched?! I didn't even move!"
                        mt "Oh god..."
                        mt "Here."
                        mr_thought "She hands him a handkerchief."
                        ss "Oh, Mira, I can't, I'd get so much blood on it."
                        mt "I'm a woman and a criminal lawyer, I know how to get blood out. Just stop bleeding on your floor."
                        ss "Thanks Mira, you're the best."
                        jump ss_evidence
            else:
                mt "I wish I knew."
                ss "...It's kinda cute. Maybe you should start selling merch-"
                mt "I'm a lawyer. Why would I want merch?"
                show stirling nervous
                ss "I mean, have you seen your tags on the internet-?"
                mt "NO AND I HAVE NO PLANS WHATSOEVER TO EVER CHECK."
                show stirling stress
                ss "O-oh, yeah, fair enough, Honey would murder half the community if she ever saw what they post-"
                mt "NOPE, WE'RE MOVING ON!"
                mr "I wonder if I have any..."
                mt "SHUSH!"
                jump ss_evidence
        "Mira's picture" :
            show stirling default
            ss "Oh! That's the picture I took!"
            mt "...Stirling, don't tell me that you brought a camera into a trial."
            show stirling smile
            ss "I mean, it wasn't murder, so it should be alright, right?"
            mt "The rule doesn't just apply to murder cases, it's for all cases!"
            show stirling surprise
            ss "...Whoops."
            show stirling nervous
            ss "Um. No one has to know?"
            mt "...Fine. It's a nice picture anyways."
            jump ss_evidence
        "Mannequin":
            show stirling default
            ss "Oh, that thing? Enoki was giving away some of her old mannequins, so I got one for Honey's room so she can put her hat on it when she visits."
            mr "...Who's Enoki again?"
            show stirling smile
            ss "The costume designer for my theatre troupe."
            jump ss_evidence
        "Nevermind":
            show stirling default
            mr "I don't know what I was going to say."
            mt "Then let's move on."
            jump interrogate

label interrogate:
    hide pitaya
    hide honey
    hide stirling
    hide jazz
    hide smith
    menu:
        mr "Who should I interrogate?"
        "Pitaya":
            jump int_pitaya
        "Honey Dew":
            jump int_honey
        "The Twins":
            jump int_twins
        "Stirling":
            jump int_stirling
        "Mira" if pc_int and ss_int and hd_int and twin_int:
            jump int_mira
        "That's all":
            jump continue_story3

label int_mira:
    show mira surprise
    mt  "Me? Why do you want to interrogate me? I wasn't here for the incident."
    mr "I know...listen, Mira-"
    mr "..."
    mr "Can I talk to you in private?"
    mt "..."
    show mira default
    mt "Alright."
    mr_thought "We moved as far as we could from the rest of the party."
    mt "What do you need?"
    mr "I just wanted to know more about our suspects."
    show mira hide
    mt "..."
    mt "I see. I'll do my best."
    with dissolve
    show mira smile
    int_box "INTERROGATE: Mira Tisu"
    label mira_ask:
        menu:
            mt "Who do you need me to talk about?"
            "Honey Dew":
                mr "How well do you know Ms Dew?"
                show mira default
                mt "...Is that how you start all interrogations?"
                mt "No, 'Hey, Hello, How are you?'"
                mr "This is very important to the case, Ms Tisu!"
                show mira default
                mt "Very well, I've known her since uni, she was a film acting major while I took law. We were flatmates with Stirling as well."
                show mira smile
                mt "Funnily enough the law classes and the film acting classes were right next to each other. "
                mr "I see...How about her personality?"
                show mira surprise
                mt "Well, she always did have a tendency to start a little drama, a fake stolen pencil here and there but it was always for a good reason. "
                show mira default
                mt "...Well in her eyes anyway."
                mt "She is also really kind and loyal towards her friends."
                show mira surprise
                mt "...Maybe not towards outsiders though."
                label ask_about_hd:
                    show mira default
                    menu:
                        mt "Anything else?"
                        "Ask about starting drama":
                            mr "You mentioned starting drama, can you elaborate?"
                            mt "Honey is known to blame someone for something they didn't do."
                            mt "It's mostly people who wrong her or our old group in any way."
                            show mira serious
                            mt "I swear she means well, but her 'end justifies the means' mindset is rather concerning sometimes."
                            mr "I see..."
                            mr_thought "Seems like something I should remember..."
                            jump ask_about_hd
                        "Ask about her loyalty":
                            $ hd_hospital = True
                            mr "How can you prove that she is as loyal as you say she is?"
                            mt "Well...I can't prove it because it's more of a feeling."
                            show mira smile
                            mt "She and Stirling were both there when I got stabbed once-"
                            mr "Woah can we cycle back to the stabbing?!"
                            show mira default
                            mt "-I woke up in the hospital with hysterical crying from..."
                            show mira surprise
                            mt "...Stirling, surprisingly. Honey never cries aloud anyways-"
                            mr "So...are we ignoring the stabbed comment or...?"
                            jump ask_about_hd
                        "Ask about the hospital" if hd_hospital:
                            mr "Okay..."
                            mr "CAN WE NOW CIRCLE BACK TO THE STABBING?!" with hpunch
                            mt "Fine, just because you asked so nicely."
                            show mira hide
                            mt "..."
                            mt "...I got stabbed."
                            mr "...That's it?!"
                            show mira default
                            mt "I don't remember why I got stabbed, I was just...stabbed."
                            mr "And you don't know who did it?"
                            mt "I..."
                            show mira damage
                            mt "Gh-!" with hpunch
                            mr "M-Mira? Are you okay?"
                            mt "I-no, I don't know. Please...{w}"
                            show mira sadly
                            extend "don't ask me about this again."
                            mr "That's enough then..."
                            jump ask_about_hd
                        "No":
                            jump mira_ask
            "Stirling Strawberry":
                mr "How well do you know Mr Strawberry?"
                show mira smile
                mt "Around the same time as I have known Honey. We went to university together. He took a musical theatre degree. In fact, we were all flatmates."
                show mira surprise
                mt "It was a bit strange how the law classes were closer to the film acting classes than the musical theatre classes were."
                mr "Okay...and his personality?"
                show mira smile
                mt "I know he acts a bit childish sometimes, but he is a responsible person. In fact, he's been taking care of the twins ever since their parents died."
                show mira sadly
                mt "To take care of two young children even while he suffered the same tragedy...his mental strength really is something."
                show mira smile
                mt "Ah, and he's incredibly loyal as well! It's quite easy to tell, he wears his heart on his sleeve."
                label ask_about_ss:
                    menu:
                        mt "Anything else?"
                        "Ask about his loyalty":
                            $ ss_hospital = True
                            show mira smile
                            mt "There was a time during our last years of university when I suffered from major blood loss."
                            mt "He and Honey were both there when I woke up at the hospital. I could already tell that he had been crying heavily, but somehow he managed to cry even more when I woke up."
                            show mira sadly
                            mt "I felt terrible for making them worry like that, but it was rather nice to see how much they cared. "
                            mt "That's something I haven't had in a while."
                            mr "Why were you losing blood though?"
                            show mira default
                            mt "Oh. I was stabbed."
                            mr "WHAT?!" with hpunch
                            mt "In the neck."
                            mr "THAT'S EVEN WORSE!!!"
                            show mira surprise
                            mt "Um...I don't quite remember how though, so I ask that you don't ask any further."
                            jump ask_about_ss
                        "Ask about the tragedy":
                            show mira sadly
                            mt "Ahh...that's a rather sensitive topic. I don't think I should talk about it."
                            mt "But just so you can tell how severe it was...there's a reason why Stirling is the one taking care of the twins now."
                            mr "...Oh."
                            show mira default
                            mt "Yeah. I suggest not bringing it up anytime soon."
                            jump ask_about_ss
                        "Ask about the hospital" if ss_hospital:
                            mr "Okay..."
                            mr "CAN WE NOW CIRCLE BACK TO THE STABBING?!" with hpunch
                            mt "Fine, just because you asked so nicely."
                            show mira hide
                            mt "..."
                            mt "...I got stabbed."
                            mr "...That's it?!"
                            show mira default
                            mt "I don't remember why I got stabbed, I was just...stabbed."
                            mr "And you don't know who did it?"
                            mt "I..."
                            show mira damage
                            mt "Gh-!" with hpunch
                            mr "M-Mira? Are you okay?"
                            mt "I-no, I don't know. Please...{w}"
                            show mira sadly
                            extend "don't ask me about this again."
                            mr "That's enough then..."
                            jump ask_about_ss
                        "No":
                            jump mira_ask
            "The Pale Twins":
                mr "And how about those gremlins?"
                show mira surprise
                mt "...You mean the twins?"
                mr "That's what I said."
                mt "They've been living with Stirling for around six years now ever since their parents passed away."
                show mira default
                mt "You'll have noticed that they insult people rather frequently. In fact, the only people I haven't seem them insult are each other and myself. Don't take it to heart though, they don't always mean it."
                mt "And yes, while they do insult Stirling on a daily basis, they do care for him. They actually care for most people around them. You'll simply never catch them dead admitting it."
                show mira serious
                mt "I hope they grow to be kinder. It's not exactly a good thing to act like they do."
                label ask_about_twins:
                    show mira default
                    menu:
                        mt "Anything else?"
                        "Ask about their insults":
                            show mira smile
                            mt "They're very creative with them. They've got quite the brilliant minds, if only they'd use them in a different context..."
                            show mira surprise
                            mt "I've seen them curse someone out in Spanish. Or was it French? I'm afraid I only know English and Italian, so I don't know for sure."
                            mt "I believe the rough translation of an insult they gave a bigot is \"I see they have succeeded in translation devices for pigs\"."
                            show mira smile
                            mt "That one was actually quite fun."
                            jump ask_about_twins
                        "Ask about their parents":
                            show mira serious
                            mt "Ahh...that's a rather sensitive topic. I don't think I should talk about it."
                            mt "But just so you can tell how severe it was...there's a reason why Stirling is the one taking care of the twins now."
                            mr "...Oh."
                            mt "Yeah. I suggest not bringing it up anytime soon. "
                            jump ask_about_twins
                        "No":
                            jump mira_ask
                jump mira_ask
            "Pitaya Crim":
                mr "What about Pitaya?"
                show mira surprise
                mt "Pitaya...? I can't really tell you much about him."
                mt "I mean, Stirling knows him better than I do. They are cousins after all."
                mr "Wait, does that mean STIRLING'S the glimmerous cousin Pitaya always talked about?!"
                show mira default
                mt "Ah, that's right, you two seemed like you knew each other. May I ask how?"
                mr "Oh, we were in high school together. I kept him company in detention whenever he beat someone up."
                show mira serious
                mt "Riiight. Stirling did say that his newly adopted cousin was a bit of a troublemaker." 
                show mira surprise
                mt "Um. If you don't mind me asking, why did he 'beat people up' in your days?"
                mr "I don't know, he never told me. He just said \"Oh, Mozz man, don't worry about those bullies anymore. I'll make sure they'll think twice about crossing us again\"."
                mr "I don't know why he called them bullies, they never bullied me."
                show mira default
                mt "..."
                mt "Hm. Well, I'm sure he always had good intentions. It's why I've never seen him on the stand for theft. It would only benefit himself and not others."
                mr "...So how many of his trials did you defend?"
                show mira surprise
                mt "Um...let's see...six murder cases, eight acts of vandalism, one case of vigilantism, and five charges of fraud."
                mr "He wouldn't do any of those! ...except maybe the vigilantism."
                show mira default
                mt "He never actually did most of those charges. He did use a forged ID, but it was an accident, so the jury acquitted him. "
                mr "He's really got horrible luck, huh?"
                show mira hide
                mt "Tell me about it. You don't understand how much of a scolding I would have given him on his last trial for murder if I hadn't passed out from the stress."
                mr "...Mira, are you okay?"
                show mira serious
                mt "I'm a criminal lawyer in this universe, of course not."
                jump mira_ask
            "Nevermind":
                mr "That's all I need. Thank you, Ms Tisu."
                show mira smile
                mt "Anytime, Mozzy."
                jump interrogate

label continue_story3:
    scene bg living room
    mr "Alright! I've got all the information I need!"
    show mira smile
    mt "And I believe we can name a culprit now."
    hide mira smile
    show honey smile
    hd "Oh, that's wonderful!"
    hide honey smile
    show jazz aloof
    jp "Finally. Took you long enough. "
    hide jazz aloof
    show smith disgust
    sp "I still think you're a dud."
    mr "Hey!"
    hide smith disgust
    show stirling surprise
    ss "Al-already? I knew you were brilliant, Mira, but this is fast even for you!"
    mr_thought "Yeah, actually...I thought Mira would give me some time first. Was this case really so simple for her?"
    hide stirling surprise
    show honey default
    hd "So who is it? Tell me!"
    hide honey default
    show mira smile
    mt "Well, Mozzy? Go ahead."
    mr "Oh, okay..."
    hide mira smile
    mr_thought "Let's look at all the clues and the testimony."
    mr_thought "There's a lot of ways this could have gone, but in this instance..."
    menu:
        mr "The culprit is..."
        "Pitaya":
            jump culprit_pc
        "Honey Dew":
            jump culprit_hd
        "The Twins":
            jump culprit_pale
        "Stirling": 
            jump culprit_ss

label culprit_pc:
    $ pitaya_guilt = True
    show pitaya damage
    pc "Wh-WHAT?!"
    hide pitaya damage
    show mira serious
    mt "..."
    hide mira serious
    show pitaya damage
    mr "If I'm perfectly honest..."
    mr "I don't think you actually did it."
    mr "I mean, you basically confirmed your alibi when you said you saw the twins enter and when you told us about the new lawyer game."
    mr "But I genuinely can't tell who did!"
    mr "So...I'm pointing at you?"
    pc "..."
    show pitaya smile
    pc "Y'know what? I'll take that."
    show pitaya curious
    pc "So what you're saying is that...there is no culprit?"
    mr "I guess? Sorry to disappoint."
    hide pitaya curious
    show honey grumpy
    hd "Absolutely not! I cannot accept this!"
    mr "H-HUH?!"
    hd "Maybe you don't think so, but it's clear that Mira disagrees with you somehow!"
    hide honey grumpy
    show stirling determined
    ss "She's right! "
    show stirling stress
    ss "...Though I also don't think it was Pitaya. Come on, Mira, speak up!"
    hide stirling stress
    show mira default
    mt "..."
    hide mira default
    show jazz angry
    jp "Yeah! Not to mention, we found brass knuckles in her room! Who else would they belong to but that punkish loser named after a fruit?"
    hide jazz angry
    show pitaya angry
    pc "Oh, is that right, miss drama queen? "
    pc "Go right ahead then! Search my bags! I assure you, I'm innocent!"
    hide pitaya angry
    show honey grumpy
    hd "As a matter of fact, I believe I will."
    hide honey grumpy
    show stirling shock
    ss "Honey, WAIT FOR US-!"
    mr "Dang, she's fast!"
    jump wrong_end

label culprit_hd:
    show honey surprise
    hd "I...don't understand."
    mr "Ditto. Neither do I."
    mr "But like the Great Detective always says, once you eliminate the impossible, whatever's left, no matter how absurd, must be the truth! ...Roughly paraphrased."
    hide honey surprise
    show pitaya deadpan
    pc "I swear Mozzy, if you're basing your deductions off the one in your new lawyer game-"
    hide pitaya deadpan
    show honey surprise
    mr "In any case! Let me explain why it couldn't have been anyone else."
    mr "Mr Crim confirmed his alibi when he told us about the twins coming into the living room from the hallway."
    mr "The twins are petty, but they've made their distaste for your necklace pretty clear."
    mr "And Mr Strawberry may not be able to confirm his alibi, but this is his own house. Why on earth would he attempt to steal something here, of all places?"
    mr "And to top it all off..."
    mr "Mira happened to mention that you have a reputation for starting drama, pretending to get things stolen to frame other people."
    hide honey surprise
    show mira smile
    mt "It seems that we reached the same conclusion, Mozzy."
    hide mira smile
    show stirling shock
    ss "You...you knew, Mira?"
    hide stirling shock
    show mira smile
    mt "Stirling, you really should pay more attention to context clues."
    hide mira glad
    show stirling awkward
    ss "Ngh...not my fault I'm socially inept!"
    hide stirling awkward
    show honey surprise
    mr "So my question is not if you did this, but why?"
    hd "..."
    show honey default
    hd "I wanted to see Mira again."
    mr "..."
    mr "Are you kidding me."
    show honey smile
    hd "Mira is a dear friend and a brilliant woman! Of course I wanted to provide a case for her when we met again."
    hide honey smile
    show mira serious
    mt "Honey, you saw me three weeks ago."
    hide mira serious
    show honey surprise
    hd "But that was so long ago! So I pretended to get the Melon Baller stolen, knowing that Stirling would call you for help."
    hd "I planned this when we had more people coming but I didn't think we'd have such a small cast."
    mr "Have I ever told you to be a normal person for one day and just give her a call?"
    show honey smile
    hd "Where's the fun in that?"
    hide honey smile
    show mira serious
    mt "Honey, please. You need to stop doing stuff like this, my hair's turning white because of you people."
    mr "I thought your hair naturally had white streaks?"
    show mira smile
    mt "Anyone can have natural white streaks if they're stressed enough."
    hide mira smile
    show honey smile
    hd "She means yes."
    hide honey smile
    show stirling smile
    ss "Well, glad that's how it happened. I was worried that I might have somehow accidentally stolen it!"
    show jazz disgust at left
    jp "...That makes like no sense."
    show smith smug at right
    sp "Leave him be, hes a blond in spirit."
    mr "Again, you guys are also blond, what are you on about."
    jump good_end

label culprit_pale:
    $ twin_guilt = True
    show jazz damage at left
    show smith angry at right
    jp "You stupid..."
    sp "Putrid..."
    jp "Yammering..."
    sp "Blumbering..."
    "Jazz and Smith" "MEDDLING, NO GOOD," 
    extend " FOOL!!" with hpunch
    hide jazz damage
    hide smith damage
    show mira serious
    mt "..."
    hide mira serious
    show jazz damage at left
    show smith angry at right
    jp "How dare you accuse us?!"
    sp "Under what evidence, huh? I bet this is just a senseless accusation from a stupid FRAUD like you!"
    mr "Well, in case you forgot..."
    mr "You two were trying to hide the fact that you were in Ms Dew's room. In fact, you hid it to the point where you denied ever being in the living room! "
    mr "You could have easily just been in your own rooms if you were innocent, so why did you hide?"
    mr "Not to mention, you seemed rather reluctant to answer our questions. I had to prompt you so much to get more information!"
    mr "Rather suspicious, don't you think?"
    mr "And to top it all off..."
    mr "YOU TWO ARE THE PETTIEST KIDS I HAVE EVER MET!!! I wouldn't be surprised if you stole it just to spite Ms Dew."
    show jazz disgust
    jp "Oh, no, we definitely considered that, just not with the necklace."
    show smith shock
    sp "WHY WOULD YOU ADMIT THAT, YOU IDIOT?!"
    show jazz angry
    jp "WELL CLEARLY THIS ASININE DETECTIVE IS DETERMINED TO PIN IT ON US, MIGHT AS WELL STOP HIDING HOW MUCH WE HATE THAT DIVA!!"
    show smith angry
    sp "ARGH! EVER HEARD OF INNOCENT UNTIL PROVEN GUILTY?! "
    mr_thought "...Wow, they've completely given up on hiding it."
    jp "ACTUALLY, I HAVE!! So, if I may..."
    show jazz disgust
    jp "I swear on my life, Smith didn't steal it, and neither did I!"
    show smith smug
    sp "That's right! Stick that head of yours down the drain and try to find the intelligence that you clearly lost!"
    mr_thought "...Nevermind."
    hide jazz disgust
    hide smith smug
    show honey grumpy
    hd "There is an easier way to confirm their guilt without having this back and forth debate."
    hd "Excuse me for a moment."
    hide honey grumpy
    show stirling shock
    ss "Hey, Honey, wait up!"
    jump wrong_end

label culprit_ss:
    $ stirling_guilt = True
    show stirling shock
    ss "What? Me?"
    hide stirling shock
    show mira serious
    mt "..."
    hide mira serious
    show stirling shock
    mr "Just at a glance, one would assume that you're innocent."
    mr "But I can see further! Your nervous behaviour...sure, it might have been because Mira can be a bit scary sometimes-"
    hide stirling shock
    show honey surprise
    hd "Mira? Really?"
    hide honey surprise
    show stirling shock
    mr "But the thing that really gave you away was your earring!"
    mr "You claimed that you must have left it behind while cleaning the room, but if you did, how come Ms Dew couldn't find it?"
    mr "Because surely being such good friends, if she found it, she would have returned it!"
    show stirling sweat
    ss "...That's a good point. Can't really argue with that."
    hide stirling sweat
    show pitaya damage
    pc "WHAT?!" with hpunch
    show smith disgust at left
    sp "You can definitely argue with that! Why would you steal that necklace anyways?"
    show jazz angry at right
    jp "It's not like it's your style either! And it looked really cheap anyways!"
    hide pitaya damage
    hide smith disgust
    hide jazz angry
    show honey surprise
    hd "..."
    show honey grumpy
    hd "Well, I might as well check, just to make sure."
    jump wrong_end

label wrong_end:
    scene bg end
    mr_thought "Ms Dew charged on in front of us, and the rest of us quickly followed after her."
    mr_thought "Oddly enough, Mira stayed behind, never even saying a word."

    if pitaya_guilt:
        mr_thought "We searched through Pitaya's bags, and we found the Melon Baller stuffed in his makeup bag."
        mr_thought "He denied putting it there, but the evidence is clear."
    
    if twin_guilt:
        mr_thought "We searched through their bags, and we found the Melon Baller stuffed in a game pouch."
        mr_thought "They denied putting it there, but the evidence is clear."

    if stirling_guilt:
        mr_thought "We searched through his room, and we found the Melon Baller stuffed in a pillow."
        mr_thought "He denied putting it there, but the evidence is clear."

    mr_thought "Luckily, Miss Dew was just glad that she got the necklace back, and insisted that we just forget about the incident."
    mr_thought "We stayed at Stirling's place for another week as both Honey and Stirling insisted on getting to know me better...although I think they just wanted more time with Mira."
    mr_thought "Speaking of Mira, I saw her talking with Honey in the garden on the day we found the Melon Baller. She looked really disappointed, but also unsurprised."
    mr_thought "Honey seemed to be apologizing for something, although I couldn't hear what they were saying since I was all the way up in a window."
    mr_thought "I tried asking Mira about it, but she just told me to look back on my case notes if I wanted to know. But no matter how many times I go over them, I can't see anything else."
    mr_thought "And so ends the tale of \"The Disappearance of the Melon Baller\""
    mr_thought "..."
    mr_thought "The name is a work in progress."
    "{b}Fin?{/b}"

    return

label good_end:
    scene bg good end
    mr_thought "Miss Dew apologised for making such a mess, but everyone was quick to forgive her."
    mr_thought "...Okay that's a lie but honestly Pitaya and the twins don't really forgive easily so it's a win!"
    mr_thought "We stayed at Stirling's place for another week as both Honey and Stirling insisted on getting to know me better...although I think they just wanted more time with Mira."
    mr_thought "Oh! Pitaya and I got to play the new game he found in Stirling's collection! He didn't want to play Brekkin though, so I played with the twins. The little gremlins somehow managed to defeat me. I'll get them next time!"
    mr_thought "And so ends the tale of \"The Melon Conspiracy\""
    mr_thought "..."
    mr_thought "Does this even count as a conspiracy?"
    "{b}Fin.{/b}"

    return
