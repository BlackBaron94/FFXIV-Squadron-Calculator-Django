x = ''

while x != 'exit':
    x = input('dwse:\n')
    y = '{{ form.' + str(x) + '.label }}'
    z = '{{ form.' + str(x) + ' }}'
    w = '{{ form.' + str(x) + '.errors }}'
    print(f"""
        <div class="form">
            <div class="form-row" style="background-color: purple;">
                {y}:
            </div>
            {z}
            <span>
                {w}
            </span>
        </div>
""")