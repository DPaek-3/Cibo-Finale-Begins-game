

define mr = Character("Mozzy")
define mr_thought = Character("Mozzy", what_italic=True)
define mt  = Character("Mira")
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
default pc_testimony = False
default twin_testimony = False
default successful_gaydar = False
default failed_gaydar = False
default hat = False
default gem = False
default honey_doll = False
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
    mt  "Hm?"
    mr "I mean, I know I'm an ace detective and all, but why are WE on our way to investigate a robbery here?"
    mr "It's the richest neighbourhood as well! Shouldn't someone a bit more higher-up take the case?"
    show mira hide
    mt  "..."
    show mira default
    mt  "This isn't actually an official case yet."
    mr "..."
    show mozzy shock
    mr "h-hUH?!"
    show mira smile
    mt  "A dear friend of mine asked me to help investigate before there is a scandal."
    mt  "And, well, you haven't had a case in a while either, so I decided to bring you along."
    show mira default
    show mozzy default
    mt  "Speaking of which, let's run over how to do investigations and interrogations."
    mt  "You'll notice that I haven't told you which house we're heading to."
    mt  "Your goal is to try and pull information out of me. Then, when we arrive at our stop, you'll use the information you received to find the correct house."
    menu:
        mt  "Do I interrogate Mira?"
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
    show mozzy default
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
    scene gates
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
    show mozzy shock #surprise
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
    mt  "Investigative partner, Stirling. I'm not dating anyone at the moment. I still don't have time for that. Besides, he's far too young–"
    mr "Hey! I'm only 23!, I can definitely vote....legally."
    mr_thought "Mira simply ignored me."
    show mira hide
    mt  "..."
    mt  "Stirling Strawberry, you will let us in right this moment or I will tell those cousins of yours that you ate the last cookie."
    show mozzy shock
    mr "Eep!"
    mr_thought "Mira can be so scary sometimes..."
    mt  "..."
    show mira smile
    mt  "Thanks. I'll see you soon."
    show mira default
    mt  "..."
    mt  "Sorry, did I scare you?"
    show mozzy excited
    mr "Um...I don't know what you're talking about! A great detective is never scared!"
    mr_thought "For some reason, Mira doesn't seem to believe that."
    mt  "...If you insist."
    show mozzy default
    mr "..."
    mt  "..."
    mr "Your friend is taking a while."
    mr_thought "Lo and behold, just as I said those words, the gates opened."
    show mozzy damage
    mr "Are you kidding me?"
    show mira smile
    mt  "I must say Mozzy, you have impeccable timing at times."
    mr "Let's...let's just go in."
    scene garden
    mr_thought "I fixed up my hat, and we walked through the gates."
    mr_thought "There was a really cool garden there. The fences were wrapped in ivy and roses"
    mr_thought "Suddenly, I heard a familiar voice shouting...a lot of things I won't repeat."
    show pitaya angry
    pc "That's it, you people deal with this yourself! I'm outta here!"
    mr "Pitaya!"
    #show pitaya curious
    pc "...?"
    show pitaya default
    pc "Mozzy! Hey, man!"
    mr_thought "Pitaya Crim, I was close with him during High school and college, acts like a big tough guy but he is really just a sweetheart, volunteering at nursing homes and what-not."
    mr_thought "...Okay, so MAYBE he was on trial for murder like a hundred times, but he's never actually committed any of them!"
    show pitaya angry
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
        pc "oh my gosh you oblivious swiss cheese..."
        mt  "...my goodness."

    scene bg stirling home
    "A/N: No sprites from here on out because it makes my head hurt and I don't like the placeholder sprites."
    "A/N: Feel free to use your imagination."
    pc "Well people, we have our detective and everyone's favourite lawyer."
    "???" "...He looks like a dud."
    mr "how dare you!, you...you...gremlin?, sorry you're just extremely short."
    "???" "And? We're literally fourteen."
    "???" "If anything, you're the short one."
    mr "HEY!!"
    mt  "*sigh*"
    mt  "Jazz, Smith, meet Mozzy. I met him on one of my cases."
    mt  "Mozzy, these are the Pale twins, Jazz and Smith. Jazz is the red one, Smith is green."
    jp "We met her when Stirling introduced his girlfriend to his family."
    sp "Which is just us."
    mt  "Bold of you two to assume that Stirling can last a day dating me."
    jp "Fair point."
    sp "Yeah, you deserve better anyways."
    "???" "Hey, I heard that!"
    jp "Oh, you're here? Whoops." 
    mr_thought "That was the most unsincere apology I have ever heard."
    mr_thought "And I went to school with Pitaya."
    "???" "Stirling, I would love to come to your defense, but to be honest, I do think Mira does deserve better."
    ss "So someone like you?"
    "???" "..."
    "???" "Oh, no. But certainly not you."
    ss "Why are you like thiiis?"
    "???" "Well, someone has to be a responsible adult when dear Mira's not around."
    "???" "I can hardly compare with her, but I do my best!"
    mr_thought "Wow, these guys really like Mira, huh?"
    mt  "Hi, honey."
    mr_thought "Mira using pet names? Is the world ending?"
    mt  "I don't know what you're thinking, but cut it out."
    mt  "Honey, this is Mozzy. Mozzy, meet Honey Dew. I know her from university."
    hd "Pleasure to meet you."
    mr_thought "Oh, so Honey's her name, not a term of affection."
    mr_thought "Probably should have figured that out."
    ss "And I'm Stirling Strawberry, besties with Mira since we met in college ten years ago!"
    mr "I see."
    mr "..."
    mr "Wait Mira you went to college when you were 10?"
    mt  "...How old do you think I am? "
    mr "...twenty, right?"
    mt  "I'm thirty-eight."
    mr "Oh."
    mr "Well, in any case, thank you, good madam!"
    ss "Huh? I-uh-I'm not-"
    mr "Huh? What's wrong?"
    pc "Oh, man-"
    "Jazz and Smith" "And another one bites the dust!"
    mt  "Mozzy..."
    mt  "Stirling's a man."
    mr "GAH!"
    mr "ajkfbldashfircids I am SO sorry!"
    ss "It-it's fine...it happens a lot..."
    ss "Do I really look that much like a girl...?"
    pc "Yup."
    jp "You do."
    sp "You really look like a girl."
    pc "Hey, YOU can't say anything! You and your sister look identical!"
    jp "What part of \"identical twins\" do you not understand...?"
    sp "It's only fair, I mean, she looked identical to me a few years ago, so now I'm identical to her."
    pc "I know, I know, I was there when you guys announced the change to the family!"
    hd "..."
    hd "I personally don't think you look like a girl Stirling...but I can see why people think so!"
    ss "Well...I guess that's a me problem."
    mt  "Speaking of problems...I brought Mozzy here to help with yours."
    mr "Please hold your applause, I know I'm glamorous!"
    jp "Is he always like this?"
    mr "Hey, what's that supposed to mean?"
    mt  "So if we could start our investigation soon, that would be great."
    ss "Aww, come on, Mira! All the suspects are here, can't it wait?"
    mt  "No. The faster we get this done, the less we have to worry about it."
    pc "Man, lawyers are scarily efficient."
    hd "Alright."
    hd "Stirling called you because the Melon Baller was stolen!"
    mr "The what?"
    ss "The Melon Baller. It's Honey's favourite necklace."
    jp "Favourite? She's only had it for the past week."
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

    imagebutton auto "door_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "door_hover")
        unhovered SetVariable("screen_tooltip" ,"")
        action Jump ("Leave")

