from django.db import models

TICKET_STATUS_CHOICES = (
    ('open', 'Open'),
    ('in_progress', 'In Progress'),
    ('closed', 'Closed'),
)

class Ticket(models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("authentication.TicketingUser", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='open')

    def __str__(self):
        return self.summary