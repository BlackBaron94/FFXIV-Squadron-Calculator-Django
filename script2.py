string = (
    ('allied maneuvers', '1 Squadron Enlistment Manual'),
    ('pest eradication', '1 Squadron Enlistment Manual'),
    ('imposter alert', '10 Priority Aetheryte Passes'),
    ('invasive testing', '10 Squadron Gear Maintenance Manuals'),
    ('armor annihilation', '10 Squadron Rationing Manuals'),
    ('voidsent elimination', '10 Squadron Spiritbonding Manuals'),
    ('cult crackdown', '10 Squadron Engineering Manuals'),
    ('outlaw subjugation', '10 Squadron Survival Manuals'),
    ('infiltrate and rescue', '10 Squadron Battle Manuals'),
    ('counter-magitek exercises', '10 Gold Saucer VIP Cards'),
    ('primal recon', '10 Priority Seal Allowances'),
    ('chimerical elimination', '5 Priority Aetheryte Passes'),
    ('supply wagon destruction', '5 Squadron Gear Maintenance Manuals'),
    ('criminal pursuit', '5 Rationing Manuals'),
    ('supply line disruption', '5 Squadron Rationing Manuals'),
    ('imperial feint', '5 Squadron Spiritbonding Manuals'),
    ('imperial pursuit', '5 Squadron Survival Manuals'),
    ('imperial recon', '5 Squadron Battle Manuals'),
    ('black market crackdown', '5 Gold Saucer VIP Cards'),
    ('stronghold assault', '5 Priority Seal Allowances'))
raw = ''
for p in string:
    x = p[0].split(' ')
    raw += "('"
    for i in x:
        raw += i.capitalize()
        if x.index(i) != len(x)-1:
            raw += ' '
    raw += f"', '{p[1]}'),\n"

print(raw)
    