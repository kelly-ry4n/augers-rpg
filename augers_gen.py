import subprocess

class Arrow(object):

    def __init__(self, start, end, color='black'):

        self.start = start
        self.end = end
        self.color = color

    def __repr__(self):
        try:
            return '''
            "{}"[tooltip="{}",href="{}"]
            "{}"[tooltip="{}",href="{}"]

            "{}" -> "{}"[color="{}",href="https://google.ca"];'''.format(
                self.start.full_name, 
                self.start.desc,
                'index.html#'+self.start.full_name.replace(' ','-'),

                self.end.full_name,
                self.end.desc,
                'index.html#'+self.end.full_name.replace(' ','-'),


                self.start.full_name, 
                self.end.full_name, 
                self.color)
        except:
            return ''

class S(object):

    def __init__(self, name, tier, desc):
        self.name = name
        self.tier = tier
        self.desc = desc

        self._children = []
        self._parents = []

    def __repr__(self):
        return self.name

    @property
    def full_name(self):
        return ' '.join([self.name, self.tier])

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, val):

        if isinstance(val, S):
            data = val
            color = 'black'
        else:
            data, color = val[0], val[1]

        self._children.append(Arrow(self, data, color))
        data._parents.append(self)
        return self




alive = S('Alive', "", '''+2 wounds
+4 speed
0 Khan
0 Essence
d6 Physical
''')

auger = S('Auger', "", '''+5 Khan''')
khan0 = S('Khan', '0', '''+5 Khan
    +1 Khan Resist
''')
khan2 = S('Khan', '2', '''+10 Khan''')
khan3 = S('Khan', '3', '''+15 Khan''')
khan4 = S('Khan', '4', '''+20 Khan''')
ks2 = S('Khan Sensing','2','''Passive: Recognize Augers at a glance.

Sense the powers of Augers. Tells you the highest tier Auger ability known with no risk. If they know more than one of their highest tier, DM will randomize.

+1 Khan Resist
''')
sk2 = S('Khan Sensing','2','''Passive: Sense gifted at a glance
Sense the powers of Gifted. Tells you the highest tier Gifted ability known with no risk. If they know more than one, DM will randomize.
''')
reading1 = S('Reading', '1', '''Read the surface thoughts of an enemy. You learn what they are going to do next, locking them in for their next action.

1d6 per point Khan
''')

reading2 = S('Reading', '2', '''Read the in depth thoughts of an enemy, learning what surprises or plans they might have, plus the effect of Reading 1.

1d6 per 2 points Khan
''')

control3 = S('Control', '3', '''Control the mind of target, taking over their actions.

1d6 per 3 points Khan * 1 round per 3 points Khan
''')

st1 = S('Slow Time','1','''Drop a little out of the flow of time. You move fast. Stuff moves slowly.

Gain an extra action per round
1 round per 2 points Khan
''')

st2 = S('Slow Time', '2', '''''')

st4 = S('Slow Time','4','''Slow Time 4

Drop well outside the flow of time.


Gain an extra 2 actions per round
1 round per 4 pounds Khan
''')
cft3 = S('Cast From Time', '3', '''Banish target from time for one round

1d6/2 Khan
duration 5 Khan / round
''')

ec1 = S('Essence Control', '1', '''+100 essence

Steal 50 essence from target per success

1d6/ Khan
''')

ec3 = S('Essence Control', '3', '''+20 essence

Move 50 essence from target to target

1d6/ 2 Khan
''')

skilled = S('Skilled', '', '''+1 wounds
+100 Essence
+d6 Physical
''')

educated0 = S('Educated','0', '''Once per battle, learn something useful about the environment the baddies haven't thought of.

+1 Khan Resist
''')

educated1 = S('Educated', '1', '''When you encounter a creature, you will learn something useful about its strengths or weaknesses.
''')

educated2 = S('Educated', '2','''+2 Khan Resist
''')

educated3 = S('Educated', '3','''TODO
''')

