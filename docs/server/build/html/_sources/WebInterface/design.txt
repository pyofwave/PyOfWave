UI Design Principles
********************

.. contents::

.. note:: I use the term "hacker" to refer to a collaberator on PyOfWave or 
   other OpenSource project. "Crackers" are what society calls "hackers".

   This is written in first person to make it easier to explain where I'm 
   coming from.

This file describes the UI principles used by POW (PyOfWave), it is here as a guide for web developer hackers. I want POW to be an example that OpenSource does *note* create bad designs, as I've seen some people in both general society and hackers believe.

.. _apple_hig:

Apple HIG Principles
====================

I find it generally agreed by users that Apple delivers the best experience, and I'm a Apple fanatic myself. However, it is odd that other organizations don't typically clue into this, because Apple freely (as in beer) shares this knowledge. This section describes the principles behind it as found at http://developer.apple.com/library/mac/#documentation/UserExperience/Conceptual/AppleHIGuidelines/XHIGHIDesign/XHIGHIDesign.html in a more general example.

Please acknowledge that a large quantity of this section is Apple's work, and does not belong to me.

Metaphors
---------

Take advantage of people's knowledge of the world by using metaphors to convey concepts and features of your application. Metaphors are the building blocks in the user's mental model of a task. Use metaphors that represent concrete, familiar ideas, and make the metaphors obvious, so that users can apply a set of expectations to the computer environment. A common example of a metaphor are folders to organize files into, which is anologues to a filing cabinet.

Metaphors should suggest a use for a particular element, but that use doesn't have to limit the implementation of the metaphor. It is important to strike a balance between the metaphor's suggested use and the computer's ability to support and extend the metaphor. For example, the number of items a user puts in the Trash is not limited to the number of items a physical wastebasket could hold.

.. todo:: Find metaphors for Wave.

Reflect the User's Mental Model
-------------------------------

The user already has a mental model that describes the task your software is enabling. This model arises from a combination of real-world experiences, experience with other software, and with computers in general. For example, users have real-world experience writing and mailing letters and most users have used email applications to write and send email. Based on this, a user has a conceptual model of this task that includes certain expectations, such as the ability to create a new letter, select a recipient, and send the letter. An email application that ignores the user's mental model and does not meet at least some of the user's expectations would be difficult and even unpleasant to use. This is because such an application imposes an unfamiliar conceptual model on its users instead of building on the knowledge and experiences those users already have.

Before you design your application's user interface, try to discover your users' mental model of the task your application helps them perform. Be aware of the model's inherent metaphors, which represent conceptual components of the task. In the letter-writing example, the metaphors include letters, mail boxes, and envelopes. In the mental model of a task related to photography, the metaphors include photographs, cameras, and albums. Strive to reflect the user's expectations of task components, organization, and workflow in your window layout, menu and toolbar organization, and use of panels.

You should support the user's mental model by striving to incorporate the following characteristics:

* **Familiarity** The user's mental model is based primarily on experience. When possible, enhance user interface components to reflect the model's symbology and display labels that use the model's terminology. Then, where appropriate, use familiar OS (Operating System) user interface components to offer standard functionality, such as searching and navigating hierarchical sets of data.

* **Simplicity** A mental model of a task is typically streamlined and focused on the fundamental components of the task. Although there may be myriad optional details associated with a given task, the basic components should not have to compete with the details for the user's attention.

* **Availability** A corollary of simplicity is availability. An uncluttered user interface is essential, but the availability of certain key features and settings the user needs is equally so. Avoid hiding such components too deeply in submenus or making them accessible only from a contextual menu.

* **Discoverability** Encourage your users to discover functionality by providing cues about how to use user interface elements. If an element is clickable, for example, it must appear that way, or a user may never try clicking it. Be sure to use OS controls properly and avoid making controls invisible to inexperienced users.

Explicit and Implied Actions
----------------------------

Each operation involves the manipulation of an object using an action. In the first step of this manipulation, the user sees the desired object onscreen. In the second step, the user selects or designates that object. In the final step, the user performs an action, either using a menu command or by direct manipulation of the object with the mouse or other device. This leads to two paradigms for manipulating objects: explicit and implied actions.

Explicit actions clearly state the result of manipulating an object. For example, menus list the commands that can be performed on the currently selected object. The name of the menu command clearly indicates what the action is and the current state of the command (dimmed or enabled) indicates whether that action is valid in the current context. Explicit actions do not require the user to memorize the commands that can be performed on a given object.

Implied actions convey the result of an action through visual cues or context. A drag-and-drop operation is a common example of an implied action. Dragging one object onto another object constitutes a relationship between the objects and an action to be performed by the drag operation. For example, dragging a file icon to the Trash implies the imminent removal of the underlying file from the file system. For implied actions to be apparent, the user must be able to recognize the objects involved, the manipulation to be performed, and the consequences of the action.

Keep these two paradigms in mind as you design your user interface. Examine the user's mental model of your application's task to help you determine when each type of action is appropriate. 

User Control
------------

