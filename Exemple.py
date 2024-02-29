from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def save_agenda(data, cal):
    with open("agenda.txt", "w") as f:
        f.write("_____________________________Agenda for Today______________________________\n")
        f.write(f"Today YYY/MM/DD: {data['date']}\n")
        f.write(f"The first task(08:30-11:00): {data['one']}\n")
        f.write(f"The second task(11:00-13:30): {data['to']}\n")
        f.write(f"The third task(13:30-16:00): {data['tri']}\n")
        f.write(f"The fourth task(16:00-20:00): {data['four']}\n")
        f.write(f"The of the day(20:00-00:00): {data['off']}\n")
        f.write(f"Mood of today: {data['Mod']}\n\n")
        
        f.write("__________________________Agenda for Tomorrow_______________________________\n")
        f.write(f"Today YYY/MM/DD: {cal['n1']}\n")
        f.write(f"The first task(08:30-11:00): {cal['n2']}\n")
        f.write(f"The second task(11:00-13:30): {cal['n3']}\n")
        f.write(f"The third task(13:30-16:00): {cal['n4']}\n")
        f.write(f"The fourth task(16:00-20:00): {cal['n5']}\n")
        f.write(f"The of the day(20:00-00:00): {cal['n6']}\n")
        f.write(f"Mood of today: {cal['n7']}\n\n")

def App():
    put_html('<h1 align="center"><i>Time Calendar</i></h1>').style('background-color:black; color:gold; padding:2px;')
    put_html('<p>This program is for evaluating your daily agenda</p>').style('text-align:center; font-weight:bold; ')
    data = input_group(
        'This is today work schedule.',
        [
            input('Today YYY/MM/DD :', name='date',type=DATE),
            input('The first task(08:30-11:00)', name='one'),
            input('The second task(11:00-13:30)', name='to'),
            input('The third task(13:30-16:00)', name='tri'),
            input('The fourth task(16:00-20:00)', name='four'),
            input('The of the day(20:00-00:00)', name='off'),
            radio('Your mood today', options=['Good','IDK','Bad'],inline=True ,name='Mod'),
        ],
    )
    

    cal = input_group(
        'This is  tomorrow work schedule.' ,
        [
            input('Today YYY/MM/DD :', name='n1',type=DATE),
            input('The first task(08:30-11:00)', name='n2'),
            input('The second task(11:00-13:30)', name='n3'),
            input('The third task(13:30-16:00)', name='n4'),
            input('The fourth task(16:00-20:00)', name='n5'),
            input('The of the day(20:00-00:00)', name='n6'),
            radio('Your mood today', options=['Good','IDK','Bad'],inline=True ,name='n7'),
        ],
    )
    put_table([
        [put_text('Agenda for Today').style('test-align:center;'),'Information'],
        ['Today YYY/MM/DD ', data['date']],
        ['The first task(08:30-11:00)',data['one']],
        ['The second task(11:00-13:30)',data['to']],
        ['The thrid task (13:30-16:00)',data['tri']],
        ['The fourth task(16:00-20:00)',data['four']],
        ['The of the day(20:00-00:00)',data['off']],
        ['Mood of today',data['Mod']]
    ]) 

    put_table([
        [put_text('Agenda for Tomorrow').style('test-align:center;'),'Information'],
        ['Today YYY/MM/DD ', cal['n1']],
        ['The first task(08:30-11:00)',cal['n2']],
        ['The second task(11:00-13:30)',cal['n3']],
        ['The thrid task (13:30-16:00)',cal['n4']],
        ['The fourth task(16:00-20:00)',cal['n5']],
        ['The of the day(20:00-00:00)',cal['n6']],
        ['Mood of today',cal['n7']]
    ])
    put_text('Signed by Slimani Omar 😎').style('font-weight:bold; color:green; text-align:center;')
    
    save_agenda(data, cal)


start_server(App , port=192 , debug=True)
