"""Author-defined English engineering labels; no observed predictions used as truth.

Three value sets per 70 phrasing families. This is a synthetic challenge set,
not an independent real railway corpus; near duplicates are explicitly identified.
"""
from common import ROOT, save

CLASSES = ['Arrival','Departure','Delay','Cancellation','Platform change','Emergency','Other']

def make_dataset():
    rows = []
    for v in range(3):
        n, p, q, d = str(1201+v*109), str(2+v), str(5+v), str(15+v*15)
        def add(category, text, entities, required):
            family = sum(r['category']==category and r['variant']==v for r in rows)
            rows.append(dict(id=f'{category.lower().replace(" ","-")}-{family:02}-{v}', category=category, variant=v, family=f'{category}-{family}', text=text, entities=entities, required_units=required))
        for event, category in [('arriv','Arrival'),('depart','Departure')]:
            verb = 'arrive' if event=='arriv' else 'depart'
            action = verb.upper()
            examples = [
                (f'Train {n} {verb}s at platform {p}.', {}, []),
                (f'Train number {n} is {event}ing on platform {p}.', {}, ['NOW']),
                (f'Train {n} will {verb} at platform {p}.', {}, ['FUTURE']),
                (f'Train {n} has {event}ed at platform {p}.', {}, ['ALREADY']),
                (f'{n} is {event}ing platform {p}.', {}, ['NOW']),
                (f'Train {n} {verb} at platform {p}.', {}, []),
                (f'Train {n} from Nagpur to Mumbai will {verb} at platform {p}.', {'source':'nagpur','destination':'mumbai'}, ['FROM','NAGPUR','TO','MUMBAI','FUTURE']),
                (f'Train {n} will {verb} at platform {p} at 5:30 PM.', {'arrival_time' if category=='Arrival' else 'departure_time':'5:30 pm'}, ['FUTURE','5:30 PM']),
                (f'Platform {p} train {n} Mumbai {"arrival" if category=="Arrival" else "departure"}.', {'destination':'mumbai'}, ['MUMBAI']),
                (f'The Vidarbha Express train {n} is {event}ing at platform {p}.', {'train_name':'vidarbha express'}, ['VIDARBHA EXPRESS','NOW']),
            ]
            for text, extra, required in examples:
                add(category, text, {'train_number':n,'platform':p,**extra}, ['TRAIN',n,'PLATFORM',p,action,*required])
        for text in [f'Train {n} is delayed by {d} minutes.',f'Train {n} has been delayed by {d} minutes.',f'Train {n} is delayed by {d} minutes due to fog.',f'Train {n} is running {d} minutes late.',f'A delay of {d} minutes affects train {n}.',f'Train number {n} is delayed by {d} minutes.',f'Train {n} delayed {d} minutes.',f'Passengers, train {n} is delayed by {d} minutes.',f'Train {n} from Nagpur to Mumbai is delayed by {d} minutes.',f'{n} is delayed by {d} minutes.']:
            extra = {'source':'nagpur','destination':'mumbai'} if 'from Nagpur' in text else {}
            add('Delay',text,{'train_number':n,'delay_duration':f'{d} minutes',**extra},['TRAIN',n,'DELAY',d,'MINUTE',*(['FROM','NAGPUR','TO','MUMBAI'] if extra else [])])
        for i,text in enumerate([f'Train {n} is cancelled.',f'Train {n} has been cancelled.',f'Train number {n} is cancelled.',f'Train {n} is not cancelled.',f'Train {n} has been canceled.',f'Train {n} cancellation announced.',f'Service {n} is cancelled.',f'Train {n} from Nagpur to Mumbai is cancelled.',f'Train {n} is cancelled today.',f'{n} is cancelled.']):
            extra = {'source':'nagpur','destination':'mumbai'} if 'from Nagpur' in text else {}
            add('Cancellation',text,{'train_number':n,**extra},['TRAIN',n,'CANCEL',*(['NOT'] if i==3 else []),*(['FROM','NAGPUR','TO','MUMBAI'] if extra else [])])
        for text in [f'Platform for train {n} has changed from {p} to {q}.',f'Train {n} platform changed from {p} to {q}.',f'Train {n} will use platform {q} instead of platform {p}.',f'Platform change: train {n} moves from {p} to {q}.',f'Train {n} now arrives at platform {q}, not platform {p}.',f'Platform for train number {n} has changed from {p} to {q}.',f'Attention: platform for train {n} has changed from {p} to {q}.',f'Train {n}: platform {p} replaced by {q}.',f'Platform for train {n} has changed from {p} to {q}',f'PLATFORM FOR TRAIN {n} HAS CHANGED FROM {p} TO {q}.']:
            add('Platform change',text,{'train_number':n,'old_platform':p,'new_platform':q},['TRAIN',n,'FROM','PLATFORM',p,'TO','PLATFORM',q,'CHANGE'])
        emergency = [('Emergency evacuation. Use the nearest emergency exit.',['EMERGENCY','EVACUATE','EXIT']),('Fire at platform '+p+'. Leave the station immediately.',['FIRE','PLATFORM',p,'LEAVE','STATION']),('Security alert. Do not touch unattended baggage.',['SECURITY','ALERT','NOT','TOUCH','BAGGAGE']),('An accident has occurred. Please call for help.',['ACCIDENT','HELP']),('Danger. Keep away from the tracks.',['DANGER','TRACK']),('Medical emergency at platform '+p+'.',['MEDICAL','EMERGENCY','PLATFORM',p]),('Evacuate platform '+p+' immediately.',['EVACUATE','PLATFORM',p]),('Smoke detected. Follow emergency instructions.',['SMOKE','EMERGENCY']),('Warning: suspicious object near the exit.',['WARNING','OBJECT','EXIT']),('Emergency. Stop boarding train '+n+'.',['EMERGENCY','STOP','BOARD','TRAIN',n])]
        for text, units in emergency:
            add('Emergency',text,{'platform':p} if 'platform '+p in text else {'train_number':n} if 'train '+n in text else {},units)
        other = [('Please keep your ticket ready.',['TICKET','READY']),('Board train '+n+' at platform '+p+'.',['BOARD','TRAIN',n,'PLATFORM',p]),('Train '+n+' to Pune.',['TRAIN',n,'TO','PUNE']),('Drinking water is available near platform '+p+'.',['DRINKING WATER','PLATFORM',p]),('Please mind the gap.',['GAP']),('The ticket counter is closed.',['TICKET','COUNTER','CLOSED']),('Welcome to Nagpur station.',['WELCOME','NAGPUR','STATION']),('Train '+n+' from Xylophonex to Quizzleville.',['TRAIN',n,'FROM','XYLOPHONEX','TO','QUIZZLEVILLE']),('Passengers for Mumbai should proceed to platform '+p+'.',['PASSENGER','MUMBAI','PLATFORM',p]),('Keep the station clean.',['STATION','CLEAN'])]
        for text,units in other:
            entities = {}
            if n in text: entities['train_number']=n
            if 'platform '+p in text: entities['platform']=p
            if 'to Pune' in text: entities['destination']='pune'
            if 'Xylophonex' in text: entities.update(source='xylophonex',destination='quizzleville')
            add('Other',text,entities,units)
    return rows