physical0 = S('Physical', '0', '''You're not too skinny.

+2 Wounds
+2 Movement
+d6 Physical
''')

physical2 = S('Physical', '2','''+2 Wounds
+2 Movement
+2d6 Physical
''')

wt1 = S('Weapons Training', '1', '''Your melee weapons threats are multiplied by 3
''')

wm3 = S('Weapons Mastery', '3', '''Your weapons threats are multiplied by 3. Choose which weapons this applies to.

Scales additively, so you have Weapons Training 1 and Weapons Mastery 3, you have a x6 modifier. On a sword, you have 6 threat dice, on a dagger you have 12 threat dice.
''')

at2 = S('Armor Training', '2','''Reduces incoming wounds by 1, to a minimum of 1. Apply after any division.

For example, if you take half wounds from essence based attacks, and an essence blast inflicts 6 wounds you would
Reduce the wounds to 3 by dividing
Reduce the wounds to 2 using Armor Training 2
''')

md1 = S('Muscle Development','1','''+3 Wounds
+2 Movement
''')

unsurprisable1 = S('Unsurprisable', '1', '''You can always roll for initiative, even if caught off guard
''')

ucd4 = S('Uncanny Dodge', '4', '''If you are free to move ranged attacks are disadvantaged against you.
''')

es2 = S('Essence Sensing', '2', '''In a battle, foes locations are always revealed to you''')
shielding1 = S('Shielding', '1', '''As a reaction, you can spend 400 essence to block 1 wound''')

evasion1 = S('Evasion','1', '''AOE attacks deal half wounds, round up the final number after all other factors
''')
evasion2 = S('Evasion','2', '''Melee attacks deal half wounds, round up the final number after all other factors

For example, if you take half wounds from essence based attacks, and an essence blast inflicts 6 wounds you would
Reduce the wounds to 3 by dividing
Reduce the wounds to 2 using Armor Training 2
''')

movement1 = S('Movement', '1', '''-1 Wounds from AoO. Can Reduce to 0. Applied first.
''')

discipline3 = S('Descipline','3','''Risk wounds to gain Khan.

1 Risk per 4 Khan.
''')

sh3 = S('Self Healing', '3', '''You can heal a wound you take immediately after you take it. If you fall unconscious, this effect ends. Requires 1 success

1d6/ 200 Essence/round
''')

gifted = S('Gifted', '','''You can channel Essence. Nice.

+200 Essence
''')

essence0 = S('Essence', '0', '''+1 Khan Resist
+700 Essence
''')

healing1 = S('Healing', '1', '''Attempt to heal a wound.

1d6/100 essence.
''')

healing2 = S('Healing', '2', '''Attempt to heal up to 3 wounds. Each success heals one wound.

1d6/150 essence
''')

aoeh2 = S('AOE Healing','2','''Attempt to heal 1wound/target in a 3x3 cube. Each success heals 1 wound.Effects allies and enemies.

2d6/300 essence
''')
aoes2 = S("AOE Shielding", '2', '''Selected 6 square area risks 1 wound to travel through

200 Essence/round''')

ek1 = S('Essence Knife', '1','''Manifest a dagger of essence which ignores physical armor''')
eb2 = S('Essence Blade', '2', '''Manifest a sword of essence which ignores physical armor''')
stonecutter2 = S('Stonecutter','2','''Your Essence sword can strike through 1 square of cover.
Does not give range in other circumstances''')

af5 = S('Auger Fighting', '5','''Your melee attacks may target all adjacent squares''')

mr4 = S('Massive Reserve', '4', '''You have a massive reserve of essence
    +800 essence''')

essence2 = S('Essence','2', '''+400 Essence''')
eb1 = S('Essence Blast', '1', '''Hit a foe with essence, causing max 3 wounds.
    10 range
    1d6/150 essence
''')
eblast2 = S("Essence Blast", '2', '''
    Hit target rectangle with an AOE blast, threatening max 3 wounds to each square.

    10 range
    1d6/100 essence * number of squares

    ''')