label hidden_object:
    scene bg honey room
    mr "W-wow! You weren't kidding when you said it was a mess!"
    hd "Yes, I practically turned it inside out."
    hd "You see, I first thought I misplaced it, but when I couldn't find it anywhere, I realised someone must have stolen it!"
    mt  "Understood. Honey, could you step out and join everyone else? It's easier to investigate with just the two of us."
    hd "...Fine. If you say so."
    
    label honeys_room:
        call screen honeysroom
    
    label Jewel:
        scene bg honey room
        mr "This box is really neatly organised."
        mt  "Honey has a lot of jewellery, she likes to be able to see all of them and make sure they're there."
        mr "You'd think a thief would rummage through the jewellery box too."
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
    "As of 9/6/2026, 2:27pm, we don't have the full evidence list. So, here it is:"
    "Jewellery box; Graduation banner; Brass knuckles; Mira plushie; Mira photo; Mannequin; Pillow; Stirling's smashed picture; Stirling's earring; Candles; Gem"
    "anyways, some exposition later, after finding evidence, we move on to the interrogation"
    scene living room
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
    pc "Wazzup?"
    mr "Mr Crim-"
    pc "Ooh, we're doing this PROFESSIONALLY, okay, this oughta be good!"
    mr "Aw thanks! Anyways, please give us your version of the events-"
    pc "Yeah, yeah, witness testimony, I got it."
    pc "Don't worry, I was the defendant for like half of Mira's cases, I know how this stuff works."
    mr "Wait, you guys knew each other before this?!"
    mt  "Yes, Stirling hired me as Pitaya's lawyer."
    mt  "But we're getting sidetracked. You two, lock in already."
    pc "Mira, please, never use those words again."
    scene bg interrogation
    with dissolve
    int_box "INTERROGATE: Pitaya Crim"
    label pc_ask:
        menu:
            "Testimony, please?":
                $ pc_testimony = True
                pc "I was just minding my own business, really!"
                pc "We were expecting more people, but apparently there was a flight delay, so they couldn't come. But whatever, that's not important."
                pc "So yeah, I was just minding my own business, and waiting for dinner to be done. I was also checking out Stirling's videogames when Little Miss Drama Queen runs in screaming about how her necklace got stolen."
                pc "Yeah, that's all I can think of."
                pc "By the way, I found the latest edition of that lawyer game you like so much in his collection, maybe we could play it together someday?"
                jump pc_ask
            "What is your alibi?":
                pc "I mean, I was in the living room the whole time. Although, I don't know if anyone can confirm that."
                pc "I know for a fact that I saw the twins at one point, but they came from the corridor where the rooms are and went to the dining room right after, so they can't confirm my alibi."
                pc "But I swear on Old Mrs Frap, I did not go anywhere near Dew's room."
                pc "Seriously, she'd whup my butt if I lied to you!"
                jump pc_ask
            "What's on the crime agenda this year?":
                pc "Tax evasion."
                mr "...That's it?"
                pc "What? It's a genuine crime."
                mr "Maybe, but it's also a normal thing for rich people to do."
                pc "...Fair point."
                pc "Oh well, I can change the annual crime in a few months anyways."
                mt  "What a thing to admit in front of your lawyer."
            "That's all":
                mr "Okay...thank you Mr Crim."
    
    mr "That's all we need for interrogating Pitaya."
    menu:
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "Slaughter his defenses and put his castle under siege until he has to surrender!"
            pc "Good lord, she's a lawyer again."
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
            pc "What sort of question is that? Of course I do!"
            pc "It was a gift from you, after all."
            mr "Cool, cool. Do you know anyone who uses brass knuckles?"
            pc "Brass knuckles...?"
            pc "Can't say for sure, but I heard Dew takes self-defense."
            pc "That surprised me, I mean, she's got the strength of a hundred men, what would she be trying to defend herself against?"
            mr "And you don't use brass knuckles?"
            pc "Nah, haven't beaten anyone up since we graduated."
            pc "And besides, I liked the feeling of my oppenent's skull crushing beneath my fist."
            mt  "..."
            mr "..."
            pc "..."
            pc "Too dark?"
            mt  "Pitaya, this is why people always think you're the murderer."
            pc "F-fair enough."
            jump pc_evidence
        "Broken picture":
            mr "Can I see your knuckles?"
            pc "...Weird, but okay."
            mr "..."
            mr "Okay, all done."
            pc "Great. Now, {nw}{w=.5}"
            extend "WHAT THE HECK WAS THAT ALL ABOUT?!"
            mr "There was a broken picture in Honey's room, so I was checking to see if you broke it."
            mr "But your knuckles are clean, so, no worries."
            mr "Don't punch glass by the way, it's dangerous."
            pc "Says the guy who ate an entire necklace of it."
            mr "Will you guys please let me forget that?"
            jump pc_evidence
        "Pillow": 
            mt  "...Mozzy, please don't tell me you actually put the pillow in as evidence."
            mr "It had feathers poking out of it like the hat!"
            mt  "...They're different colours?"
            mr "...Oh. They looked the same in the room."
            pc "Are those the feather pillows?"
            mr "Oh yeah, you have them in your room too, right?"
            pc "I guess? I mean, sure, they're meant to be there, but I don't use them."
            pc "They're {i}too{/i} soft to be comfortable, if you get what I mean."
            jump pc_evidence
        "Pitaya's Testimony":
            mr "Why were you looking at the game collection?"
            pc "What do you mean? I was bored, that's all."
            mr "That's the thing."
            mr "You don't like playing videogames. Not on your own, anyways."
            pc "!"
            mt  "That's right..."
            mt  "You only play if someone asks you to play with them, never on your own."
            mr "Yeah! So, my question to you, Mr Crim..."
            mr "...is why were  looking at Mr Strawberry's game collection on your own?"
            if failed_gaydar:
                mr "Could it be...that you are lying about your alibi?"
                pc "..."
                pc "Th-that's it?"
                mr "...Huh?"
                pc "Man, I was worried...you were so confident too."
                mr "W-did I get it wrong?"
                pc "Nothing to worry about man, nothing to worry about!"
                pc "I swear, on our friendship, my alibi is true."
                mr "Then...why were you looking through his videogames?"
                mr_thought "For some reason, Pitaya blushes and looks away."
                mt  "I think that is a question you should ask another time."
                jump pc_evidence
            else:
                if successful_gaydar:
                    mr "Could it be...that you were looking for someone else?"
                    pc "..."
                    pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                    mr "NOT WHAT I MEANT!"
                    mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                    mr "Someone like-"
                    mr "..."
                    mr "!"
                    mr "Wait, Pitaya-"
                    mr "Were you looking through the games...for me?"
                    pc "Gh-?!"
                    mr "Y-yikes!"
                    mr_thought "Did he just fall to the floor?"
                    pc "Y-yeah. Yeah, I was."
                    pc "That was...wow. That was impressive."
                    pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                    pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                    pc "So, yeah. Here I am. And for the record..."
                    pc "Playing those lawyer games with you are always fun. You're great at doing the voices!"
                    mr "Pitaya..."
                    mt  "As much as I don't want to interrupt this adorable moment..."
                    mt  "The twins are glaring at you two. I think you need to start wrapping up."
                    mr "Dangit!"
                    pc "O-okay!"
                else:
                    menu:
                        mr "Could it be..."
                        "That you are lying about your alibi?":
                            $ failed_gaydar = True
                            pc "..."
                            pc "Th-that's it?"
                            mr "...Huh?"
                            pc "Man, I was worried...you were so confident too."
                            mr "W-did I get it wrong?"
                            pc "Nothing to worry about man, nothing to worry about!"
                            pc "I swear, on our friendship, my alibi is true."
                            mr "Then...why were you looking through his videogames?"
                            mr_thought "For some reason, Pitaya blushes and looks away."
                            mt  "I think that is a question you should ask another time."
                            jump pc_evidence
                        "That you were looking for someone else?":
                            $ successful_gaydar = True
                            pc "..."
                            pc "Wh-what do you mean? Looking for someone in a videogame collection?"
                            mr "NOT WHAT I MEANT!"
                            mr "I mean, you were looking at the videogames, so you could share new ones with someone who DOES love videogames."
                            mr "Someone like-"
                            mr "..."
                            mr "!"
                            mr "Wait, Pitaya-"
                            mr "Were you looking through the games...for me?"
                            pc "Gh-?!"
                            mr "Y-yikes!"
                            mr_thought "Did he just fall to the floor?"
                            pc "Y-yeah. Yeah, I was."
                            pc "That was...wow. That was impressive."
                            pc "Yeah, I, uh, wanted to spend time with you, and I knew that Stirling had a few games that you also like, so I checked to see if there was anything you haven't played yet."
                            pc "'Cause, man, you're fun to be around! You're not weird like most people I know."
                            pc "So, yeah. Here I am. And for the record..."
                            pc "Playing those lawyer games with you are always fun. There's a reason they're the only videogames I play, after all!"
                            mr "Pitaya..."
                            mt  "As much as I don't want to interrupt this adorable moment..."
                            mt  "The twins are glaring at you two. I think you need to start wrapping up."
                            mr "Dangit!"
                            pc "O-okay!"
                            jump pc_evidence

        "Nevermind":
            mr "I don't know what I was going to say."
            mt  "Then let's move on."

    jump interrogate

