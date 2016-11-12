---
layout : wiki
title : Applications
type : irc
description : |
  Here is a conversation that describes the ICCCM, EWMH and how some
  applications just don't play nicely.

---

# Applications, ICCCM2 and EWMH

A conversation from May 2006 about the ICCCM and the EWMH and how some
applications don't play nicely.  This conversation took place on IRC at the
times stated in the log.  Some of the conversation has been edited to remove
surperfluous information.

## IRC Conversation

|Person|Conversation|Time|
|------|------------|----|
|thomas\_adam| Wsoprulz1299:Once upon a time, there lived a special document called the ICCCM.|22:06 |
|xevz|he wouldn't have his desktop all styled up. :P|22:06|
|xevz|Oh, this sounds good. :D| 22:06|
|thomas\_adam| xevz: There could have been ~/.fvwm/config, which takes precedence  (you're making me digress.)| 22:06|
|Wsoprulz129| there is no config file| 22:06|
|Wsoprulz129| and when I do changes in .fvwm2rc, they happen when i restart fvwm| 22:07|
|xevz| thomas\_adam: No such file exists, he untared my configuration into his ~ resulting in a .fvwm. :)|  22:07|
|thomas\_adam| Wsoprulz1299: This document was well-written, and our special little program, FVWM loved it so much, it adopted it as its template model on which to base itself.|  22:07|
|Wsoprulz129| anyways.. keep going w/ story| 22:07|
|\* xteddy| hugs fvwm :)| 22:07|
|thomas\_adam| Wsoprulz1299: It attempted to set out guidelines -- codes of conduct that the window manager should do to handle windows, and conversely what windows (XClients) should do to behave nicely with other applications and the window manager. |22:08|
|thomas\_adam| Wsoprulz1299: The ICCCM and FVWM loved each other so much, they got married.|   22:09|
|thomas\_adam |  Wsoprulz1299: It worked for a time.  Other applications started to realise just how nice the ICCCM was to everyone, and so everyone started to use it.  It couldn't have been a nicer match for all concerned...  |22:10|
|thomas\_adam| Wsoprulz1299: But one day, things started to go Really Bad for our little guy....|  22:10|
|thomas\_adam| Wsoprulz1299: People grew weary of the ICCCM.  It was growing older -- and no longer retained that youthfulness it once had.  Society doesn't "respect their elders" and so applications started to deviate from the ICCCM, preferring to add extension of their own.|   22:11|
|thomas\_adam|  Wsoprulz1299: Poor FVWM.  You have to feel sorry for it.  |22:12|
|thomas\_adam| Wsoprulz1299: It grew up with ICCCM.  It loved the ICCCM.  |22:12|
|thomas\_adam|Wsoprulz1299: But, how was it supposed to fulfil its duty if applications weren't respecting it properly?| 22:12|
|thomas\_adam| Wsoprulz1299: Firefox and Mozilla, the beasties from Over Yonder were well-known rebels.|  22:13|
|thomas\_adam| Wsoprulz1299: And one day they decided to do a number of things to try and upset the ICCCM.|  22:13|
|thomas\_adam| Wsoprulz1299: Sure they stuck to some of it, after all, like most hatrid-centric things, they actually like the thing they project the hate for.  But they were rebellious in nature.  They didn't do *everything* quite right.  Naughty applications.  Tut. |  22:14|
|Comete|  sorry but could you explain me please what is MwmDecorMax MwmDecorMin for, i don't understand the man page ? please|  22:15|
|marco13185|  thomas\_adam, ready to suggest a good alternative to firefox?  | 22:15|
|thomas\_adam| Comete: Inherent properties that some motif apps have for providing XAtom hints.|  22:15|
|thomas\_adam |  marco13185: Sssh.  (http://edulinux.homeunix.org/elinks) |22:15|
|Wsoprulz129| but thomas\_adam: why does firefox work for others?|  22:15 |
|Comete|  thomas\_adam lol| 22:15|
|thomas\_adam |  Wsoprulz1299: I'm getting to that.|  22:15|
|Wsoprulz129| xevz didnt have a trouble w/ firefox  |  22:15|
|marco13185 | Wsoprulz1299, your pretty much using xevz's config too, lol| 2:16|
|Comete|  thomas\_adam the man page is clear near your explanation :) | 22:16|
|xevz | Wsoprulz1299: But I never tried to make Firefox use a new size on the other hand.| 22:16|
|xevz | Oops. :P |   22:16|
|marco13185 | I might have the same problem but I don't care | 22:16|
|xevz | :P | 22:16|
|Wsoprulz129| sorry, accidentally exited | 22:17|
|xevz  |  Wsoprulz1299: But I never tried to make Firefox use a new size on the other hand.| 22:17|
|thomas\_adam |  Wsoprulz1299: Firefox being rebellious decided to ignore placement issues.  It wanted to do that for itself.  Naughty.  The ICCCM says that geometries as set by the user take precedent over anything else, and that a default is only logical when none is provided. FVWM needs to know this when deciding how to map the application.   But FF knew better.  A stubborn beast, it just didn't want to let go of doing things its own way.  What was FVWM to do?| 22:21|
|thomas\_adam |  Wsoprulz1299: So, two things happen.  FVWM can be told to ignore two hints that XClients set:  PPosition, and PSize.|  22:22|
|thomas\_adam |  Wsoprulz1299: PPosition is "Program Position" (i.e. where the hell on the screen I'm to be put, and that's final!),. and PSize -- the program size. |  22:22|
|\* hank|.oO( someone should start collecting thomas\_adam's excursions in a short story book... )| 22:23|
|thomas\_adam |  Wsoprulz1299: Guess what FF does with those two hints?  |22:23|
|thomas\_adam |  Wsoprulz1299: It sets them time and again, over and over for FVWM... how nice of it, right  Hmm, not quite.| 22:23|
|thomas\_adam |  Wsoprulz1299: One day, FVWM was very sad. |  22:23|
|thomas\_adam |  Wsoprulz1299: It didn't like the rebellious nature that FF was exerting. |  22:24|
|thomas\_adam |  Wsoprulz1299: So it stood up for itself.  It decided to fight back, and look back to its old friend, the ICCCM.| 22:24|
|thomas\_adam |  Wsoprulz1299: It's not brilliant, but it's better than it was.  You can tell various clients through the use of Style lines to (try and) ignore PPosition and PSize (see NoPPosition and VariablePSize).  |22:25|
|Wsoprulz129 |so why does it work for some and not others?  |  22:25|
|thomas\_adam |  Wsoprulz1299: FVWM rejoyced, and had a nice party that evening, at its new found functionality. | 22:25|
|\* xteddy| hugs fvwm :)| 22:25|
|Wsoprulz129| heh| 22:26|
|thomas\_adam |  Wsoprulz1299: It mapped xteddy and him bounce all around the screen.| 22:26|
|thomas\_adam |  Wsoprulz1299: FF has no way of actively setting the geometry of its window -- it *breaks* the holy document that is the ICCCM.  Yes, it has these -width and -height options, but they're just a piss in the wind. |22:28 |
|marco13185 | thomas\_adam, we must destroy it, lol | 22:28|
|thomas\_adam |  Wsoprulz1299: The only way you can probably get around this is to actively resize the window once it's mapoed, as per the example shown to you last night.|  22:28|
|thomas\_adam |  Wsoprulz1299: Since then, FVWM has lived (relatively) happy ever after.| 22:30|
|thomas\_adam |  Wsoprulz1299: ~ The End. ~|  22:30|