#tendrils, whips, flux
ea2 = S('Essence Armor', '2', '''
    When you risk wounds from a melee attack, they are disadvantaged
    200 essence/round
''')

ef2 = S('Essence Finesse', '2', '''When using an ability with an essence cost, 6s explode, allowing you to roll another die.
    ''')


alive.children = auger
alive.children = skilled
alive.children = gifted

auger.children = khan0
khan0.children = ec1
khan0.children = reading1
khan0.children = ks2
khan0.children = st1

ec1.children = khan2, 'red'
ec1.children = ec3
ec3.children = khan3
reading1.children = reading2
reading1.children = khan2, 'red'
reading2.children = control3

st1.children = khan2, 'red'
khan2.children = khan3, 'red'
khan2.children = control3

khan3.children = st4
st4.children = af5

skilled.children = educated0
educated0.children = ks2
educated0.children = educated1
educated1.children = educated2
educated2.children = educated3

skilled.children = physical0

physical0.children = evasion1
physical0.children = unsurprisable1
physical0.children = movement1
physical0.children = wt1
physical0.children = md1
physical0.children = es2

evasion1.children = physical2, 'red'
unsurprisable1.children = physical2, 'red'
movement1.children = physical2, 'red'
wt1.children = physical2, 'red'
wt1.children = at2
md1.children = physical2, 'red'
md1.children = sh3

physical2.children = wm3
wt1.children = wm3
physical2.children = discipline3
physical2.children = st4
physical2.children = sh3
st1.children = cft3
khan2.children = cft3

evasion1.children = evasion2
evasion2.children = ucd4
unsurprisable1.children = ucd4
st1.children = ucd4
ec3.children = mr4
physical2.children = mr4

gifted.children = essence0
essence0.children = ek1
ek1.children = eb2
essence2.children = sh3
essence0.children = es2
essence0.children = shielding1
essence0.children = ek1
essence0.children = healing1
essence0.children = eb1
essence0.children = ef2
shielding1.children = aoes2
eb1.children = aoes2
eb1.children = aoeh2
ek1.children = stonecutter2
shielding1.children = ea2

healing1.children = healing2
healing1.children = aoeh2

shielding1.children = essence2, 'red'
ek1.children = essence2, 'red'
healing1.children = essence2, 'red'
eb1.children = essence2, 'red'
eb1.children = eblast2
stonecutter2.children =af5

#TODO add teleport of some sort

def dot_children_arrows(node, done=None, strfunc=repr):

    if done is None:
        done = []


    if not node.children:
        return '\n'

    out = []
    for arrow in node.children:

        if arrow not in done:

            out.append(strfunc(arrow) + '\n' + dot_children_arrows(arrow.end, done, strfunc))
            done.append(arrow)
    return ''.join(out)


def describe(arrow):

    return '''"{}" -> "{}"[color={}]'''.format(arrow.start.desc, arrow.end.desc, arrow.color)

def html_repr(arrow):

    return '''
<h3 id="{}">{}</h3>
<p>{}</p>
    '''.format(arrow.start.full_name.replace(' ','-'), arrow.start.full_name, arrow.start.desc)

def dot_parent_arrows(node, done=None):
    if done is None:
        done = []

    if not node.parents:
        return '\n'

    out = []
    for node in node.parents:
        pass

from graph_template import graph_template
from html_template import html_template

def graph_file_from_node(node, fname,strfunc=repr ,format='svg'):

    with open(fname + '.dot', 'w') as f:
        graph_text = graph_template % dot_children_arrows(node, strfunc=strfunc)
        f.write(graph_text)

    subprocess.call(['dot', '-T'+format, fname+'.dot', '-o'+fname+'.'+format])


graph_file_from_node(alive, 'full_graph', repr, 'svg')




def make_html_file(node, fname):

    with open(fname+'.html', 'w') as f:
        html_text = html_template % dot_children_arrows(node, strfunc=html_repr)
        f.write(html_text)

make_html_file(alive, 'index')
