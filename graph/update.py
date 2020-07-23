import os
from .models import CovidWeek, CovidScores,AverageWeek
from . import ons_fetch,model_calcs,phe_fetch,scotland,import_csv,n_ireland,infections
from django.db.models import Sum
from .ons_week import stored_names


#constant files:
POP_FILE="ONS_UK_pop.csv"
EW_AV_FILE="ONSaverages_20152019.csv"
SCOT_AV_FILE="Scotland_averages_15-19_data.csv"

DATA_STORE=model_calcs.DATA_STORE

"""
data glitches:  #TO DO AUTO FIXING OF GLITCHES
MISSING AVERAGES AND CASES DATA FOR N IRELAND

Buckinghamshire combined
Isles of Scilly sometimes part of Cornwall and Isles of Scilly
City of London soemetimes part of Hackney and City of London


"""
class Updater():
    def __init__(self):
        #self.checks()
        pass
        
    def checks(self):
        """check population data and excess deaths calcs"""
        for name in stored_names.values():
            try:
                q=CovidScores.objects.get(areaname=name)
            except:
                print(f'data for {name} missing')
                break
            try:
                assert q.population is not None
            except Exception as e:
                print(f'population data for {name} missing')
            try:
                assert q.excess_deaths is not None
            except Exception as e:
                print(f'excess death calculation for {name} missing')
                
                
        for areacode in stored_names.keys():
            try:
                q=AverageWeek.objects.filter(areacode=areacode)
                if not q:
                    print(f'Average 5 years data for {stored_names[areacode]} missing')  
            except Exception as e:
                print(e)        
        av_h=AverageWeek.objects.filter(weeklyhospitaldeaths__isnull=True).count()
        av_all=AverageWeek.objects.all().count()
        av_deaths=AverageWeek.objects.filter(weeklyalldeaths__isnull=True).count()
        print(f"Average data : av. hospital data MISSING in {av_h} places, all deaths data MISSING in {av_deaths} places out of {av_all} all places")
        
    
    def process(self):
        """check for updates of deaths and cases data & download updates"""
        
        update_deaths=False
        
        print('Checking ONS for weekly deaths update - normally released Tuesday')
        wz=ons_fetch.ONS_Importer()
        if wz.process(): #import and parse if new data available
            update_deaths=True
        
                
        print('Updating Scottish deaths - normally released Wednesday')
        self.scot=scotland.Scot_Importer()
        if self.scot.update_check():
            self.scot.process()
            update_deaths=True
        
        
        
        print('Updating N Irish deaths')
        ni=n_ireland.NI_Importer()
        ni.process()
        if ni.check_update():
           ni.parse()
           update_deaths=True

        
        #READJUST HERE FOR ANY GLITCHES
        if update_deaths:
            print('Updating cumulative deaths')
            model_calcs.update_cum_deaths()

            print('Updating excess deaths')
            self.check_excess()
            
            print('Updating Reuters infection curve')
            infections.calc()

        print('Checking PHE case - England and Wales - released daily')
        cz=phe_fetch.Fetch_PHE()
        cz.process()
        
#        self.cz.update_totals()
        print('Updating Scottish cases - released daily')
        self.scot2=scotland.Scot_Cases()
        self.scot2.process()
        

    def load_constants(self):
        
        #all UK population
        import_csv.AddPop(os.path.join(DATA_STORE,POP_FILE))
        
        #add average deaths
        #England and Wales
        import_csv.AddAverages(os.path.join(DATA_STORE,EW_AV_FILE))
        
        #Scotland
        sa=scotland.Scot_Average()
        sa.process(os.path.join(DATA_STORE,SCOT_AV_FILE))
        sa.parse()
        
        #Ireland

    def check_excess(self):
        model_calcs.excess_deaths()


def sums():
    weeks=[w['date'] for w in CovidWeek.objects.values('date').distinct().order_by('date')]
    print(f'Total weeks: {len(weeks)}')
    print([f"{w:%d/%m}" for w in weeks])
    nations=nations_list()
    nations_set=nations_filter()
    for nation in nations:
        print(nation)
        for week in weeks:
            _set=nations_set[nation]
            _thisweek=_set.filter(date=week)
            deathtoll=_thisweek.aggregate(Sum('weeklyalldeaths'))['weeklyalldeaths__sum']
            c19deaths=_thisweek.aggregate(Sum('weeklydeaths'))['weeklydeaths__sum']
            #deathtoll=sum([i.weeklyalldeaths for i in _thisweek])
            print(f'{nation} week ending {week:%d/%m} deaths: {deathtoll}  COVIDdeaths: {c19deaths}')

def nations_list():
    return ['England','Wales','Scotland','Northern Ireland']

def nations_filter():
    nations=nations_list()
    nations_set= {}
    for nation in nations:
        nations_set[nation]=CovidWeek.objects.filter(nation=nation)
    return nations_set
    
    
    
#    CovidWeek.objects.filter(areaname=place,date__range=RANGE)
    
