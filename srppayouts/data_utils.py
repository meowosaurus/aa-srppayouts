from django.db import models

from .models import Ship, Reimbursement, Payout

def add_example_reimbursements():
    if not Reimbursement.objects.filter(name="CTA", index=0).exists():
        Reimbursement.objects.create(name="CTA", index=0)
    if not Reimbursement.objects.filter(name="Strategic", index=1).exists():
        Reimbursement.objects.create(name="Strategic", index=1)
    if not Reimbursement.objects.filter(name="Fun Fleet", index=2).exists():
        Reimbursement.objects.create(name="Fun Fleet", index=2)

def add_example_payouts():
    cta_reimbursement = Reimbursement.objects.get(name="CTA", index=0)
    strat_reimbursement = Reimbursement.objects.get(name="Strategic", index=1)
    fun_reimbursement = Reimbursement.objects.get(name="Fun Fleet", index=2)
    ferox = Ship.objects.get(name="Ferox")
    osprey = Ship.objects.get(name="Osprey")
    sabre = Ship.objects.get(name="Sabre")
    cyclone = Ship.objects.get(name="Cyclone")
    monitor = Ship.objects.get(name="Monitor")

    if not Payout.objects.filter(reimbursement=cta_reimbursement, ship=ferox, value=100000000).exists():
        Payout.objects.create(reimbursement=cta_reimbursement, ship=ferox, value=100000000)
    if not Payout.objects.filter(reimbursement=strat_reimbursement, ship=ferox, value=70000000).exists():
        Payout.objects.create(reimbursement=strat_reimbursement, ship=ferox, value=70000000)
    if not Payout.objects.filter(reimbursement=fun_reimbursement, ship=ferox, value=30000000).exists():
        Payout.objects.create(reimbursement=fun_reimbursement, ship=ferox, value=30000000)
    
    if not Payout.objects.filter(reimbursement=cta_reimbursement, ship=osprey, value=3000000).exists():
        Payout.objects.create(reimbursement=cta_reimbursement, ship=osprey, value=30000000)
    if not Payout.objects.filter(reimbursement=strat_reimbursement, ship=osprey, value=3000000).exists():
        Payout.objects.create(reimbursement=strat_reimbursement, ship=osprey, value=30000000)
    if not Payout.objects.filter(reimbursement=fun_reimbursement, ship=osprey, value=1500000).exists():
        Payout.objects.create(reimbursement=fun_reimbursement, ship=osprey, value=15000000)

    if not Payout.objects.filter(reimbursement=cta_reimbursement, ship=sabre, value=10000000).exists():
        Payout.objects.create(reimbursement=cta_reimbursement, ship=sabre, value=100000000)
    if not Payout.objects.filter(reimbursement=strat_reimbursement, ship=sabre, value=7000000).exists():
        Payout.objects.create(reimbursement=strat_reimbursement, ship=sabre, value=70000000)
    if not Payout.objects.filter(reimbursement=fun_reimbursement, ship=sabre, value=50000000).exists():
        Payout.objects.create(reimbursement=fun_reimbursement, ship=sabre, value=50000000)
    
    if not Payout.objects.filter(reimbursement=cta_reimbursement, ship=cyclone, value=5000000).exists():
        Payout.objects.create(reimbursement=cta_reimbursement, ship=cyclone, value=50000000)
    if not Payout.objects.filter(reimbursement=strat_reimbursement, ship=cyclone, value=3000000).exists():
        Payout.objects.create(reimbursement=strat_reimbursement, ship=cyclone, value=30000000)
    if not Payout.objects.filter(reimbursement=fun_reimbursement, ship=cyclone, value=0).exists():
        Payout.objects.create(reimbursement=fun_reimbursement, ship=cyclone, value=0)

    if not Payout.objects.filter(reimbursement=cta_reimbursement, ship=monitor, value=300000000).exists():
        Payout.objects.create(reimbursement=cta_reimbursement, ship=monitor, value=300000000)
    if not Payout.objects.filter(reimbursement=strat_reimbursement, ship=monitor, value=200000000).exists():
        Payout.objects.create(reimbursement=strat_reimbursement, ship=monitor, value=200000000)
    if not Payout.objects.filter(reimbursement=fun_reimbursement, ship=monitor, value=0).exists():
        Payout.objects.create(reimbursement=fun_reimbursement, ship=monitor, value=0)