label int_honey:
    $ hd_int = True
    hd "Hm? Can I help you?"
    mr "Ms Dew, we know that it was your necklace that was stolen, but can we still ask for your version of the events?"
    hd "My, my! You're talking so professionally! Mira taught you well."
    mr "Mozzy worked as a detective before meeting me."
    hd "...Oh. That's...a surprise."
    mr_thought "Is it?"
    scene bg interrogation
    with dissolve
    int_box "INTERROGATE: Honey Dew"
    menu:
        "Testimony, please":
            hd "Why, of course."
            hd "I showed everyone the Melon Baller during lunch. It is quite a beautiful necklace, and I got it for quite the steal!"
            hd "After lunch, I put it back on the mannequin in my room."
            hd "You know, Mira, I'm glad Stirling gave the two of us permanent rooms in his house. Saves the hassle of packing unnecessary luggage!"
            hd "But anyways! I then went to the garden, and I spent about two hours reading my book."
            hd "Then I went back through the living room back to my room when I noticed that the Melon Baller wasn't on the mannequin."
            hd "I thought perhaps I put it somewhere else, so I searched through my room, but it still wasn't anywhere! My apologies for the mess, by the way, it must have been hard to investigate with everything thrown about. "
            hd "I ran back to the living room to let everyone else know of the theft, and..."
            hd "Now you're here, Mira."
            mr_thought "Did I just get ignored?"
        "Alibi?":
            hd "My alibi? Why do I need an alibi, it's my necklace that got stolen!"
            hd "You don't think I'm that much of an attention seeker, do you?"
        "That's all":
            mr "Right! Thank you for your help, Ms Dew!"
    menu: 
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "But be careful. Honey has more bite than I do."
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
            hd "I'm not sure. It was labelled that way when I bought it."
            hd "In any case, what do you want to know about the hat?"
            mr "Do you wear it often?"
            hd "Of course! It's such a precious item, and I love it so much!"
            hd "It means so much to me, and it looks fabulous!"
            mt  "...I'm glad, Honey."
            mr "Cool!"
            mr "So where did you get such a cheap hat that looks so good?"
            mt  "Ng-?!"
            hd "What?"
            mr "There's a feather missing from the hat, and I can see a glue strip here. But it also looks like it would be a really good quality hat."
            mr "My question is where did you get such a cheap hat?"
            mt  "Mozzy, the truth is that I-"
            hd "Oh, YOU WANNA FIGHT, BOY?! YOU WANT TO FIGHT ME?!"
            mt  "Aaand here we go again. Oh boy."
            hd "MIRA BOUGHT THAT FOR ME, OKAY?! YOU THINK IT'S CHEAP BEING A UNIVERSITY STUDENT?! STIRLING MAY BE A NEPO BABY, AND MY PARENTS MAY BE PRETTY WELL OFF, BUT MIRA WAS DOING THE BEST SHE COULD TO GET HER LAW DEGREE!"
            if gem:
                mr "Didn't we do this before?!"
            hd "The fact that despite ALL of that, she bought that hat as a gift for ME! ME! She got the best hat she could find within her budget, despite all her tight schedules, despite all her student loans! Got it? GOT IT?!"
            mt  "Yes, yes, we get it, Honey! Please, calm down!"
            hd "..."
            hd "Oh, of course! I'm so sorry. Let's forget this, shall we?"
            jump hd_evidence
        "Brass knuckles":
            hd "Oh, those? They must be that punks'."
            mr "...You mean Pitaya?"
            hd "Yes, him."
            jump hd_evidence
        "The twins' testimony":
            if twin_testimony:
                mr "The twins were also in the garden. Did you see them?"
                hd "They were? I'm afraid I didn't notice."
                hd "Though, I was reading a rather interesting book. Would you like to read it?"
                mr "...{i}Bejewelled Jaws{/i} by Constance Dew?"
                hd "My sister wrote it. She's a botanist, you see. She specializes in carnivorous plants."
                mt  "Yes, I remember that."
                mt  "I didn't know Sun's name was actually Constance."
                hd "Yes, well, our parents weren't the best at naming us. There's a reason I changed my name."
                mr "...Cool."
            else:
                hd "Oh, the heirs to the Pale family? What about them?"
                mr "...That is a very good question."
                mt  "Mozzy, remember to get the testimony first before using it as evidence."
            jump hd_evidence
        "Mira plushie":
            $ honey_doll = True
            mr "Where did you get this?"
            mt  "Ng-!"
            hd "Oh, that? I commissioned it myself!"
            hd "I can't see you these days because of how busy our schedules are! So I commissioned a plushie of you that I can talk to when I'm not with you!"
            mr "Ms Dew, have you considered maybe giving her a phone call like a normal person?"
            hd "But that's boring!"
            mt  "Can we please stop talking about this?!"
            jump hd_evidence
        "Gem":
            $ gem = True
            mr "What can you tell us about this gem?"
            hd "Ah, this must be from the Melon Baller. Where did you find it?"
            mr "On the bed. It's really neat, by the way. Why's that?"
            hd "I like keeping my bed neat. And well, since it's so neat, I saw no reason to look through it as I'd be able to see if there's anything underneath anyways."
            menu: 
                mr_thought "Should I ask her why there's glue on this?"
                "Yes":
                    hd "What."
                    mr "I was just curious, since you said you got this for a steal."
                    mr "Did you get scammed, by any chance?"
                    hd "I. Don't. Know. What. You're. Talking. About."
                    mr "I mean, getting it for a steal implies that you got a expensive thing for cheap."
                    mr "But the glue here suggests otherwise."
                    mt  "Mozzy, you really shouldn't-"
                    mr "So I was just wondering if you got scammed or if you were lying about how valuable it is."
                    mt  "Mozzy, I think you need to stop-"
                    hd "CURSE YOU!"
                    mr "Gah!?"
                    hd "FIRST, you DARE interrupt my time with Mira. THEN, you ask for my alibi even though I'M THE VICTIM. And NOW, YOU JUDGE ME FOR BUYING CHEAP JEWELLERY?!"
                    if hat:
                        mr "Didn't we do this before?!"
                    mt  "Honey, please, calm down-"
                    hd "WHO CARES?! WHO CARES IF I BUY CHEAP JEWELLERY?! IT DOES ITS JOB SO LONG AS IT LOOKS PRETTY, NO?! WHO ARE YOU TO JUDGE ME?!"
                    hd "I HAVE BETTER THINGS TO SPEND MY MONEY ON THAN RIDICULOUSLY EXPENSIVE JEWELLERY."
                    mt  "Honey-"
                    hd "You know what? FINE! I SAID IT WAS VALUABLE SO THOSE BRATS WOULDN'T MAKE FUN OF ME! OKAY?! SO SHUT THAT STUPID TRAP OF YOURS AND-"
                    mt  "Honey Dew, calm down! Now!"
                    hd "..."
                    hd "Ah, sorry. My temper went out of hand there, didn't it?"
                    hd "This is embarrassing. I apologize."
                    hd "Shall we move on?"
                    mt  "..."
                    mt  "Honey, we're going to talk about this later."
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
    jp "What do you want?"
    mt  "Just a routine inspection, nothing more. We need all the information we can get if we want to solve this case, so would you be willing to cooperate?"
    jp "..."
    sp "..."
    sp "Does...he have to be here too?"
    mt  "Well, two heads are better than one."
    jp "But he's so...blond. I don't see what help he could be."
    mr_thought "Aren't you guys also blond?"
    mt  "Jazz, what did I say about saying stuff like that?"
    jp "...If you don't have anything nice to say, don't say anything at all."
    mt  "That's right."
    mt  "I know that you insult those close to you as a love language, but you do need to be mindful of what is banter and what is actually hurtful."
    mt  "That applies to you too, Smith. Do you understand?"
    sp "...Yeah."
    mt  "Great. Let's begin."
    scene bg interrogation
    with dissolve
    int_box "INTERROGATE: the Twins"
    label twin_ask:
        menu:
            "Testimony, please?":
                $ twin_testimony = True
                jp "Surely you don't think we were the ones who stole that tacky necklace."
                sp "I mean, seriously, who wears a jewel THAT big?"
                mr_thought "After hearing that insults are their love language, I genuinely can't tell if they hate Honey or not."
                jp "I personally wouldn't steal something like that, so you better go find someone with horrible taste."
                sp "Hey, maybe this \"detective\" stole it! He certainly fits the bill for horrible taste!"
                mr "Hey! I don't have horrible taste!"
                jump twin_ask
            "What is your alibi?":
                jp "Seriously? You still think we did it? Ugh."
                jp "But whatever. I was with Smith the whole time. I never even went near Dew's room."
                sp "I can say the same...for obvious reasons." 
                sp "We were in the kitchen and the garden since lunch."
                sp "Besides, that watermelon scent is too strong for us. What reason would we have to go there?"
                jp "Is that all, you cretin?"
                jump twin_ask
            "That's all":
                mr "Okay...thanks, guys."
                mr_thought "I guess."
    menu:
        mt  "Well, Mozzy? Can you find any contradictions?"
        "YES!":
            mr "Well, I don't know if it's really a contradiction..."
            mr "But I want more information on something."
            mt  "Well, then, go right ahead."
            mt  "Leave no stone of their testimony unturned and unveil the truth for all to see!"
            jp "Can we make fun of her for that?"
            sp "Are you insane!? No!"
            jump twin_evidence
        "No?": 
            mt  "Well then, we should move on."
            jump interrogate

