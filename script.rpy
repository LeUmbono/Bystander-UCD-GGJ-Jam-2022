define l = Character("Luna", color="#E03B8B")
default mentality = 50

define b1 = Character("Bully 1")

define b2 = Character("Bully 2")

label start:
    scene bg old school
    play sound "<from 0 to 30.8>audio/happy.mp3" 
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Joe"
    scene bg classroom
    "It’s Monday morning and you’ve just made it into your math class."
    "You don’t feel excited, but you know your best friend Luna, who is on the basketball team, had a game last night."
    show luna neutral
    player_name "Hey, Luna! How was the game yesterday?"
    stop sound
    show luna sad
    play sound "<from 0 to 30.8>audio/sad.mp3" 
    l "Hi, %(player_name)s. It was ok…."
    "Something seems to be off about her…"

menu:
    "Ask if everything is okay":
		##$ mentality += 10
        jump checkHer 
    "...she's probably alright":
		$ mentality -= 5
        jump classStarts

label checkHer:
    player_name "Hey, is everything alright? I know you were really excited about the game."
    l "Yeah, everything is just fine… We won…"
    "Things still don’t seem quite right…"
    stop sound

menu:
    "Something still feels off, but I should hold back from asking for now":
        jump classStarts
    "Probe further":
		$ mentality -= 5
        jump probeFurther

label probeFurther:
    player_name "You don’t seem all that happy about it. You sure you’re okay?"
    show luna angry
    l "I told you everything is fine, just leave me alone!"

label classStarts:
    hide luna
    "Class begins and you go through the motions of the day. As always, the lessons bore you to death but you manage to make it to the bell." 
    "Something’s still bothering you about Luna. She just didn’t seem her usual self earlier."
    "Normally, she’s the first person greeting you as you walk through the door, a cheerful smile plastered on her face."
    "Basketball had always been the world to her; her current mood couldn’t have had anything to do with the game the other day, could it?"

label gym:
    with wipeleft
    scene bg gym
    play sound "audio/bell.mp3" 
    "It’s finally time for P.E. — the only thing you look forward to during school."
    stop sound
    play sound "<from 0 to 40.8>audio/tension.mp3" 
    show bully smug at left
    show bully2 smug at right
    "As you walk past the bleachers, you notice two of Luna’s teammates talking to each other."
    play sound "audio/basketball.mp3" 
    "You overhear Luna’s name being tossed around in their conversation. You decide to…"

menu:
    "Approach the two of them":
        jump approach1
    "Sneak under the bleachers and continue listening in":
        jump approach1b
    "Ignore":
		$ mentality -= 10
        jump choiceLunch

label approach1:
    player_name "Hey, how was the game last night?"
    play sound "<from 0 to 2.8>audio/giggle.mp3"
    b1 "We won of course. I’m sure YOU’VE heard about Luna last night."
    stop sound
    b2 "I always knew something was wrong with her…"

menu:
    "Defend Luna":
		$ mentality += 15
        jump approach1a
    "Do nothing":
		$ mentality -= 5
        jump approach2

label approach1a:
    player_name "Hey, don’t say that about my friend!"
    b1 "Your {b}friend{/b}? Don’t make me laugh. Do you even know what {b}she{/b} did to the captain?"
    b2 "If you ask me, she deserved what she got last night. I bet she thinks of you the same way."
    player_name "What do you mean? Did something happen to Luna last night?"
    b1 "She just revealed her true colors, that’s all. I’m not even surprised."
    play sound "<from 0 to 2.8>audio/giggle.mp3"
    b2 "You must be blind if you didn’t notice too…"
    stop sound
    jump approach2

label approach1b:
    b1 "I can’t believe what Luna’s doing. She must be out of her mind! "
    b2 "Yeah, who does she even think she is? Next thing you know, she’ll be …"
    "You can’t make out the rest of their conversation. They walk away, and you know it is time to leave too."
    play sound "audio/bell.mp3" 
    "The bell rings once again, signaling the start of lunch."
    stop sound
    "At the same time, you remember Luna sometimes going to the rooftop when she needed a breath of fresh air."
    "You decide to…"
    jump choiceLunch

label approach2:
    "Come to think of it, Luna did start acting weird around three weeks ago."
    play sound "audio/tension.mp3" 
    hide bully
    hide bully2
    "It seems like the events from last night only made things worse. You wonder if you could’ve done anything to help her."
    "As you ponder on your thoughts, the bell rings once again, signaling the start of lunch."
    "At the same time, you remember Luna sometimes going to the rooftop when she needed a breath of fresh air."
    "You decide to go to the…"

menu choiceLunch:
    "Cafeteria for lunch ":
        jump lunch
    "Rooftop":
        jump rooftop

