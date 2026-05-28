

define mr = Character("Mozzy")
define mr_thought = Character("Mozzy", what_italic=True)
define mt = Character("Mira")
define pc = Character("Pitaya")
define hd = Character("Honey")
define ss = Character("Stirling")
define jp = Character("Jazz")
define sp = Character("Smith")
default twin_int = False
default ss_int = False
default hd_int = False
default pc_int = False
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
    show mozzy default at left 

    mr "I just don’t get it, Mira!"
    mt "Hm?"
    mr "I mean, I know I’m an ace detective and all, but why are WE on our way to investigate a robbery here?"
    mr "It’s the richest neighbourhood as well! Shouldn’t someone a bit more higher-up take the case?"
    show mira hide
    mt "…"
    show mira default
    mt "This isn’t actually an official case yet."
    mr "…"
    show mozzy shock
    mr "h-hUH?!"
    show mira smile
    mt "A dear friend of mine asked me to help investigate before there is a scandal."
    mt "And, well, you haven’t had a case in a while either, so I decided to bring you along."
    show mira default
    show mozzy default
    mt "Speaking of which, let’s run over how to do investigations and interrogations."
    mt "You’ll notice that I haven’t told you which house we’re heading to."
    mt "Your goal is to try and pull information out of me. Then, when we arrive at our stop, you’ll use the information you received to find the correct house."
    menu:
        mt "Do I interrogate Mira?"
        "Yeah, we need information!":
            jump interrogate_tut
        "No, I feel like I've done this before.":
            jump skip_tut
    
label interrogate_tut:
    show mozzy excited
    mr "Alright!"
    mr "Bring it on!"
    scene bg interrogation
    show mira smile at right
    show mira smile at default
    with move
    "INTERROGATE: Mira Tisu"
    menu: 
        mt "Well, Mozzy? Ask away."
        "What colour is the house?":
            jump house_colour
        "What is the address?": 
            jump house_address
        "Who is the owner of the house?":
            jump house_owner

    label house_colour:
        mt "Well, my dear friend adores the colour pink."
        mt "That’s why the house is a sort of reddish pink colour."
        mt "The roof, however, is covered in black shingles."
        jump question_list

    label house_address:
        show mira default
        mt "That’s a good question."
        show mira smile
        mt "But where’s the fun in just telling you the answer?"
        mr_thought "(Mira, quit trolling me…!)"
        jump question_list
        
label house_owner:
    show mira default
    mt "The owner of the house…? Odd question to ask in this scenario."
    mt "Well, it is none other than my dear friend, Stirling Strawberry."
    mt "But that really doesn’t seem like a question that will help you."
    mr "Huh? O-oh!"
    mr_thought "(Dang…she’s right!)"
    mt "It’s quite alright, but just remember that others aren’t so forgiving as I am when you ask irrelevant questions."
    jump question_list

    label question_list:
        menu:
            mt "Any other questions?"
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
    mr "I'm getting a lot of deja vu. I think I can find the house without any help."
    mt "I will never understand your strange sixth sense."
    mr_thought "(We talked about some of our coworkers for the rest of the bus ride.)"
    jump tutorial_end

label tutorial_end:
    scene bg bus
    show mozzy default at left
    show mira default at right
    mr "Right…I think that’s all the information need."
    mt "Hm, and just in time too."
    mt "This is where we get off."
    mr_thought "Mira and I thanked the bus driver and jumped off the bus."
    scene bg rich street
    with dissolve
    show mozzy default at left
    show mira default at right
    mt "Alright Mozzy, time to put the clues you gathered to good use."
    mt "Can you find the house now?"
    show mozzy excited
    mr "Of course!"
    show mozzy default
    mr "But, uh, Mira…?"
    show mira default #curious, but we don't have the time for that as of now
    mt "?"
    mr "How much time do I have?"
    show mira surprise
    mt "!"
    show mira smile
    mt "That’s what you’re worried about? Don’t worry, take all the time you need. We’re in no hurry."
    show mozzy excited
    mr "Phew! Thanks, Mira!"

#insert HOG here

