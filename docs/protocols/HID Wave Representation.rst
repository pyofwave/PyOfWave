HID Wave UI
+++++++++++

Overview
========

This is a non-normative standard aiming to encourage consistancy in visual wave (refered to as the interface) representations on non-mobile, full-color screens. 

HID stands for High Information Density, referring to the fact that every pixal in this design communicates something, even the white/negative -space. 

Adhearing lightly to this standard will help ease the initial intuitiveness of your Wave client, and is designed to ease the long term intuitiveness as well as short term. 

Underlaying Design Principles
=============================

To keep this standard "User Friendly", it builds some principles defined here and drawn from sources considered by the mainstream to be "User Friendly".

Inspiration
-----------

The principles in this section draw from three main sources, which all follow an approach called User Centered Design. 

- Edwarde Tufte Envisioning information

	Non-computing specific. Uses detail, layering, small multiples, and color as major techniques to communicate to intelligent readers. 

- Apple, Inc.

	Has revolutionized desktop/laptop, smart phone, and tablet interfaces and spurred those markets with their designs through their high-control closed-source systems. 

- GNOME

	Was chosen by the Ubuntu OS, which aims to be the most user friendly Open Source operating and is currently the the most popular of them. Echoes several principles of Apple's while also drawing from other sources. 

Focus on text
-------------

Since Wave is so flexible in usage, anything except the contributed text *can* be noise. Therefore all non-contributed text must appear minimal and unobtrusive. 

Color as Noun/Quantity/Representation/Beauty
--------------------------------------------

Tufte writes that the fundamental uses of color are: "*to label* (color as a noun), *to measure* (color as a quantity), *to represent or imitate reality* (color as representation), and *to enliven or decorate* (color as beauty)." Color should be used effectively to deepen and minimalize the interface. 

Consistancy
-----------

Apple and GNOME agree that applications should be consistant with itself, the OS, and the world. This means that users have less to learn and will more quickly pick up your application.

In using this standard, it is recommended that OS equivalants are used as inputs, native menus, tooltips, and scrolling is used.

Metaphors
---------

Apple and GNOME also agree that metaphors to the physical world are used to enhance consistancy to the outside world. In this standard, a bulletin board or other shared layout of notes is used as a metaphor. 

If it won't look "cheesy" on your target OS (i.e. builtin applications do it) use a unobtrusive background image to emphasize this metaphor.

Keep Comparable Items in an Eyespan
-----------------------------------

Tufte advises that comparable items must be kept within an eyespan. Comparable items here are considered the siblings in a thread. 

To Clarify Add Detail
---------------------

Refered to by Tufte as micro-macro designs, precise detail is drawn to give an effective big picture.

Animation to Communicate
------------------------

Apple states that animation is effective when used to communicate and not to look good. 

Layering & Seperation
---------------------

Tufte states that to avoid confusion and clutter, differently styled layers can be used to seperate information at the risk of the 1+1=3 effect (as in | + | = | |) or noise. 

Representation
==============

Participants
------------

To label, participants are refered to as colors (as a noun) adjusted from hues (as in HSV) provided by the participant's account. They're alias' color, if present, should outline them. This dramatically cuts down noise.

To reference (in participant lists), avatars from their account are displayed with a border of their color (to act as a key). Their name (again provided by their account) should be displayed underneath their avatar.

Either way, tooltips should identify users by their Wave Address. 

Posts
-----

Uses a metaphor of paper or "post-its" to communicate individual messages that go together. This is communicated by a seperating frame (and perhaps light background) and a light background color (consistancy here is important as unconsistancy may mess with the display of user's text). 

The frame is color coded to the last participant to edit it, seperating posts via layering. Animation can be used to signify changes. 

Clicking the frame should reveal a menu providing options to edit post content, insert an inline reply, or private reply all from the clicked point. Editing options should be outside the wave representation and isn't standardized here.

In the top right corner (which shouldn't be missed by user's content) should be the time/date of the last edit (localized) underlined by all participants of the post as colors. This area should signify clickability using system techniques, e.g. pointer cursor, and show a menu of actions to perform on that post (leniency on exact options). 

In the bottom right corner should be an icon, e.g. a quote mark, which reveals the post's replies thread by animation. In the bottom left corner, an icon may be used to reveal

Typing
------

Several subtle techniques should be used to communicate the people who are editing the wave. 

Their selection should have that contributor's color with opacity (to differentiate from set background colors) and a "cursor" at the end again color coded to that participant. The cursor can be anything common on the system, as long as it does not offset the text layout.

The box under the time of the post their editing should shift downward to signify a change and their name in the participants bar should change color, which may be their color. 

Names aren't placed in posts because they may qualify as noise for some use cases.

Threads
-------

As the bulletin board metaphor organizes posts by implicit grouping, so would this representation. 

Threads should be representated by a sequence of justified posts with a *small* amount of whitespace in between (to differentiate them without seperating them from the thread). 

The last item should look like an empty post with no date or participants on it with the user's color as it's border (to signify it can be theirs). It may have grey text reading along the lines of "Add new post". 

They should be paired with a consistant icon which shows and hides the thread via animation unless they are the root thread of a wavelet. They should be initially hidden so they do not split comparable items (siblings in a thread) and decrease the readability. 

Wavelets & Waves
----------------

Wavelet representation should appear to be their root thread with a "participants bar" above and tags below, all in filled rounded rectangles simalor to posts (consistancy).

The participants bar should appear as a horizontal sequence of the participants full representation followed by an icon for adding a participant. Online, offline, and robot users (judging by their profile) should be seperated by a thin line. 

Waves should render as their root wavelet.

Tags
----

Tags should should render as a filled bar (to differentiate) at the bottom of their parent item. In this bar should be a sequence of circled individual tags (in the form *key* : *value* or *key*), where private and public tags have different backgrounds. 
