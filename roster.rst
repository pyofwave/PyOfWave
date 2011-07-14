kaPOW Roster
++++++++++++

In order to speed production of POW, I, alcinnz, will roster off tasks for extensions to add to POW. Each root extension will be fairly equal and sizable while the leafs would generally, if it has a parent, be fairly small. To register for a task, please message me and I will put you on this roster.

Once everyone has completed their tasks, this document will turn into credits with the final names.

Participation Instructions
==========================

To participate,

#. Ensure you've got a GitHub account, and have installed Git. 

#. Select a task from the list below (preferably a root one, but if you're not up for that, choose a leaf).

#. Message me, alcinnz, I will add your name under that item. 

#. Fork this project, setup a repository on your machine, and install Twisted and zope.interface.

#. Get hacking! I'll be watching.

Standards will be standardized on XCCC. A link will be provided soon.

Roster Tasks
============
In format:
Task Overview (notes) -- implementer's GitHub username ( )

Between the final parenthesese will appear an X when the task is completed.

Protocols
---------

Please be aware we are currently in the middle of standardizing Wave, so these protocols may change on you. It'll be important to stay up to date on discussions and any concerns will be heard. 

Look at this as an opportunity, for you may be implementing a reference implementation. Also any protocol issues will be fixed and you don't have to be stuck with them.

- Federation Protocol (via python-xmpp-server) -- mor1 ( )

- Wave Client Protocol <client basic> -- alcinnz ( )

- Authentication Protocols

   - IP authentication

   - SSL <client basic>

   - alias (via HTTP for groups)

Integration (nice, but not necessary)
-----------

- RSS notification

- SMTP receive (robot for more challenging sending/reply)

- Test Web-app

Storage Schemes (either of these can be implemented for basic features)
---------------

- SQL

- CouchDB

Miscellaneous (all required for basic features)
-------------

- Operations (listed "domains")- txusinho ( )

  - auth

  - robot

  - wavelet

  - blip

  - document

- Document-Based Authentication