def main():
    data = make_dataset()
    assert len(data)==210 and len({r['id'] for r in data})==210
    save(ROOT/'tests/research_evaluation/announcements.json',data)
    conflicts=[]
    for i in range(10):
        n,p = str(1201+i), str(1+i%7)
        base=f'Train {n} from Nagpur to Mumbai will arrive at platform {p} at 5:30 PM'
        for kind, wrong in [('train_number',base.replace(n,str(9901+i))),('platform',base.replace('platform '+p,'platform '+str(int(p)+1))),('destination',base.replace('Mumbai','Pune')),('time',base.replace('5:30','6:30')),('cancellation_status',f'Train {n} from Nagpur to Mumbai is cancelled')]:
            conflicts.append(dict(id=f'{kind}-{i}',kind=kind,announcement=base,trusted_statement=wrong,expected_conflict=True))
        conflicts.append(dict(id=f'no-conflict-{i}',kind='negative_control',announcement=base,trusted_statement=base,expected_conflict=False))
    save(ROOT/'tests/research_evaluation/safety_conflicts.json',conflicts)
    robustness=[('empty',''),('whitespace','   '),('numbers','1201'),('unknown_station','Train 1201 arrives from Xylophonex'),('misspelled_station','Train 1201 arrives at Nagpoor'),('mixed_case','tRaIn 1201 ArRiVeS aT pLaTfOrM 2'),('spaces','  Train   1201 arrives  at platform 2  '),('punctuation','Train 1201, arrives at platform 2!!!'),('too_long','Train '*500),('invalid_train','Train ABC arrives at platform 2'),('invalid_platform','Train 1201 arrives at platform 999'),('unsupported_grammar','Platform 2 train 1201 Mumbai departure'),('hindi','ट्रेन 1201 प्लेटफॉर्म 2 पर आ रही है'),('marathi','गाडी 1201 फलाट 2 वर येत आहे'),('mandatory','Train 1201 arrives at platform 2')]
    save(ROOT/'tests/research_evaluation/robustness.json',[dict(id=i,text=t) for i,t in robustness])
    print('Created 210 labelled announcements, 50 conflicts + 10 controls, 15 robustness cases.')

if __name__=='__main__': main()