def add_ships():
    if not Ship.objects.filter(name='Absolution', ship_id=22448).exists():
        Ship.objects.create(name='Absolution', ship_id=22448)
    if not Ship.objects.filter(name='Algos', ship_id=32872).exists():
        Ship.objects.create(name='Algos', ship_id=32872)
    if not Ship.objects.filter(name='Anathema', ship_id=11188).exists():
        Ship.objects.create(name='Anathema', ship_id=11188)
    if not Ship.objects.filter(name='Apostle', ship_id=37604).exists():
        Ship.objects.create(name='Apostle', ship_id=37604)
    if not Ship.objects.filter(name='Arazu', ship_id=11969).exists():
        Ship.objects.create(name='Arazu', ship_id=11969)
    if not Ship.objects.filter(name='Arbitrator', ship_id=628).exists():
        Ship.objects.create(name='Arbitrator', ship_id=628)
    if not Ship.objects.filter(name='Archon', ship_id=23757).exists():
        Ship.objects.create(name='Archon', ship_id=23757)
    if not Ship.objects.filter(name='Ares', ship_id=11202).exists():
        Ship.objects.create(name='Ares', ship_id=11202)
    if not Ship.objects.filter(name='Ashimmu', ship_id=17922).exists():
        Ship.objects.create(name='Ashimmu', ship_id=17922)
    if not Ship.objects.filter(name='Astero', ship_id=33468).exists():
        Ship.objects.create(name='Astero', ship_id=33468)
    if not Ship.objects.filter(name='Augoror', ship_id=625).exists():
        Ship.objects.create(name='Augoror', ship_id=625)
    if not Ship.objects.filter(name='Augoror Navy Issue', ship_id=29337).exists():
        Ship.objects.create(name='Augoror Navy Issue', ship_id=29337)
    if not Ship.objects.filter(name='Badger', ship_id=648).exists():
        Ship.objects.create(name='Badger', ship_id=648)
    if not Ship.objects.filter(name='Bantam', ship_id=582).exists():
        Ship.objects.create(name='Bantam', ship_id=582)
    if not Ship.objects.filter(name='Barghest', ship_id=33820).exists():
        Ship.objects.create(name='Barghest', ship_id=33820)
    if not Ship.objects.filter(name='Basilisk', ship_id=11985).exists():
        Ship.objects.create(name='Basilisk', ship_id=11985)
    if not Ship.objects.filter(name='Bellicose', ship_id=630).exists():
        Ship.objects.create(name='Bellicose', ship_id=630)
    if not Ship.objects.filter(name='Bhaalgorn', ship_id=17920).exists():
        Ship.objects.create(name='Bhaalgorn', ship_id=17920)
    if not Ship.objects.filter(name='Bifrost', ship_id=37480).exists():
        Ship.objects.create(name='Bifrost', ship_id=37480)
    if not Ship.objects.filter(name='Blackbird', ship_id=632).exists():
        Ship.objects.create(name='Blackbird', ship_id=632)
    if not Ship.objects.filter(name='Broadsword', ship_id=12013).exists():
        Ship.objects.create(name='Broadsword', ship_id=12013)
    if not Ship.objects.filter(name='Brutix', ship_id=16229).exists():
        Ship.objects.create(name='Brutix', ship_id=16229)
    if not Ship.objects.filter(name='Brutix Navy Issue', ship_id=33151).exists():
        Ship.objects.create(name='Brutix Navy Issue', ship_id=33151)
    if not Ship.objects.filter(name='Burst', ship_id=599).exists():
        Ship.objects.create(name='Burst', ship_id=599)
    if not Ship.objects.filter(name='Buzzard', ship_id=11192).exists():
        Ship.objects.create(name='Buzzard', ship_id=11192)
    if not Ship.objects.filter(name='Caedes', ship_id=42246).exists():
        Ship.objects.create(name='Caedes', ship_id=42246)
    if not Ship.objects.filter(name='Caldari Navy Hookbill', ship_id=17619).exists():
        Ship.objects.create(name='Caldari Navy Hookbill', ship_id=17619)
    if not Ship.objects.filter(name='Capsule', ship_id=670).exists():
        Ship.objects.create(name='Capsule', ship_id=670)
    if not Ship.objects.filter(name='Caracal', ship_id=621).exists():
        Ship.objects.create(name='Caracal', ship_id=621)
    if not Ship.objects.filter(name='Caracal Navy Issue', ship_id=17634).exists():
        Ship.objects.create(name='Caracal Navy Issue', ship_id=17634)
    if not Ship.objects.filter(name='Catalyst', ship_id=16240).exists():
        Ship.objects.create(name='Catalyst', ship_id=16240)
    if not Ship.objects.filter(name='Catalyst Navy Issue', ship_id=73796).exists():
        Ship.objects.create(name='Catalyst Navy Issue', ship_id=73796)
    if not Ship.objects.filter(name='Celestis', ship_id=633).exists():
        Ship.objects.create(name='Celestis', ship_id=633)
    if not Ship.objects.filter(name='Cheetah', ship_id=11182).exists():
        Ship.objects.create(name='Cheetah', ship_id=11182)
    if not Ship.objects.filter(name='Chimera', ship_id=23915).exists():
        Ship.objects.create(name='Chimera', ship_id=23915)
    if not Ship.objects.filter(name='Claw', ship_id=11196).exists():
        Ship.objects.create(name='Claw', ship_id=11196)
    if not Ship.objects.filter(name='Claymore', ship_id=22468).exists():
        Ship.objects.create(name='Claymore', ship_id=22468)
    if not Ship.objects.filter(name='Coercer', ship_id=16236).exists():
        Ship.objects.create(name='Coercer', ship_id=16236)
    if not Ship.objects.filter(name='Coercer Navy Issue', ship_id=73789).exists():
        Ship.objects.create(name='Coercer Navy Issue', ship_id=73789)
    if not Ship.objects.filter(name='Confessor', ship_id=34317).exists():
        Ship.objects.create(name='Confessor', ship_id=34317)
    if not Ship.objects.filter(name='Corax', ship_id=32876).exists():
        Ship.objects.create(name='Corax', ship_id=32876)
    if not Ship.objects.filter(name='Cormorant', ship_id=16238).exists():
        Ship.objects.create(name='Cormorant', ship_id=16238)
    if not Ship.objects.filter(name='Cormorant Navy Issue', ship_id=73795).exists():
        Ship.objects.create(name='Cormorant Navy Issue', ship_id=73795)
    if not Ship.objects.filter(name='Crow', ship_id=11176).exists():
        Ship.objects.create(name='Crow', ship_id=11176)
    if not Ship.objects.filter(name='Crucifier', ship_id=2161).exists():
        Ship.objects.create(name='Crucifier', ship_id=2161)
    if not Ship.objects.filter(name='Crucifier Navy Issue', ship_id=37453).exists():
        Ship.objects.create(name='Crucifier Navy Issue', ship_id=37453)
    if not Ship.objects.filter(name='Cruor', ship_id=17926).exists():
        Ship.objects.create(name='Cruor', ship_id=17926)
    if not Ship.objects.filter(name='Crusader', ship_id=11184).exists():
        Ship.objects.create(name='Crusader', ship_id=11184)
    if not Ship.objects.filter(name='Curse', ship_id=20125).exists():
        Ship.objects.create(name='Curse', ship_id=20125)
    if not Ship.objects.filter(name='Cyclone', ship_id=16231).exists():
        Ship.objects.create(name='Cyclone', ship_id=16231)
    if not Ship.objects.filter(name='Cynabal', ship_id=17720).exists():
        Ship.objects.create(name='Cynabal', ship_id=17720)
    if not Ship.objects.filter(name='Damavik', ship_id=47269).exists():
        Ship.objects.create(name='Damavik', ship_id=47269)
    if not Ship.objects.filter(name='Damnation', ship_id=22474).exists():
        Ship.objects.create(name='Damnation', ship_id=22474)
    if not Ship.objects.filter(name='Daredevil', ship_id=17928).exists():
        Ship.objects.create(name='Daredevil', ship_id=17928)
    if not Ship.objects.filter(name='Deacon', ship_id=37457).exists():
        Ship.objects.create(name='Deacon', ship_id=37457)
    if not Ship.objects.filter(name='Devoter', ship_id=12017).exists():
        Ship.objects.create(name='Devoter', ship_id=12017)
    if not Ship.objects.filter(name='Dragoon', ship_id=32874).exists():
        Ship.objects.create(name='Dragoon', ship_id=32874)
    if not Ship.objects.filter(name='Drake', ship_id=24698).exists():
        Ship.objects.create(name='Drake', ship_id=24698)
    if not Ship.objects.filter(name='Drake Navy Issue', ship_id=33153).exists():
        Ship.objects.create(name='Drake Navy Issue', ship_id=33153)
    if not Ship.objects.filter(name='Dramiel', ship_id=17932).exists():
        Ship.objects.create(name='Dramiel', ship_id=17932)
    if not Ship.objects.filter(name='Draugur', ship_id=52254).exists():
        Ship.objects.create(name='Draugur', ship_id=52254)
    if not Ship.objects.filter(name='Drekavac', ship_id=49711).exists():
        Ship.objects.create(name='Drekavac', ship_id=49711)
    if not Ship.objects.filter(name='Eagle', ship_id=12011).exists():
        Ship.objects.create(name='Eagle', ship_id=12011)
    if not Ship.objects.filter(name='Endurance', ship_id=37135).exists():
        Ship.objects.create(name='Endurance', ship_id=37135)
    if not Ship.objects.filter(name='Enforcer', ship_id=44995).exists():
        Ship.objects.create(name='Enforcer', ship_id=44995)
    if not Ship.objects.filter(name='Enyo', ship_id=12044).exists():
        Ship.objects.create(name='Enyo', ship_id=12044)
    if not Ship.objects.filter(name='Eos', ship_id=22442).exists():
        Ship.objects.create(name='Eos', ship_id=22442)
    if not Ship.objects.filter(name='Eris', ship_id=22460).exists():
        Ship.objects.create(name='Eris', ship_id=22460)
    if not Ship.objects.filter(name='Exequror', ship_id=634).exists():
        Ship.objects.create(name='Exequror', ship_id=634)
    if not Ship.objects.filter(name='Exequror Navy Issue', ship_id=29344).exists():
        Ship.objects.create(name='Exequror Navy Issue', ship_id=29344)
    if not Ship.objects.filter(name='Falcon', ship_id=11957).exists():
        Ship.objects.create(name='Falcon', ship_id=11957)
    if not Ship.objects.filter(name='Federation Navy Comet', ship_id=17841).exists():
        Ship.objects.create(name='Federation Navy Comet', ship_id=17841)
    if not Ship.objects.filter(name='Ferox', ship_id=16227).exists():
        Ship.objects.create(name='Ferox', ship_id=16227)
    if not Ship.objects.filter(name='Flycatcher', ship_id=22464).exists():
        Ship.objects.create(name='Flycatcher', ship_id=22464)
    if not Ship.objects.filter(name='Garmur', ship_id=33816).exists():
        Ship.objects.create(name='Garmur', ship_id=33816)
    if not Ship.objects.filter(name='Gila', ship_id=17715).exists():
        Ship.objects.create(name='Gila', ship_id=17715)
    if not Ship.objects.filter(name='Gnosis', ship_id=3756).exists():
        Ship.objects.create(name='Gnosis', ship_id=3756)
    if not Ship.objects.filter(name='Griffin', ship_id=584).exists():
        Ship.objects.create(name='Griffin', ship_id=584)
    if not Ship.objects.filter(name='Griffin Navy Issue', ship_id=37455).exists():
        Ship.objects.create(name='Griffin Navy Issue', ship_id=37455)
    if not Ship.objects.filter(name='Guardian', ship_id=11987).exists():
        Ship.objects.create(name='Guardian', ship_id=11987)
    if not Ship.objects.filter(name='Harbinger', ship_id=24696).exists():
        Ship.objects.create(name='Harbinger', ship_id=24696)
    if not Ship.objects.filter(name='Harbinger Navy Issue', ship_id=33155).exists():
        Ship.objects.create(name='Harbinger Navy Issue', ship_id=33155)
    if not Ship.objects.filter(name='Harpy', ship_id=11381).exists():
        Ship.objects.create(name='Harpy', ship_id=11381)
    if not Ship.objects.filter(name='Hawk', ship_id=11379).exists():
        Ship.objects.create(name='Hawk', ship_id=11379)
    if not Ship.objects.filter(name='Hecate', ship_id=35683).exists():
        Ship.objects.create(name='Hecate', ship_id=35683)
    if not Ship.objects.filter(name='Helios', ship_id=11172).exists():
        Ship.objects.create(name='Helios', ship_id=11172)
    if not Ship.objects.filter(name='Heretic', ship_id=22452).exists():
        Ship.objects.create(name='Heretic', ship_id=22452)
    if not Ship.objects.filter(name='Hound', ship_id=12034).exists():
        Ship.objects.create(name='Hound', ship_id=12034)
    if not Ship.objects.filter(name='Huginn', ship_id=11961).exists():
        Ship.objects.create(name='Huginn', ship_id=11961)
    if not Ship.objects.filter(name='Hurricane', ship_id=24702).exists():
        Ship.objects.create(name='Hurricane', ship_id=24702)
    if not Ship.objects.filter(name='Hurricane Fleet Issue', ship_id=33157).exists():
        Ship.objects.create(name='Hurricane Fleet Issue', ship_id=33157)
    if not Ship.objects.filter(name='Hyena', ship_id=11387).exists():
        Ship.objects.create(name='Hyena', ship_id=11387)
    if not Ship.objects.filter(name='Imperial Navy Slicer', ship_id=17703).exists():
        Ship.objects.create(name='Imperial Navy Slicer', ship_id=17703)
    if not Ship.objects.filter(name='Ishkur', ship_id=12042).exists():
        Ship.objects.create(name='Ishkur', ship_id=12042)
    if not Ship.objects.filter(name='Ishtar', ship_id=12005).exists():
        Ship.objects.create(name='Ishtar', ship_id=12005)
    if not Ship.objects.filter(name='Jackdaw', ship_id=34828).exists():
        Ship.objects.create(name='Jackdaw', ship_id=34828)
    if not Ship.objects.filter(name='Jaguar', ship_id=11400).exists():
        Ship.objects.create(name='Jaguar', ship_id=11400)
    if not Ship.objects.filter(name='Keres', ship_id=11174).exists():
        Ship.objects.create(name='Keres', ship_id=11174)
    if not Ship.objects.filter(name='Kestrel', ship_id=602).exists():
        Ship.objects.create(name='Kestrel', ship_id=602)
    if not Ship.objects.filter(name='Kikimora', ship_id=49710).exists():
        Ship.objects.create(name='Kikimora', ship_id=49710)
    if not Ship.objects.filter(name='Kirin', ship_id=37458).exists():
        Ship.objects.create(name='Kirin', ship_id=37458)
    if not Ship.objects.filter(name='Kitsune', ship_id=11194).exists():
        Ship.objects.create(name='Kitsune', ship_id=11194)
    if not Ship.objects.filter(name='Lachesis', ship_id=11971).exists():
        Ship.objects.create(name='Lachesis', ship_id=11971)
    if not Ship.objects.filter(name='Legion', ship_id=29986).exists():
        Ship.objects.create(name='Legion', ship_id=29986)
    if not Ship.objects.filter(name='Leshak', ship_id=47271).exists():
        Ship.objects.create(name='Leshak', ship_id=47271)
    if not Ship.objects.filter(name='Lif', ship_id=37606).exists():
        Ship.objects.create(name='Lif', ship_id=37606)
    if not Ship.objects.filter(name='Loki', ship_id=29990).exists():
        Ship.objects.create(name='Loki', ship_id=29990)
    if not Ship.objects.filter(name='Machariel', ship_id=17738).exists():
        Ship.objects.create(name='Machariel', ship_id=17738)
    if not Ship.objects.filter(name='Magus', ship_id=37483).exists():
        Ship.objects.create(name='Magus', ship_id=37483)
    if not Ship.objects.filter(name='Malediction', ship_id=11186).exists():
        Ship.objects.create(name='Malediction', ship_id=11186)
    if not Ship.objects.filter(name='Maller', ship_id=624).exists():
        Ship.objects.create(name='Maller', ship_id=624)
    if not Ship.objects.filter(name='Manticore', ship_id=12032).exists():
        Ship.objects.create(name='Manticore', ship_id=12032)
    if not Ship.objects.filter(name='Marshal', ship_id=44996).exists():
        Ship.objects.create(name='Marshal', ship_id=44996)
    if not Ship.objects.filter(name='Maulus', ship_id=609).exists():
        Ship.objects.create(name='Maulus', ship_id=609)
    if not Ship.objects.filter(name='Maulus Navy Issue', ship_id=37456).exists():
        Ship.objects.create(name='Maulus Navy Issue', ship_id=37456)
    if not Ship.objects.filter(name='Megathron', ship_id=641).exists():
        Ship.objects.create(name='Megathron', ship_id=641)
    if not Ship.objects.filter(name='Megathron Navy Issue', ship_id=17728).exists():
        Ship.objects.create(name='Megathron Navy Issue', ship_id=17728)
    if not Ship.objects.filter(name='Minokawa', ship_id=37605).exists():
        Ship.objects.create(name='Minokawa', ship_id=37605)
    if not Ship.objects.filter(name='Moa', ship_id=623).exists():
        Ship.objects.create(name='Moa', ship_id=623)
    if not Ship.objects.filter(name='Moros', ship_id=19724).exists():
        Ship.objects.create(name='Moros', ship_id=19724)
    if not Ship.objects.filter(name='Moros Navy Issue', ship_id=73792).exists():
        Ship.objects.create(name='Moros Navy Issue', ship_id=73792)
    if not Ship.objects.filter(name='Muninn', ship_id=12015).exists():
        Ship.objects.create(name='Muninn', ship_id=12015)
    if not Ship.objects.filter(name='Myrmidon', ship_id=24700).exists():
        Ship.objects.create(name='Myrmidon', ship_id=24700)
    if not Ship.objects.filter(name='Naga', ship_id=4306).exists():
        Ship.objects.create(name='Naga', ship_id=4306)
    if not Ship.objects.filter(name='Naglfar', ship_id=19722).exists():
        Ship.objects.create(name='Naglfar', ship_id=19722)
    if not Ship.objects.filter(name='Nemesis', ship_id=11377).exists():
        Ship.objects.create(name='Nemesis', ship_id=11377)
    if not Ship.objects.filter(name='Nereus', ship_id=650).exists():
        Ship.objects.create(name='Nereus', ship_id=650)
    if not Ship.objects.filter(name='Nidhoggur', ship_id=24483).exists():
        Ship.objects.create(name='Nidhoggur', ship_id=24483)
    if not Ship.objects.filter(name='Nighthawk', ship_id=22470).exists():
        Ship.objects.create(name='Nighthawk', ship_id=22470)
    if not Ship.objects.filter(name='Ninazu', ship_id=37607).exists():
        Ship.objects.create(name='Ninazu', ship_id=37607)
    if not Ship.objects.filter(name='Omen', ship_id=2006).exists():
        Ship.objects.create(name='Omen', ship_id=2006)
    if not Ship.objects.filter(name='Omen Navy Issue', ship_id=17709).exists():
        Ship.objects.create(name='Omen Navy Issue', ship_id=17709)
    if not Ship.objects.filter(name='Oneiros', ship_id=11989).exists():
        Ship.objects.create(name='Oneiros', ship_id=11989)
    if not Ship.objects.filter(name='Onyx', ship_id=11995).exists():
        Ship.objects.create(name='Onyx', ship_id=11995)
    if not Ship.objects.filter(name='Oracle', ship_id=4302).exists():
        Ship.objects.create(name='Oracle', ship_id=4302)
    if not Ship.objects.filter(name='Orthrus', ship_id=33818).exists():
        Ship.objects.create(name='Orthrus', ship_id=33818)
    if not Ship.objects.filter(name='Osprey', ship_id=620).exists():
        Ship.objects.create(name='Osprey', ship_id=620)
    if not Ship.objects.filter(name='Osprey Navy Issue', ship_id=29340).exists():
        Ship.objects.create(name='Osprey Navy Issue', ship_id=29340)
    if not Ship.objects.filter(name='Panther', ship_id=22440).exists():
        Ship.objects.create(name='Panther', ship_id=22440)
    if not Ship.objects.filter(name='Phantasm', ship_id=17718).exists():
        Ship.objects.create(name='Phantasm', ship_id=17718)
    if not Ship.objects.filter(name='Phobos', ship_id=12021).exists():
        Ship.objects.create(name='Phobos', ship_id=12021)
    if not Ship.objects.filter(name='Phoenix', ship_id=19726).exists():
        Ship.objects.create(name='Phoenix', ship_id=19726)
    if not Ship.objects.filter(name='Phoenix Navy Issue', ship_id=73793).exists():
        Ship.objects.create(name='Phoenix Navy Issue', ship_id=73793)
    if not Ship.objects.filter(name='Pilgrim', ship_id=11965).exists():
        Ship.objects.create(name='Pilgrim', ship_id=11965)
    if not Ship.objects.filter(name='Pontifex', ship_id=37481).exists():
        Ship.objects.create(name='Pontifex', ship_id=37481)
    if not Ship.objects.filter(name='Porpoise', ship_id=42244).exists():
        Ship.objects.create(name='Porpoise', ship_id=42244)
    if not Ship.objects.filter(name='Praxis', ship_id=47466).exists():
        Ship.objects.create(name='Praxis', ship_id=47466)
    if not Ship.objects.filter(name='Procurer', ship_id=17480).exists():
        Ship.objects.create(name='Procurer', ship_id=17480)
    if not Ship.objects.filter(name='Prophecy', ship_id=16233).exists():
        Ship.objects.create(name='Prophecy', ship_id=16233)
    if not Ship.objects.filter(name='Prospect', ship_id=33697).exists():
        Ship.objects.create(name='Prospect', ship_id=33697)
    if not Ship.objects.filter(name='Proteus', ship_id=29988).exists():
        Ship.objects.create(name='Proteus', ship_id=29988)
    if not Ship.objects.filter(name='Purifier', ship_id=12038).exists():
        Ship.objects.create(name='Purifier', ship_id=12038)
    if not Ship.objects.filter(name='Rapier', ship_id=11963).exists():
        Ship.objects.create(name='Rapier', ship_id=11963)
    if not Ship.objects.filter(name='Raptor', ship_id=11178).exists():
        Ship.objects.create(name='Raptor', ship_id=11178)
    if not Ship.objects.filter(name='Redeemer', ship_id=22428).exists():
        Ship.objects.create(name='Redeemer', ship_id=22428)
    if not Ship.objects.filter(name='Republic Fleet Firetail', ship_id=17812).exists():
        Ship.objects.create(name='Republic Fleet Firetail', ship_id=17812)
    if not Ship.objects.filter(name='Retribution', ship_id=11393).exists():
        Ship.objects.create(name='Retribution', ship_id=11393)
    if not Ship.objects.filter(name='Revelation', ship_id=19720).exists():
        Ship.objects.create(name='Revelation', ship_id=19720)
    if not Ship.objects.filter(name='Revelation Navy Issue', ship_id=73790).exists():
        Ship.objects.create(name='Revelation Navy Issue', ship_id=73790)
    if not Ship.objects.filter(name='Rodiva', ship_id=49712).exists():
        Ship.objects.create(name='Rodiva', ship_id=49712)
    if not Ship.objects.filter(name='Rokh', ship_id=24688).exists():
        Ship.objects.create(name='Rokh', ship_id=24688)
    if not Ship.objects.filter(name='Rook', ship_id=11959).exists():
        Ship.objects.create(name='Rook', ship_id=11959)
    if not Ship.objects.filter(name='Rupture', ship_id=629).exists():
        Ship.objects.create(name='Rupture', ship_id=629)
    if not Ship.objects.filter(name='Sabre', ship_id=22456).exists():
        Ship.objects.create(name='Sabre', ship_id=22456)
    if not Ship.objects.filter(name='Sacrilege', ship_id=12019).exists():
        Ship.objects.create(name='Sacrilege', ship_id=12019)
    if not Ship.objects.filter(name='Scalpel', ship_id=37460).exists():
        Ship.objects.create(name='Scalpel', ship_id=37460)
    if not Ship.objects.filter(name='Scimitar', ship_id=11978).exists():
        Ship.objects.create(name='Scimitar', ship_id=11978)
    if not Ship.objects.filter(name='Scythe', ship_id=631).exists():
        Ship.objects.create(name='Scythe', ship_id=631)
    if not Ship.objects.filter(name='Scythe Fleet Issue', ship_id=29336).exists():
        Ship.objects.create(name='Scythe Fleet Issue', ship_id=29336)
    if not Ship.objects.filter(name='Sentinel', ship_id=11190).exists():
        Ship.objects.create(name='Sentinel', ship_id=11190)
    if not Ship.objects.filter(name='Sigil', ship_id=19744).exists():
        Ship.objects.create(name='Sigil', ship_id=19744)
    if not Ship.objects.filter(name='Sin', ship_id=22430).exists():
        Ship.objects.create(name='Sin', ship_id=22430)
    if not Ship.objects.filter(name='Sleipnir', ship_id=22444).exists():
        Ship.objects.create(name='Sleipnir', ship_id=22444)
    if not Ship.objects.filter(name='Stabber', ship_id=622).exists():
        Ship.objects.create(name='Stabber', ship_id=622)
    if not Ship.objects.filter(name='Stabber Fleet Issue', ship_id=17713).exists():
        Ship.objects.create(name='Stabber Fleet Issue', ship_id=17713)
    if not Ship.objects.filter(name='Stiletto', ship_id=11198).exists():
        Ship.objects.create(name='Stiletto', ship_id=11198)
    if not Ship.objects.filter(name='Stork', ship_id=37482).exists():
        Ship.objects.create(name='Stork', ship_id=37482)
    if not Ship.objects.filter(name='Stormbringer', ship_id=54732).exists():
        Ship.objects.create(name='Stormbringer', ship_id=54732)
    if not Ship.objects.filter(name='Stratios', ship_id=33470).exists():
        Ship.objects.create(name='Stratios', ship_id=33470)
    if not Ship.objects.filter(name='Succubus', ship_id=17924).exists():
        Ship.objects.create(name='Succubus', ship_id=17924)
    if not Ship.objects.filter(name='Sunesis', ship_id=42685).exists():
        Ship.objects.create(name='Sunesis', ship_id=42685)
    if not Ship.objects.filter(name='Svipul', ship_id=34562).exists():
        Ship.objects.create(name='Svipul', ship_id=34562)
    if not Ship.objects.filter(name='Talos', ship_id=4308).exists():
        Ship.objects.create(name='Talos', ship_id=4308)
    if not Ship.objects.filter(name='Talwar', ship_id=32878).exists():
        Ship.objects.create(name='Talwar', ship_id=32878)
    if not Ship.objects.filter(name='Taranis', ship_id=11200).exists():
        Ship.objects.create(name='Taranis', ship_id=11200)
    if not Ship.objects.filter(name='Tempest Fleet Issue', ship_id=17732).exists():
        Ship.objects.create(name='Tempest Fleet Issue', ship_id=17732)
    if not Ship.objects.filter(name='Tengu', ship_id=29984).exists():
        Ship.objects.create(name='Tengu', ship_id=29984)
    if not Ship.objects.filter(name='Thalia', ship_id=37459).exists():
        Ship.objects.create(name='Thalia', ship_id=37459)
    if not Ship.objects.filter(name='Thanatos', ship_id=23911).exists():
        Ship.objects.create(name='Thanatos', ship_id=23911)
    if not Ship.objects.filter(name='Thorax', ship_id=627).exists():
        Ship.objects.create(name='Thorax', ship_id=627)
    if not Ship.objects.filter(name='Thrasher', ship_id=16242).exists():
        Ship.objects.create(name='Thrasher', ship_id=16242)
    if not Ship.objects.filter(name='Thrasher Fleet Issue', ship_id=73794).exists():
        Ship.objects.create(name='Thrasher Fleet Issue', ship_id=73794)
    if not Ship.objects.filter(name='Tornado', ship_id=4310).exists():
        Ship.objects.create(name='Tornado', ship_id=4310)
    if not Ship.objects.filter(name='Typhoon', ship_id=644).exists():
        Ship.objects.create(name='Typhoon', ship_id=644)
    if not Ship.objects.filter(name='Vedmak', ship_id=47270).exists():
        Ship.objects.create(name='Vedmak', ship_id=47270)
    if not Ship.objects.filter(name='Vengeance', ship_id=11365).exists():
        Ship.objects.create(name='Vengeance', ship_id=11365)
    if not Ship.objects.filter(name='Vexor', ship_id=626).exists():
        Ship.objects.create(name='Vexor', ship_id=626)
    if not Ship.objects.filter(name='Vexor Navy Issue', ship_id=17843).exists():
        Ship.objects.create(name='Vexor Navy Issue', ship_id=17843)
    if not Ship.objects.filter(name='Vigil', ship_id=3766).exists():
        Ship.objects.create(name='Vigil', ship_id=3766)
    if not Ship.objects.filter(name='Vigil Fleet Issue', ship_id=37454).exists():
        Ship.objects.create(name='Vigil Fleet Issue', ship_id=37454)
    if not Ship.objects.filter(name='Vigilant', ship_id=17722).exists():
        Ship.objects.create(name='Vigilant', ship_id=17722)
    if not Ship.objects.filter(name='Vulture', ship_id=22446).exists():
        Ship.objects.create(name='Vulture', ship_id=22446)
    if not Ship.objects.filter(name='Widow', ship_id=22436).exists():
        Ship.objects.create(name='Widow', ship_id=22436)
    if not Ship.objects.filter(name='Wolf', ship_id=11371).exists():
        Ship.objects.create(name='Wolf', ship_id=11371)
    if not Ship.objects.filter(name='Worm', ship_id=17930).exists():
        Ship.objects.create(name='Worm', ship_id=17930)
    if not Ship.objects.filter(name='Zirnitra', ship_id=52907).exists():
        Ship.objects.create(name='Zirnitra', ship_id=52907)
    if not Ship.objects.filter(name='Monitor', ship_id=45534).exists():
        Ship.objects.create(name='Monitor', ship_id=45534)
