# coding=utf-8
'''
https://alex-d.github.io/Trumbowyg/documentation.html
'''

from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils import translation
from json import dumps


class EditorWidget(Textarea):

    class Media:
        css = {
            'all': (
                'bootstrap/dist/css/bootstrap.min.css',
                'trumbowyg/dist/ui/trumbowyg.css',
            )
        }

        js = (
            'jquery/dist/jquery.min.js',
            'bootstrap/dist/js/bootstrap.min.js',
            'trumbowyg/dist/trumbowyg.min.js',
        )

    def __init__(self, attrs=None, buttons=None):
        super(EditorWidget, self).__init__(attrs=None)
        self.editor = {}
        if buttons:
            self.editor['btns'] = buttons
        lang = translation.get_language()
        if lang:
            self.editor['lang'] = lang
            js = 'trumbowyg/dist/langs/%s.min.js' % lang
            if js not in self.Media.js:
                self.Media.js += (js, )

    def render(self, name, value, attrs=None):
        output = super(EditorWidget, self).render(name, value, attrs)
        script = u'''
            <script> $('#id_%s').trumbowyg(%s); </script>
        ''' % (name, dumps(self.editor))
        output += mark_safe(script)
        return output
