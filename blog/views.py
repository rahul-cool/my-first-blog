from django.shortcuts import render

def post_List(request):
    return render(request,'blog/post_List.html',{})