label continue_story1:
    scene gates
    "{i}One hidden object tutorial later...{/i}"
    show mozzy excited at left
    show mira smile at right
    mr "Okay! Made it!"
    mt "That was quick. Well done."
    mr "Of course! It was a piece of pie for the Great Detective Mozzy Rella!"
    mt "Hm…of course."
    mr "Well, what are we waiting for? Let’s go!"
    show mira surprise
    mt "Mozzy, wait–!"
    show mozzy shock #surprise
    mr "…!"
    mr "The gates…are locked!"
    mt "Of course they are! Stirling kept them locked so that the thief couldn’t get out."
    show mozzy damage
    mr_thought "(Can’t a thief just climb over the gates though?)"
    show mira default
    show mozzy default
    mt "I’ll let Stirling know that we’re here."
    "{i}(insert ringtone){/i}"
    mt "…"
    mt "Hey Stirling. My partner and I are outside your gates. Do you mind letting us in?"
    mt "…"
    mt "Investigative partner, Stirling. I’m not dating anyone at the moment. I still don’t have time for that. Besides, he’s far too young–"
    mr "Hey! I’m only 23!, I can definitely vote….legally."
    mr_thought "Mira simply ignored me."
    show mira hide
    mt "…"
    mt "Stirling Strawberry, you will let us in right this moment or I will tell those cousins of yours that you ate the last cookie."
    show mozzy shock
    mr "Eep!"
    mr_thought "(Mira can be so scary sometimes…)"
    mt "…"
    show mira smile
    mt "Thanks. I’ll see you soon."
    show mira default
    mt "…"
    mt "Sorry, did I scare you?"
    show mozzy excited
    mr "Um…I don’t know what you’re talking about! A great detective is never scared!"
    mr_thought "For some reason, Mira doesn’t seem to believe that."
    mt "…If you insist."
    show mozzy default
    mr "…"
    mt "…"
    mr "Your friend is taking a while."
    mr_thought "Lo and behold, just as I said those words, the gates opened."
    show mozzy damage
    mr "Are you kidding me?"
    show mira smile
    mt "I must say Mozzy, you have impeccable timing at times."
    mr "Let’s…let’s just go in."
    scene garden
    mr_thought "I fixed up my hat, and we walked through the gates."
    mr_thought "There was a really cool garden there. The fences were wrapped in ivy and roses"
    mr_thought "Suddenly, I heard a familiar voice shouting…a lot of things I won’t repeat."
    show pitaya angry
    pc "That’s it, you people deal with this yourself! I’m outta here!"
    mr "Pitaya!"
    show pitaya curious
    pc "…?"
    show pitaya default
    pc "Mozzy! Hey, man!"
    mr_thought "Pitaya Crim, I was close with him during High school and college, acts like a big tough guy but he is really just a sweetheart, volunteering at nursing homes and what-not."
    mr_thought "…Okay, so MAYBE he was on trial for murder like a hundred times, but he’s never actually committed any of them!"
    show pitaya disgust
    pc "Mozzy you’re spacing out again."
    pc "Are you doing that thing where you introduce people in your head completely out of character?"
    mr_thought "Ack. Guilty."
    menu:
        mr_thought "Quick, Mozzy, deflect!"
        "Actually, I'm thinking about koalas.":
            jump koalas
        "No, I'm thinking about you.":
            jump gay

    label gay:
        mr "No, I'm thinking about you."
        show pitaya damage
        pc "W-W-What?!"
        mr_thought "Hehe, that always catches him off guard."
        jump enter_house

    label koalas:
        mr "Actually, I'm thinking about koalas."
        pc "...Koalas?"
        mr "Yeah! Did you know, a koala could frame someone for a crime!"
        pc "How would a koala-"
        mr "Koalas have fingerprints, just like us! So, if a koala commits a crime and leaves its fingerprints everywhere, you'd think a human did it!"
        pc "Wow...so they do teach detectives something."
        mr "Oh, nah, I learnt this one myself."
        pc "...From where?"
        mr "So, there's this social media site called-"
        pc "Nevermind, I got what you're saying."
        jump enter_house

    label enter_house:
        mr "Anyways, time to get a move on people!, no time to waste!"
        pc "oh my gosh you oblivious swiss cheese…"
        mt "…my goodness."

    scene bg stirling home
    pc "Well people, we have our detective and everyone’s favourite lawyer."
    "???" "...He looks like a dud. "
    mr "how dare you!, you…you…gremlin?, sorry you’re just extremely short. "
    "???" "And? We’re literally fourteen."
    "???" "If anything, you’re the short one."
    mr "HEY!!"
    mt "*sigh*"
    mt "Jazz, Smith, meet Mozzy. I met him on one of my cases."
    mt "Mozzy, these are the Pale twins, Jazz and Smith. Jazz is the red one, Smith is green."
    jp "We met her when Stirling introduced his girlfriend to his family."
    sp "Which is just us."
    mt "Bold of you two to assume that Stirling can last a day dating me."
    jp"Fair point."
    sp "Yeah, you deserve better anyways."
    "???" "Hey, I heard that!"
    "Some more exposition later..."
    ss "And I’m Stirling Strawberry, besties with Mira since we met in college ten years ago!"
    mr "I see. "
    mr "…"
    mr "Wait Mira you went to college when you were 10?"
    mt "…How old do you think I am? "
    mr "…twenty, right?"
    mt "I’m thirty-eight."
    mr "Oh."
    #Stirling intro, after everyone else.
    mr "Thank you, good madam!"
    ss "Huh? I–uh–I’m not–"
    mr "Huh? What’s wrong?"
    pc "Oh, man–"
    "Jazz and Smith" "And another one bites the dust!"
    mt "Mozzy…"
    mt "Stirling’s a man."
    mr "GAH!"
    mr "ajkfbldashfircids I am SO sorry!"
    ss "It-it’s fine…it happens a lot…"
    ss "Do I really look that much like a girl…?"
    pc "Yup."
    jp "You do."
    sp "You really look like a girl."
    pc "Hey, YOU can’t say anything! You and your sister look identical!"
    jp "What part of “identical twins” do you not understand…?"
    sp "It’s only fair, I mean, she looked identical to me a few years ago, so now I’m identical to her."
    pc "I know, I know, I was there when you guys announced the change to the family!"
    hd "…"
    hd "I personally don’t think you look like a girl Stirling…but I can see why people think so!"
    ss "Well…I guess that’s a me problem."
    mt "Speaking of problems…I brought Mozzy here to help with yours."
    mr "Please hold your applause, I know I'm glamorous!"
    jp "Is he always like this?"
    mr "Hey, what's that supposed to mean?"

