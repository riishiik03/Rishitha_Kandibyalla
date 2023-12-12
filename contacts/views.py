from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm



# View to list all contacts
def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts_list.html', {'contacts': contacts})

# View to create a new contact
def contacts_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contacts_form.html', {'form': form})

# View to display contact details
def contacts_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts/contacts_detail.html', {'contact': contact})

# View to edit an existing contact
def contacts_edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts_detail', id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contacts_update.html', {'form': form})

# View to delete a contact
def contacts_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('contacts_list')
    return render(request, 'contacts/contacts_confirm_delete.html', {'contact': contact})

#view for creating a contact
def contacts_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contacts_create.html', {'form': form})



