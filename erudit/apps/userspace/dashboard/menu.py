from django.utils.translation import ugettext_lazy as _

from navutils import menu

main_menu = menu.Menu('main')
menu.register(main_menu)

userspace = menu.Node(
    id='userspace',
    label=_('Mon espace'),
    pattern_name='userspace:dashboard',
    context={'icon': 'fa-home'},
)
main_menu.register(userspace)

journal = menu.AnyPermissionsNode(
    id='journal',
    label=_('Information de la revue'),
    pattern_name='userspace:journal:journal-information',
    permissions=['journal.edit_journal', ],
    context={'icon': 'fa-folder-o'},
)

editor = menu.AnyPermissionsNode(
    id='editor',
    label=_('Dépôts de numéros'),
    pattern_name='userspace:editor:issues',
    permissions=['editor.manage_issuesubmission', ],
    context={'icon': 'fa-folder-open-o'},
)

permissions = menu.AnyPermissionsNode(
    id='permissions',
    label=_('Permissions'),
    pattern_name='userspace:permissions:perm_list',
    permissions=['userspace.manage_permissions', ],
    context={'icon': 'fa-lock'},
)

subscription = menu.AnyPermissionsNode(
    id='subscription',
    label=_('Abonnements individuels'),
    pattern_name='userspace:subscription:account_list',
    permissions=['subscription.manage_account', ],
    context={'icon': 'fa-users'},
)

userspace.children.append(journal)
userspace.children.append(editor)
userspace.children.append(permissions)
userspace.children.append(subscription)
