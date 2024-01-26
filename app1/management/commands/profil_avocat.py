
from random import randint
from django.db import IntegrityError
from django.core.management.base import BaseCommand
from app1.models import Avocat, ProfilAvocat, Blog
import random

class Command(BaseCommand):
    help = 'Create profile instances for each avocat with varying values'

    def handle(self, *args, **options):
        avocats = Avocat.objects.all()


        experience_choices = [
    "Handled high-profile divorce cases with successful outcomes",
    "Successfully represented clients in complex real estate disputes",
    "Advised multinational corporations on international business law",
    "Negotiated favorable settlements in personal injury cases",
    "Served as a legal consultant for technology startups",
    "Managed a diverse caseload covering various areas of law",
    "Provided pro bono legal services for community outreach programs",
    "Litigated cases at both trial and appellate court levels",
    "Navigated clients through intricate intellectual property matters",
    "Collaborated with government agencies on regulatory compliance",
    "Published articles on legal topics in reputable journals",
    "Led a legal team in high-stakes class-action lawsuits",
    "Advised clients on employment law and HR issues",
    "Resolved complex business disputes through alternative dispute resolution",
    "Defended clients against white-collar crime allegations",
    "Guided clients through the intricacies of international trade law",
    "Provided legal counsel to non-profit organizations",
    "Assisted clients with estate planning and probate matters",
    "Handled cases involving environmental law and sustainability",
    "Advocated for clients in administrative hearings",
    "Specialized in negotiating and drafting commercial contracts",
    "Advised clients on compliance with data protection and privacy laws",
    "Represented individuals in asylum and immigration proceedings",
    "Handled high-stakes criminal defense cases",
    "Navigated clients through bankruptcy proceedings",
    "Provided legal support for mergers and acquisitions",
    "Served as a legal expert on panels and conferences",
    "Defended clients in high-profile product liability cases",
    "Assisted clients with trademark and patent applications",
    "Represented clients in workers' compensation cases",
    "Provided legal guidance in complex tax matters",
    "Advised clients on issues related to family and children's rights",
    "Litigated cases involving construction and real estate development",
]

        

        

        for avocat in avocats:
            try:
                # Create profile instance for each avocat
                profil_instance = ProfilAvocat.objects.create(
                    avocat=avocat,
                    experience=random.choice(experience_choices),
                    rating=randint(0,5),  # Varying rating between 3 and 5
                    site_web=f"http://www.{avocat.nom.lower()}-{avocat.prenom.lower()}.com",
                )

                # Add blogs to the profile (you can customize this based on your data)
                blogs = Blog.objects.all()[:3]  # Assuming you have some blogs already created
                profil_instance.blogs.set(blogs)

            except IntegrityError as e:
                print(f"Error: {e}. Skipping duplicate entry for avocat {avocat}.")
                continue  # Skip to the next iteration or handle it as needed

        print("Profile instances created successfully.")
