from django.template.context_processors import csrf

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from erudit.models import Journal, Publisher
from editor.models import IssueSubmission
from editor.forms import IssueSubmissionForm, IssueSubmissionUploadForm


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)


class DashboardView(LoginRequiredMixin, ListView):

    template_name = 'dashboard.html'

    def get_queryset(self):

        publishers = Publisher.objects.filter(
            members=self.request.user
        )

        return IssueSubmission.objects.filter(
            journal__publisher=publishers
        ).order_by(
            'journal__publisher'
        )


class IssueSubmissionCreate(LoginRequiredMixin, CreateView):
    model = IssueSubmission
    form_class = IssueSubmissionForm
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(csrf(self.request))
        return context

    def get_form(self, form_class):
        form = super().get_form(form_class)
        form.fields['journal'].queryset = Journal.objects.all()
        form.fields['journal'].initial = form.fields['journal'].queryset.first()
        form.fields['contact'].initial = form.fields['contact'].queryset.first()
        return form


class IssueSubmissionUpdate(LoginRequiredMixin, UpdateView):
    model = IssueSubmission
    form_class = IssueSubmissionUploadForm
    template_name = 'form.html'

    def get_form(self, form_class):
        form = super().get_form(form_class)
        if self.get_object().status in (
                IssueSubmission.VALID, IssueSubmission.SUBMITTED):
            form.disable_form()
        return form

    def dispatch(self, request, *args, **kwargs):
        submission = IssueSubmission.objects.get(pk=kwargs['pk'])
        if not submission.has_access(request.user):
            return HttpResponseRedirect(reverse('editor:dashboard'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('editor:dashboard')


class IssueSubmissionList(LoginRequiredMixin, ListView):

    template_name = 'issues.html'

    def get_queryset(self):

        publishers = Publisher.objects.filter(
            members=self.request.user
        )

        return IssueSubmission.objects.filter(
            journal__publisher=publishers
        ).order_by(
            'journal__publisher'
        )
