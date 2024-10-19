from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.decorators import login_required

@login_required
def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migraciones ejecutadas.")
