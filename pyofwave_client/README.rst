PyOfWave Client
===============

PyOfWave Client is the major web-based Wave UI for Wave Providers to embed in their site. It follows guidelines of GNOME, Apple, and Edwarde Tufte to create a user friendly UI through User Centered Design, with full keyboard accessibility.

It builds upon a custom engine (an XML builder, data access, & bindings system) which transforms our XML between our Model, View, & Controller and aims to:

- Be User Friendly :-|)
- Keyboard Accessible
- Small footprint
- Cross browser
- i18n-ized
- Embeddable and themable

Underlaying Technologies
------------------------

- Strophe.js
- jQuery
- RepoTheWeb
- Knockout.js (finally found a framework which seems to support what I want to do)

jQuery contrib:

- jsTree
- Farbtastic
- jQueryUI

Compilation
-----------

PyOfWave client is compiled using Require.js/Almond.js with help from the i18n and text extensions.

To compile, run the following command from the src directory:

		node ../lib/r.js -o name=../lib/almond include=amdtemplate out=../../build/pow.min.js baseUrl=.
