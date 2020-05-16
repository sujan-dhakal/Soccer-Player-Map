from django.db import models

class High_school(models.Model):
    """
    high school data
    """
    name = models.CharField(name='Name', max_length = 100)
    location_lat = models.DecimalField(name = 'location_lat', decimal_places=9, max_digits= 12)
    location_long = models.DecimalField(name = 'location_long', decimal_places=9, max_digits= 12)


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'high_school'
        verbose_name_plural = 'high_school'


class College(models.Model):
    """
    college data
    """

    CATEGORY = (
        ('0', 'Null'),
        ('1', 'America East Conference'),
        ('2', 'American Athletic Conference'),
        ('3', 'ASUN Conference'),
        ('4', 'Atlantic 10 Conference'),
        ('5', 'Atlantic Coast Conference'),
        ('6', 'Big East Conference'),
        ('7', 'Big South Conference'),
        ('8', 'Big Ten Conference'),
        ('9', 'Big West Conference'),
        ('10', 'Colonial Athletic Association'),
        ('11', 'Conference USA'),
        ('12', 'Horizon League'),
        ('13', 'Ivy League'),
        ('14', 'Metro Atlantic Athletic Conference'),
        ('15', 'Mid-American Conference'),
        ('16', 'Missouri Valley Conference'),
        ('17', 'Northeast Conference'),
        ('18', 'Pac-12 Conference'),
        ('19', 'Patriot League'),
        ('20', 'Southern Conference'),
        ('21', 'The Summit League'),
        ('22', 'Sun Belt Conference'),
        ('23', 'West Coast Conference'),
        ('24', 'Western Athletic Conference'),

    )

    name = models.CharField(name='Name', max_length=80)
    College_League = models.IntegerField(name = 'College_League', choices=CATEGORY)


    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'College'


class Player(models.Model):
    """
    player data
    """

    CATEGORY = (
        (0, 'AMERICAN ATHLETIC'),
        (1, 'BIG EAST'),
        (2, 'PATRIOT'),
        (3, 'IVY'),
        (4, 'COLONIAL ATHLETIC ASSOCIATION'),
        (5, 'SOUTHERN'),
        (6, 'PAC-12'),
        (7, 'WAC'),
    )

    first_name = models.CharField(name='first_name', max_length=20)
    last_name = models.CharField(name='last_name', max_length=20)
    height = models.DecimalField(name = 'Height', decimal_places=2, max_digits=4, null=True,blank=True)
    weight = models.IntegerField(name = 'Weight', null=True,blank=True)
    state = models.CharField(name = 'State/Country', max_length=20, null=True,blank=True)
    hometown = models.CharField(name='Hometown', max_length=60, null=True,blank=True)
    High_school = models.ForeignKey(High_school,name = 'High_School', on_delete=models.CASCADE)
    Team = models.ForeignKey(College,name = 'College', on_delete=models.CASCADE)


    def get_start_year(self):
        return Record.objects.filter(Player_id = self.id, Is_starter = True).count()

    def get_conf_year(self):
        return Accolade.objects.filter(Player_id = self.id).count()

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.first_name + ' '+ self.last_name

class Record(models.Model):
    """
    record data
    """

    POSITION = (
        (0, 'Forward'),
        (1, 'Midfielder'),
        (2, 'Defender'),
        (3, 'Back'),
        (4, 'Goalkeeper'),
    )

    potential_strat = models.IntegerField(name = 'Potential_Strats',  null=True,blank=True)
    GP = models.IntegerField(name = 'GP',  null=True,blank=True)
    GS = models.IntegerField(name = 'GS',  null=True,blank=True)
    is_starter = models.NullBooleanField(name = 'Is_starter', null = True)

    Position1 = models.IntegerField(name = 'Position1', choices=POSITION,null=True)
    Position2 = models.IntegerField(name = 'Position2', choices=POSITION,null=True)
    Position3 = models.IntegerField(name = 'Position3', choices=POSITION,null=True)

    Roster_Year = models.IntegerField(name = 'Roster_Year',null=True,blank=True)
    Year = models.IntegerField(name = 'Year', null=True,blank=True)
    Player_num = models.IntegerField(name = 'Player_num', null=True,blank=True)


    Player = models.ForeignKey(Player, name = 'Player', on_delete=models.CASCADE)
    College = models.ForeignKey(College, name = 'College', on_delete=models.CASCADE)

    bio_link = models.CharField(name='bio_link', max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Record'

class Accolade(models.Model):
    """
    college data
    """

    TYPE = (
        ('0', 'First Team'),
        ('1', 'Second Team'),
        ('2', 'Third Team'),
        ('3', 'Rookie Team'),
        ('4', 'Honorable Mention'),
        ('5', 'Freshman Team'),
    )

    Year = models.IntegerField(name = 'Year')
    Accolade = models.IntegerField(name='Accolade', choices=TYPE)

    Player = models.ForeignKey(Player, name = 'Player', on_delete=models.CASCADE)
    College = models.ForeignKey(College, name = 'College', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Accolade'
        verbose_name_plural = 'Accolade'
