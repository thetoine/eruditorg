from django import forms
from django.utils.translation import gettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from datetimewidget.widgets import DateWidget
from django_select2.forms import Select2Widget

from plupload.forms import PlUploadFormField

from editor.models import JournalSubmission


class JournalSubmissionForm(forms.ModelForm):
    class Meta:
        model = JournalSubmission

        fields = [
            'journal',
            'volume',
            'date_created',
            'contact',
            'comment',
            'submission_file'
        ]

        widgets = {
            'date_created': DateWidget(
                attrs={'id': "date_created"},
                usel10n=True,
                bootstrap_version=3,
                options={
                    'todayHighlight': True,
                }
            ),
            'journal': Select2Widget,
            'contact': Select2Widget,
        }

    submission_file = PlUploadFormField(
        path='uploads',
        options={
            "max_file_size": '5000mb'
        }
    )

    def __init__(self, *args, **kwargs):

        super(JournalSubmissionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'

        self.helper.add_input(
            Submit('submit', _("Envoyer le fichier"))
        )
