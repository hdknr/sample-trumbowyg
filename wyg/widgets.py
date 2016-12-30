# coding=utf-8

from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
# from django.utils.translation import get_language, get_language_info


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
            'trumbowyg/dist/langs/ja.min.js',
        )

    def render(self, name, value, attrs=None):
        output = super(EditorWidget, self).render(name, value, attrs)
        # lang = get_language_info(get_language())['code']
        script = u'''
            <script>
            $('#id_%s').trumbowyg();
            </script>
        ''' % (name)
        output += mark_safe(script)
        return output
