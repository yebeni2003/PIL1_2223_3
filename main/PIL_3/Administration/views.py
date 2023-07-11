from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .models import Emploi,Professeur,Matiere,Salle,Filiere,Semestre,Etudiant
from itertools import groupby
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from Administration.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from PIL_3 import settings
from django.db.models import F,Q
from django.shortcuts import render, redirect, HttpResponseRedirect
from datetime import datetime
# Create your views here.



    



def add_course(request):
    
    semestres = Semestre.objects.all()
    filieres = Filiere.objects.all()
    matieres = Matiere.objects.all()
    salles = Salle.objects.all()
    teachers = Professeur.objects.all()
    
    if request.method=="POST":
        matiere = request.POST["matiere"]
        teacher = request.POST["teacher"]
        salle = request.POST["salle"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        filiere = request.POST["filiere"]
        semestre = request.POST["semestre"]
        print("jfflflf")
        
        Emploi.objects.create(
            subject = Matiere.objects.get(id=matiere),
            filiere = Filiere.objects.get(id=filiere),
            start_time = start_time,
            end_time = end_time,
            classroom = Salle.objects.get(id=salle),
            teacher = Professeur.objects.get(id=teacher),
            semestre = Semestre.objects.get(id=semestre)
        )
        print("oootojjv")
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
        difference = end_time - start_time
        difference_hours = difference.total_seconds() / 3600 
        subject = Matiere.objects.get(id_mat=matiere)
        subject.masse_horraire_utilisee += int(difference_hours)
    else:
        print("jglglg")
        
    return render(request,'my_dashboard.html',{'semestres':semestres,'filieres':filieres,'matieres':matieres,'salles':salles,'teachers':teachers})
    """
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            semaine = form.cleaned_data['semaine']
            courses = Emploi.objects.all().order_by('semaine')
            grouped_courses = []
            for semaine, group in groupby(courses, key=lambda course: course.semaine):
                grouped_courses.append(list(group))
            messages.success(request,"Votre emploi du temps a été bien enregistrer. Merci!!!")
            # return redirect('etre')
    else:
        form = CourseForm()
    
    context = {
        'form': form
    }
    return render(request, 'gestionE.html', context)

def etreP(request):
    # if not request.user.profile.is_profile_complete:
    #     messages.warning(request, "Veuillez compléter votre profil avant de continuer.")
    #     return redirect('profil')
    # else:
    courses = Emploi.objects.all().order_by('semaine')
    grouped_courses = []
    for semaine, group in groupby(courses, key=lambda course: course.semaine):
        grouped_courses.append(list(group))
     
    context = {
        'courses': courses,
        'grouped_courses': grouped_courses
       
    }
    return render(request, 'etreP.html', context)
"""
"""
@login_required('login_admin')
def update(request, id):
    if request.method == 'POST':
        pi = Course.objects.get(pk=id)
        fm = CourseForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            send_notification_to_users()
            messages.success(request, "Votre emploi du temps a été modifié avec succès. Merci!!!")
    else:
        pi = Course.objects.get(pk=id)
        fm = CourseForm(instance=pi)
    return render(request, 'update.html' ,{'form': fm})
"""
"""
@login_required('login_admin')

def delete_course(request, id):
    if request.method == 'POST':
        pi = Course.objects.get(pk=id) 
        pi.delete()
        send_notification_to_users()
        return HttpResponseRedirect('/etre')
"""    
def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_admin==True:
            auth_login(request, user)
            
            return redirect(reverse('schedule',args=[0]))
        elif user is None:
            messages.error(request, 'Mauvaise Authentification')
        else:
            try:
                my_user = User.objects.get(username=username)
                if not my_user.is_active:
                    messages.error(request, "Vous n'avez pas confirmé votre email. Faites-le avant de vous connecter")
            except User.DoesNotExist:
                messages.error(request, 'Mauvaise Authentification')
            
            return redirect('login_admin')
    
    return render(request, 'login.html')

def send_notification_to_users(message):
    users = User.objects.filter(is_student=True)
    recipients = [user.email for user in users]
    
    subject = "Notification de l'Administration by TimePlan"
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipients)





