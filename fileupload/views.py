from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CatsData, CatsNi, CheckFile
# from .forms import UploadFileForm



# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             process_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

def process_file(request):
	print "something"
	import ipdb;ipdb.set_trace()
	email_of_file_records_to_delete = []
	file_records = CheckFile.objects.all()
	for file_record in file_records:
		catsdata = CatsData.objects.get(email = file_record.email) | CatsData.objects.get(mobile = file_record.mobile)
		catsni = CatsNi.objects.get(email = file_record.email) | CatsNi.objects.get(mobile = file_record.mobile)
		if catsdata or catsni :
			email_of_file_records_to_delete.append(file_record.email)
	CheckFile.objects.filter(email__in = email_of_file_records_to_delete).delete()	
	# html = '<H1>Thank You</H1>'
	# html = <a href = >Click</a>
	return HttpResponseRedirect('/admin/fileupload/checkfile/export/')