label lunch:
    scene bg cafeteria
    stop sound
    show luna sad
    "You see Luna sitting alone at lunch. She doesn’t have her red lunchbox with her."
    "She isn’t sitting with her usual group of friends either. You decide to…"
    play sound "audio/sad.mp3" 

menu:
    "Ignore her":
		$ mentality -= 10
        jump lunchIgnore
    "Approach her table":
		$ mentality += 5
        jump lunchProbe

label lunchIgnore:
    "You decide that it would be better to leave her alone for now."
    jump home

label lunchProbe:
    hide luna
    "As you near Luna’s table, you notice her lunchbox sitting in the trash can a couple feet away."
    show luna sad at right
    "You turn to face Luna. You decide to... "

menu:
    "Talk to her about the lunchbox":
		$ mentality += 15
        jump lunchBox
    "Ignore her":
		$ mentality -= 10
        jump lunchLeave

label lunchBox:
    player_name "Everything alright? I saw your lunchbox in the trash earlier."
    ##play sound "audio/cries.mp3"
    l "I don’t know…"
    show luna sad at right
    player_name "Did someone do that to you?"
    show trash normal at left
    "You point towards the trash can"
    l "*nods*"
    player_name " Are you comfortable talking about it?"
    "Luna explains her circumstances to you, detailing the incident from last night,"
    "as well as the bullying she had been going through lately. You shudder at her recount, but you choose to stick it out with her nonetheless."
    l "I’ve been keeping this to myself for far too long."
    l "Thanks for being here for me. I don’t know if it’ll get any better,"
    show luna smile
    l "but it feels as though a huge weight has been lifted off my shoulders. "
    show luna smile2
    player_name "Of course. Let me know if you need anything else."
    "Things seem better now. You talk to Luna throughout lunch."
    jump home

label lunchLeave:
    "Luna leaves as you approach her, tears streaming down her face."
    hide luna
    "You reach out your hand to try to stop her, but to no avail; she has already disappeared from sight."
    jump home

label rooftop:
    with fade
    scene bg rooftop
    "Opening the door to the rooftop, something peeks out from the corner of your eye."
    "It’s Luna, close to the edge, looking out over the railing. At the sight, you…"

menu:
    "Call out to her":
		$ mentality += 20
        jump callOut
    "Watch her silently":
		$ mentality -= 10
        jump home

label callOut:
    p "Luna, what the hell are you doing?!"
    l "Umm, i-it’s nothing! I was just taking in the view!"
    p "Don’t lie to me! You’ve been acting weird all week! It’s time you come clean with me."
    l "*sheds tear* I-I don’t know, I don’t know what to do anymore… "
    p "Take a deep breath and tell me what’s wrong, if you’re fine with that."
    "Luna explains her circumstances to you, detailing the incident from last night, as well as the bullying she had been going through lately."
    "You shudder at her recount, but you choose to stick it out with her nonetheless."
    l "I’ve been keeping this to myself for far too long. Thanks for being here for me."
    l "I don’t know if it’ll get any better, but it feels as though a huge weight has been lifted off my shoulders."
    p "Of course. Let me know if you need anything else."
    "Things seem better now. You talk to Luna throughout lunch."

label home:
    scene bg old school
    "Before long, it was already the end of the day."
	"Students start streaming out of the classrooms, tidying up their lockers as they prepare to head home."
    "As you make your way towards the school gates, you think back upon the events of the day."
	
	if mentality >= 80:
		jump ending1
	else if mentality >= 40:
		jump ending2
	else:
		jump ending3

label ending1:
	"The next few days pass by in the blink of an eye."
	play sound "<from 0 to 30.8>audio/happy.mp3"
	"Luna seems to be getting back to her usual self, greeting you as you walk into the classroom with her characteristic smile."
	"One afternoon, you spot Luna talking with her teammates; they appear happy, as if they had cleared the air with one another."
	"All seems to be well."
	
	jump credits
	
label ending2:
	"The next few days pass by in the blink of an eye."
	
	"Luna seems to be getting back to her usual self, greeting you as you walk into the classroom with her characteristic cheerfulness."
	"One afternoon, she comes up to you and tells you that she has left the basketball team."
	"She says she is happy about it, but the hesitance in her eyes tells you otherwise."
	"Perhaps you could have done more to help her……"
	
	jump credits
	
label ending3:
	"The next few days pass by in the blink of an eye."
	play sound "<from 0 to 30.8>audio/sad.mp3" 
	"Luna continues to act out, refusing to talk to you whenever you call out to her."
	"No matter what you try to do, nothing seems to get through to her."
	"One day, she stops coming to class entirely."
	"The teacher announces that she has transferred to another school."
	"Distracted, you look through the window during class, wondering if perhaps you could have been more than just a bystander."
	
    jump credits

label credits:
	return