def schedule(request, pk):
    try:
        current_level = Filiere.objects.get(id_fil=pk)
    except Filiere.DoesNotExist:
        current_level = Filiere.objects.first()
        pk = current_level.id_fil

    error, success = None, None

    teachers = Professeur.objects.all()
    matieres = Matiere.objects.all()

    current_week = datetime.now().isocalendar()[1]
    current_week = int(request.GET.get('week', current_week))

    if request.method == "POST":
        teacher = request.POST.get('teacher')
        subject = request.POST.get('matiere')
        classroom_id = request.POST.get('salle')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        print(
            "teacher",teacher,
            "subject",subject,
            "salle",classroom_id,
            "debut",start_time,
            "fin",end_time,
            sep="\n"
        )
        if True:
            date = datetime.fromisoformat(start_time)
            weekNum = date.isocalendar()[1]
            
            start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
            end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
            difference = end - start
            difference_hours = difference.total_seconds() / 3600 
            subject = Matiere.objects.get(id_mat=subject)
            updated = difference_hours
            subject.masse_horraire_utilisee = F('masse_horraire_utilisee') + int(difference_hours)
            subject.save()
            current_time_used =  int(updated)
            
            
            Emploi.objects.create(
                teacher=Professeur.objects.get(id_prof=teacher),
                subject=subject,
                classroom=Salle.objects.get(id_sal=classroom_id),
                filiere=Filiere.objects.get(id_fil=pk),
                start_time=start_time,
                end_time=end_time,
                week_num=weekNum,
                current_time_used = current_time_used
            )
            
           
            print("difference ",int(difference_hours))
            
            success = "Votre emploi du temps a bien été créé"
  
            try:
                pass
            except:
                error = "Erreur lors de la création du programme"
        else:
            error = "Veuillez remplir tous les champs"

    timetable_data = get_timetable_data(pk, current_week)

    context = {
        'filieres': Filiere.objects.all(),
        'salles': Salle.objects.all(),
        'filiere': current_level,
        'teachers': teachers,
        'matieres': matieres,
        'errors': error,
        'success': success,
        'timetable_data': timetable_data[0],
        'all_week': timetable_data[1],
        'current_week': current_week,
    }

    return render(request, 'my_dashboard.html', context)


@login_required
def students_schedule(request):
    current_week = datetime.now().isocalendar()[1]
    current_week = int(request.GET.get('week', current_week))
    user_pk = request.user.pk
    user = User.objects.get(pk=user_pk)

    # Récupérer l'étudiant associé à l'utilisateur
    etudiant = Etudiant.objects.get(user=user)

    # Récupérer la filière de l'étudiant
    filiere = etudiant.filiere

    timetable_data = get_timetable_data(filiere, current_week)

    # Filtrer les emplois du temps publiés
    filtered_timetable_data = []
    for day_data in timetable_data[0]:
        filtered_time_slots = {}
        for hour_range, time_slots in day_data['time_slots'].items():
            filtered_time_slots[hour_range] = [slot for slot in time_slots if slot['published']]
        filtered_day_data = {
            'day_name': day_data['day_name'],
            'time_slots': filtered_time_slots
        }
        filtered_timetable_data.append(filtered_day_data)

    context = {
        'timetable_data': filtered_timetable_data,
        'all_week': timetable_data[1],
        'current_week': current_week,
        'level': filiere.id_fil,
    }

    return render(request, 'my_dashboard.html', context)



def get_hour_range(time):
    hour = time.hour

    if 0 <= hour < 10:
        return 1
    elif 10 <= hour < 13:
        return 2
    elif 13 <= hour < 16:
        return 3
    elif 16 <= hour < 24:
        return 4


def get_timetable_data(level_id, week):
    timetable_entries = Emploi.objects.filter(filiere=level_id, week_num=week)
    timetable_all = Emploi.objects.filter(filiere=level_id)
    
    all_week = []

    for entry in timetable_all:
        week_number = entry.start_time.isocalendar()[1]

        if week_number not in all_week:
            all_week.append(week_number)

    grouped_timetable = {}

    for entry in timetable_entries:
        week_number = entry.start_time.isocalendar()[1]
        day_name = entry.start_time.strftime('%A')

        if week_number not in grouped_timetable:
            grouped_timetable[week_number] = {}

        if day_name not in grouped_timetable[week_number]:
            grouped_timetable[week_number][day_name] = {
                1: [],
                2: [],
                3: [],
                4: [],
            }

        hour_range = get_hour_range(entry.start_time.time())

        grouped_timetable[week_number][day_name][hour_range].append({
            'id': entry.id,
            'subject': entry.subject.serialize(),
            'teacher': entry.teacher.serialize(),
            'filiere': entry.filiere.serialize(),
            'classroom': entry.classroom.serialize(),
            'start_time': str(entry.start_time.strftime("%d/%m/%Y, %H:%M")),
            'end_time': str(entry.end_time.strftime("%d/%m/%Y, %H:%M")),
            'published':entry.published
        })

    timetable_data = []

    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_day_index = datetime.now().weekday()

    for i in range(7):
        day_index = (current_day_index + i +4) % 7
        day_name = days_of_week[day_index]
        day_data = {
            'day_name': day_name.capitalize(),
            'time_slots': {},
        }

        for hour_range in range(1, 5):
            hour_range_data = grouped_timetable.get(week, {}).get(day_name, {}).get(hour_range, [])
            day_data['time_slots'][hour_range] = hour_range_data

        timetable_data.append(day_data)

    return [timetable_data, all_week]


