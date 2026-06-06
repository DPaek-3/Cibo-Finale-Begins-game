

define mr = Character("Mozzy")
define mr_thought = Character("Mozzy", what_italic=True)
define mt = Character("Mira")
define pc = Character("Pitaya")
define hd = Character("Honey")
define ss = Character("Stirling")
define jp = Character("Jazz")
define sp = Character("Smith")
define int_box = Character(None, what_xalign=0.5, what_text_align=0.5)
default twin_int = False
default ss_int = False
default hd_int = False
default pc_int = False
#default pc_testimony = False
#default ss_testimony = False
#default hd_testimony = False
#default twin_testimony = False
#default pc_alibi = False
#default hd_alibi = False
#default ss_alibi = False
#default twin_alibi = False
default successful_gaydar = False
default failed_gaydar = False
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

    mr "I just don't get it, Mira!"
    mt "Hm?"
    mr "I mean, I know I'm an ace detective and all, but why are WE on our way to investigate a robbery here?"
    mr "It's the richest neighbourhood as well! Shouldn't someone a bit more higher-up take the case?"
    show mira hide
    mt "…"
    show mira default
    mt "This isn't actually an official case yet."
    mr "…"
    show mozzy shock
    mr "h-hUH?!"
    show mira smile
    mt "A dear friend of mine asked me to help investigate before there is a scandal."
    mt "And, well, you haven't had a case in a while either, so I decided to bring you along."
    show mira default
    show mozzy default
    mt "Speaking of which, let's run over how to do investigations and interrogations."
    mt "You'll notice that I haven't told you which house we're heading to."
    mt "Your goal is to try and pull information out of me. Then, when we arrive at our stop, you'll use the information you received to find the correct house."
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
    int_box "INTERROGATE: Mira Tisu"
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
        mt "That's why the house is a sort of reddish pink colour."
        mt "The roof, however, is covered in black shingles."
        jump question_list

    label house_address:
        show mira default
        mt "That's a good question."
        show mira smile
        mt "But where's the fun in just telling you the answer?"
        mr_thought "(Mira, quit trolling me…!)"
        jump question_list
        
    label house_owner:
        show mira default
        mt "The owner of the house…? Odd question to ask in this scenario."
        mt "Well, it is none other than my dear friend, Stirling Strawberry."
        mt "But that really doesn't seem like a question that will help you."
        mr "Huh? O-oh!"
        mr_thought "(Dang…she's right!)"
        mt "It's quite alright, but just remember that others aren't so forgiving as I am when you ask irrelevant questions."
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
    mr "Right…I think that's all the information need."
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
    mt "That's what you're worried about? Don't worry, take all the time you need. We're in no hurry."
    show mozzy excited
    mr "Phew! Thanks, Mira!"

#insert HOG tutorial here

