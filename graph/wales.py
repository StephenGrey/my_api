import pandas,requests,pytz, logging
from . import n_ireland
from .models import DailyCases
from .ons_week import wales_codes
from .phe_fetch import update_weekly_cases, Check_PHE
from uk_covid19 import Cov19API
log = logging.getLogger('api.graph.wales')
import configs
from configs import userconfig

URL_DASHBOARD="https://public.tableau.com/profile/public.health.wales.health.protection#!/vizhome/RapidCOVID-19virology-Public/Headlinesummary"
#http://www2.nphs.wales.nhs.uk:8080/CommunitySurveillanceDocs.nsf/CategoryPublic2/77FDB9A33544AEE88025855100300CAB?opendocument
#http://www2.nphs.wales.nhs.uk:8080/CommunitySurveillanceDocs.nsf/
				
SPREADSHEET="http://www2.nphs.wales.nhs.uk:8080/CommunitySurveillanceDocs.nsf/61c1e930f9121fd080256f2a004937ed/77fdb9a33544aee88025855100300cab/$FILE/Rapid%20COVID-19%20surveillance%20data.xlsx"

class Wales_Check(Check_PHE):
    def __init__(self):
        self.api = Cov19API(filters=self.filters, structure=self.structure)
        PHEstored=configs.config.get('Wales')
        if PHEstored:
            self.Wales_cases=PHEstored.get('wales_total_cases')
        else:
            self.Wales_cases=None
        self.top()

    def top(self):
        """get latest total"""
        self.api.latest_by='cumCasesByPublishDate'
        self.get()
        self.latest_total=self.data['data'][0]['cumCasesByPublishDate']
        log.info(f'Wales latest total: {self.latest_total}')
        if self.latest_total:
            if self.Wales_cases:
                if int(self.Wales_cases)==self.latest_total:
                    log.info('nothing new here')
                    self._update=False
                    return False
            userconfig.update('Wales','wales_total_cases',str(self.latest_total))
        self._update=True
        return True
        
    
    @property
    def filters(self):
        """override to any filter"""
        return ['areaType=nation','areaName=Wales']
    


class Wales_Cases():
    
    def process(self):
        self.open_excel()
        self.parse()
        update_weekly_cases('Wales')
    
    def open_excel(self):
         self.data=pandas.read_excel(SPREADSHEET,sheet_name="Tests by specimen date")

    def districts(self):
        return wales_codes.values()
        
        
    def parse(self):
        for areacode, district in wales_codes.items():
            self.parse_district(district,areacode)
            
    def parse_district(self,district,areacode,_update=True):
        sub=self.data[self.data['Local Authority']==district] 
        for xcldate in sub['Specimen date'].values:
            totalcases,newcases=sub[sub['Specimen date']==xcldate][['Cumulative cases','Cases (new)']].values[0]
            
            i,created=DailyCases.objects.get_or_create(specimenDate=timeaware(pandas.to_datetime(xcldate)),areaname=district)
            i.dailyLabConfirmedCases=newcases
            i.totalLabConfirmedCases=totalcases
            i.areacode=areacode
            #print(newcases,totalcases)
            i.save()



#latency calcs





            
            
#        
#        
#        
#        district=ni_codes_inv[areacode] #different syntax on import
#        
#        print(week,district)
#        
#        _allc19=zero_null(self.data[(self.data['Registration Week']==week)][district])
#        _all=zero_null(self.data2[(self.data2['Registration Week']==week)][district])
#        careh19=zero_null(self.data3[(self.data3['Registration Week']==week)][district])
#        
#                 today=0
#            
#            print(f'Place:{place} Date: {day:%d/%m} Yesterday:{yesterday} Today:{today} Total:{totalcases}')
#            #datestring=item['specimenDate']
#            date=day
#            areacode=scotcode[place]
#            row,created=DailyCases.objects.get_or_create(specimenDate=timeaware(date),areacode=areacode)
#            row.areaname=place
#            row.dailyLabConfirmedCases=today
#            row.totalLabConfirmedCases=totalcases
#            row.changeInDailyCases=None #item['changeInDailyCases']
#            row.dailyTotalLabConfirmedCasesRate=None #item['dailyTotalLabConfirmedCasesRate']
#            row.previouslyReportedDailyCases=None #item['previouslyReportedDailyCases']
#            row.previouslyReportedTotalCases=None #item['previouslyReportedTotalCases']
#            row.changeInTotalCases=None #item['changeInTotalCases']
#            row.save()
#            counter+=1
#        print(f'Processed: {counter} rows')
#        update_weekly_total(areacode=scotcode[place],areaname=place)



def valid_int(s):
    try:
        n=int(s)
        return n
    except:
        return None
    
    
def zero_null(s):
    try:
        n=int(s)
        return n
    except:
        return 0

def timeaware(dumbtimeobject):
    return pytz.timezone("GMT").localize(dumbtimeobject)
#Mac / Linux stores all file times etc in GMT, so localise to GMT