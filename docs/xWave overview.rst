xWave
++++++

When collaborating to try to standardize Wave, I, "alcinnz" Adrian  
Cochrane, picked up on a few ideas which combined to give a much  
simpler protocol design and therefore architecture. I call the result  
xWave for XMPP or XML. This document describes the decisions behind it.

XMPP
======

A major decision in this architecture was to raise the task of XMPP,  
commanly used in IM as Jabber, from the Federation syntax to the whole  
underlaying system.

XMPP's well tested (in Jabber) SASL is a great benefit of XMPP.  
Authentication will no longer need to be provided by Wave as that's  
provided by SASL (with the same eMail-like syntax), but even better  
servers can authentication with SASL. This helps a lot with Federation.

Another nicety of XMPP is BOSH (Bidirectional Over Secure HTTP) which  
will ease development of the web client. There are a number of nice  
adapters and clients for BOSH like Strophe. Hopefully our choice of  
XMPP Server, Python XMPP Server, will finish their work on a builtin  
BOSH.

Over all, XMPP is a great protocol with plenty of room for extension  
and takes care of the underlying system behind all the forms of  
protocols we need.

Full Federation
===============

The idea that enabled the move to XMPP was full decentralisation. In  
networking, there's a practice of providing alternate routes to  
minimize "failure zones", the number of devices effected by a failure.  
The plan here was to follow Git on this practice by making Federation  
another client.

Handling Federation as a client dramatically simplifies the protocols,  
as we no longer need to define seperate client protocols and delta  
application.

Why operations instead of deltas? Operations are atomic units which  
can be applied *slightly* out of order to acheive the same results.  
They also encapsulate nice in XMPP/XML (better than JSON as Google  
did) and are more succinct and efficient (can be routed).

Event System
==============

The client protocols have always registered events, but the events  
needed a lookover for Federation to view events received as  
operations. Most of these events (apart contributorsChanged) were  
notifications that a specific operation was applied, so I used the  
operations as their events.

This allows for a symmetrical protocol in which each server treats all  
other servers as clients. In such a system, there's no central server,  
reducing chances of failure.

However, servers still need to be handled differently, and I'm still  
engineering exactly how in the Federation operations.

Cursor Based Locking
=====================

The operations that deal with editing documents needed a redesign with
these changes, because without a central server, I can't have a central
version. This causes difficulty in applying editting operations.

To get around this drawback, I refactored selection information out of
the edit operations into it's own so I can track it and perform locking
based on that information.

Minor changes
===============

I have added to the standards items which were missing from Google's  
protocols such as

- An inbox system (wrapping searches)
- Moving from the term "blip" to "post" to use language already in common use.
- Contacts via an extension of rosters
   > Added colour field for an early UI decision of mine
- URL linking & identification
- Gadget redesign

Gadget Redesign
----------------

Gadgets are mini RIAs, so I redesigned gadgets with a simpler API  
(using KVO, Key Value Observing, and the latest JS) and fully  
JavaScript based (easier for gadgets & clients to implement).