label twin_evidence:
    menu:
        mr "What evidence do I present?"
        "Stirling's earring":
            mr "Do either of you guys wear earrings?"
            sp "No."
            mr "..."
            mr "Does anyone else wear earrings?"
            jp "Yeah, that punk loser named after a fruit does. So does Stirling."
            sp "And he wonders why people mistake him for a her."
            jump twin_evidence
        "Pitaya's testimony":
            if pc_testimony:
                mr "Are you sure you were in the kitchen the whole time?"
                jp "Didn't we literally say that we were also in the garden too?"
                mr "No! I mean, I have evidence that you went other places too!"
                mr "Mr Crim told us that he was in the living room, and at one point, you two walked in from the hallway."
                mr "The hallway...where the rooms are!"
                sp "What?! No way, we didn't see him-"
                jp "Shut up!"
                mt  "Too late."
                jp "M-Mira?"
                mt  "I'm sorry, I'm aware that I'm being a bit harsh on you. But I do have to do my job."
                mr "And it seems you two just admitted that you went to the living room!"
                jp "W-you're forgetting something! We may have gone to the living room, but we didn't see that punk loser anywhere! "
                sp "Yeah! He's lying about seeing us come from the hallway!"
                mt  "That can also be explained."
                mt  "Pitaya was looking at the videogame collection."
                jp "Aha! More proof! He hates videogames!"
                mt  "Indeed he does. I cannot explain why he was looking through the collection without speculation, but I do have proof that he was there. "
                mt  "Tell me, when did Pitaya arrive here?"
                sp "This morning. Why?"
                mt  "That's what I thought."
                mt  "You see, he mentioned a certain lawyer game. I know for a fact that the game he was referring to was only bought after his last visit to Stirling." 
                mt  "He wouldn't have had time to look through it this morning as he only just arrived. So the only way he could have known that Stirling bought that game..."
                mr "...Is if his alibi is true!"
                mt  "Precisely. And if he was looking through the collection, he would probably be down on the ground, and anyone walking in wouldn't see him because he was covered by the couch."
                mr "But if you're behind the couch like this..."
                pc "What? Mozzy, what are you-"
                mr "You can still see the door to the hallway!"
                mr "What do you say to that?"
                jp "Argh!"
                sp "Impossible...!"
                jp "You're telling us..."
                sp "That you figured all of that out..."
                "Jazz and Pale" "Just by one man's word?!"
                mr "That's Mira for you!"
                mt  "Well, to be honest, you also slipped up when you mentioned that the watermelon scent would be too strong for you."
                jp "...This is your fault."
                sp "My fault?! Why is it my fault?!"
                jp "You're the one that slipped up! Now they know that we were in that diva's room!"
                mt  "I mean, we didn't quite know that yet. Thank you for the confirmation."
                jp "...Miercoles."
                sp "See?! You messed too!"
                sp "Oh, and also, you said a naughty word!"
                jp "Nuh uh! I said \"Wednesday\"!"
                sp "Yuh huh!"
                jp "Nuh uh!"
                mr "Will you two stop so we can carry on our investigation?"
                "Jazz and Pale" "CALLATE!"
                mr "Yikes!"
                mt  "Jazz. Smith."
                "Jazz and Pale" "Sorry."
                jump twin_evidence
            else:
                mt  "What do you mean, Pitaya's testimony?"
                mr "What? My gut instinct tells me that this is important! And that's why-"
                mr "..."
                mr "I just remembered we haven't actually talked to him yet."
                jump twin_evidence
        "Candles":
            mr "You said you never went near Ms. Dew's room, correct?"
            jp "Yeah...? I think I was pretty clear when I said that."
            mr "If that's the case...then how did you know it smelt like watermelon?"
            jp "Ngh!"
            sp "Gh?!"
            jp "I-well, isn't it obvious? The smell was so strong that we could smell it from outside the hallway!"
            sp "Y-yeah! It is quite strong, after all!"
            mr "Hm"
            mt  "I'll just let you know: the windows, as well as the door, were closed all day."
            jp "Who-who said we smelt watermelons today? We're just talking about what we smelt on...Wednesday! Yeah!"
            mr_thought "... No way for me to disprove that, but that was such an obvious lie that even I can catch it."
            jump twin_evidence
        "Nevermind":
            mr "I don't know what I was going to say."
            mt  "Then, let's move on."

    
    jump interrogate