label continue_story1:
    scene gates
    "{i}One hidden object tutorial later...{/i}"
    show mozzy excited at left
    show mira smile at right
    mr "Okay! Made it!"
    mt "That was quick. Well done."
    mr "Of course! It was a piece of pie for the Great Detective Mozzy Rella!"
    mt "Hm…of course."
    mr "Well, what are we waiting for? Let's go!"
    show mira surprise
    mt "Mozzy, wait–!"
    show mozzy shock #surprise
    mr "…!"
    mr "The gates…are locked!"
    mt "Of course they are! Stirling kept them locked so that the thief couldn't get out."
    show mozzy damage
    mr_thought "(Can't a thief just climb over the gates though?)"
    show mira default
    show mozzy default
    mt "I'll let Stirling know that we're here."
    "{i}(insert ringtone){/i}"
    mt "…"
    mt "Hey Stirling. My partner and I are outside your gates. Do you mind letting us in?"
    mt "…"
    mt "Investigative partner, Stirling. I'm not dating anyone at the moment. I still don't have time for that. Besides, he's far too young–"
    mr "Hey! I'm only 23!, I can definitely vote….legally."
    mr_thought "Mira simply ignored me."
    show mira hide
    mt "…"
    mt "Stirling Strawberry, you will let us in right this moment or I will tell those cousins of yours that you ate the last cookie."
    show mozzy shock
    mr "Eep!"
    mr_thought "(Mira can be so scary sometimes…)"
    mt "…"
    show mira smile
    mt "Thanks. I'll see you soon."
    show mira default
    mt "…"
    mt "Sorry, did I scare you?"
    show mozzy excited
    mr "Um…I don't know what you're talking about! A great detective is never scared!"
    mr_thought "For some reason, Mira doesn't seem to believe that."
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
    mr "Let's…let's just go in."
    scene garden
    mr_thought "I fixed up my hat, and we walked through the gates."
    mr_thought "There was a really cool garden there. The fences were wrapped in ivy and roses"
    mr_thought "Suddenly, I heard a familiar voice shouting…a lot of things I won't repeat."
    show pitaya angry
    pc "That's it, you people deal with this yourself! I'm outta here!"
    mr "Pitaya!"
    show pitaya curious
    pc "…?"
    show pitaya default
    pc "Mozzy! Hey, man!"
    mr_thought "Pitaya Crim, I was close with him during High school and college, acts like a big tough guy but he is really just a sweetheart, volunteering at nursing homes and what-not."
    mr_thought "…Okay, so MAYBE he was on trial for murder like a hundred times, but he's never actually committed any of them!"
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
    pc "Well people, we have our detective and everyone's favourite lawyer."
    "???" "...He looks like a dud. "
    mr "how dare you!, you…you…gremlin?, sorry you're just extremely short. "
    "???" "And? We're literally fourteen."
    "???" "If anything, you're the short one."
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
    ss "And I'm Stirling Strawberry, besties with Mira since we met in college ten years ago!"
    mr "I see. "
    mr "…"
    mr "Wait Mira you went to college when you were 10?"
    mt "…How old do you think I am? "
    mr "…twenty, right?"
    mt "I'm thirty-eight."
    mr "Oh."
    #Stirling intro, after everyone else.
    mr "Thank you, good madam!"
    ss "Huh? I–uh–I'm not–"
    mr "Huh? What's wrong?"
    pc "Oh, man–"
    "Jazz and Smith" "And another one bites the dust!"
    mt "Mozzy…"
    mt "Stirling's a man."
    mr "GAH!"
    mr "ajkfbldashfircids I am SO sorry!"
    ss "It-it's fine…it happens a lot…"
    ss "Do I really look that much like a girl…?"
    pc "Yup."
    jp "You do."
    sp "You really look like a girl."
    pc "Hey, YOU can't say anything! You and your sister look identical!"
    jp "What part of “identical twins” do you not understand…?"
    sp "It's only fair, I mean, she looked identical to me a few years ago, so now I'm identical to her."
    pc "I know, I know, I was there when you guys announced the change to the family!"
    hd "…"
    hd "I personally don't think you look like a girl Stirling…but I can see why people think so!"
    ss "Well…I guess that's a me problem."
    mt "Speaking of problems…I brought Mozzy here to help with yours."
    mr "Please hold your applause, I know I'm glamorous!"
    jp "Is he always like this?"
    mr "Hey, what's that supposed to mean?"

label hidden_object:
    scene bg honey room
    "So, there's nothing in here as of now."
    "this is a placeholder for the actual hidden object game"

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
    int_box "INTERROGATE: Pitaya Crim"
    pc "Wazzup?"
    mr "Mr Crim–"
    pc "Ooh, we're doing this PROFESSIONALLY, okay, this oughta be good!"
    mr "Aw thanks! Anyways, please give us your version of the events–"
    pc "Yeah, yeah, witness testimony, I got it."
    pc "Don't worry, I was the defendant for like half of Mira's cases, I know how this stuff works."
    mr "Wait, you guys knew each other before this?!"
    mt "Yes, Stirling hired me as Pitaya's lawyer."
    mt "But we're getting sidetracked. You two, lock in already."
    pc "Mira, please, never use those words again."
    label pc_ask:
        menu:
            "Testimony, please?":
                pc "I was just minding my own business, really!"
                pc "We were expecting more people, but apparently there was a flight delay, so they couldn't come. But whatever, that's not important."
                pc "So yeah, I was just minding my own business, and waiting for dinner to be done. I was also checking out Stirling's videogames when Little Miss Drama Queen runs in screaming about how her necklace got stolen."
                pc "Yeah, that's all I can think of."
                pc "By the way, I found the latest edition of that lawyer game you like so much in his collection, maybe we could play it together someday?"
                jump pc_ask
            "What is your alibi?":
                pc "I mean, I was in the living room the whole time. Although, I don't know if anyone can confirm that."
                pc "I did see the twins at one point, but they came from the corridor where the rooms are and went to the dining room right after, so they can't confirm my presence."
                pc "But I swear on Old Mrs Frap's life, I did not go anywhere near Dew's room"
                jump pc_ask
            "That's all":
                mr "Okay...thank you Mr Crim."
    
    mr "That's all we need for interrogating Pitaya."
    menu:
        mt "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction…"
            mr "But I want more information on something."
            mt "Well, then, go right ahead."
            mt "Slaughter his defenses and put his castle under siege until he has to surrender!"
            pc "Good lord, she's a lawyer again."
            pc "Okay, go on. Cross examine me."
            jump pc_evidence
        "No?": 
            mt "Well then, we should move on."
            jump interrogate