label hidden_object:
    scene bg honey room
    "So, there's nothing in here as of now."
    "this is a placeholder for the actual hidden object game"

label hidden_object:
    scene bg honey room

    label honeysroom:
        call screen honeysroom 
    label Jewelbox:
        mr "This box is really neatly organised."
        mt "Honey has a lot of jewellery, she likes to be able to see all of them and make sure they’re there."
        mr "You’d think a thief would rummage through the jewellery box too."

        
    "anyways, some exposition later, after finding evidence, we move on to the interrogation"

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
    scene bg interrogation
    show pitaya default at default
    pc "Wazzup?"
    jump interrogate

label int_honey:
    $ hd_int = True
    scene bg interrogation
    show honey default at default
    hd "Hm? Can I help you?"
    jump interrogate

label int_twins:
    $ twin_int = True
    scene bg interrogation
    show jazz default at left
    show smith default at right
    jp "What do you want?"
    jump interrogate

label int_stirling:
    $ ss_int = True
    scene bg interrogation
    show stirling default at default
    ss "Heyo!"
    jump interrogate
    #ask

label interrogate:
    if pc_int:
        if ss_int:
            if twin_int:
                if hd_int:
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
                        "Mira":
                            jump int_mira
                        "That's all":
                            jump continue_story2
                else:
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
                        "That's all":
                            jump continue_story2
            else:
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
                    "That's all":
                        jump continue_story2
        else:
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
                "That's all":
                    jump continue_story2
    else:
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
            "That's all":
                jump continue_story2

label int_mira:
    scene bg interrogation
    show mira default
    mt "Me? Why do you want to interrogate me? I wasn't here for the incident."
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
        "Mira":
            jump int_mira
        "That's all":
            jump continue_story2

label continue_story2:
    scene bg dining room
    menu:
        mr "And the culprit is..."
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
    show pitaya guilty
    pc "Wh-WHAT?!"
    jump wrong_end

label culprit_hd:
    show honey guilty
    hd "I...don't understand."
    jump good_end

label culprit_pale:
    $ twin_guilt = True
    show twin guilty
    jp "You brutish..."
    sp "Putrid..."
    jp "Yammering..."
    sp "Blumbering..."
    "Jazz and Pale" "FOOLISH, OBSOLETE, BASTARD!!"
    jump wrong_end

label culprit_ss:
    $ stirling_guilt = True
    show stirling guilty
    pc "What? Me?"
    jump wrong_end

label wrong_end:
    if pitaya_guilt:
        mr_thought "We searched through Pitaya's bags, and we found the Melon Baller stuffed in his makeup bag."
        mr_thought "He denied putting it there, but the evidence is clear."
    
    if twin_guilt:
        mr_thought "We searched through their bags, and we found the Melon Baller stuffed in a game pouch."
        mr_thought"They denied putting it there, but the evidence is clear."

    if stirling_guilt:
        mr_thought "We searched through his room, and we found the Melon Baller stuffed in a pillow."
        mr_thought "He denied putting it there, but the evidence is clear."

    mr_thought "Luckily, Miss Dew was just glad that she got the necklace back, and insisted that we just forget about the incident."
    mr_thought "We stayed at Stirling's place for another week as both Honey and Stirling insisted on getting to know me better...although I think they just wanted more time with Mira."
    mr_thought "And so ends the tale of \"The Disappearance of the Melon Baller\""
    mr_thought "..."
    mr_thought "The name is a work in progress."
    "{b}End?{/b}"

    return

label good_end:
    mr_thought "Miss Dew apologised for making such a mess, but everyone was quick to forgive her."
    mr_thought "...Okay that's a lie but honestly Pitaya and the twins don't really forgive easily so it's a win!"
    mr_thought "And so ends the tale of \"The Melon Conspiracy\""
    mr_thought "..."
    mr_thought "Does this count as a conspiracy?"
    "{b}End.{/b}"

    return