label int_stirling:
    $ ss_int = True
    ss "Heyo!"
    mt "Alright, Stirling. You know the rules of an interrogation. Stick to facts as much as you can."
    ss "Yeah! Yeah, of course!"
    ss "Hope I can help!"
    mr_thought "Why is he so nervous?"
    mt "..."
    mt "Are you sure you're alright, Stirling?"
    ss "What? Oh! Yeah, of course, why wouldn't I be? Let's just start the interrogation now, yeah?"
    scene bg interrogation
    with dissolve
    int_box "INTERROGATE: Stirling Strawberry"
    label ss_ask:
        menu:
            "Testimony, please":
                ss "I wanted to hold a big party, so I invited most people I know. Honey and Pitaya were the only ones who could show up though. And well, Jazz and Smith live here anyways."
                ss "Honey's been here since Thursday, and Pitaya arrived just this morning."
                ss "I made a strawberry cheesecake, so we had that for lunch. Although, I had a tiramisu, since I kinda need the caffeine diet right now. Pitaya just collapsed on the couch, so he skipped lunch."
                ss "What else? Oh, Honey showed us the Melon Baller. She sounded really proud of it...I hope we find it soon. "
                ss "Although, I did find it weird how she talked about how valuable it is...she doesn't like buying expensive jewellery. Probably not important though."
                ss "After lunch, I went to my room. I can't quite remember what I was doing, but I'm pretty sure I stayed there until Pitaya came to tell me that the Melon Baller was stolen."
                ss "I asked around, but nobody confessed, so I called you, and now the two of you are here."
                jump ss_ask
            "What is your alibi?":
                ss "I'm sorry, I don't really have an alibi. I was in my room the whole time, but no one can confirm that."
                jump ss_ask
            "Why are you so nervous?":
                ss "Whaat? Nervous? Who, me? Nah, I'm not nervous!"
                mr "..."
                mt "..."
                ss "...Okay, maybe I'm a bit nervous. "
                menu:
                    "Why?":
                        ss "I don't know."
                        menu:
                            "Why?":
                                ss "What did I just say? I don't know!"
                                menu:
                                    "Why?":
                                        ss "I'm not saying anything."
                                        menu:
                                            "Why?":
                                                ss "I-I just won't! Okay?"
                                                menu:
                                                    "Why?":
                                                        ss "Ngh-do I have the right to silence?"
                                                        menu:
                                                            "Why?":
                                                                ss "I don't want to say it! Alright?"
                                                                menu:
                                                                    "Why?":
                                                                        ss "Stop! Why are you like this?"
                                                                        menu:
                                                                            "Why?":
                                                                                ss "Gh-"
                                                                                menu:
                                                                                    "Why?":
                                                                                        ss "BECAUSE THIS IS THE FIRST TIME I'VE EVER BEEN QUESTIONED AND MIRA'S SO SERIOUS IT'S KINDA SCARY OKAY?!"
                mt "..."
                mr "..."
                ss "..."
                ss "Ack, didn't mean to say that."
                mr "Well, that's an easy fix!"
                mr "Just stop thinking of Mira as scary!"
                ss "..."
                mt "..."
                mt "I don't think it works like that."
                mt "Am I really that scary?"
                mr "...So I think we should move on."
                mt "Why does nobody ever answer that question?"
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
            ss "Slay, queen!"
            jump ss_evidence
        "No?":
            mt "Well then, let's move on."
            jump interrogate

