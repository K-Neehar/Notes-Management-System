from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StForm
from NotesApp.models import Student,Notes,Requests,Accepted
from NotesManagement import settings
from django.core.mail import send_mail

# Create your views here.

def landing(request):
	return render(request,'landingpage.html')

def login(request):
	if request.method=="POST":
		try:
			g=Student.objects.get(email=request.POST['email'])
			if request.POST['Pass']==g.password:
				print("Successssss")
				return redirect('/mainpage/'+str(g.id))
		except:
			print("Faileddd")

	return render(request,'login.html')

def register(request):
	if request.method=="POST":
		g=StForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/')
		else:
			print(g.errors)
	g=StForm()
	return render(request,'register.html',{'form':g})

def mainpage(request,id):
	return render(request,'mainpage.html',{'ID':id})

def home(request,n_id):
	z=Student.objects.get(id=n_id)
	return render(request,'home.html',{'note':z,'ID':n_id})

def createnote(request,id):
	if request.method == 'POST':
		st_id = id
		s_sbj = request.POST['sb']
		s_note = request.POST['note']
		w=Notes.objects.create(sid=st_id,sub=s_sbj,note=s_note,like=0,dislike=0)
		# return redirect('/mainpage/'+str(st_id))	
		return render(request,'createnote.html',{'ID':id})

	return render(request,'createnote.html',{'ID':id})

def displaynote(request,id):
	d=Notes.objects.all()
	e=Student.objects.get(id=id)
	return render(request,'displaynote.html',{'ID':id,'notes':d,'ids':e})

def viewnote(request,id,nid):
	d=Notes.objects.get(id=nid)
	return render(request,'viewnote.html',{'ID':id,'notes':d})

def updatenote(request,id,nid):
	z=Notes.objects.get(id=nid)
	if request.method == 'POST':
		z.sub=request.POST['s_sub']
		z.note=request.POST['s_note']
		z.save()
		return redirect('/display/'+str(id))
	return render(request,'updatenote.html',{'ID':id,'notes':z})

def deletenote(request,id,nid):
	z=Notes.objects.get(id=nid)
	if request.method=="POST":
		z.delete()
		return redirect('/display/'+str(id))
	return render(request,'deletenote.html',{'ID':id,'notes':z})

def othernote(request,id):
	d=Notes.objects.all()
	e=Requests.objects.filter(rid=id)
	e1=Accepted.objects.filter(rid=id)
	values_list = [ obj.ntid for obj in e]
	values_list1 = [ obj.nid for obj in e1]
	print(values_list)
	return render(request,'othernote.html',{'ID':id,'notes':d,'req':values_list,'req1':values_list1})

def requestnote(request,id,sid,nid,s_sub,s_note):
	g=Student.objects.get(id=id)
	g1=Student.objects.get(id=sid)
	w=Requests.objects.create(sname=g.name,rid=id,sub=s_sub,atid=sid,ntid=nid)
	sbj="Request from Notes Management App"
	file_content = open(r"D:\Django\request_mail_sending.txt").read()
	file_content = file_content.replace("[Student's Name]",g.name)
	file_content = file_content.replace("[Subject Name]",s_sub)
	m=file_content
	t=settings.EMAIL_HOST_USER

	b=send_mail(sbj,m,t,[g1.email])
	return redirect('/mainpage/'+str(id))

def reqpage(request,id):
	e=Requests.objects.filter(atid=id)
	return render(request,'requestnote.html',{'ID':id,'requests':e})

def accepted(request,id,rid,atid,nid):
	q=Notes.objects.get(id=nid)
	g1=Student.objects.get(id=atid)
	g2=Student.objects.get(id=rid)
	r = Requests.objects.filter(rid=rid, ntid=nid).first()
	r.delete()
	w=Accepted.objects.create(rid=rid,nid=nid,s_sub=q.sub,s_note=q.note)
	sbj="Accepted Request from Notes Management App"
	file_content = open(r"D:\Django\accepted_mail_sending.txt").read()
	file_content = file_content.replace("[Req Student's Name]",g2.name)
	file_content = file_content.replace("[Student's Name]",g1.name)
	file_content = file_content.replace("[Subject Name]",q.sub)
	m=file_content
	t=settings.EMAIL_HOST_USER

	b=send_mail(sbj,m,t,[g2.email])
	e=Requests.objects.filter(atid=id)
	return render(request,'requestnote.html',{'ID':id,'requests':e})

def declined(request,id,rid,atid,nid):
	q=Notes.objects.get(id=nid)
	g1=Student.objects.get(id=atid)
	g2=Student.objects.get(id=rid)
	r = Requests.objects.filter(rid=rid, ntid=nid).first()
	r.delete()
	sbj="Declined Request from Notes Management App"
	file_content = open(r"D:\Django\declined_mail_sending.txt").read()
	file_content = file_content.replace("[Req Student's Name]",g2.name)
	file_content = file_content.replace("[Student's Name]",g1.name)
	file_content = file_content.replace("[Subject Name]",q.sub)
	m=file_content
	t=settings.EMAIL_HOST_USER

	b=send_mail(sbj,m,t,[g2.email])
	# return redirect('/mainpage/'+str(id))
	e=Requests.objects.filter(atid=id)
	return render(request,'requestnote.html',{'ID':id,'requests':e})

def acceptednotes(request,id):
	e=Accepted.objects.filter(rid=id)
	return render(request,'acceptednote.html',{'ID':id,'requests':e})

def viewreqnote(request,id,nid):
	d=Notes.objects.get(id=nid)
	return render(request,'viewreqnote.html',{'ID':id,'notes':d})

def likebutton(request,id,nid):
	d=Notes.objects.get(id=nid)
	d.like+=1
	d.save()
	e=Accepted.objects.filter(rid=id)
	return render(request,'acceptednote.html',{'ID':id,'requests':e})

def dislikebutton(request,id,nid):
	d=Notes.objects.get(id=nid)
	d.dislike+=1
	d.save()
	e=Accepted.objects.filter(rid=id)
	return render(request,'acceptednote.html',{'ID':id,'requests':e})
