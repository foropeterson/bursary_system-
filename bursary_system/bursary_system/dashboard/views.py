# views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Ng-CDF Team').exists())
def dashboard(request):
    # Your dashboard view logic
    return render(request, 'dashboard.html')
