Progressive Wave Representation
+++++++++++++++++++++++++++++++

Overview
========

This is a non-normative standard which aims to encourage consistancy in wave representations (refered to as the interface) on mobile screen sizes or other output device of limited real-estate (e.g. voice). With alterations it may also work on large screen sizes. 

Progressive refers to both progressive navigation and enhancement, both of which are present in this standard. 

Adhearing lightly to this standard will ease the initial intuitiveness of your Wave client on devices with limited real-estate and is designed for long term intuitiveness as well as short term. However, this standard is not suited well to large usage (where you should use HID) but for quick usage. 

Underlaying Design Principles
=============================

To keep this standard "User Friendly", it builds some principles defined here and drawn from sources considered by the mainstream to have guided "User Friendly" smart phones.

Inspiration
-----------

The inspiration here is drawn from two main sources:

- Apple iOS HIG

	Having been the first to design the common use smart phone design, inspiring several simalor projects most notably Google Android and jQuery Mobile, Apple may know these designs the best.

- Wave in a Box alternative UI (TODO: find it's name)

	A contributor to Apache Wave in a Box has built an alternative navigation based UI mockup. With it's own benefits and drawbacks, the ideas in this design should fit on a smart phone screen and the drawbacks would be unavoidable. 

Navigation
----------

Handled consistantly be modern smartphones, navigation is a long standing design component primarily used in games, phones, file systems, and websites. Apple implemented the modern phone design in their iPhone UI components of a Navigation View Controller and Table View Controller and dictated their use in iOS in the iOS HIG. 

This design consists of a header (Navigation Bar) with a labeled back button, title, and optional additional button with a Table or List View underneath. This List View consists of several large tapable cells seperated by lines. Each cell consists of a lable or content on the left and an icon (sometimes tapable) on the right. 

Minimize UI
-----------

Apple dictates that any non crucial feature is removed from smart phone apps. This is a good practice with limited real-estate, so it's followed here.

All Tapable Objects > 44 pixels^2
---------------------------------

Another dictation of Apple's, any smaller object would be hard to tap leading to frustration.

Screens
=======

This design has various screens as it can't fit them all on one screen. However these screens all fit in the navigation system and may draw from the List View design.

All unspecified screens are purpousefully so and left up to implementors to decide.

Threads
-------

A thread should be represented by a List View like list of all it's posts. A plus button in the Navigation Bar should create a new post and enable editing of it. 

Each post should be split into three parts: last editor, content, and "disclosure" icon. The last editor should be a thin bar with the address of the last user to edit the post and the date in their color. The content should fill most the cell with the provided text. The disclosure icon should navigate to the reply thread. Taping the cell should activate editing.

What exactly activating editing consists of is not defined in this document.

Wavelets
--------

Should appear simalor to the thread screen for it's root thread, with an additional header and footer in the list. 

The header should contain avatars of the top participants where tapping the row icon shows a full list and tapping each avatar leads to their profile.

The footer should lead to the tags on the wavelet. 

Participants
------------

Should show all the participant avatar in a grid or list with a plus button in the Navigation Bar to add a new one. 

Gadgets/Attachments
-------------------

Gadgets and attachments should have an (almost) full screen real-estate to render on, navigated to from the content of the parent post. They may be paged to allow easy access to all attachments. 
