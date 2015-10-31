# -*- coding: utf-8 -*-
import os
import dateutil.parser
from pydozer import BlogPost
from slugify import slugify

scalable_tech = BlogPost()

# These are all optional
scalable_tech.data['author'] = 'Tod Hansmann'
scalable_tech.data['tags'] = ['tech', 'design', 'architecture', 'opinions']

# These are not optional at all
scalable_tech.data['posted_date'] = dateutil.parser.parse('Wed Oct 21 14:00:00 MST 2015')
scalable_tech.data['title'] = '1995 Oriented Design'
scalable_tech.data['filename'] = slugify(unicode(scalable_tech.data['title']))
scalable_tech.data['hook'] = """
<p>We are not designers here at NSC.  We have an artist, but not a web designer of any kind, so how do you design a UI when all you have is really good engineers and no idea what "pretty" is outside your world?</p>
"""
scalable_tech.data['content'] = """
<p>We started making <a href="https://phonejanitor.com">Phone Janitor</a> in June.  We had the idea a long time ago, but it was time to put it into action.  It was simple, give people the ability to make all their annoying calls go away by controlling who could get through to them, and how.</p>
<p>The only problem is we had (and still have) no idea what makes a pretty UI, and had to start somewhere.  We decided to start by prototyping user interaction flow.  This meant we needed to be able to iterate, have it usable, but we weren't going to be able to do it pretty.  We aren't really web devs by trade, more systems developers.</p>
<div class="section_header">Introducing the 90s, again for the first time</div>
<img class="article_img" src="/images/early-prototype.png"/>
<div class="caption">Our never published UI.</div>
<p>We started with what we knew really well: Geocities level web design.  This style used marquees, crappy javascript counters, iframes, and tables.  It was never meant to be seen by actual customers using the thing, so we got to be a bit silly and threw it together in an afternoon.  This had two benefits.</p>
<p>First, we could do it really fast and didn't have to focus on how it looked but how it performed.  Second, we didn't have to spend a lot of time learning a new tech stack just to get a prototype.  The old web still does indeed work on modern browsers (though it's slower somehow).</p>
<p>We had a working prototype of the frontend in about 3 days, all inclusive and that was with several iterations and tests with friends (who are not devs, and certainly didn't use the web back then).  This separated feedback about function from feedback of look and feel.</p>
<div class="section_header">Gussy it up</div>
<p>We opted to let our skills in modern javascript come from doing everything raw, without a framework.  We wrote our own ajax call mechanisms and bumped heads with every browser's ridiculous assumptions about what is or is not a good user experience.  (Later I plan to write about how Firefox is the new IE, and how silly Microsoft was for not playing .wav files.)</p>
<img class="article_img" src="/images/oldbusted-routing.png"/>
<div class="caption">The soft launch UI served several customers well, even ones that weren't beta customers.</div>
<p>What we did ended up being more than usable, but had some visual issues for a lot of people, and didn't work on mobile (a failure to understand the significance of mobile on our part).  This wound up getting posted by one of our beta customers and it got reposted lots of places.  It was very strange to watch.</p>
<p>Ultimately we needed to changed it, which we knew we'd have to when we could afford a web designer of the right calibre. This ended up being a push we had to make sooner rather than later.</p>
<div class="section_header">Back to Formula</div>
<p>Luckily, we didn't have to remake any of our backend API to redesign the front-end.  This was great, but it came with a cost.  Our self-made "framework" had no warnings on the console, no CSS deprecated nonsense, and would load in less than a second on a dial-up connection.  The new one was about 8 times the size and the frameworks we use yell about a lot of things we can't avoid, despite those things not being an actual problem.</p>
<img class="article_img" src="/images/newhotness-routing.png"/>
<div class="caption">The "improved" UI for our actual launch, which will still not be the last.</div>
<p>This iterative process is not new, but it started with function over form and then adopted form to the function.  We believe that is a good possible design philosophy, and will probably use it in the future.  We do not pretend to think this will fit everyone's workflow, but if you have little design skills, this might be a good starting pattern.  It certainly led to a performant and useful UI for us, and gives us room to improve on a lot of fronts we're comfortable knowing we lack in for now.</p>
"""
