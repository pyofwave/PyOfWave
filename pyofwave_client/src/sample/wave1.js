define(['sample/builder'], function($) {
	return $('wave_wave', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/', modified: '09:23:30 01/01/2013'},
		$('wave_author', {}, 'mal@serenity.ship'),
		$('wave_wavelet', {}, 
			$('wave_participant', {}, 'mal@serenity.ship'),
			$('wave_participant', {}, 'derrial@serenity.ship'),
			$('wave_participant', {}, 'spock@federation.gov'),
			$('wave_thread', {}, 
				$('wave_post', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/0', modified: '09:23:30 21/12/2012'},
					$('wave_participant', {}, 'mal@serenity.ship'),
					$('wave_participant', {}, 'derrial@serenity.ship'),
					$('wave_p', {s: 'h'}, 'POW Sample Wave'),
					$('wave_p', {}, 'Have you noticed that the frame surrounding this blip ("wave post") identifies it\'s last contributor. This makes for a lighter weight and more versitile design (especially with soft, rounded corners) for now the only dominant item contained inside the blip is it\'s content.'),
					$('wave_p', {}, "Yet still we maintained all the metadata presented in Google Wave, and more. Miracle, isn't it? I acknowledge Edward Tufte's Envisioning Information."),
					$('wave_thread', {},
						$('wave_post', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/0/0', modified: '10:24:31 22/12/2012'},
							$('wave_participant', {}, 'derrial@serenity.ship'),
							$('wave_p', {}, 'This is a blip in a thread. You notice that it is visually seperated from the last thread through use of padding? The power of whitespace.'),
						),
						$('wave_post', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/0/1', modified: '11:25:32 23/12/2012'},
							$('wave_participant', {}, 'spock@federation.gov'),
							$('wave_p', {}, 'Yet all the blips are held closely together, making a solid thread.'),
							$('wave_thread', {},
								$('wave_post', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/0/1/0', modified: '12:26:33 30/12/2012'}, 
									$('wave_participant', {}, 'spock@federation.gov'),
									$('wave_p', {}, 'And another layer in, so as to show that embedded comments work well. Don\'t they?')
								)
							)
						)
					)
				),
				$('wave_post', {wave_href : 'wave://mal@serenity.ship/4rep9jrjkljklk/1', modified: '09:23:30 1/01/2013'},
					$('wave_participant', {}, 'spock@federation.gov'),
					$('wave_p', {}, 'We have also avoided breaks in reading, for the Apple HIG said "Only show the user what they want to see" and Edward Tufte counsels to keep comparible items within an eyespan. Don\'t you prefer it?'),
					$('wave_p', 'This sample data is explicitely organized to aid transition to something more real.')
				)
			)
		)
	)
});
