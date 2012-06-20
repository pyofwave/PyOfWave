/* Contacts sample data
*
* Extremely geeky sample contacts for PyOfWave Client development.
*/
define(['sample/builder'], function($) {
	return [
		$('group', {name : 'StarWars'},
			$('foaf_person', {foaf_name: 'Obi Wan Kanobi', foaf_mbox: 'obiwan@jedi.org', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Anakin Skywalker', foaf_mbox: 'anakin@jedi.org', foaf_depiction: 'avatars/anakin.jpg'}),
			$('foaf_person', {foaf_name: 'Yoda', foaf_mbox: 'yoda@jedi.org', foaf_depiction: 'avatars/yoda.jpg'}),
			$('foaf_person', {foaf_name: 'Padme Amidala', foaf_mbox: 'amidala@senate.gov.gr', foaf_depiction: 'avatars/padme.jpg'}),
			$('foaf_person', {foaf_name: 'Darth Vadar', foaf_mbox: 'vadar@senate.gov.gr', foaf_depiction: 'avatars/vadar.jpg'}),
			$('foaf_person', {foaf_name: 'Luke Skywalker', foaf_mbox: 'luke@jedi.org', foaf_depiction: 'avatars/luke.jpg'}),
			$('foaf_person', {foaf_name: 'Han Solo', foaf_mbox: 'han@resistance.org', foaf_depiction: 'avatars/solo.jpg'}),
			$('foaf_person', {foaf_name: 'Princess Leia Organa', foaf_mbox: 'leia@resistance.org', foaf_depiction: 'avatars/leia.jpg'})
		),
		$('group', {name : 'Doctor Who'}, 
			$('foaf_person', {foaf_name: 'The Doctor', foaf_mbox: 'doctor@timelords.gal', foaf_depiction: 'avatars/doctor.jpg'}),
			$('foaf_person', {foaf_name: 'The Master', foaf_mbox: 'master@timelords.gal', foaf_depiction: 'avatars/master.jpg'})
		),
		$('group', {name : 'Star Gate'},
			$('foaf_person', {foaf_name: "Jack O'Neill", foaf_mbox: 'oneill@sgc.airforce.com', foaf_depiction: 'avatars/oneill.jpg'}),
			$('foaf_person', {foaf_name: 'Daniel Jackson', foaf_mbox: 'jackson@sgc.airforce.com', foaf_depiction: 'avatars/jackson.jpg'}),
			$('foaf_person', {foaf_name: 'Samantha Carter', foaf_mbox: 'carter@sgc.airforce.com', foaf_depiction: 'avatars/carter.jpg'}),
			$('foaf_person', {foaf_name: "Tea'lc", foaf_mbox: 'tealc@sgc.airforce.com', foaf_depiction: 'avatars/tealc.jpg'}),
			$('foaf_person', {foaf_name: 'George Hammond', foaf_mbox: 'hammond@sgc.airforce.com', foaf_depiction: 'avatars/hammond.jpg'})
		),
		$('group', {name : 'Firefly'},
			$('foaf_person', {foaf_name: 'Mal Reynolds', foaf_mbox: 'mal@serenity.ship', foaf_depiction: 'avatars/reynolds.jpg'}),
			$('foaf_person', {foaf_name: 'Zoe Washburne', foaf_mbox: 'zoe@serenity.ship', foaf_depiction: 'avatars/washburne.jpg'}),
			$('foaf_person', {foaf_name: 'Hoben Washburne', foaf_mbox: 'hoben@serenity.ship', foaf_depiction: 'avatars/hoben.jpg'}),
			$('foaf_person', {foaf_name: 'Inara Serra', foaf_mbox: 'inara@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Jayne Cobb', foaf_mbox: 'jayne@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Kaylee Frye', foaf_mbox: 'frye@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Simon Tam', foaf_mbox: 'simon@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'River Tam', foaf_mbox: 'river@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Derriel Book', foaf_mbox: 'derrial@serenity.ship', foaf_depiction: 'avatars/obiwan.jpg'})
		),
		$('group', {name: 'Startrek'},
			$('foaf_person', {foaf_name: 'James T. Kirk', foaf_mbox: 'kirk@federation.gov', foaf_depiction: 'avatars/kirk.jpg'}),
			$('foaf_person', {foaf_name: 'Spock', foaf_mbox: 'spock@federation.gov', foaf_depiction: 'avatars/spock.jpg'}),
			$('foaf_person', {foaf_name: 'Leonard McCoy', foaf_mbox: 'mccoy@federation.gov', foaf_depiction: 'avatars/mccoy.jpg'}),
			$('foaf_person', {foaf_name: 'Montgomery Scott', foaf_mbox: 'scott@federation.gov', foaf_depiction: 'avatars/scott.jpg'}),
			$('foaf_person', {foaf_name: 'Nyota Uhura', foaf_mbox: 'uhura@federation.gov', foaf_depiction: 'avatars/uhura.jpg'}),
			$('foaf_person', {foaf_name: 'Hikaru Sulu', foaf_mbox: 'sulu@federation.gov', foaf_depiction: 'avatars/sulu.jpg'}),
			$('foaf_person', {foaf_name: 'Pavel Checkov', foaf_mbox: 'checkov@federation.gov', foaf_depiction: 'avatars/obiwan.jpg'}),
			$('foaf_person', {foaf_name: 'Janice Rand', foaf_mbox: 'rand@federation.gov', foaf_depiction: 'avatars/rand.jpg'}),
			$('foaf_person', {foaf_name: 'Christine Chapel', foaf_mbox: 'chapel@federation.gov', foaf_depiction: 'avatars/chapel.jpg'})
		)
	]
})
