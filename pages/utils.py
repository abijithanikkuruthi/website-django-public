from django.core.mail import EmailMessage
from django.contrib.auth.models import User
import datetime

def get_page_object(page, num_pages):
    p_obj = {}
    if(page != 1):
        p_obj["prev"] = page - 1
    if(page != num_pages):
        p_obj["next"] = page + 1
    if num_pages == 1:
        p_list = []
    elif(num_pages < 5):
        p_list = list(range(1, num_pages + 1))
    elif(page < 3):
        p_list = list(range(1, 6))
    elif(num_pages < page + 2):
        p_list = list(range(num_pages-4, num_pages + 1))
    else:
        p_list = list(range(page-2,page+3))
    p_obj["list"] = p_list
    p_obj["page"] = page
    return p_obj

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_email_body(m_obj):
    e_body = ''
    for key, value in m_obj.items():
        e_body = e_body + '\n' + key + ": " + value
    e_body = e_body + '\n\nSent from ' + m_obj["host"] + ' at ' + str(datetime.datetime.now())
    return e_body

def send_email(m_obj, to_email_list):
    e_subject = m_obj["host"] + ": New Message/Comment from '" + m_obj["name"] + "' (" + m_obj["ip"] +")"
    e_body = get_email_body(m_obj)
    email = EmailMessage(subject=e_subject, body=e_body, to=to_email_list)
    email.send()

def send_email_to_admin(m_obj):
    superusers_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
    send_email(m_obj, superusers_emails)