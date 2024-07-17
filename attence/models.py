
from django.db import models

class course_ug(models.Model):
    department = models.CharField(max_length=100)
    year1 = models.CharField(max_length=100)
    year2 = models.CharField(max_length=100)
    year3 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.department
    
    
class course_pg(models.Model):
    department = models.CharField(max_length=100)
    year1 = models.CharField(max_length=100)
    year2 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.department
    
class entry_panal(models.Model):
    day=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    dayorder=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.date+'_'+self.date+'_'+self.dayorder






class student_details(models.Model):
    key=models.CharField(max_length=100)
    regnumber=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    day1 = models.CharField(max_length=100)
    day2 = models.CharField(max_length=100)
    day3 = models.CharField(max_length=100)
    day4 = models.CharField(max_length=100)
    day5 = models.CharField(max_length=100)
    day6 = models.CharField(max_length=100)
    day7 = models.CharField(max_length=100)
    day8 = models.CharField(max_length=100)
    day9 = models.CharField(max_length=100)
    day10 = models.CharField(max_length=100)
    day11 = models.CharField(max_length=100)
    day12 = models.CharField(max_length=100)
    day13 = models.CharField(max_length=100)
    day14 = models.CharField(max_length=100)
    day15 = models.CharField(max_length=100)
    day16 = models.CharField(max_length=100)
    day17 = models.CharField(max_length=100)
    day18 = models.CharField(max_length=100)
    day19 = models.CharField(max_length=100)
    day20 = models.CharField(max_length=100)
    day21 = models.CharField(max_length=100)
    day22 = models.CharField(max_length=100)
    day23 = models.CharField(max_length=100)
    day24 = models.CharField(max_length=100)
    day25 = models.CharField(max_length=100)
    day26 = models.CharField(max_length=100)
    day27 = models.CharField(max_length=100)
    day28 = models.CharField(max_length=100)
    day29 = models.CharField(max_length=100)
    day30 = models.CharField(max_length=100)
    day31 = models.CharField(max_length=100)
    day32 = models.CharField(max_length=100)
    day33 = models.CharField(max_length=100)
    day34 = models.CharField(max_length=100)
    day35 = models.CharField(max_length=100)
    day36 = models.CharField(max_length=100)
    day37 = models.CharField(max_length=100)
    day38 = models.CharField(max_length=100)
    day39 = models.CharField(max_length=100)
    day40 = models.CharField(max_length=100)
    day41 = models.CharField(max_length=100)
    day42 = models.CharField(max_length=100)
    day43 = models.CharField(max_length=100)
    day44 = models.CharField(max_length=100)
    day45 = models.CharField(max_length=100)
    day46 = models.CharField(max_length=100)
    day47 = models.CharField(max_length=100)
    day48 = models.CharField(max_length=100)
    day49 = models.CharField(max_length=100)
    day50 = models.CharField(max_length=100)
    day51 = models.CharField(max_length=100)
    day52 = models.CharField(max_length=100)
    day53 = models.CharField(max_length=100)
    day54 = models.CharField(max_length=100)
    day55 = models.CharField(max_length=100)
    day56 = models.CharField(max_length=100)
    day57 = models.CharField(max_length=100)
    day58 = models.CharField(max_length=100)
    day59 = models.CharField(max_length=100)
    day60 = models.CharField(max_length=100)
    day61 = models.CharField(max_length=100)
    day62 = models.CharField(max_length=100)
    day63 = models.CharField(max_length=100)
    day64 = models.CharField(max_length=100)
    day65 = models.CharField(max_length=100)
    day66 = models.CharField(max_length=100)
    day67 = models.CharField(max_length=100)
    day68 = models.CharField(max_length=100)
    day69 = models.CharField(max_length=100)
    day70 = models.CharField(max_length=100)
    day71 = models.CharField(max_length=100)
    day72 = models.CharField(max_length=100)
    day73 = models.CharField(max_length=100)
    day74 = models.CharField(max_length=100)
    day75 = models.CharField(max_length=100)
    day76 = models.CharField(max_length=100)
    day77 = models.CharField(max_length=100)
    day78 = models.CharField(max_length=100)
    day79 = models.CharField(max_length=100)
    day80 = models.CharField(max_length=100)
    day81 = models.CharField(max_length=100)
    day82 = models.CharField(max_length=100)
    day83 = models.CharField(max_length=100)
    day84 = models.CharField(max_length=100)
    day85 = models.CharField(max_length=100)
    day86 = models.CharField(max_length=100)
    day87 = models.CharField(max_length=100)
    day88 = models.CharField(max_length=100)
    day89 = models.CharField(max_length=100)
    day90 = models.CharField(max_length=100)
   
    def __str__(self) -> str:
        return self.key+"-"+self.regnumber+'-'+self.name

    