label ss_evidence:
    menu:
        mr "What evidence do I present?"
        "Stirling's earring":
            ss "!"
            ss "Where did you find that? I've been looking for it everywhere!"
            mr "...On the floor of Ms Dew's room."
            ss "Huh? That doesn't make any - oh! I remember now!"
            ss "I was cleaning Honey's room before she arrived - it must have fallen off then."
            ss "Well, in any case, thanks for finding it!"
        "Mira's plushie":
            ss "I didn't know you had merch, Mira."
            mt "...I don't."
            ss "...Oh. Then what's this?"
            if honey_doll:
                mr "Apparently Ms Dew commissioned it."
                ss "Oh, yeah, it looks like she commissioned Enoki for it."
                mr "Who?"
                ss "Oh, she's the costume designer of Fruta Cabaret. She makes dolls as well."
                mr_thought "That answers nothing!"
                mt "Stirling, Mozzy doesn't know what Fruta Cabaret is."
                ss "Oh! That's right. Fruta Cabaret is my theatre company. "
                ss "Our production of Romeo and Juliet is on two months from now! Will you come?"
                menu:
                    "Sure?":
                        ss "Great! Hope to see you there!"
                        mr "Are you playing Romeo?"
                        ss "Ah, no... I haven't really had many big roles. I guess I'm not cut out for it yet."
                        mt "Really? I always thought you were rather good."
                        ss "Aw, thanks Mira!"
                        ss "Although, I don't think I would have wanted to be Romeo anyways."
                        ss "Hm. Or maybe I'm just having too much fun as Benvolio."
                        ss "Well, in any case, glad you're coming!"
                    "Not interested":
                        show stirling damage
                        ss "Gah!"
                        mr_thought "Why'd you react like you just got punched?! I didn't even move!"
                        mt "Oh god..."
                        mt "Here."
                        mr_thought "She hands him a handkerchief."
                        ss "Oh, Mira, I can't, I'd get so much blood on it."
                        mt "I'm a woman and a criminal lawyer, I know how to get blood out. Just stop bleeding on your floor."
                        ss "Thanks Mira, you're the best."
            else:
                mt "I wish I knew."
                ss "...It's kinda cute. Maybe you should start selling merch-"
                mt "I'm a lawyer. Why would I want merch?"
                ss "I mean, have you seen your tags on the internet-?"
                mt "NO AND I HAVE NO PLANS WHATSOEVER TO EVER CHECK."
                ss "O-oh, yeah, fair enough, Honey would murder half the community if she ever saw what they post..."
                mt "NOPE, WE'RE MOVING ON!"
        "Mira's picture" :
            ss "Oh! That's the picture I took!"
            mt "...Stirling, don't tell me that you brought a camera into a trial."
            ss "I mean, it wasn't murder, so it should be alright, right?"
            mt "The rule doesn't just apply to murder cases, it's for all cases!"
            ss "...Whoops."
            ss "Um. No one has to know?"
            mt "...Fine. It's a nice picture anyways."
            jump ss_evidence
        "Mannequin":
            ss "Oh, that thing? Enoki was giving away some of her old mannequins, so I got one for Honey's room so she can put her hat on it when she visits."
            mr "...Who's Enoki again?"
            ss "The costume designer for my theatre troupe."
            jump ss_evidence
        "Nevermind":
            mr "I don't know what I was going to say."
            mt "Then let's move on."
            jump interrogate

