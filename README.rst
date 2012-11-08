PyOfWave server and webclient (in development, pre-beta)
=======================

Wave is the features of common communication platforms (eMail, IM, forums, wikis, social networking, etc.) merged into one system. 

PyOfWave implements Wave in Python (for the browser) with a re-factored XMPP based protocol dubbed xWave. It uses compiled & compressed CoffeeScript for Web browsers. 

We hope to keep PyOfWave a moderate code base for maintainability and speed, and in cases download size. We also focus on decentralization (we don't create everything users might want in house) and provide strong customizability. 

Furthermore, we hope to undo whatever it was that made Google Wave fall (lack of "integration"? Complex UI? Centralized groups & embedding/linking? Bad pitch?). Whatever it was, we'll do it right. 

Components
----------

PyOfWave has a number of components, including:

- Server
- Client
- Mobile (planned)
- Pad (planned)

Each has it's own README which talks about it in relation to PyOfWave, although they can be substituted for a compatible one (except the planned Mobile and Pad will use other components directly). 

Technical Components
--------------------

Although PyOfWave for the most part uses well tested dependancies, in some cases we had to write software ourselves for satisfaction. These technical projects include:

- Mozilla RepoTheWeb

Other Software
--------------

We provide additional projects to be used as tools and reference implementations, but in order to encourage decentralization and decrease workload I (Adrian Cochrane "alcinnz", Project Manager) want to limit these. This way competition can grow in place of "official" robots. 

These include:

- pywavebot (planned)
- iWave (planned)
- robots (planned, lacks repo)