Allow the user, not the computer, to initiate and control actions. Some applications attempt to assist the user by offering only those alternatives deemed good for the user or by protecting the user from having to make detailed decisions. Because this approach puts the computer, not the user, in control, it is best confined to parts of the user interface aimed at novice users. Provide the level of user control that is appropriate for your audience

Feedback and Communication
--------------------------

Feedback and communication encompass far more than merely displaying alerts when something goes wrong. Instead, it involves keeping users informed about what's happening by providing appropriate feedback and enabling communication with your application.

When a user initiates an action, always provide an indication that your application has received the user's input and is operating on it. Users want to know that a command is being carried out. If a command can't be carried out, they want to know why it can't and what can be done instead. When used sparingly, animation is one of the best ways to show a user that a requested action is being carried out. 

Consistancy
-----------

Consistency in the interface allows users to transfer their knowledge and skills from one application to another. Use standard controls to achieve consistancy with the OS. 

* **Is it consistent with Mac OS X standards?** For example, does the application use the reserved and recommended keyboard equivalents (see “Keyboard Shortcuts Quick Reference”) for their correct purposes? Is it Aqua-compliant? Does it use the solutions to standard tasks Mac OS X provides? (For more information on these solutions, see “Using Mac OS X Technologies.”)

* **Is it consistent within itself?** Does it use consistent terminology for labels and features? Do icons mean the same thing every time they are used? Are concepts presented in similar ways across all modules? Are similar controls and other user interface elements located in similar places in windows and dialogs?

* **Is it consistent with earlier versions of the product?** Have the terms and meanings remained the same between releases? Are the fundamental concepts essentially unchanged?

* **Is it consistent with people's expectations?** Does it meet the needs of the user without extraneous features? Does it conform to the user's mental model?

WYSIWYG (What You See Is What You Get)
--------------------------------------

In applications in which users can format data for printing, publish to the web, or write to film, DVD, or other formats, make sure there are no significant differences between what users see onscreen and what they receive in the final output. When the user makes changes to a document, display the results immediately; the user shouldn't have to wait for the final output or make mental calculations about how the document will look later. Use a preview function if necessary.

People should be able to find all the available features in your application. Don't hide features by failing to make commands available in a menu. Menus present lists of commands so that people can see their choices rather than try to remember command names. Avoid providing access to features only in toolbars or contextual menus. 

Forgiveness
-----------

Encourage people to explore your application by building in forgiveness—that is, making most actions easily reversible. People need to feel that they can try things without damaging the system or jeopardizing their data. Create safety nets, such as the Undo and Revert to Saved commands, so that people will feel comfortable learning and using your product.

Warn users when they initiate a task that will cause irreversible loss of data. If alerts appear frequently, however, it may mean that the product has some design flaws. When options are presented clearly and feedback is timely, using an application should be relatively error-free.

Anticipate common problems and alert users to potential side effects. Provide extensive feedback and communication at every stage so users feel that they have enough information to make the right choices.

Percieved Stability
-------------------

To give users a conceptual sense of stability, the interface provides a clear, finite set of objects and a set of actions to perform on those objects. For example, when a menu command doesn't apply to a selected object or to the object in its current state, the command is dimmed rather than omitted.

To help convey the perception of stability, preserve user-modifiable settings such as window dimensions and locations. When a user sets up his or her onscreen environment to have a certain layout, the settings should stay that way until the user changes them.

Providing status and feedback also contributes to perceived stability by letting users know that the application is performing the specified task.

Asthetic Integrity
------------------

Aesthetic integrity means that information is well organized and consistent with principles of good visual design. Your product should look pleasant on the screen, even when viewed for a long time.

Keep graphics simple, and use them only when they truly enhance usability. Don't overload windows and dialogs with dozens of icons or buttons. Don't use arbitrary symbols to represent concepts; they may confuse or distract users. The overall layout of your windows and design of user interface elements should reflect the user's mental model of the task your application performs.

Modelessness
------------

As much as possible, allow users to do whatever they want at all times. Avoid using modes that lock them into one operation and prevent them from working on anything else until that operation is completed.

POW Specific Design
===================

Familiarity
-----------

To achieve familiarity, as described in the previous section :ref:`apple_hig`, use one of the following guidelines explained below:

* Use semantic elements if the browser provides what you are looking for. This is the optimal solution, because it provides consistancy with the OS.

* Use commonly used jQuery widgets, at least users may have ran into them somewhere. A good example of this is our use of Farbtastic which is used on Twitter.

* Put any custom widgets in :file:`pyofwave_client/pyofwave_client/api/jqueryUIx.js`.

Keep a Static Screen
--------------------

Wave provides live data, which changes all the time. This may overwhelm users, so do not change anything else and keep changes to reflect either 

* An addition to a Wave 

* Or a reflow of content (which allows better layout of data and screen use). 

Place Actions in the Toolbar
----------------------------

This provides tidy organization to the screen, with all actions clearly associated with a section of the screen holding content. 

An exception to this is the edit and playback actions in the Wave view. This is placed in a secondary toolbar below the toolbar and is there to maintain a more static screen as described above. 