@login_required
   def edit_profile(request):
    if request.POST:
    if 'logout' in request.POST:
        return HttpResponseRedirect('/logout/')

    elif 'save' in request.POST:
        user = User.objects.get(username= request.user)
        user.user=request.POST.get('user')
                    user.name=request.POST.get('name')
        user.address=request.POST.get('address')
        user.designation=request.POST.get('designation')                        
        user.email=request.POST.get('email') 
        user.role=request.POST.get('role')
        user.project=request.POST.get('project')                        
        user.task=request.POST.get('task')
        user.save()
        return HttpResponseRedirect('/view_profile/')




                   # user.set_password(form.cleaned_data['password'])

                    #drinker=user.get_profile();
                    #drinker.name=form.cleaned_data['name']
                    #drinker.address=form.cleaned_data['address']
                    #drinker.save()

    elif 'cancel' in request.POST:
        return                 HttpResponseRedirect('/view_profile/')               


user_profile = request.user.get_profile()
return render_to_response('edit_profile.html',{'profile':user_profile },context_in