def destroy_schedule(request, pk):
    next_url = request.GET.get('next')

    if not request.user.is_superuser or not request.user.is_admin:
        return redirect('student_schedule')

    Emploi.objects.get(id=pk).delete()

    return redirect(next_url) 



def update_schedule(request, schedule_id):
    

    # Passer les données au template
   
    if request.method == 'POST':
        # Récupérer l'objet Emploi correspondant à l'ID donné
        schedule = Emploi.objects.get(id=schedule_id)

        # Traiter les données du formulaire de modification
        matiere = request.POST['matiere']
        teacher = request.POST['teacher']
        salle = request.POST['salle']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        # Mettre à jour les attributs de l'objet Emploi
        schedule.subject = Matiere.objects.get(id_mat=matiere)
        schedule.teacher = Professeur.objects.get(id_prof = teacher)
        schedule.classroom = Salle.objects.get(id_sal = salle)
        schedule.start_time = start_time
        schedule.end_time = end_time
        
        start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
        difference = end - start
        difference_hours = difference.total_seconds() / 3600 
        
        
        old = int(schedule.current_time_used)
        subject = schedule.subject
        subject.masse_horraire_utilisee = F('masse_horraire_utilisee') - old
        subject.masse_horraire_utilisee = F('masse_horraire_utilisee') + int(difference_hours)
        subject.save()
        
        schedule.current_time_used = int(difference_hours)
        
        # Enregistrer les modifications dans la base de données
        schedule.save()
        
        week_num = schedule.week_num
        url = reverse('schedule', args=[week_num])
        url = f'{url}?week={week_num}'
    return redirect(url)
        # Rediriger vers la page de l'emploi du temps après la mise à jour

def publish_schedule(request, week_num):
    
        # Récupérer tous les emplois du temps dont week_num est égal à la valeur passée en tant que paramètre
        employments = Emploi.objects.filter(week_num=week_num)

        # Mettre à jour la valeur de l'attribut "published" pour tous les emplois du temps
        employments.update(published=True)
        url = reverse('schedule', args=[week_num])
        url = f'{url}?week={week_num}'
        return redirect(url)
        # Redirection vers la page souhaitée après la publication

    # Gérer le cas où la méthode de requête n'est pas POST (par exemple, afficher la page avec le formulaire)


def emploi_search(request):
    search_query = request.GET.get('search_query')
    week_num = request.GET.get('week_num')
    filiere_id = request.GET.get('filiere_id')
    filieres = Filiere.objects.all()
    emplois = Emploi.objects.all()
    slots = emplois
    
        
    
    if search_query !=None:
        emplois = emplois.filter(
            Q(subject__nom_mat__icontains=search_query) |
            Q(classroom__nom_sal__icontains=search_query) |
            Q(teacher__nom_prof__icontains=search_query) |
            Q(filiere__nom_fil__icontains=search_query)
        )
    else:
        emplois=Emploi.objects.all()
        search_query = ""
    if week_num:
        emplois = emplois.filter(week_num=week_num)
    
    if filiere_id != 'null':
        fil =Filiere.objects.filter(id_fil=filiere_id).first()
        emplois = emplois.filter(filiere=fil)
    
    all_week =[]
    for i in slots:
        all_week.append(i.week_num)
    a = set(all_week)
    all_week = list(a)
    context = {
        'emplois': emplois,
        'search_query': search_query,
        'week_num': week_num,
        'filiere_id': filiere_id,
        'filieres':filieres,
        'slots':slots,
        'all_week':all_week
    }
    
    return render(request, 'search.html', context)