label interrogate:
    if pc_int:
        scene living room
        if ss_int:
            scene living room
            if twin_int:
                scene living room
                if hd_int:
                    scene living room
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
                            jump continue_story3
                else:
                    scene living room
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
                            jump continue_story3
            else:
                scene living room
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
                        jump continue_story3
        else:
            scene living room
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
                    jump continue_story3
    else:
        scene living room
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
                jump continue_story3

label int_mira:
    mt  "Me? Why do you want to interrogate me? I wasn't here for the incident."
    scene bg interrogation
    with dissolve
    int_box "INTERROGATE: Mira Tisu"
    jump interrogate

label continue_story3:
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
    show pitaya shock
    pc "Wh-WHAT?!"
    jump wrong_end

label culprit_hd:
    show honey surprise
    hd "I...don't understand."
    jump good_end

label culprit_pale:
    $ twin_guilt = True
    show twin guilty
    jp "You stupid..."
    sp "Putrid..."
    jp "Yammering..."
    sp "Blumbering..."
    "Jazz and Smith" "MEDDLING, NO GOOD, BASTARD!!"
    jump wrong_end

label culprit_ss:
    $ stirling_guilt = True
    show stirling guilty
    ss "What? Me?"
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
    "{b}Fin?{/b}"

    return

label good_end:
    mr_thought "Miss Dew apologised for making such a mess, but everyone was quick to forgive her."
    mr_thought "...Okay that's a lie but honestly Pitaya and the twins don't really forgive easily so it's a win!"
    mr_thought "And so ends the tale of \"The Melon Conspiracy\""
    mr_thought "..."
    mr_thought "Does this count as a conspiracy?"
    "{b}Fin.{/b}"

    return