label pc_evidence:
    menu:
        mr "What evidence do I present?"
        "Brass knuckles":                    
            mr "Do you know anyone who uses brass knuckles?"
            pc "Brass knuckles…?"
            pc "Can't say for sure, but I heard Dew takes self-defense."
            pc "That surprised me, I mean, she's got the strength of a hundred men, what would she be trying to defend herself against?"
            mr "And you don't use brass knuckles?"
            pc "Nah, haven't beaten anyone up since we graduated."
            pc "And besides, I liked the feeling of my oppenent's skull crushing beneath my fist."
            mt "..."
            mr "..."
            pc "..."
            pc "Too dark?"
            mt "Pitaya, this is why people always think you're the murderer."
            show pitaya damage
            pc "F-fair enough."
            jump pc_evidence
        "Broken picture":
            mr "Can I see your knuckles?"
            pc "...Weird, but okay."
            mr "..."
            mr "Okay, all done."
            pc "Great. Now, {nw}{w=.5}"
            show pitaya awkward
            extend "WHAT THE HECK WAS THAT ALL ABOUT?!"
            mr "There was a broken picture in Honey's room, so I was checking to see if you broke it."
            mr "But your knuckles are clean, so, no worries."
            mr "Don't punch glass by the way, it's dangerous."
            pc "Says the guy who ate an entire necklace of it."
            mr "Will you guys please let me forget that?"
            jump pc_evidence
        "Pillow": 
            mt "...Mozzy, please don't tell me you actually put the pillow in as evidence."
            mr "It had feathers poking out of it like the hat!"
            mt "...They're different colours?"
            mr "...Oh. They looked the same in the lighting."
            pc "Are those the feather pillows?"
            mr "Oh yeah, you have them in your room too, right?"
            pc "I guess? I mean, sure, they're meant to be there, but I don't use them."
            pc "They're {i}too{/i} soft to be comfortable, if you get what I mean."
            jump pc_evidence
        "Testimony: \"I was also checking out Stirling's videogames\"":
            mr "Why were you looking at the game collection?"
            show pitaya smile
            pc "What do you mean? I was bored, that's all."
            mr "That's the thing."
            mr "You don't like playing videogames. Not on your own, anyways."
            show pitaya shock
            pc "!"
            mt "That's right..."
            mt "You only play if someone asks you to play with them, never on your own."
            mr "Yeah! So, my question to you, Mr Crim..."
            mr "...is why were  looking at Mr Strawberry's game collection on your own?"
            if failed_gaydar:
                mr "Could it be...that you are lying about your alibi?"
                pc "..."
                show pitaya laugh
                pc "Th-that's it?"
                mr "...Huh?"
                pc "Man, I was worried...you were so confident too."
                mr "W-did I get it wrong?"
                pc "Nothing to worry about man, nothing to worry about!"
                pc "I swear, on our friendship, my alibi is true."
                mr "Then...why were you looking through his videogames?"
                show pitaya embarrassed
                mr_thought "For some reason, Pitaya blushes and looks away."
                mt "I think that is a question you should ask another time."
                jump pc_evidence
            else:
                if successful_gaydar:
                    mr "Could it be...that you were looking for someone else?"
                    pc "..."
                    show pitaya nervous
                    pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                    mr "NOT WHAT I MEANT!"
                    mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                    mr "Someone like-"
                    mr "..."
                    mr "!"
                    mr "Wait, Pitaya-"
                    mr "Were you looking through the games...for me?"
                    show pitaya damage
                    mr "Y-yikes!"
                    mr_thought "Did he just fall to the floor?"
                    show pitaya smile
                    pc "Y-yeah. Yeah, I was."
                    pc "That was...wow. That was impressive."
                    pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                    pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                    pc "So, yeah. Here I am. And for the record..."
                    pc "Playing those lawyer games with you are always fun. You're great at doing the voices!"
                    mr "Pitaya..."
                    mt "As much as I don't want to interrupt this adorable moment..."
                    mt "The twins are glaring at you two. I think you need to start wrapping up."
                    show pitaya embarrassed
                    mr "Dangit!"
                    pc "O-okay!"
                else:
                    menu:
                        mr "Could it be..."
                        "That you are lying about your alibi?":
                            $ failed_gaydar = True
                            pc "..."
                            show pitaya laugh
                            pc "Th-that's it?"
                            mr "...Huh?"
                            pc "Man, I was worried...you were so confident too."
                            mr "W-did I get it wrong?"
                            pc "Nothing to worry about man, nothing to worry about!"
                            pc "I swear, on our friendship, my alibi is true."
                            mr "Then...why were you looking through his videogames?"
                            show pitaya embarrassed
                            mr_thought "For some reason, Pitaya blushes and looks away."
                            mt "I think that is a question you should ask another time."
                            jump pc_evidence
                        "That you were looking for someone else?":
                            $ successful_gaydar = True
                            pc "..."
                            show pitaya nervous
                            pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                            mr "NOT WHAT I MEANT!"
                            mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                            mr "Someone like-"
                            mr "..."
                            mr "!"
                            mr "Wait, Pitaya-"
                            mr "Were you looking through the games...for me?"
                            show pitaya damage
                            mr "Y-yikes!"
                            mr_thought "Did he just fall to the floor?"
                            show pitaya smile
                            pc "Y-yeah. Yeah, I was."
                            pc "That was...wow. That was impressive."
                            pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                            pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                            pc "So, yeah. Here I am. And for the record..."
                            pc "Playing those lawyer games with you are always fun. You're great at doing the voices!"
                            mr "Pitaya..."
                            mt "As much as I don't want to interrupt this adorable moment..."
                            mt "The twins are glaring at you two. I think you need to start wrapping up."
                            show pitaya embarrassed
                            mr "Dangit!"
                            pc "O-okay!"

        "Nevermind":
            mr "I don't know what I was going to say."
            mt "Then let's move on."

    jump interrogate

