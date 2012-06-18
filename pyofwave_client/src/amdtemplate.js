/* AMDTemplates
*
* Loads KnockOut.js templates from a AMD store, used to make POW more self
* contained.
*/
define(['../api/knockout-2.1.0', 'tpl/index.js'], function(ko, templates){
	ko.templateSources.stringTemplate = function(template, templates) {
    this.templateName = template;
    this.templates = templates;
	};

	ko.templateSources.stringTemplate.prototype = {
		text: function(value) {
     if (arguments.length === 0) {
        return this.templates[this.templateName];
     }
     this.templates[this.templateName] = value;
		},
		data: function(key, value) {
			this.templates._data = this.templates._data || {};
			this.templates._data[this.templateName] = this.templates._data[this.templateName] || {};

			if (arguments.length === 1) {
			    return this.templates._data[this.templateName][key];
			}

			this.templates._data[this.templateName][key] = value;
		}
	}

	function createStringTemplateEngine(templateEngine, templates) {
    templateEngine.makeTemplateSource = function(template) {
        return new ko.templateSources.stringTemplate(template, templates);
    }
    return templateEngine;
	}

	ko.setTemplateEngine(createStringTemplateEngine(new ko.nativeTemplateEngine(), templates));
})
