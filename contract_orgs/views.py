from django.shortcuts import render
from .models import ContractOrg


def contract_orgs_index(request):
    contract_orgs = ContractOrg.objects.all()
    count_contract_orgs = contract_orgs.count()
    context = {'contract_orgs': contract_orgs, 'count_contract_orgs': count_contract_orgs}

    return render(request, 'contract_orgs/index.html', context)