label int_honey:
    $ hd_int = True
    scene bg interrogation
    show honey default at default
    int_box "INTERROGATE: Honey Dew"
    hd "Hm? Can I help you?"
    jump interrogate

label int_twins:
    $ twin_int = True
    scene bg interrogation
    show jazz default at left
    show smith default at right
    int_box "INTERROGATE: the Twins"
    jp "What do you want?"
    jump interrogate

label int_stirling:
    $ ss_int = True
    scene bg interrogation
    show stirling default at default
    int_box "INTERROGATE: Stirling Strawberry"
    ss "Heyo!"
    jump interrogate
    #ask

label interrogate:
    if pc_int:
        if ss_int:
            if twin_int:
                if hd_int:
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
                        "Mira":
                            jump int_mira
                        "That's all":
                            jump continue_story2
                else:
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
                        "That's all":
                            jump continue_story2
            else:
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
                    "That's all":
                        jump continue_story2
        else:
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
                "That's all":
                    jump continue_story2
    else:
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
            "That's all":
                jump continue_story2

label int_mira:
    scene bg interrogation
    show mira default
    int_box "INTERROGATE: Mira Tisu"
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
    "{b}NOT GUILTY{/b}"

    return

label good_end:
    mr_thought "Miss Dew apologised for making such a mess, but everyone was quick to forgive her."
    mr_thought "...Okay that's a lie but honestly Pitaya and the twins don't really forgive easily so it's a win!"
    mr_thought "And so ends the tale of \"The Melon Conspiracy\""
    mr_thought "..."
    mr_thought "Does this count as a conspiracy?"
    "{b}GUILTY{/b}"

    return
