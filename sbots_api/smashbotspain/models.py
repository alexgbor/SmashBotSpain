from django.db import models
from django.core import validators

# Create your models here.

class Region(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 

class Character(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name 

class Tier(models.Model):
    """
    Model for tiers. More weight == better role.
    Tier 1 > Tier 3
    """
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    weight = models.IntegerField(default=0)
    channel_id = models.BigIntegerField()

    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    
    characters = models.ManyToManyField(Character, through="Main")
    regions = models.ManyToManyField(Region)
    
    tier = models.ForeignKey(Tier, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.tier})"

class Main(models.Model):
    MAIN_SECOND = [
        ('MAIN', 'Main'),
        ('SECOND', 'Second')
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)   
    
    main = models.CharField(max_length=10, choices=MAIN_SECOND)

class Arena(models.Model):
    STATUS = [
        ('WAITING', 'Waiting'),
        ('CONFIRM', 'Confirmation'),
        ('PLAYING', 'Playing'),
        ('CLOSED', 'Closed'),
    ]
    
    MODE = [
        ("FRIENDLIES", "Friendlies"),
        ("RANKED", "Ranked")
    ]
    
    created_by = models.ForeignKey(Player, null=True, related_name="created_by", on_delete=models.SET_NULL)
    status = models.CharField(max_length=7, choices=STATUS, default="WAITING")
    mode = models.CharField(max_length=10, choices=MODE, default="FRIENDLIES")
    
    max_tier = models.ForeignKey(Tier, null=True, related_name="max_tier", on_delete=models.SET_NULL)
    min_tier = models.ForeignKey(Tier, null=True, related_name="min_tier", on_delete=models.SET_NULL)

    max_players = models.IntegerField(validators=[validators.MinValueValidator(2)])
    num_players = models.IntegerField()

    players = models.ManyToManyField(Player, through="ArenaPlayer", blank=True)

    def __str__(self):
        return f"Arena #{self.id}"

class ArenaPlayer(models.Model):
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE, null=True, blank=True)
    player = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL)
    
    STATUS = [
        ('WAITING', 'Waiting'),
        ('CONFIRMED', 'Confirmed'),
        ('PLAYING', 'Playing'),
        ('GGS', 'GGs'),
        ('INVITED', 'Invited'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return f"{self.player} in {self.arena}"