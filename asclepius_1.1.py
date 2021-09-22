from os import error
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import I, Output, Popup
import pymysql as maria
import array
from decimal import Decimal
import sys
import time
from time import sleep

sg.theme('LightGrey2')

layout_conexaodb = [[sg.Text('Sistema de Cotações', justification='center', size=(33,1))],
                    [sg.Text('Login', size=(13,1)), sg.Input(key='usuario', size=(20,1))],
                    [sg.Text('Senha', size=(13,1)), sg.Input(key='senha', password_char='*', size=(20,1))],
                    [sg.Button('Conectar', bind_return_key=True, size=(15,1)), sg.Button('Fechar', size=(14,1))],
                    [sg.Text('Asclepius v.1.1', justification='center', size=(30,1))]]

janela_conexaodb = sg.Window('Conectar ao serviço', layout_conexaodb)

while True:
    event_connect, values_connect = janela_conexaodb.read()

    if event_connect in (sg.WIN_CLOSED, 'Fechar'):
        break

    else:
        try:
            conn = maria.connect(
                user=values_connect['usuario'],
                password=values_connect['senha'],
                host='45.171.124.80',
                port=3306,
                database='asclepius_db',
            )
            cursor = conn.cursor()
            cursor.execute('SELECT VERSION()')
            print(cursor.fetchone())
            sg.Popup('Conectado com sucesso!', keep_on_top=True)
            janela_conexaodb.close()
            start = 1

            def pst_login(start):

                if start == 1:

                    def inicio_centro():

                        tosqlmain = ("SELECT * FROM dados_usuario WHERE usuario=%s")
                        cursor.execute(tosqlmain, values_connect['usuario'])
                        valores = cursor.fetchall()
                        usuario = valores[0]

                        tosqlmain = ("SELECT chave_cotacao FROM cotacoes WHERE consultor=%s ORDER BY chave_cotacao ASC")
                        cursor.execute(tosqlmain, usuario[1])
                        chave = cursor.fetchall()

                        layout_ic = [[sg.Text('Centro de Cotações', size=(40,1), justification='center')],
                                    [sg.Text('')],
                                    [sg.Combo(values=chave, size=(33,6), key='selcliente'), sg.Button('Selecionar', size=(10,1))],
                                    [sg.Text('')],
                                    [sg.Button('Criar Cotação', size=(20,1)), sg.Button('Fechar', size=(20,1))]]

                        janela_ic = sg.Window('Centro de Cotações', layout_ic)

                        while True:
                            event_ic, values_ic = janela_ic.read()

                            if event_ic in ('Fechar', sg.WIN_CLOSED):
                                janela_ic.close()
                                start = 1
                                pst_login(start)

                            elif event_ic == 'Criar Cotação':
                                janela_ic.close()
                                
                                cursor.execute("SELECT nome_plano FROM asclepius_db.planos_cadastrados ORDER BY nome_plano ASC")
                                planos = cursor.fetchall()

                                layout_crcot = [[sg.Text('Criador de Cotações', size=(90,1), justification='center')],
                                                [sg.Text('')],
                                                [sg.Text('Nome do Cliente:', size=(20,1)), sg.Input(key='nomecliente', size=(80,1))],
                                                [sg.Text('\n')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo1'), sg.Text('Idade:'), sg.Input(key='idade1', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa1', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo2'), sg.Text('Idade:'), sg.Input(key='idade2', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa2', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo3'), sg.Text('Idade:'), sg.Input(key='idade3', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa3', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo4'), sg.Text('Idade:'), sg.Input(key='idade4', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa4', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo5'), sg.Text('Idade:'), sg.Input(key='idade5', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa5', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo6'), sg.Text('Idade:'), sg.Input(key='idade6', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa6', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo7'), sg.Text('Idade:'), sg.Input(key='idade7', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa7', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo8'), sg.Text('Idade:'), sg.Input(key='idade8', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa8', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo9'), sg.Text('Idade:'), sg.Input(key='idade9', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa9', size=(10,1), default_text='0')],
                                                [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo10'), sg.Text('Idade:'), sg.Input(key='idade10', size=(5,1)), sg.Text('Taxa: R$'), sg.Input(key='taxa10', size=(10,1), default_text='0')],
                                                [sg.Text('')],
                                                [sg.Text('Desconto total (em %):'), sg.Input(key='desconto', size=(5,1), default_text='0')],
                                                [sg.Text('')],
                                                [sg.Button('Voltar', size=(30,2)), sg.Text('', size=(27,1)), sg.Button('Gerar', size=(30,2), bind_return_key=True)]]

                                janela_crcot = sg.Window('Criando cotação', layout_crcot)

                                while True:
                                    event_crcot, values_crcot = janela_crcot.read()

                                    if event_crcot in ('Voltar', sg.WIN_CLOSED):
                                        janela_crcot.close()
                                        inicio_centro()

                                    elif event_crcot == 'Gerar':

                                        if values_crcot['nomecliente'] in (None, '0', ''):
                                            sg.Popup('Nome do cliente vazio!')

                                        else:
                                            try:
                                                planos = []
                                                idades = []
                                                taxas = []

                                                desc = float(values_crcot['desconto'])

                                                t1 = float(values_crcot['taxa1'])
                                                t2 = float(values_crcot['taxa2'])
                                                t3 = float(values_crcot['taxa3'])
                                                t4 = float(values_crcot['taxa4'])
                                                t5 = float(values_crcot['taxa5'])
                                                t6 = float(values_crcot['taxa6'])
                                                t7 = float(values_crcot['taxa7'])
                                                t8 = float(values_crcot['taxa8'])
                                                t9 = float(values_crcot['taxa9'])
                                                t10 = float(values_crcot['taxa10'])
                                                
                                                c1 = values_crcot['combo1']
                                                c2 = values_crcot['combo2']
                                                c3 = values_crcot['combo3']
                                                c4 = values_crcot['combo4']
                                                c5 = values_crcot['combo5']
                                                c6 = values_crcot['combo6']
                                                c7 = values_crcot['combo7']
                                                c8 = values_crcot['combo8']
                                                c9 = values_crcot['combo9']
                                                c10 = values_crcot['combo10']

                                                i1r = values_crcot['idade1']
                                                i2r = values_crcot['idade2']
                                                i3r = values_crcot['idade3']
                                                i4r = values_crcot['idade4']
                                                i5r = values_crcot['idade5']
                                                i6r = values_crcot['idade6']
                                                i7r = values_crcot['idade7']
                                                i8r = values_crcot['idade8']
                                                i9r = values_crcot['idade9']
                                                i10r = values_crcot['idade10']

                                                nome_cliente = values_crcot['nomecliente']

                                                if c1 != None and i1r != None:
                                                    i1 = int(i1r)
                                                    planos.append(c1[0])
                                                    idades.append(i1)
                                                    taxas.append(t1)

                                                if c2 != None and i2r != None:
                                                    i2 = int(i2r)
                                                    planos.append(c2[0])
                                                    idades.append(i2)
                                                    taxas.append(t2)

                                                if c3 != None and i3r != None:
                                                    i3 = int(i3r)
                                                    planos.append(c3[0])
                                                    idades.append(i3)
                                                    taxas.append(t3)

                                                if c4 != None and i4r != None:
                                                    i4 = int(i4r)
                                                    planos.append(c4[0])
                                                    idades.append(i4)
                                                    taxas.append(t4)

                                                if c5 != None and i5r != None:
                                                    i5 = int(i5r)
                                                    planos.append(c5[0])
                                                    idades.append(i5)
                                                    taxas.append(t5)

                                                if c6 != None and i6r != None:
                                                    i6 = int(i6r)
                                                    planos.append(c6[0])
                                                    idades.append(i6)
                                                    taxas.append(t6)

                                                if c7 != None and i7r != None:
                                                    i7 = int(i7r)
                                                    planos.append(c7[0])
                                                    idades.append(i7)
                                                    taxas.append(t7)

                                                if c8 != None and i8r != None:
                                                    i8 = int(i8r)
                                                    planos.append(c8[0])
                                                    idades.append(i8)
                                                    taxas.append(t8)

                                                if c9 != None and i9r != None:
                                                    i9 = int(i9r)
                                                    planos.append(c9[0])
                                                    idades.append(i9)
                                                    taxas.append(t9)

                                                if c10 != None and i10r != None:
                                                    i10 = int(i10r)
                                                    planos.append(c10[0])
                                                    idades.append(i10)
                                                    taxas.append(t10)

                                                print(planos)
                                                print(idades)
                                                print('TEST APPEND')

                                            except:
                                                print('ERROR 11 - IS EVERYTHING OK?')

                                            try:
                                                plano_out_glob = []
                                                valor_glob = []
                                                idade_glob = []

                                                for na in range(len(planos)):

                                                    plano = planos[na]
                                                    idade = idades[na]

                                                    try:
                                                        tosql_main = ("SELECT * FROM planos_cadastrados WHERE nome_plano=%s")
                                                        tosql_var = plano
                                                        cursor.execute(tosql_main, tosql_var)
                                                        conn.commit()
                                                        sqlraw = cursor.fetchall()
                                                        fromsql = sqlraw[0]
                                                        print(fromsql)

                                                    except maria.Error as e:
                                                        sg.Popup(e)

                                                    try:
                                                        plano_out = fromsql[0]

                                                        if idade <= 18:
                                                            valor = fromsql[1]
                                                            print('OK')

                                                        elif idade <= 23:
                                                            valor = fromsql[2]
                                                            print('OK')

                                                        elif idade <= 28:
                                                            valor = fromsql[3]
                                                            print('OK')

                                                        elif idade <= 33:
                                                            valor = fromsql[4]
                                                            print('OK')

                                                        elif idade <= 38:
                                                            valor = fromsql[5]
                                                            print('OK')

                                                        elif idade <= 43:
                                                            valor = fromsql[6]
                                                            print('OK')

                                                        elif idade <= 48:
                                                            valor = fromsql[7]
                                                            print('OK')

                                                        elif idade <= 53:
                                                            valor = fromsql[8]
                                                            print('OK')

                                                        elif idade <= 58:
                                                            valor = fromsql[9]
                                                            print('OK')

                                                        elif idade >= 59:
                                                            valor = fromsql[10]
                                                            print('OK')

                                                        else:
                                                            sg.Popup('Erro 6')

                                                        plano_out_glob.append(plano_out)
                                                        valor_glob.append(valor)
                                                        idade_glob.append(idade)
                                                    
                                                    except:
                                                        sg.Popup('Erro 6a')

                                            except:
                                                sg.Popup('Erro 8a')                    

                                            try:
                                                print('OK UNTILL TRY CALCULE')
                                                print(str(plano_out_glob), str(valor_glob), str(idade_glob))
                                                try:
                                                    valor_calculado = 0

                                                    for n in range(len(valor_glob)):
                                                        valor_calculado = float(valor_calculado) + float(valor_glob[n] + float(taxas[n]))
                                                        valor_calculado = round(valor_calculado, 2)
                                                        print('\nCALCULATED: OK')
                                                        print(valor_calculado)
                                                        print('\nOK UNTILL END FUNCTION')
                                                        print(idade_glob[n], valor_glob[n], plano_out_glob[n], taxas[n], n)
                                                        print('\nEND FUNCTION')

                                                    desconto = desc / 100

                                                    descvar = float(valor_calculado) * float(desconto)
                                                    valor_final = valor_calculado - descvar

                                                    print(desconto)
                                                    print(valor_final)

                                                except:
                                                    sg.Popup('Erro 9a')

                                                try:
                                                    layout_showcrcot = [[sg.Text('MOSTRANDO COTAÇÃO', size=(100,1), justification='center')],
                                                                        [sg.Text('')],
                                                                        [sg.Text('Chave de identificação da cotação:', size=(50,1)), sg.Input(key='chavecota', size=(63,1))],
                                                                        [sg.Text('')],
                                                                        [sg.Multiline(size=(120,20), key='-out-', do_not_clear=True, auto_refresh=True)],
                                                                        [sg.Button('Gerar', size=(20,2)), sg.Button('Salvar', size=(20,2)), sg.Button('Fechar', size=(20,2))]]

                                                    janela_showcrcot = sg.Window('Cotação criada', layout_showcrcot)

                                                except:
                                                    sg.Popup('Erro 9b')
                                                
                                                while True:
                                                    janela_crcot.close()
                                                    event_showcrcot, values_showcrcot = janela_showcrcot.read()

                                                    if event_showcrcot == 'Gerar':
                                                        valor_final = round(valor_final, 2)
                                                        desc = int(desc)
                                                        valor_calculado = round(valor_calculado, 2)
                                                        janela_showcrcot['-out-'].update('')
                                                        janela_showcrcot['-out-'].print('Olá ' + str(nome_cliente) + ',\n')
                                                        for n in range(len(idade_glob)):
                                                            janela_showcrcot['-out-'].print('O plano - ' + str(plano_out_glob[n]) + ' - para ' + str(idade_glob[n]) + ' anos está custando R$' + str(valor_glob[n]) + ' + Taxa de R$' + str(taxas[n]))
                                                        janela_showcrcot['-out-'].print('\n' + 'O valor total é de R$' + str(valor_calculado) + '\n\nCom desconto de ' + str(desc) + '% = R$' + str(valor_final))

                                                    elif event_showcrcot in ('Fechar', sg.WIN_CLOSED):
                                                        inicio_centro()

                                                    elif event_showcrcot == 'Salvar':
                                                        if values_showcrcot['chavecota'] in (None, '', ' '):
                                                            sg.Popup('O valor da chave não pode estar vazio!')
                                                        
                                                        else:
                                                            try:
                                                                tosql_main = ("INSERT INTO cotacoes (chave_cotacao, consultor, cliente, dados) VALUES (%s, %s, %s, %s)")
                                                                tosql_var = (values_showcrcot['chavecota'], usuario[1], nome_cliente, values_showcrcot['-out-'])
                                                                cursor.execute(tosql_main, tosql_var)
                                                                conn.commit()
                                                                sg.Popup('Cotação salva com sucesso!')
                                                                janela_showcrcot.close()
                                                                inicio_centro()
                                                            
                                                            except:
                                                                sg.Popup('Erro')

                                            except ValueError as e:
                                                sg.Popup(e)

                            elif event_ic == 'Selecionar':
                                if values_ic['selcliente'] == None:
                                    sg.Popup('Selecione alguma cotação ou crie uma nova!')

                                else:
                                    try:
                                        tosql_main = ("SELECT * FROM cotacoes WHERE chave_cotacao=%s")
                                        tosql_var = values_ic['selcliente']
                                        cursor.execute(tosql_main, tosql_var)
                                        fromsql = cursor.fetchall()
                                        fromsql = fromsql[0]
                                        print(fromsql)
                                        janela_ic.close()
                
                                        layout_selcota = [[sg.Text('Consultar Cotação - Cliente: ' + str(fromsql[1]), size=(90,1), justification='center')],
                                                        [sg.Multiline(str(fromsql[2]), size=(100,20), key='box')],
                                                        [sg.Text('Gerado originalmente por: ' + str(fromsql[0]), size=(90,1), justification='center')],
                                                        [sg.Text('Código da cotação: ' + str(fromsql[3]), size=(90,1), justification='center')],
                                                        [sg.Button('Fechar', size=(20,2)), sg.Button('Salvar Modificações', size=(20,2), key='smod'), sg.Text('', size=(24,1)), sg.Button('Excluir', size=(20,2))]]

                                        janela_selcota = sg.Window('Visualizando cotação', layout_selcota)

                                        while True:
                                            event_selcota, values_selcota = janela_selcota.read()

                                            if event_selcota in ('Fechar', sg.WIN_CLOSED):
                                                janela_selcota.close()
                                                inicio_centro()

                                            elif event_selcota == 'Excluir':
                                                layout_ctz = [[sg.Text('Tem certeza que deseja deletar?\nEsta ação não poderá ser desfeita')],
                                                            [sg.Button('Sim'), sg.Button('Não')]]

                                                janela_ctz = sg.Window('CUIDADO!', layout_ctz)

                                                while True:
                                                    event_ctz, values_ctz = janela_ctz.read()

                                                    if event_ctz in ('Não', sg.WIN_CLOSED):
                                                        janela_ctz.close()

                                                    elif event_ctz == 'Sim':
                                                        try:
                                                            janela_selcota.close()
                                                            janela_ctz.close()
                                                            tosql_delmain = ("DELETE FROM cotacoes WHERE chave_cotacao=%s")
                                                            tosql_delvar = values_ic['selcliente']
                                                            cursor.execute(tosql_delmain, tosql_delvar)
                                                            conn.commit()
                                                            sg.Popup('Cotação deletada com sucesso!')
                                                            inicio_centro()

                                                        except maria.Error as e:
                                                            sg.Popup(e)

                                            elif event_selcota == 'smod':
                                                layout_ctz = [[sg.Text('Tem certeza que deseja alterar?\nEsta ação não poderá ser desfeita')],
                                                            [sg.Button('Sim'), sg.Button('Não')]]

                                                janela_ctz = sg.Window('CUIDADO!', layout_ctz)

                                                while True:
                                                    event_ctz, values_ctz = janela_ctz.read()

                                                    if event_ctz in ('Não', sg.WIN_CLOSED):
                                                        janela_ctz.close()

                                                    elif event_ctz == 'Sim':
                                                        try:
                                                            tosqlmain = ('UPDATE cotacoes SET dados=%s WHERE chave_cotacao=%s')
                                                            tosqlvar = (values_selcota['box'], values_ic['selcliente'])
                                                            cursor.execute(tosqlmain, tosqlvar)
                                                            conn.commit()
                                                            sg.Popup('Alterado com sucesso!')
                                                            janela_ctz.close()
                                                            janela_selcota.close()
                                                            inicio_centro()

                                                        except:
                                                            sg.Popup('Erro na modificação')

                                    except:
                                        sg.Popup('Erro Genérico')

                    def consulta_idade():

                        def inicio_ci():
                            try:
                                cursor.execute("SELECT nome_plano FROM asclepius_db.planos_cadastrados ORDER BY nome_plano ASC")
                                planos = cursor.fetchall()

                            except:
                                sg.Popup('Erro 2')
                                start = 1
                                pst_login(start)

                            layout_conid = [[sg.Text('Selecione a tabela e a idade')],
                                            [sg.Text('Plano:'), sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo'), sg.Text(' Idade:'), sg.Input(key='idade', size=(5,1))],
                                            [sg.Button('Pesquisar'), sg.Button('Cancelar')]]

                            janela_conid = sg.Window('Consulta por Idade', layout_conid)

                            while True:
                                event_conid, values_conid = janela_conid.read()

                                if event_conid in ('Cancelar', sg.WIN_CLOSED):
                                    janela_conid.close()
                                    start = 1
                                    pst_login(start)

                                elif event_conid in 'Pesquisar':
                                    if values_conid['idade'] in (None, '', ' '):
                                        sg.Popup('Idade vazia!')

                                    elif values_conid['combo'] in (None, '0', '', ' '):
                                        sg.Popup('Selecione um plano!')

                                    else:
                                        janela_conid.close()
                                        try:
                                            idade = float(values_conid['idade'])

                                            try:
                                                tosql_main = ("SELECT * FROM planos_cadastrados WHERE nome_plano=%s")
                                                tosql_var = (values_conid['combo'])
                                                cursor.execute(tosql_main, tosql_var)
                                                conn.commit()
                                                sqlraw = cursor.fetchall()
                                                fromsql = sqlraw[0]
                                                print(fromsql)

                                            except maria.Error as e:
                                                sg.Popup(e)

                                            plano = fromsql[0]

                                            if idade <= 18:
                                                valor = fromsql[1]
                                                print('OK')

                                            elif idade <= 23:
                                                valor = fromsql[2]
                                                print('OK')

                                            elif idade <= 28:
                                                valor = fromsql[3]
                                                print('OK')

                                            elif idade <= 33:
                                                valor = fromsql[4]
                                                print('OK')

                                            elif idade <= 38:
                                                valor = fromsql[5]
                                                print('OK')

                                            elif idade <= 43:
                                                valor = fromsql[6]
                                                print('OK')

                                            elif idade <= 48:
                                                valor = fromsql[7]
                                                print('OK')

                                            elif idade <= 53:
                                                valor = fromsql[8]
                                                print('OK')

                                            elif idade <= 58:
                                                valor = fromsql[9]
                                                print('OK')

                                            elif idade >= 59:
                                                valor = fromsql[10]
                                                print('OK')

                                            else:
                                                sg.Popup('Erro 6')

                                            try:
                                                layout_showci = [[sg.Text('Plano:   '+ str(plano))],
                                                                [sg.Text('Idade:   '+ str(idade))],
                                                                [sg.Text('Valor:   R$'+ str(valor))],
                                                                [sg.Button('Fechar')]]

                                                janela_showci = sg.Window('Resultado', layout_showci)

                                                while True:
                                                    events_result, values_result = janela_showci.read()

                                                    if events_result in ('Fechar', sg.WIN_CLOSED):
                                                        janela_showci.close()
                                                        start = 1
                                                        pst_login(start)
                        
                                            except:
                                                sg.Popup('Erro 9')

                                        except:
                                            sg.Popup('Erro 8')

                        inicio_ci()

                    def con_tab():

                        try:
                            cursor.execute("SELECT nome_plano FROM asclepius_db.planos_cadastrados ORDER BY nome_plano ASC")
                            planos = cursor.fetchall()

                        except:
                            sg.Popup('Erro 2')
                            start = 1
                            pst_login(start)

                        layout_con_tab = [[sg.Text('Selecione uma tabela ou crie uma nova')],
                                        [sg.Combo(values=planos, size=(60, 6), enable_events=True, key='combo')],
                                        [sg.Button('Selecionar'), sg.Button('Adicionar'), sg.Button('Voltar')]]

                        janela_con_tab = sg.Window('Controle de Tabelas', layout_con_tab)

                        while True:
                            event_ct, values_ct = janela_con_tab.read()

                            if event_ct in ('Voltar', sg.WIN_CLOSED):
                                janela_con_tab.close()
                                start = 1
                                pst_login(start)

                            elif event_ct == 'Selecionar':
                                if values_ct['combo'] in (None, '0', '', ' '):
                                    sg.Popup('Selecione uma tabela!')

                                else:
                                    janela_con_tab.close()
                                    try:
                                        tosql_atmain = ("SELECT * FROM asclepius_db.planos_cadastrados WHERE nome_plano=%s")
                                        cursor.execute(tosql_atmain, values_ct['combo'])
                                        fromsqlret = cursor.fetchall()
                                        print(fromsqlret)
                                        fromsql = fromsqlret[0]
                                        print(fromsql)

                                    except maria.Error as e:
                                        sg.Popup(e)

                                    try:
                                        layout_seltab = [[sg.Text('Alterando tabela', size=(40,1), justification='center')],
                                                            [sg.Text('Nome: '+ str(fromsql[0]), size=(40,1), justification='center')],
                                                            [sg.Text('0 à 18 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[1], size=(10,1))],
                                                            [sg.Text('19 à 23 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[2], size=(10,1))],
                                                            [sg.Text('24 à 28 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[3], size=(10,1))],
                                                            [sg.Text('29 à 33 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[4], size=(10,1))],
                                                            [sg.Text('34 à 38 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[5], size=(10,1))],
                                                            [sg.Text('39 à 43 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[6], size=(10,1))],
                                                            [sg.Text('44 à 48 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[7], size=(10,1))],
                                                            [sg.Text('49 à 53 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[8], size=(10,1))],
                                                            [sg.Text('54 à 58 anos - R$', size=(30,1)), sg.Input(default_text = fromsql[9], size=(10,1))],
                                                            [sg.Text('59 anos ou mais - R$', size=(30,1)), sg.Input(default_text = fromsql[10], size=(10,1))],
                                                            [sg.Text('')],
                                                            [sg.Text('Aumento por porcentagem:'), sg.Input(size=(5,1), key='porce'), sg.Text('%'), sg.Button('+', key='adc')],
                                                            [sg.Text('')],
                                                            [sg.Button('Alterar'), sg.Button('Deletar'), sg.Button('Fechar')]]

                                        janela_seltab = sg.Window('Alterando tabelas', layout_seltab)

                                        while True:
                                            event_st, values_st = janela_seltab.read()

                                            if event_st == 'adc':
                                                layout_ctz = [[sg.Text('Tem certeza que deseja adicionar o aumento?\nEsta ação não poderá ser desfeita')],
                                                            [sg.Button('Sim'), sg.Button('Não')]]

                                                janela_ctz = sg.Window('CUIDADO!', layout_ctz)

                                                while True:
                                                    event_ctz, values_ctz = janela_ctz.read()

                                                    if event_ctz in ('n', sg.WIN_CLOSED):
                                                        janela_ctz.close()

                                                    elif event_ctz == 'Sim':
                                                        janela_ctz.close()
                                                        print(values_st['porce'])

                                                        try:
                                                            porc = float(values_st['porce']) / 100
                                                            values_alt = []
                                                            out = []
                                                            print(porc)

                                                        except:
                                                            sg.Popup('Erro 11a')

                                                        try:
                                                            for n in range(0, 10):
                                                                outporc = float(values_st[n]) * float(porc)
                                                                print(outporc)
                                                                out = float(values_st[n]) + outporc
                                                                out = round(out, 2)
                                                                print(out)
                                                                values_alt.append(out)
                                                                print(out)

                                                        except:
                                                            sg.Popup('Erro 11b')

                                                        print(values_alt)

                                                        try:
                                                            tosql_upmain = ("UPDATE planos_cadastrados SET 0_18=%s,19_23=%s,24_28=%s,29_33=%s,34_38=%s,39_43=%s,44_48=%s,49_53=%s,54_58=%s,59om=%s WHERE nome_plano=%s")
                                                            tosql_data = (values_alt[0], values_alt[1], values_alt[2], values_alt[3], values_alt[4], values_alt[5], values_alt[6], values_alt[7], values_alt[8], values_alt[9], fromsql[0])
                                                            cursor.execute(tosql_upmain, tosql_data)
                                                            conn.commit()
                                                            sg.Popup('Tabela alterada com sucesso!')
                                                            janela_seltab.close()
                                                            con_tab()

                                                        except maria.Error as e:
                                                            sg.Popup('Erro 4: Há campos vazios ou inválidos!')

                                            elif event_st in ('Fechar', sg.WIN_CLOSED):
                                                janela_seltab.close()
                                                con_tab()

                                            elif event_st == 'Alterar':
                                                layout_ctz = [[sg.Text('Tem certeza que deseja alterar?\nEsta ação não poderá ser desfeita')],
                                                            [sg.Button('Sim'), sg.Button('Não')]]

                                                janela_ctz = sg.Window('CUIDADO!', layout_ctz)

                                                while True:
                                                    event_ctz, values_ctz = janela_ctz.read()

                                                    if event_ctz in ('n', sg.WIN_CLOSED):
                                                        janela_ctz.close()

                                                    elif event_ctz == 'Sim':
                                                        try:
                                                            janela_seltab.close()
                                                            janela_ctz.close()
                                                            tosql_upmain = ("UPDATE planos_cadastrados SET 0_18=%s,19_23=%s,24_28=%s,29_33=%s,34_38=%s,39_43=%s,44_48=%s,49_53=%s,54_58=%s,59om=%s WHERE nome_plano=%s")
                                                            tosql_data = (values_st[0], values_st[1], values_st[2], values_st[3], values_st[4], values_st[5], values_st[6], values_st[7], values_st[8], values_st[9], values_ct['combo'])
                                                            cursor.execute(tosql_upmain, tosql_data)
                                                            conn.commit()
                                                            sg.Popup('Tabela alterada com sucesso!')
                                                            con_tab()

                                                        except maria.Error as e:
                                                            sg.Popup('Erro 4: Há campos vazios ou inválidos!')
                                        
                                            elif event_st == 'Deletar':
                                                layout_ctz = [[sg.Text('Tem certeza que deseja deletar?\nEsta ação não poderá ser desfeita')],
                                                            [sg.Button('Sim'), sg.Button('Não')]]

                                                janela_ctz = sg.Window('CUIDADO!', layout_ctz)

                                                while True:
                                                    event_ctz, values_ctz = janela_ctz.read()

                                                    if event_ctz in ('Não', sg.WIN_CLOSED):
                                                        janela_ctz.close()

                                                    elif event_ctz == 'Sim':
                                                        try:
                                                            janela_seltab.close()
                                                            janela_ctz.close()
                                                            tosql_delmain = ("DELETE FROM planos_cadastrados WHERE nome_plano=%s")
                                                            tosql_delvar = values_ct['combo']
                                                            cursor.execute(tosql_delmain, tosql_delvar)
                                                            conn.commit()
                                                            sg.Popup('Tabela deletada com sucesso!')
                                                            con_tab()

                                                        except maria.Error as e:
                                                            sg.Popup(e)

                                    except:
                                        sg.Popup('Erro 5')

                            elif event_ct == 'Adicionar':
                                janela_con_tab.close()

                                layout_adtab =  [[sg.Text('Criando tabela (DIVIDIR VALORES COM . E NÃO,)\n', size=(40,2), justification='center')],
                                                    [sg.Text('Nome ', size=(17,1)), sg.Input(size=(25,1))],
                                                    [sg.Text('')],
                                                    [sg.Text('0 à 18 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('19 à 23 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('24 à 28 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('29 à 33 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('34 à 38 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('39 à 43 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('44 à 48 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('49 à 53 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('54 à 58 anos - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Text('59 anos ou mais - R$', size=(25,1)), sg.Input(size=(15,1))],
                                                    [sg.Button('Criar'), sg.Button('Fechar')]]

                                janela_adtab = sg.Window('Criando tabela', layout_adtab)

                                while True:

                                    event_at, values_at = janela_adtab.read()

                                    if event_at in (None, 'Fechar', sg.WIN_CLOSED):
                                        janela_adtab.close()
                                        con_tab()

                                    elif event_at == 'Criar':
                                        try:
                                            tosql_atmain = "INSERT INTO planos_cadastrados (nome_plano, 0_18, 19_23, 24_28, 29_33, 34_38, 39_43, 44_48, 49_53, 54_58, 59om) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                            tosql_atvar = (values_at[0], values_at[1], values_at[2], values_at[3], values_at[4], values_at[5], values_at[6], values_at[7], values_at[8], values_at[9], values_at[10])
                                            tosql_final = (
                                                tosql_atmain, tosql_atvar
                                            )
                                            print(tosql_final)
                                            cursor.execute(tosql_atmain, tosql_atvar)
                                            conn.commit()
                                            sg.Popup('Tabela adicionada com sucesso!')
                                            janela_adtab.close()
                                            con_tab()

                                        except maria.Error as e:
                                            sg.Popup('Erro 4: Há campos vazios, inválidos ou a tabela já existe')
                                            
                    def menu_in():
                        tosqlmain = ("SELECT * FROM dados_usuario WHERE usuario=%s")
                        cursor.execute(tosqlmain, values_connect['usuario'])
                        valores = cursor.fetchall()
                        valores = valores[0]

                        layout_min = [[sg.Text('Menu inicial\n', size=(42,1), justification='center')],
                                    [sg.Text('')],
                                    [sg.Button('Centro de Cotações', key='cota', size=(42,2))],
                                    [sg.Button('Consultar', key='cons', size=(42,2))],
                                    [sg.Button('Modificar Tabelas', key='contab', size=(42,2))],
                                    [sg.Button('Fechar', size=(42,2))],
                                    [sg.Text('')],
                                    [sg.Text('Logado como: ' + str(valores[1]) + ' - ' + str(valores[2]), justification='center', size=(42,1))]]

                        janela_min = sg.Window('Inicio - Asclepius', layout_min)

                        while True:
                            event, values = janela_min.read()

                            if event in ('Fechar', sg.WIN_CLOSED):
                                janela_min.close()
                                sys.exit()

                            elif event == 'contab':
                                janela_min.close()
                                con_tab()

                            elif event == 'cota':
                                janela_min.close()
                                inicio_centro()

                            elif event == 'cons':
                                janela_min.close()
                                consulta_idade()

                    menu_in()

                else:
                    sys.exit(0)

            pst_login(start)

        except maria.Error as e:
            sg.Popup('Erro ao conectar! Tente novamente')
